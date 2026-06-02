"""
Kestrel: Fine-tune DistilBERT for merchant name extraction from credit card transactions.

This trains a seq2seq-style model using encoder-decoder approach:
- Input: raw transaction string (e.g., "MCDONALD'S F2548 RT 35 & AMBOY...")
- Output: clean merchant name (e.g., "McDonald's")

We frame this as a text generation task using a small encoder-decoder model,
or alternatively as a sequence classification task where we predict start/end
positions of the merchant name within the input.

For simplicity and accuracy, we use a T5-small model (60M params) which handles
seq2seq natively and produces clean text output.
"""

import torch
from datasets import load_dataset, Dataset
from kestrel_metrics import load_eval_descriptions
from transformers import (
    T5ForConditionalGeneration,
    AutoTokenizer,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    DataCollatorForSeq2Seq,
)


def main():
    # Detect device
    if torch.backends.mps.is_available():
        device = "mps"
        print("Using Apple Silicon MPS")
    elif torch.cuda.is_available():
        device = "cuda"
        print(f"Using CUDA: {torch.cuda.get_device_name()}")
    else:
        device = "cpu"
        print("Using CPU (this will be slow)")

    # Load dataset from combined_transactions.csv (exclude held-out eval rows)
    print("Loading combined_transactions.csv...")
    dataset = load_dataset("csv", data_files="combined_transactions.csv", split="train")
    dataset = dataset.rename_column("description", "transaction")
    eval_desc = load_eval_descriptions()
    if eval_desc:
        before = len(dataset)
        dataset = dataset.filter(lambda row: row["transaction"] not in eval_desc)
        print(f"  Excluded {before - len(dataset)} held-out eval rows ({len(eval_desc)} descriptions)")

    # Split into train/test (85/15)
    split = dataset.train_test_split(test_size=0.15, seed=42)
    dataset = split
    print(f"Train: {len(dataset['train'])} examples")
    print(f"Test: {len(dataset['test'])} examples")

    # Print a few examples
    print("\nSample data:")
    for i in range(3):
        row = dataset["train"][i]
        print(f"  Input:  {row['transaction'][:80]}...")
        print(f"  Output: {row['merchant']}")
        print()

    # Load model and tokenizer
    model_name = "t5-small"
    print(f"Loading {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Preprocessing
    prefix = "extract merchant: "
    max_input_length = 128
    max_target_length = 64

    def preprocess(examples):
        inputs = [prefix + tx for tx in examples["transaction"]]
        targets = examples["merchant"]

        model_inputs = tokenizer(
            inputs,
            max_length=max_input_length,
            truncation=True,
            padding="max_length",
        )

        labels = tokenizer(
            targets,
            max_length=max_target_length,
            truncation=True,
            padding="max_length",
        )

        # Replace padding token id with -100 so it's ignored in loss
        labels["input_ids"] = [
            [(l if l != tokenizer.pad_token_id else -100) for l in label]
            for label in labels["input_ids"]
        ]

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    print("Tokenizing dataset...")
    tokenized_train = dataset["train"].map(
        preprocess, batched=True, remove_columns=dataset["train"].column_names
    )
    tokenized_test = dataset["test"].map(
        preprocess, batched=True, remove_columns=dataset["test"].column_names
    )

    # Training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir="./output",
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=3e-4,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=10,
        weight_decay=0.01,
        predict_with_generate=True,
        generation_max_length=max_target_length,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        save_total_limit=2,
        fp16=False,  # MPS doesn't support fp16 well
        report_to="none",
        logging_steps=50,
        warmup_steps=100,
    )

    # Data collator
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_test,
        processing_class=tokenizer,
        data_collator=data_collator,
    )

    # Train
    print("\nStarting training...")
    print(f"  Epochs: {training_args.num_train_epochs}")
    print(f"  Batch size: {training_args.per_device_train_batch_size}")
    print(f"  Learning rate: {training_args.learning_rate}")
    print(f"  Device: {device}")
    print()

    trainer.train()

    # Save final model
    print("\nSaving model to ./output/final...")
    trainer.save_model("./output/final")
    tokenizer.save_pretrained("./output/final")

    # Quick evaluation
    print("\nRunning evaluation on test set...")
    results = trainer.evaluate()
    print(f"  Eval loss: {results['eval_loss']:.4f}")

    # Generate predictions on a few examples
    print("\nSample predictions:")
    model.eval()
    test_inputs = [
        "NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA",
        "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA",
        "WAL-MART #2825 1126 US HIGHWAY 9 OLD BRIDGE 08857 NJ USA",
        "GOOGLE *YOUTUBEPREMIUM1600 AMPHITHEATRE PKWY 650-253-0000 94043 CA USA",
        "PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB",
        "TRADER_JS_092 07/08 #XXXXX0092 PURCHASE GROCERIES MONROVIA CA",
        "GEICO *AUTO ONE GEICO PLAZA 800-841-3000 20076 DC USA",
        "APPLE.COM/BILL ONE APPLE PARK WAY 866-712-7753 95014 CA USA",
        "SHOPRITE HAZLET S1 3150 STATE HIGHWAY 35 HAZLET 07735 NJ USA",
        "NJ EZPASS 375 MCCARTER HIGHWAY NEWARK 07114 NJ USA",
    ]

    for tx in test_inputs:
        input_text = prefix + tx
        input_ids = tokenizer(input_text, return_tensors="pt", max_length=max_input_length, truncation=True).input_ids
        if device != "cpu":
            input_ids = input_ids.to(device)
            model = model.to(device)

        with torch.no_grad():
            outputs = model.generate(input_ids, max_length=max_target_length)

        predicted = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"  {tx[:60]:<62} -> {predicted}")

    print("\nDone! Model saved to ./output/final")
    print("Next: run export_onnx.py to convert to ONNX format")


if __name__ == "__main__":
    main()
