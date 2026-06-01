"""
Generate merchant_category.csv mapping each merchant to a 3-level hierarchy.
Root levels: Expense, Income

Includes a public_category column with the verbatim category name
from public sources (Google Maps, MCC codes, industry databases).
"""
import csv

# Merchant -> (public_category, root, mid, leaf) mapping
# Leaf categories are kept to ~20 chars
CATEGORIES = {}


def assign(merchants_with_public_cat, root, mid, leaf):
    """Bulk assign merchants. Each entry is (merchant, public_category)."""
    for merchant, public_cat in merchants_with_public_cat:
        CATEGORIES[merchant] = (public_cat, root, mid, leaf)



# ============================================================
# FOOD & DINING - Groceries
# ============================================================

assign([
    ("ACME", "Supermarket"),
    ("ACME Markets", "Supermarket"),
    ("ALDI", "Discount Supermarket"),
    ("Albert Heijn", "Supermarket Chain"),
    ("Albertsons", "Supermarket"),
    ("APNA BAZAR", "Indian Grocery Store"),
    ("BHAVANI FARMERS MARKET", "Indian Grocery Store"),
    ("Big Basket", "Online Grocery Delivery"),
    ("Big C", "Hypermarket"),
    ("Biedronka", "Discount Supermarket"),
    ("Billa", "Supermarket Chain"),
    ("BJ's Wholesale Club", "Wholesale Club"),
    ("Bravo", "Supermarket"),
    ("Carrefour", "Hypermarket Chain"),
    ("Chedraui", "Supermarket Chain"),
    ("Cold Storage", "Premium Supermarket"),
    ("Coles", "Supermarket Chain"),
    ("Coop", "Cooperative Supermarket"),
    ("Costco", "Wholesale Club"),
    ("COSTCO", "Wholesale Club"),
    ("Coto", "Supermarket Chain"),
    ("Countdown", "Supermarket Chain"),
    ("EDEKA", "Supermarket Chain"),
    ("E-Mart", "Hypermarket Chain"),
    ("Exito", "Hypermarket Chain"),
    ("Extra", "Supermarket Chain"),
    ("FairPrice", "Supermarket Chain"),
    ("Fairprice", "Supermarket Chain"),
    ("Food 4 Less", "Discount Supermarket"),
    ("Food Lion", "Supermarket"),
    ("Føtex", "Supermarket Chain"),
    ("Giant", "Supermarket"),
    ("Giant Eagle", "Supermarket"),
    ("Globus", "Hypermarket"),
    ("H-E-B", "Supermarket Chain"),
    ("Hannaford", "Supermarket"),
    ("Harris Teeter", "Supermarket"),
    ("Hemköp", "Supermarket Chain"),
    ("Hy-Vee", "Supermarket"),
    ("ICA", "Supermarket Chain"),
    ("IGA", "Independent Supermarket"),
    ("Indomaret", "Convenience Store Chain"),
    ("Ingles Market", "Supermarket"),
    ("Intermarché", "Supermarket Chain"),
    ("Jewel-Osco", "Supermarket"),
    ("Jumbo", "Supermarket Chain"),
    ("Kaufland", "Hypermarket Chain"),
    ("Kroger", "Supermarket Chain"),
    ("Lawson", "Convenience Store Chain"),
    ("Leclerc", "Hypermarket Chain"),
    ("Lidl", "Discount Supermarket"),
    ("Loblaws", "Supermarket Chain"),
    ("Lotte Mart", "Hypermarket Chain"),
    ("LOTTE PLAZA", "Asian Supermarket"),
    ("Lulu Hypermarket", "Hypermarket Chain"),
    ("Magnit", "Supermarket Chain"),
    ("Maxi", "Supermarket Chain"),
    ("Meijer", "Supercenter"),
    ("Mercadona", "Supermarket Chain"),
    ("Metro", "Wholesale & Retail"),
    ("Migros", "Supermarket Chain"),
    ("Ministop", "Convenience Store Chain"),
    ("Monoprix", "Department Store & Supermarket"),
    ("Morrisons", "Supermarket Chain"),
], "Expense", "Food & Dining", "Groceries")

assign([
    ("Netto", "Discount Supermarket"),
    ("OXXO", "Convenience Store Chain"),
    ("ParknShop", "Supermarket Chain"),
    ("Pão de Açúcar", "Supermarket Chain"),
    ("Perekrestok", "Supermarket Chain"),
    ("Pick n Pay", "Supermarket Chain"),
    ("Price Chopper", "Supermarket"),
    ("Publix", "Supermarket"),
    ("Ralphs", "Supermarket"),
    ("Rema 1000", "Discount Supermarket"),
    ("REWE", "Supermarket Chain"),
    ("Safeway", "Supermarket"),
    ("Sainsbury's", "Supermarket Chain"),
    ("Save A Lot", "Discount Grocery Store"),
    ("Schnucks", "Supermarket"),
    ("Shoppers Drug Mart", "Pharmacy & Convenience"),
    ("ShopRite", "Supermarket"),
    ("SHOPRITE", "Supermarket"),
    ("Shufersal", "Supermarket Chain"),
    ("Sobeys", "Supermarket"),
    ("Soriana", "Hypermarket Chain"),
    ("SPAR", "Supermarket Chain"),
    ("Spinneys", "Premium Supermarket"),
    ("SPROUTS FARMERS MARKET", "Natural & Organic Grocery"),
    ("Sprouts", "Natural & Organic Grocery"),
    ("Stop & Shop", "Supermarket"),
    ("STOP & SHOP", "Supermarket"),
    ("SUBZI MANDI", "South Asian Grocery"),
    ("SAMAHA'S FARM", "Halal Grocery & Farm"),
    ("SAMAHA`S FARM", "Halal Grocery & Farm"),
    ("Tesco", "Supermarket Chain"),
    ("Tesco Lotus", "Hypermarket Chain"),
    ("Trader Joe's", "Specialty Grocery Store"),
    ("Union Coop", "Cooperative Supermarket"),
    ("Vons", "Supermarket"),
    ("Waitrose", "Premium Supermarket"),
    ("Wegmans", "Supermarket"),
    ("WEGMANS", "Supermarket"),
    ("Weis Markets", "Supermarket"),
    ("Wellcome", "Supermarket Chain"),
    ("Whole Foods", "Natural & Organic Grocery"),
    ("WHOLE FOODS", "Natural & Organic Grocery"),
    ("Winn Dixie", "Supermarket"),
    ("Winn-Dixie", "Supermarket"),
    ("Woolworths", "Supermarket Chain"),
    ("A101", "Discount Supermarket"),
    ("PATEL BROTHERS", "Indian Grocery Store"),
    ("STAR BAZAAR", "Hypermarket"),
    ("AT YOUR CONVENIENCE", "Convenience Store"),
    ("FamilyMart", "Convenience Store Chain"),
    ("7-Eleven", "Convenience Store Chain"),
    ("Cumberland Farms", "Convenience Store & Gas"),
    ("Casey's General Store", "Convenience Store & Gas"),
    ("Kwik Trip", "Convenience Store & Gas"),
    ("Kwik-E-Mart", "Convenience Store"),
    ("Stewart's Shops", "Convenience Store"),
    ("Holiday Station Stores", "Convenience Store & Gas"),
    ("QUICK CHEK", "Convenience Store"),
    ("ASDA", "Supermarket Chain"),
    ("Auchan", "Hypermarket Chain"),
    ("CONAD", "Cooperative Supermarket"),
    ("Circle K", "Convenience Store & Gas"),
    ("Sam's Club", "Wholesale Club"),
    ("Thorntons", "Convenience Store & Gas"),
    ("Tinex", "Supermarket Chain"),
    ("EMIR HALAL", "Halal Meat Market"),
    ("MARS HALAL", "Halal Meat Market"),
    ("SHAHNAWAZ HALAL MEAT.", "Halal Meat Market"),
    ("SHALIMAR HALAL MEAT", "Halal Meat Market"),
    ("SHILLEH HALAL", "Halal Meat Market"),
    ("ROBAAZ", "Halal Grocery"),
], "Expense", "Food & Dining", "Groceries")


# ============================================================
# FOOD & DINING - Fast Food
# ============================================================

assign([
    ("Arby's", "Fast Food Restaurant"),
    ("Bojangles", "Fast Food Restaurant"),
    ("Burger King", "Fast Food Restaurant"),
    ("Carl's Jr.", "Fast Food Restaurant"),
    ("Chick-fil-A", "Fast Food Restaurant"),
    ("Culver's", "Fast Casual Restaurant"),
    ("Culvers", "Fast Casual Restaurant"),
    ("Domino's", "Pizza Delivery & Carryout"),
    ("DOMINO'S", "Pizza Delivery & Carryout"),
    ("El Pollo Loco", "Fast Food Restaurant"),
    ("Firehouse Subs", "Fast Casual Sandwich Shop"),
    ("Five Guys", "Fast Casual Burger Restaurant"),
    ("In-N-Out Burger", "Fast Food Restaurant"),
    ("Jack in the Box", "Fast Food Restaurant"),
    ("Jimmy John's", "Fast Casual Sandwich Shop"),
    ("KFC", "Fast Food Restaurant"),
    ("Krispy Kreme", "Doughnut Shop & Coffee"),
    ("Little Caesars", "Pizza Chain"),
    ("McDonald's", "Fast Food Restaurant"),
    ("MCDONALD'S", "Fast Food Restaurant"),
    ("Moe's Southwest Grill", "Fast Casual Mexican"),
    ("Noodles & Company", "Fast Casual Restaurant"),
    ("Papa John's", "Pizza Delivery & Carryout"),
    ("PAPA JOHN'S", "Pizza Delivery & Carryout"),
    ("Panda Express", "Fast Food Chinese Restaurant"),
    ("Panda", "Fast Food Chinese Restaurant"),
    ("Pizza Hut", "Pizza Restaurant Chain"),
    ("Popeyes", "Fast Food Restaurant"),
    ("Quiznos", "Fast Casual Sandwich Shop"),
    ("Raising Cane's", "Fast Food Restaurant"),
    ("Raising Canes", "Fast Food Restaurant"),
    ("SBARRO", "Pizza Chain"),
    ("Schlotzsky's", "Fast Casual Sandwich Shop"),
    ("Shake Shack", "Fast Casual Burger Restaurant"),
    ("Sonic Drive In", "Fast Food Drive-In"),
    ("Subway", "Fast Food Sandwich Chain"),
    ("Taco Bell", "Fast Food Mexican Restaurant"),
    ("TACO BELL", "Fast Food Mexican Restaurant"),
    ("Taco 911", "Fast Food Taco Shop"),
    ("Taco Fiesta", "Fast Food Taco Shop"),
    ("Wendy's", "Fast Food Restaurant"),
    ("WENDY'S", "Fast Food Restaurant"),
    ("Whataburger", "Fast Food Restaurant"),
    ("Wingstop", "Fast Casual Wing Restaurant"),
    ("Zaxby's", "Fast Casual Chicken Restaurant"),
    ("Burger Bliss", "Fast Casual Burger Restaurant"),
    ("SMASHVILLE HOT CHICKEN", "Fast Casual Chicken Restaurant"),
    ("ROUND PIE PIZZA", "Pizzeria"),
    ("THE PIZZERIA", "Pizzeria"),
    ("SALERNOS PIZZERIA", "Pizzeria"),
    ("Jaans Pizza", "Pizzeria"),
    ("Mighty Pizza", "Pizzeria"),
    ("Pizza Paradise", "Pizzeria"),
    ("DOORDASH CROWN FRIED CHICKEN", "Fried Chicken Restaurant"),
    ("ROYAL CHICKEN", "Fried Chicken Restaurant"),
    ("GERMAN DONER KEBAB", "Fast Casual Kebab Restaurant"),
    ("CHIPOTLE", "Fast Casual Mexican"),
    ("Chipotle", "Fast Casual Mexican"),
    ("JENKINSON'S CANDY", "Confectionery & Candy Shop"),
    ("GOLDIE LOX", "Fast Casual Restaurant"),
    ("MDC WENDYS", "Fast Food Restaurant"),
    ("MDM JERRYS", "Fast Food Restaurant"),
], "Expense", "Food & Dining", "Fast Food")


# ============================================================
# FOOD & DINING - Restaurants
# ============================================================

assign([
    ("AUBONPAIN", "Bakery Cafe Chain"),
    ("Applebee's", "Casual Dining Restaurant"),
    ("BAITHAKH RESTAURANT", "South Asian Restaurant"),
    ("Bratwurst Haus", "German Sausage Restaurant"),
    ("CHARRITOS", "Mexican Restaurant"),
    ("CHEESECAKE FACTORY", "Casual Dining Restaurant"),
    ("Corner Bakery Cafe", "Bakery Cafe"),
    ("Cracker Barrel", "Family Restaurant & Gift Shop"),
    ("Einstein Bros Bagels", "Bagel Shop & Deli"),
    ("FLAME KABOB", "Middle Eastern Restaurant"),
    ("GYRO", "Greek Fast Food"),
    ("Gyros Galore", "Greek Restaurant"),
    ("HALAL EATZ", "Halal Restaurant"),
    ("IBBY'S FALAFEL", "Middle Eastern Restaurant"),
    ("IHOP", "Family Restaurant (Pancakes)"),
    ("Jason's Deli", "Deli & Sandwich Restaurant"),
    ("Jersey Mike's", "Sub Sandwich Restaurant"),
    ("GRUBHUB JERSEY MIKES", "Sub Sandwich Restaurant"),
    ("KABAB PARADISE", "Middle Eastern Restaurant"),
    ("KANDAHAR", "Afghan Restaurant"),
    ("KARAHI HOUSE", "Pakistani Restaurant"),
    ("Kebab King Istanbul", "Turkish Kebab Restaurant"),
    ("LA CONTESSA", "Italian Restaurant"),
    ("LAHORE RESTAURANT", "Pakistani Restaurant"),
    ("MAZA RESTAURANTS", "Middle Eastern Restaurant"),
    ("McAlister's Deli", "Deli & Sandwich Restaurant"),
    ("N THAI", "Thai Restaurant"),
    ("Olive Garden", "Italian Casual Dining"),
    ("Panera Bread", "Bakery Cafe Chain"),
    ("Pasta Paradise", "Italian Restaurant"),
    ("Paella Paradise", "Spanish Restaurant"),
    ("Pierogi Palace", "Eastern European Restaurant"),
    ("Potbelly Sandwich Shop", "Sandwich Restaurant"),
    ("Poutine Paradise", "Canadian Restaurant"),
    ("RAAVI NAAN KABAB", "Pakistani Restaurant"),
    ("RIFFYS KITCHEN", "Restaurant"),
    ("Schnitzel Haus", "German Restaurant"),
    ("Schnitzel Shack", "German Restaurant"),
    ("SHAAN GRILL", "South Asian Grill"),
    ("Sizzling Szechuan", "Chinese Szechuan Restaurant"),
    ("Spicy Ramen", "Japanese Ramen Restaurant"),
    ("Sushi Sensation", "Japanese Sushi Restaurant"),
    ("Sushi Supreme", "Japanese Sushi Restaurant"),
    ("Tapas Bar", "Spanish Tapas Bar"),
    ("Tapas Town", "Spanish Tapas Restaurant"),
    ("TERMINAL 9 GRILL", "Bar & Grill"),
    ("Texas Roadhouse", "Steakhouse"),
    ("THE HALAL CRAVE", "Halal Restaurant"),
    ("TGI Fridays", "Casual Dining Restaurant"),
    ("THE ANCHOR FISH", "Seafood Restaurant"),
    ("TURKUAZ RESTAURANT", "Turkish Restaurant"),
    ("TURNING POINT", "Breakfast & Brunch Restaurant"),
    ("GOOD FOOD BY UZMA", "Home Kitchen Restaurant"),
    ("GRUBHUB GOOD FOOD BY UZMA", "Home Kitchen Restaurant"),
    ("ZAIKA BBQ", "South Asian BBQ Restaurant"),
    ("Falafel Feast", "Middle Eastern Restaurant"),
    ("Currywurst Corner", "German Street Food"),
    ("Fish and Chips", "British Fish & Chips Shop"),
    ("DOORDASH KANDAHAR", "Afghan Restaurant"),
    ("DOORDASH KHOKHA", "South Asian Restaurant"),
    ("DOORDASH RIFFYS KITCHEN", "Restaurant"),
    ("DOORDASH ROUND PIE PIZZA", "Pizzeria"),
    ("GRUBHUB ROUND PIE PIZZA", "Pizzeria"),
    ("GRUBHUB MCDONALDS", "Fast Food Restaurant"),
    ("DOORDASH MCDONALDS", "Fast Food Restaurant"),
    ("Food Truck", "Mobile Food Vendor"),
    ("The Cheesecake Factory", "Casual Dining Restaurant"),
    ("FRIENDLY", "Family Restaurant"),
    ("JIN SOY", "Asian Restaurant"),
    ("SAHARA", "Middle Eastern Restaurant"),
    ("Sub Zero", "Ice Cream & Dessert Shop"),
    ("MEAL MAGIC", "Meal Prep Service"),
], "Expense", "Food & Dining", "Restaurants")


# ============================================================
# FOOD & DINING - Coffee & Tea
# ============================================================

assign([
    ("Starbucks", "Coffee Shop Chain"),
    ("STARBUCKS", "Coffee Shop Chain"),
    ("Peet's Coffee", "Specialty Coffee Roaster"),
    ("MDC PEETS", "Specialty Coffee Roaster"),
    ("Dunkin' Donuts", "Coffee & Donut Chain"),
    ("DUNKIN", "Coffee & Donut Chain"),
    ("DOORDASH DUNKIN", "Coffee & Donut Chain"),
    ("DAVIDsTEA", "Specialty Tea Retailer"),
    ("Local Coffee Brewery", "Independent Coffee Shop"),
    ("Coffee Haven", "Coffee Shop"),
    ("REFRESH TEA", "Tea House"),
    ("TEN TEA", "Bubble Tea Shop"),
], "Expense", "Food & Dining", "Coffee & Tea")

# ============================================================
# FOOD & DINING - Bakery & Desserts
# ============================================================

assign([
    ("ABBATE BAKERY", "Bakery"),
    ("BAKED BY MELISSA", "Specialty Cupcake Bakery"),
    ("Boulangerie Baguette Magique", "French Artisan Bakery"),
    ("Boulangerie Fougasse", "French Artisan Bakery"),
    ("Boulangerie Le Petit Pain", "French Artisan Bakery"),
    ("Boulangerie Pain au Chocolat", "French Artisan Bakery"),
    ("Boulangerie Pain aux Cereales", "French Artisan Bakery"),
    ("Boulangerie Pain aux Figues", "French Artisan Bakery"),
    ("Boulangerie Pain aux Graines", "French Artisan Bakery"),
    ("Boulangerie Pain aux Noix", "French Artisan Bakery"),
    ("Boulangerie Pain aux Olives", "French Artisan Bakery"),
    ("Boulangerie Pain aux Raisins", "French Artisan Bakery"),
    ("Boulangerie Pain de Campagne", "French Artisan Bakery"),
    ("Boulangerie Pain de Seigle", "French Artisan Bakery"),
    ("Boulangerie Patisserie Artisanale", "French Artisan Bakery & Patisserie"),
    ("Cinnabon", "Cinnamon Roll Bakery Chain"),
    ("CINNABON-CARVEL", "Bakery & Ice Cream Combo"),
    ("LA BON BAKE SHOPPES", "Bakery"),
    ("Patisserie Chocolaterie Delice", "French Patisserie"),
    ("Patisserie Chouquette", "French Patisserie"),
    ("Patisserie Eclair", "French Patisserie"),
    ("Patisserie Financier", "French Patisserie"),
    ("Patisserie Gateaux Divins", "French Patisserie"),
    ("Patisserie Macaron", "French Patisserie"),
    ("Patisserie Madeleine", "French Patisserie"),
    ("Patisserie Mille-Feuille", "French Patisserie"),
    ("Patisserie Opera Cake", "French Patisserie"),
    ("Patisserie Palmier", "French Patisserie"),
    ("Patisserie Paris-Brest", "French Patisserie"),
    ("Patisserie Religieuse", "French Patisserie"),
    ("Patisserie Saint Honore", "French Patisserie"),
    ("Positive Bakery", "Bakery"),
    ("ROSETTA BAKERY", "Italian Bakery"),
    ("Wetzel's Pretzels", "Soft Pretzel Chain"),
    ("AUNTIE ANNE'S", "Soft Pretzel Chain"),
    ("Auntie Anne's", "Soft Pretzel Chain"),
], "Expense", "Food & Dining", "Bakery & Desserts")

# ============================================================
# FOOD & DINING - Ice Cream & Yogurt
# ============================================================

assign([
    ("Baskin Robbins", "Ice Cream Chain"),
    ("Cold Stone Creamery", "Ice Cream Chain"),
    ("COLD STONE", "Ice Cream Chain"),
    ("Dairy Queen", "Ice Cream & Fast Food Chain"),
    ("Frozen Yogurt", "Frozen Yogurt Shop"),
    ("Gelato Dreams", "Gelato Shop"),
    ("Gelateria Artigianale", "Artisan Gelato Shop"),
    ("ICE CREAM MONSTER", "Ice Cream Shop"),
    ("ICECREAM TRUCK", "Mobile Ice Cream Vendor"),
    ("ICY MELON", "Frozen Dessert Shop"),
    ("JOYCE CREAMERY", "Ice Cream Shop"),
    ("Menchie's", "Self-Serve Frozen Yogurt"),
    ("Orange Leaf", "Self-Serve Frozen Yogurt"),
    ("Pinkberry", "Frozen Yogurt Chain"),
    ("Red Mango", "Frozen Yogurt Chain"),
    ("SWEET ICE CREAMERY", "Ice Cream Shop"),
    ("Sweet Frog", "Self-Serve Frozen Yogurt"),
    ("TCBY", "Frozen Yogurt Chain"),
    ("Tutti Frutti", "Self-Serve Frozen Yogurt"),
    ("Yogen Früz", "Frozen Yogurt Chain"),
    ("Yogurt City", "Frozen Yogurt Shop"),
    ("Yogurt Mountain", "Self-Serve Frozen Yogurt"),
    ("Yogurt World", "Frozen Yogurt Shop"),
    ("Yogurt Zone", "Frozen Yogurt Shop"),
    ("Yogurtland", "Self-Serve Frozen Yogurt"),
    ("SUNDAES INTERNATIONAL", "Ice Cream & Sundae Shop"),
], "Expense", "Food & Dining", "Ice Cream & Yogurt")

# ============================================================
# FOOD & DINING - Food Delivery
# ============================================================

assign([
    ("DoorDash", "Food Delivery Platform"),
    ("DOORDASH CROWN FRIED CHICKEN", "Food Delivery Platform"),
    ("Deliveroo", "Food Delivery Platform"),
    ("Foodora", "Food Delivery Platform"),
    ("Foodpanda", "Food Delivery Platform"),
    ("Glovo", "Multi-Category Delivery Platform"),
    ("GrubHub", "Food Delivery Platform"),
    ("Grubhub", "Food Delivery Platform"),
    ("Instacart", "Grocery Delivery Platform"),
    ("Jumia Food", "Food Delivery Platform"),
    ("Just Eat", "Food Delivery Platform"),
    ("Postmates", "Multi-Category Delivery Platform"),
    ("Rappi", "Multi-Category Delivery Platform"),
    ("Seamless", "Food Delivery Platform"),
    ("Skip The Dishes", "Food Delivery Platform"),
    ("Swiggy", "Food Delivery Platform"),
    ("Takeaways", "Food Delivery Platform"),
    ("Talabat", "Food Delivery Platform"),
    ("UBR POSTMATES", "Multi-Category Delivery Platform"),
    ("Uber Eats", "Food Delivery Platform"),
    ("UBER EATS", "Food Delivery Platform"),
    ("Wolt", "Food Delivery Platform"),
    ("Zomato", "Food Delivery & Restaurant Discovery"),
    ("Caviar", "Premium Food Delivery Platform"),
], "Expense", "Food & Dining", "Food Delivery")

# ============================================================
# FOOD & DINING - Snacks & Drinks
# ============================================================

assign([
    ("JUICE AND DESSERT", "Juice Bar & Dessert Shop"),
    ("Jamba Juice", "Smoothie & Juice Chain"),
    ("Smoothie King", "Smoothie Chain"),
    ("REAL FRUIT BUBBLE", "Bubble Tea Shop"),
    ("KING SWEETS", "South Asian Sweet Shop"),
    ("SHALIMAR SWEETS", "South Asian Sweet Shop"),
    ("GERTRUDE HAWK CHOCOLATE", "Chocolatier & Candy Shop"),
    ("POTATO PALOOZA", "Specialty Snack Shop"),
    ("FERRERO ROCHER", "Chocolate & Confectionery"),
    ("Ferrero Rocher", "Chocolate & Confectionery"),
    ("NAYAX VENDING", "Vending Machine Operator"),
], "Expense", "Food & Dining", "Snacks & Drinks")


# ============================================================
# TRANSPORTATION
# ============================================================

assign([
    ("BP", "Gas Station & Convenience"),
    ("Chevron", "Gas Station"),
    ("CITGO", "Gas Station"),
    ("Citgo", "Gas Station"),
    ("CONOCO", "Gas Station"),
    ("Conoco", "Gas Station"),
    ("COSTCO GAS", "Wholesale Club Gas Station"),
    ("Exxon Mobil", "Gas Station"),
    ("EXXON MOBIL", "Gas Station"),
    ("Marathon", "Gas Station"),
    ("PHILLIPS 66", "Gas Station"),
    ("Phillips 66", "Gas Station"),
    ("Pilot Travel", "Truck Stop & Travel Center"),
    ("RaceTrac", "Gas Station & Convenience"),
    ("QuikTrip", "Gas Station & Convenience"),
    ("SHELL OIL", "Gas Station"),
    ("Shell", "Gas Station"),
    ("SPEEDWAY", "Gas Station & Convenience"),
    ("Speedway", "Gas Station & Convenience"),
    ("SUNOCO", "Gas Station"),
    ("Sunoco", "Gas Station"),
    ("Texaco", "Gas Station"),
    ("Valero", "Gas Station"),
    ("Love's Travel Stops", "Truck Stop & Travel Center"),
    ("Maverik", "Gas Station & Convenience"),
    ("Sheetz", "Gas Station & Convenience Store"),
    ("Wawa", "Gas Station & Convenience Store"),
    ("WAWA", "Gas Station & Convenience Store"),
], "Expense", "Transportation", "Gas & Fuel")

assign([
    ("Bolt", "Ride-Hailing Service"),
    ("Cabify", "Ride-Hailing Service"),
    ("Careem", "Ride-Hailing Service"),
    ("DiDi", "Ride-Hailing Service"),
    ("Gett", "Ride-Hailing Service"),
    ("Gojek", "Ride-Hailing & Multi-Service"),
    ("Grab", "Ride-Hailing & Multi-Service"),
    ("Kakao T", "Ride-Hailing Service"),
    ("Lyft", "Ride-Hailing Service"),
    ("Mytaxi", "Ride-Hailing Service"),
    ("Ola", "Ride-Hailing Service"),
    ("Taxify", "Ride-Hailing Service"),
    ("Uber", "Ride-Hailing Service"),
    ("UBER", "Ride-Hailing Service"),
], "Expense", "Transportation", "Rideshare")

assign([
    ("NJ TRANSIT", "Public Transit Authority"),
    ("NEW JERSEY E-ZPASS", "Electronic Toll Collection"),
    ("NJ EZPASS", "Electronic Toll Collection"),
], "Expense", "Transportation", "Public Transit")

assign([
    ("SPOTHERO", "Parking Reservation App"),
], "Expense", "Transportation", "Tolls & Parking")

assign([
    ("Advance Auto Parts", "Auto Parts Retailer"),
    ("AutoZone", "Auto Parts Retailer"),
    ("CIRCLE CHEVROLET", "Automobile Dealership"),
    ("DCH ACADEMY HONDA", "Automobile Dealership"),
    ("HONDA", "Automobile Manufacturer"),
    ("HYUNDAI BLUE LINK", "Connected Car Service"),
    ("HYUNDAI SERVICE", "Automobile Service Center"),
    ("NRS Tint Shop", "Auto Window Tinting"),
    ("PEP BOYS", "Auto Parts & Service"),
    ("REYDEL VOLKSWAGEN", "Automobile Dealership"),
    ("Volkswagen", "Automobile Manufacturer"),
    ("XPEL", "Paint Protection Film"),
], "Expense", "Transportation", "Car Service & Parts")


# ============================================================
# SHOPPING
# ============================================================

assign([
    ("AMAZON.COM", "Online Marketplace"),
    ("Amazon", "Online Marketplace"),
    ("AMAZON DIGITAL", "Digital Content Store"),
    ("Dollar General", "Discount Variety Store"),
    ("DOLLAR GENERAL", "Discount Variety Store"),
    ("Dollar Tree", "Dollar Store Chain"),
    ("DOLLAR TREE", "Dollar Store Chain"),
    ("DOLLARTREE", "Dollar Store Chain"),
    ("DOLLARS N THINGS", "Dollar Store"),
    ("A DOLLAR", "Dollar Store"),
    ("A-Z DOLLAR", "Dollar Store"),
    ("M CITY DOLLAR", "Dollar Store"),
    ("FAMILY DOLLAR", "Discount Variety Store"),
    ("Family Dollar", "Discount Variety Store"),
    ("FIVE BELOW", "Discount Retailer (Under $5)"),
    ("MARSHALLS", "Off-Price Department Store"),
    ("Marshalls", "Off-Price Department Store"),
    ("HOMEGOODS", "Home Furnishings Retailer"),
    ("Overstock", "Online Discount Retailer"),
    ("Ross", "Off-Price Department Store"),
    ("T.J. Maxx", "Off-Price Department Store"),
    ("Target", "General Merchandise Retailer"),
    ("TARGET", "General Merchandise Retailer"),
    ("Walmart", "Supercenter & General Merchandise"),
    ("WALMART", "Supercenter & General Merchandise"),
    ("PAYPAL WALMART", "Supercenter & General Merchandise"),
    ("Wayfair", "Online Home Goods Retailer"),
    ("Wish", "Online Discount Marketplace"),
    ("eBay", "Online Auction & Marketplace"),
    ("Ali Express", "Online Marketplace (China)"),
    ("AMERICAN DREAM MALL", "Shopping & Entertainment Complex"),
    ("MINISO", "Variety Store Chain"),
    ("Etsy", "Handmade & Vintage Marketplace"),
    ("ETSY", "Handmade & Vintage Marketplace"),
    ("CLAIRE'S", "Fashion Accessories Retailer"),
    ("Michaels", "Arts & Crafts Retailer"),
    ("MICHAELS", "Arts & Crafts Retailer"),
    ("LOVELY", "Gift & Variety Store"),
    ("Jerry's PC Enterprise", "Computer Parts Retailer"),
    ("Jerico's Dairy", "Dairy Products Store"),
], "Expense", "Shopping", "General Retail")

assign([
    ("Abercrombie & Fitch", "Casual Apparel Retailer"),
    ("Adidas", "Athletic Apparel & Footwear"),
    ("Aerie", "Intimates & Loungewear"),
    ("American Eagle", "Casual Apparel Retailer"),
    ("Anthropologie", "Women's Apparel & Home"),
    ("Balenciaga", "Luxury Fashion House"),
    ("Banana Republic", "Premium Casual Apparel"),
    ("Birkenstock", "Footwear Manufacturer"),
    ("Bulgari", "Luxury Jewelry & Accessories"),
    ("BURLINGTON STORES", "Off-Price Department Store"),
    ("Canada Goose", "Premium Outerwear Brand"),
    ("Coach", "Luxury Handbags & Accessories"),
    ("Crocs", "Casual Footwear Brand"),
    ("Dior", "Luxury Fashion House"),
    ("Dolce & Gabbana", "Luxury Fashion House"),
    ("Express", "Fashion Apparel Retailer"),
    ("Fendi", "Luxury Fashion House"),
    ("Ferrari Store", "Luxury Brand Merchandise"),
    ("Forever 21", "Fast Fashion Retailer"),
    ("Fossil", "Watches & Accessories"),
    ("Gap", "Casual Apparel Retailer"),
    ("Gucci", "Luxury Fashion House"),
    ("H & M", "Fast Fashion Retailer"),
    ("H&M", "Fast Fashion Retailer"),
    ("Hollister", "Teen Casual Apparel"),
    ("J. Crew", "Preppy Apparel Retailer"),
    ("J.Crew", "Preppy Apparel Retailer"),
    ("JCPenney", "Department Store"),
    ("Kohl's", "Department Store"),
    ("KOHL'S", "Department Store"),
    ("L.L.Bean", "Outdoor Apparel & Gear"),
    ("Louis Vuitton", "Luxury Fashion House"),
    ("Lululemon", "Athletic Apparel (Yoga)"),
    ("Mango", "Fashion Apparel Retailer"),
    ("New Balance", "Athletic Footwear & Apparel"),
    ("Nike", "Athletic Apparel & Footwear"),
    ("Nordstrom", "Upscale Department Store"),
    ("Old Navy", "Value Casual Apparel"),
    ("OLD NAVY", "Value Casual Apparel"),
    ("Prada", "Luxury Fashion House"),
    ("PUMA", "Athletic Apparel & Footwear"),
    ("Ralph Lauren", "Premium Fashion & Lifestyle"),
    ("Reebok", "Athletic Footwear & Apparel"),
    ("Revolution Clothing", "Fashion Retailer"),
    ("Skechers", "Casual & Athletic Footwear"),
    ("Ted Baker", "Designer Fashion Brand"),
    ("The North Face", "Outdoor Apparel & Gear"),
    ("Tiffany's", "Luxury Jewelry Retailer"),
    ("Tissot", "Swiss Watch Manufacturer"),
    ("Tommy Hilfiger", "Premium Fashion Brand"),
    ("Under Armour", "Athletic Apparel & Footwear"),
    ("Uniqlo", "Casual Apparel Retailer"),
    ("Vans", "Skate & Casual Footwear"),
    ("Yves Saint Laurent", "Luxury Fashion House"),
    ("Zara", "Fast Fashion Retailer"),
    ("ZGMYC Fashion Leopard", "Fashion Accessories"),
    ("Omega", "Luxury Swiss Watch"),
    ("Zappos", "Online Shoe & Apparel Retailer"),
    ("FILA", "Athletic Apparel & Footwear"),
    ("FIT N FEET", "Footwear Retailer"),
    ("FLYNN & O HARA", "School Uniform Supplier"),
    ("KIDS FOOT LOCKER", "Children's Athletic Footwear"),
    ("Foot Locker", "Athletic Footwear Retailer"),
    ("Cartier", "Luxury Jewelry & Watches"),
    ("Asos", "Online Fashion Retailer"),
    ("CHAMPION", "Athletic Apparel Brand"),
    ("Macy's", "Department Store"),
    ("Pandora", "Jewelry Retailer"),
], "Expense", "Shopping", "Clothing & Apparel")

assign([
    ("Acer", "Computer Hardware Manufacturer"),
    ("AMD", "Semiconductor Manufacturer"),
    ("Apple", "Consumer Electronics & Software"),
    ("APPLE", "Consumer Electronics & Software"),
    ("ASUS", "Computer Hardware Manufacturer"),
    ("B&H PHOTO", "Electronics & Camera Retailer"),
    ("Beats", "Audio Equipment Brand"),
    ("BenQ", "Display & Projector Manufacturer"),
    ("Best Buy", "Consumer Electronics Retailer"),
    ("BESTBUY", "Consumer Electronics Retailer"),
    ("Bose", "Audio Equipment Manufacturer"),
    ("Canon", "Camera & Imaging Manufacturer"),
    ("Dell", "Computer Hardware Manufacturer"),
    ("DJI", "Drone & Camera Manufacturer"),
    ("Ford", "Automobile Manufacturer"),
    ("HP", "Computer Hardware Manufacturer"),
    ("Intel", "Semiconductor Manufacturer"),
    ("Lenovo", "Computer Hardware Manufacturer"),
    ("LG", "Electronics Manufacturer"),
    ("MACSALES.COM", "Mac Hardware & Upgrades"),
    ("Mattel", "Toy Manufacturer"),
    ("Microsoft", "Software & Hardware Company"),
    ("MSI", "Computer Hardware Manufacturer"),
    ("Netgear", "Networking Equipment Manufacturer"),
    ("NVIDIA", "Semiconductor & GPU Manufacturer"),
    ("OTHER WORLD COMPUTING", "Mac & PC Hardware Retailer"),
    ("Qualcomm", "Semiconductor Manufacturer"),
    ("Razer", "Gaming Peripherals Manufacturer"),
    ("Samsung", "Electronics Conglomerate"),
    ("Sony", "Electronics & Entertainment"),
    ("TESLA", "Electric Vehicle & Energy Company"),
    ("Tesla", "Electric Vehicle & Energy Company"),
], "Expense", "Shopping", "Electronics")


assign([
    ("Abagail Furniture", "Furniture Store"),
    ("Ace Hardware", "Hardware Store"),
    ("ANDERSEN WINDOWS", "Window & Door Manufacturer"),
    ("BED BATH & BEYOND", "Home Goods Retailer"),
    ("Bed Bath & Beyond", "Home Goods Retailer"),
    ("HOME DEPOT", "Home Improvement Retailer"),
    ("Home Depot", "Home Improvement Retailer"),
    ("IKEA", "Furniture & Home Goods Retailer"),
    ("LOWES", "Home Improvement Retailer"),
    ("Lowe's", "Home Improvement Retailer"),
    ("Pottery Barn", "Home Furnishings Retailer"),
    ("YANKEE CANDLE", "Candle & Home Fragrance"),
    ("ARCTIC AIR", "Portable Air Cooler Brand"),
    ("GUARDIAN TECHNOLOGIES", "Air Purifier Manufacturer"),
    ("CRYSTAL SPRINGS", "Water Delivery Service"),
    ("DS SERVICES", "Water & Coffee Delivery"),
    ("PRIMO WATER", "Water Delivery & Dispensers"),
    ("HandyTools", "Tools & Hardware Store"),
    ("RangeShop", "Appliance Retailer"),
    ("NORDMARK PURE", "Home & Air Products"),
    ("NORDIC PURE", "Air Filter Manufacturer"),
    ("The Bricks", "Furniture & Appliance Store"),
], "Expense", "Shopping", "Home & Garden")

assign([
    ("Academy", "Sporting Goods Retailer"),
    ("Bass Pro Shops", "Outdoor & Sporting Goods"),
    ("Dick's Sporting Goods", "Sporting Goods Retailer"),
    ("DICK'S CLOTHING & SPORT", "Sporting Goods Retailer"),
    ("Hibbett Sports", "Athletic Footwear & Apparel"),
    ("RTIC Outdoors", "Outdoor Coolers & Drinkware"),
    ("Salty Crew", "Fishing & Surf Apparel"),
    ("Sports Authority", "Sporting Goods Retailer"),
    ("Sports Store", "Sporting Goods Retailer"),
    ("TEAM EXPRESS", "Team Sports Equipment"),
    ("LS SKATE PRO INC.", "Skateboard Shop"),
], "Expense", "Shopping", "Sporting Goods")

assign([
    ("Office Depot", "Office Supply Retailer"),
    ("Staples", "Office Supply Retailer"),
    ("STAPLES", "Office Supply Retailer"),
], "Expense", "Shopping", "Office Supplies")

assign([
    ("Groupon", "Online Deals & Coupons"),
    ("StubHub", "Event Ticket Marketplace"),
], "Expense", "Shopping", "Online Marketplace")

assign([
    ("Chewy", "Online Pet Supply Retailer"),
    ("Petco", "Pet Supply Retailer"),
    ("PetSmart", "Pet Supply Retailer"),
], "Expense", "Shopping", "Pet Supplies")

assign([
    ("Audible", "Audiobook & Podcast Service"),
    ("Barnes & Noble", "Book Retailer"),
    ("BARNES & NOBLE", "Book Retailer"),
    ("Books-A-Million", "Book Retailer"),
    ("Goodreads", "Book Community Platform"),
    ("Scholastic", "Children's Book Publisher"),
    ("SCHOLASTIC BOOK FAIRS", "Children's Book Fair"),
    ("KENDALL HUNT PUBLISHING", "Educational Publisher"),
], "Expense", "Shopping", "Books & Media")

assign([
    ("PARTY CITY", "Party Supply Retailer"),
    ("Party City", "Party Supply Retailer"),
], "Expense", "Shopping", "Discount Stores")


# ============================================================
# ENTERTAINMENT
# ============================================================

assign([
    ("AMAZON PRIME VIDEO", "Video Streaming Service"),
    ("AMAZON PRIME", "Subscription Streaming & Shipping"),
    ("BritBox", "British TV Streaming Service"),
    ("Cinemax", "Premium Cable & Streaming"),
    ("Criterion Channel", "Classic Film Streaming"),
    ("Crunchyroll", "Anime Streaming Service"),
    ("DISNEY PLUS", "Video Streaming Service"),
    ("Disney+", "Video Streaming Service"),
    ("Discovery+", "Reality & Documentary Streaming"),
    ("ESPN", "Sports Broadcasting Network"),
    ("Fubo", "Sports Streaming Service"),
    ("Funimation", "Anime Streaming Service"),
    ("HBO", "Premium Cable & Streaming"),
    ("Hulu", "Video Streaming Service"),
    ("MUBI", "Curated Film Streaming"),
    ("Netflix", "Video Streaming Service"),
    ("NETFLIX.COM", "Video Streaming Service"),
    ("Paramount+", "Video Streaming Service"),
    ("Peacock", "Video Streaming Service"),
    ("Philo", "Live TV Streaming Service"),
    ("Plex", "Media Server & Streaming"),
    ("Prime Video", "Video Streaming Service"),
    ("Roku", "Streaming Media Player & Service"),
    ("Showtime", "Premium Cable & Streaming"),
    ("Shudder", "Horror Streaming Service"),
    ("Sling TV", "Live TV Streaming Service"),
    ("Starz", "Premium Cable & Streaming"),
    ("Sundance Now", "Independent Film Streaming"),
    ("Tubi", "Free Video Streaming Service"),
    ("Vimeo", "Video Hosting Platform"),
    ("Vudu", "Video on Demand Service"),
    ("YouTube", "Video Sharing & Streaming"),
    ("GOOGLE YOUTUBE", "Video Sharing & Streaming"),
    ("Curiosity Stream", "Documentary Streaming Service"),
], "Expense", "Entertainment", "Streaming Video")

assign([
    ("Spotify", "Music Streaming Service"),
    ("Tidal", "Hi-Fi Music Streaming Service"),
], "Expense", "Entertainment", "Streaming Music")

assign([
    ("Activision", "Video Game Publisher"),
    ("Electronic Arts", "Video Game Publisher"),
    ("GameStop", "Video Game Retailer"),
    ("Gamestop", "Video Game Retailer"),
    ("Nintendo", "Video Game Company"),
    ("PlayStation", "Video Game Console & Service"),
    ("Xbox Live", "Gaming Subscription Service"),
    ("Twitch", "Live Streaming Platform (Gaming)"),
    ("Discord", "Gaming Communication Platform"),
], "Expense", "Entertainment", "Gaming")

assign([
    ("AMC", "Movie Theater Chain"),
    ("Broadway", "Live Theater"),
    ("CINEMARK", "Movie Theater Chain"),
    ("CONDOCERTS", "Concert & Live Events"),
    ("RCMH FOOD & MERCH", "Entertainment Venue Concessions"),
    ("Ticketmaster", "Event Ticketing Platform"),
    ("TICKETMASTER", "Event Ticketing Platform"),
    ("NYC FILM LAB", "Film Processing Laboratory"),
    ("NOMURA", "Entertainment Venue"),
    ("NOMURA CAF\xe9", "Entertainment Venue Cafe"),
    ("NOMURA CAF\ufffd", "Entertainment Venue Cafe"),
    ("WAVE HOSPITALITY", "Hospitality & Events"),
    ("SHOWCASE", "Entertainment & Retail"),
    ("VFS SERVICES", "Visa & Travel Services"),
    ("SUBMITTABLE", "Submission Management Platform"),
    ("LAAM TECHNOLOGIES", "Entertainment Technology"),
    ("MAZUMDER ENTERTAINMENT", "Entertainment Services"),
    ("RAVE", "Movie Theater Chain"),
    ("Bingo", "Bingo Hall & Gaming"),
    ("Oh Happy Day", "Event & Party Planning"),
    ("FRAN LEBOWITZ", "Author & Speaker Event"),
    ("SUMMIT ONE", "Observation Deck & Attraction"),
], "Expense", "Entertainment", "Movies & Events")

assign([
    ("BEAR MOUNTAIN", "State Park & Hiking"),
    ("CHILDREN'S MUSEUM", "Children's Museum"),
    ("CRAYOLA EXPERIENCE", "Family Attraction"),
    ("ESCAPOLOGY", "Escape Room Entertainment"),
    ("HERITAGE AMUSEMENT", "Amusement Park"),
    ("JENKINSON'S AQUARIUM", "Aquarium & Boardwalk"),
    ("JENKINSON'S PAVILLION", "Boardwalk Amusement"),
    ("LEGOLAND DISCOVERY", "Theme Park & Discovery Center"),
    ("LIBERTY SCIENCE CENTER", "Science Museum"),
    ("LUMINOCITY", "Holiday Light Festival"),
    ("PLAYLAND", "Amusement Park"),
    ("ROCK N AIR ADVENTURE", "Trampoline & Adventure Park"),
    ("Space Needle", "Observation Tower & Attraction"),
    ("URBAN AIR", "Trampoline & Adventure Park"),
    ("FUN KIDS TRAIN", "Children's Ride Attraction"),
    ("FANTASY RIDE", "Amusement Ride"),
    ("AIR PLAY", "Indoor Play Center"),
    ("SWING LOOSE", "Indoor Play & Recreation"),
    ("HERSHEY PARK", "Theme & Amusement Park"),
], "Expense", "Entertainment", "Amusement & Parks")

assign([
    ("Gulfstream Park", "Horse Racing & Casino"),
    ("NFL Shop", "Professional Sports Merchandise"),
    ("MONMOUTH COUNTY PARK", "County Park System"),
    ("OLD BRIDGE PARK", "Municipal Park & Recreation"),
    ("SPRING LAKE COMMUNITY", "Community Recreation Center"),
    ("NEW JERSEY TITANS HOCKEY", "Youth Hockey Organization"),
], "Expense", "Entertainment", "Sports & Recreation")

assign([
    ("ARC STUDIO", "Art Studio & Creative Space"),
], "Expense", "Entertainment", "Arts & Hobbies")


# ============================================================
# TRAVEL
# ============================================================

assign([
    ("Alaska Airlines", "Commercial Airline"),
    ("Allegiant Air", "Ultra-Low-Cost Airline"),
    ("American Airlines", "Commercial Airline"),
    ("Delta Air Lines", "Commercial Airline"),
    ("ETIHAD AIRWAYS", "Commercial Airline"),
    ("Frontier Airlines", "Ultra-Low-Cost Airline"),
    ("Hawaiian Airlines", "Commercial Airline"),
    ("JetBlue", "Low-Cost Airline"),
    ("QATAR AIRWAYS", "Commercial Airline"),
    ("SAS", "Commercial Airline (Scandinavian)"),
    ("Southwest Airlines", "Low-Cost Airline"),
    ("Spirit Airlines", "Ultra-Low-Cost Airline"),
    ("United Airlines", "Commercial Airline"),
], "Expense", "Travel", "Airlines")

assign([
    ("Airbnb", "Short-Term Rental Platform"),
    ("Best Western", "Hotel Chain"),
    ("COMFORT INNS", "Hotel Chain (Economy)"),
    ("COURTYARD BY MARRIOT", "Hotel Chain (Select-Service)"),
    ("Four Seasons", "Luxury Hotel Chain"),
    ("Grand Hyatt", "Luxury Hotel Brand"),
    ("HAMPTON INNS", "Hotel Chain (Economy)"),
    ("Hilton", "Hotel Chain"),
    ("Hilton Garden Inn", "Hotel Chain (Upscale)"),
    ("Hyatt", "Hotel Chain"),
    ("Hyatt Regency", "Hotel Chain (Upscale)"),
    ("Intercontinental", "Luxury Hotel Chain"),
    ("Mandarin Oriental", "Luxury Hotel Chain"),
    ("Marriott", "Hotel Chain"),
    ("Park Hyatt", "Luxury Hotel Brand"),
    ("Peninsula Hotel", "Luxury Hotel Chain"),
    ("Ritz-Carlton", "Luxury Hotel Chain"),
    ("Shangri-La", "Luxury Hotel Chain"),
    ("Sheraton", "Hotel Chain (Upscale)"),
    ("Sofitel", "Luxury Hotel Chain"),
    ("St. Regis", "Luxury Hotel Brand"),
    ("W Hotel", "Lifestyle Hotel Brand"),
    ("Waldorf Astoria", "Luxury Hotel Brand"),
    ("Westin", "Hotel Chain (Upscale)"),
], "Expense", "Travel", "Hotels & Lodging")

assign([
    ("Booking.com", "Online Travel Agency"),
    ("EXPEDIA", "Online Travel Agency"),
    ("Expedia", "Online Travel Agency"),
], "Expense", "Travel", "Travel Booking")

assign([
    ("Hertz", "Car Rental Company"),
], "Expense", "Travel", "Car Rental")

# ============================================================
# HEALTH & WELLNESS
# ============================================================

assign([
    ("BARNABAS HEALTH", "Hospital & Health System"),
    ("BAYSHORE OPHTHALMOLOGY", "Ophthalmology Practice"),
    ("FRANK LIPMAN, M.D.", "Integrative Medicine Physician"),
    ("FUSION REHABILITATIVE", "Physical Therapy & Rehab"),
    ("HOCH ORTHODONTICS", "Orthodontics Practice"),
    ("IMAMIA MEDICS", "Medical Practice"),
    ("JERSEY COAST NEPHROLOGY", "Nephrology Practice"),
    ("KIDZDENT", "Pediatric Dentistry"),
    ("MINUTE CLINIC", "Walk-In Health Clinic"),
    ("ORAL SURGERY GROUP", "Oral Surgery Practice"),
    ("QUEST DIAGNOSTICS", "Clinical Laboratory"),
    ("RMG PEDIATRICS", "Pediatrics Practice"),
    ("SERENITY DENTAL", "Dental Practice"),
    ("WOODBRIDGE INTERNAL MEDICINE", "Internal Medicine Practice"),
], "Expense", "Health & Wellness", "Medical & Dental")

assign([
    ("CVS", "Pharmacy & Drugstore Chain"),
    ("Rite Aid", "Pharmacy & Drugstore Chain"),
    ("Walgreens", "Pharmacy & Drugstore Chain"),
    ("WALGREENS", "Pharmacy & Drugstore Chain"),
    ("Boots", "Pharmacy & Health/Beauty Retailer"),
], "Expense", "Health & Wellness", "Pharmacy")

assign([
    ("LA FITNESS", "Gym & Fitness Club"),
    ("Peloton", "Connected Fitness Equipment"),
    ("YMCA", "Community Fitness & Recreation"),
    ("Yoga Studio", "Yoga & Wellness Studio"),
    ("Zumba Power Gym", "Dance Fitness Studio"),
    ("TEAM BEACHBODY", "Home Fitness Program"),
], "Expense", "Health & Wellness", "Fitness & Gym")

assign([
    ("AAINA BEAUTY PARLOR", "Beauty Salon"),
    ("Bath & Body Works", "Bath & Body Products Retailer"),
    ("Birchbox", "Beauty Subscription Box"),
    ("CELINES SPA", "Day Spa"),
    ("D'BELLA SALON", "Hair Salon"),
    ("HEAD OVER HEELS", "Hair & Beauty Salon"),
    ("HUMA BEAUTY SALON", "Beauty Salon"),
    ("MASSAGE ENVY", "Massage & Spa Franchise"),
    ("MASSAGELUXE", "Massage & Facial Spa"),
    ("Sephora", "Beauty & Cosmetics Retailer"),
    ("SEPHORA.COM", "Beauty & Cosmetics Retailer"),
    ("Ulta Beauty", "Beauty & Cosmetics Retailer"),
    ("ULTA", "Beauty & Cosmetics Retailer"),
    ("ZARA SALON", "Hair & Beauty Salon"),
    ("J & G SALON", "Hair Salon"),
], "Expense", "Health & Wellness", "Beauty & Spa")

assign([
    ("3X4 GENETICS", "Nutrigenomics & DNA Testing"),
    ("3X4GENETICS", "Nutrigenomics & DNA Testing"),
    ("CRI GENETICS", "Consumer DNA Testing"),
    ("EUVEXIA", "Nutraceutical Company"),
    ("FATTY15", "Nutritional Supplement Brand"),
    ("FOREVER LIVING", "Health & Wellness MLM"),
    ("FULLSCRIPT", "Practitioner-Grade Supplements"),
    ("HOLISTIC HEALTH LABS", "Natural Supplements Brand"),
    ("LEVELS", "Continuous Glucose Monitor"),
    ("Omron", "Health Monitoring Devices"),
    ("OURA RING INC.", "Wearable Health Tracker"),
    ("SENSATE", "Stress Relief Device"),
], "Expense", "Health & Wellness", "Health Products")


# ============================================================
# HOUSING & UTILITIES
# ============================================================

assign([
    ("Comcast", "Cable TV & Internet Provider"),
    ("NEW JERSEY NATURAL GAS", "Natural Gas Utility"),
    ("OPTIMUM", "Cable TV & Internet Provider"),
    ("VONAGE", "VoIP Telephone Service"),
], "Expense", "Housing & Utilities", "Utilities")

assign([
    ("GEICO", "Auto Insurance Company"),
    ("RENTERS/CONDO INSURANCE", "Property Insurance"),
], "Expense", "Housing & Utilities", "Insurance")

assign([
    ("ALL CITY ELECTRICAL", "Electrical Contractor"),
    ("DIVINE TOUCH CLEANERS", "Dry Cleaning & Laundry"),
    ("ECOSHIELD", "Pest Control Service"),
    ("GLOBAL PLUMBING", "Plumbing Contractor"),
    ("GLOW EXPRESS CAR WASH", "Car Wash"),
    ("OXFORD CONTRACTING", "General Contractor"),
], "Expense", "Housing & Utilities", "Home Services")

assign([
    ("ALTICEMOBILE.COM", "Mobile Virtual Network Operator"),
    ("T-MOBILE", "Wireless Telecommunications"),
    ("VERIZON", "Wireless Telecommunications"),
    ("VERIZON WIRELESS", "Wireless Telecommunications"),
    ("Verizon", "Wireless Telecommunications"),
], "Expense", "Housing & Utilities", "Telecom & Internet")

# ============================================================
# EDUCATION
# ============================================================

assign([
    ("DIOCESE OF TRENTON", "Catholic Diocese (School)"),
    ("EDMENTUM", "K-12 Online Learning Platform"),
    ("EXL PREP", "Test Prep & Tutoring"),
    ("JOSTENS INC.", "School Rings & Graduation"),
    ("MIDDLESEX COUNTY COLLEGE", "Community College"),
    ("PAYPAL JAFARIA SCHOOOL", "Religious School"),
    ("ST JOHN VIANNEY HIGH SCHOOL", "Catholic High School"),
    ("ST JOHN'S NURSERY SCHOOL", "Preschool & Nursery"),
    ("ST. BENEDICT", "Catholic School"),
    ("ST.BENEDICT", "Catholic School"),
    ("BNL SCHOOL PICTURES", "School Photography Service"),
    ("CODE NINJAS", "Kids Coding Education Center"),
    ("RAZ SPARDHA LEARNINGS", "Tutoring & Education Center"),
], "Expense", "Education", "Tuition & School")

assign([
    ("BRILLIANT.ORG", "STEM Learning Platform"),
    ("Chegg", "Online Tutoring & Textbooks"),
    ("IXL", "K-12 Online Learning Platform"),
    ("KHAN ACADEMY", "Free Online Learning Platform"),
    ("KHANACADEMY", "Free Online Learning Platform"),
    ("LEARNER.COM", "Online Course Platform"),
    ("LEETCODE.COM", "Coding Interview Prep Platform"),
    ("VARSITYTUTORS", "Online Tutoring Platform"),
], "Expense", "Education", "Online Learning")

# ============================================================
# FINANCIAL SERVICES
# ============================================================

assign([
    ("ALLY", "Online Bank"),
    ("ATB", "Regional Bank"),
    ("BANK OF AMERICA", "Commercial Bank"),
    ("Clearbanks", "Digital Banking Platform"),
    ("HDFC BANK LTD.", "Commercial Bank (India)"),
    ("FIDELITY", "Investment & Brokerage Firm"),
    ("THE DEPOSITORY TRUST & CLEARING CORP.", "Financial Market Infrastructure"),
], "Expense", "Financial Services", "Banking Fees")

assign([
    ("SOFI LENDING", "Online Personal Lending"),
    ("APPRAISAL FEE SERVICES", "Real Estate Appraisal Service"),
], "Expense", "Financial Services", "Lending & Loans")

assign([
    ("Acorn", "Micro-Investing App"),
    ("MOTLEY.FOOL.COM", "Investment Advisory & News"),
], "Expense", "Financial Services", "Investment")

assign([
    ("THE CRYPTO MERCHANT", "Cryptocurrency Exchange/ATM"),
], "Expense", "Financial Services", "Crypto & Trading")


# ============================================================
# TECHNOLOGY
# ============================================================

assign([
    ("Adobe", "Creative & Document Software"),
    ("Atlassian", "Team Collaboration Software"),
    ("Autodesk", "CAD & Design Software"),
    ("Canva", "Online Graphic Design Platform"),
    ("Cisco", "Networking & IT Infrastructure"),
    ("Datorama", "Marketing Analytics Platform"),
    ("DocuSign", "Electronic Signature Platform"),
    ("Dropbox", "Cloud Storage & Collaboration"),
    ("Evernote", "Note-Taking Application"),
    ("GitHub", "Code Hosting & Collaboration"),
    ("GoDaddy", "Domain & Web Hosting Provider"),
    ("GOOGLE", "Search Engine & Technology"),
    ("Google", "Search Engine & Technology"),
    ("Grammarly", "AI Writing Assistant"),
    ("GRAMMARLY", "AI Writing Assistant"),
    ("Intuit", "Financial Software (TurboTax/QB)"),
    ("JetBrains", "Developer Tools & IDEs"),
    ("LinkedIn", "Professional Networking Platform"),
    ("OPENAI", "Artificial Intelligence Research"),
    ("Oracle", "Enterprise Software & Cloud"),
    ("ProtonMail", "Encrypted Email Service"),
    ("Salesforce", "CRM & Cloud Platform"),
    ("Slack", "Team Messaging Platform"),
    ("Snowflake", "Cloud Data Platform"),
    ("Splunk", "Data Analytics & Monitoring"),
    ("Squarespace", "Website Builder Platform"),
    ("VMware", "Virtualization Software"),
    ("Workday", "HR & Finance Cloud Software"),
    ("Zscaler", "Cloud Security Platform"),
    ("ZOOM", "Video Conferencing Platform"),
    ("Zoom", "Video Conferencing Platform"),
    ("IBM", "Enterprise Technology & Consulting"),
    ("Akamai", "Content Delivery Network"),
    ("Yandex", "Search Engine & Technology"),
    ("MYQ", "Smart Home & Garage Technology"),
    ("Synapse", "Technology Platform"),
], "Expense", "Technology", "Software & SaaS")

assign([
    ("Avast", "Cybersecurity & Antivirus"),
    ("CyberGhost", "Virtual Private Network"),
    ("CyberGhost VPN", "Virtual Private Network"),
    ("ExpressVPN", "Virtual Private Network"),
    ("GhostPath", "Virtual Private Network"),
    ("GhostVPN", "Virtual Private Network"),
    ("HideMyAss", "Virtual Private Network"),
    ("HotSpot Shield", "Virtual Private Network"),
    ("IPVanish", "Virtual Private Network"),
    ("LastPass", "Password Manager"),
    ("Dashlane", "Password Manager"),
    ("Mullvad", "Virtual Private Network"),
    ("NordVPN", "Virtual Private Network"),
    ("Private Internet Access", "Virtual Private Network"),
    ("PrivateVPN", "Virtual Private Network"),
    ("ProtonVPN", "Virtual Private Network"),
    ("PureVPN", "Virtual Private Network"),
    ("SaferVPN", "Virtual Private Network"),
    ("StrongVPN", "Virtual Private Network"),
    ("Surfshark", "Virtual Private Network"),
    ("TorGuard", "Virtual Private Network"),
    ("Trust.Zone", "Virtual Private Network"),
    ("TunnelBear", "Virtual Private Network"),
    ("VPN Unlimited", "Virtual Private Network"),
    ("VPNArea", "Virtual Private Network"),
    ("VPNSecure", "Virtual Private Network"),
    ("VyprVPN", "Virtual Private Network"),
    ("Windscribe", "Virtual Private Network"),
    ("ZenMate", "Virtual Private Network"),
], "Expense", "Technology", "VPN & Privacy")

assign([
    ("ICOM", "Radio Communications Equipment"),
    ("Borg Warner", "Automotive Parts Manufacturer"),
], "Expense", "Technology", "Hardware")

# ============================================================
# DONATIONS & GIFTS
# ============================================================

assign([
    ("ACTBLUE STACEY.ABRAMS", "Political Fundraising Platform"),
    ("ACTBLUE VOTE.ORG", "Voter Registration Nonprofit"),
    ("CHANGE.ORG", "Online Petition Platform"),
    ("GIRL SCOUTS", "Youth Organization"),
    ("JUSTGIVING.COM", "Charity Fundraising Platform"),
    ("RACE REGISTER DONATIONS", "Race & Charity Event Platform"),
    ("THE NATIONAL SOCIETY", "Nonprofit Organization"),
], "Expense", "Donations & Gifts", "Charity & Donations")

assign([
    ("CARDMART", "Greeting Card & Gift Store"),
    ("ZOLA.COM", "Wedding Registry & Planning"),
    ("Shutterfly", "Photo Printing & Gifts"),
], "Expense", "Donations & Gifts", "Gifts & Cards")


# ============================================================
# KIDS & FAMILY
# ============================================================

assign([
    ("KUUQA Kids Art", "Children's Art Supplies"),
    ("SNAPOLOGY", "Kids STEM Education Center"),
    ("THE CHILDREN'S PLACE", "Children's Clothing Retailer"),
    ("THE HOBBY", "Hobby & Craft Store"),
    ("TOYS STOP", "Toy Store"),
    ("Toys R Us", "Toy Store Chain"),
    ("Bob's Hobbies", "Hobby & Model Shop"),
    ("Hobby Store", "Hobby & Craft Store"),
], "Expense", "Kids & Family", "Toys & Activities")

assign([
    ("PRESCHOOL SMILES", "Preschool & Childcare"),
], "Expense", "Kids & Family", "Childcare")

# ============================================================
# PERSONAL SERVICES
# ============================================================

assign([
    ("DWAYNES PHOTO", "Photo Processing Lab"),
    ("PICTURE PEOPLE", "Portrait Photography Studio"),
    ("TEDDYBEARPORTRAITS.COM", "Children's Portrait Studio"),
], "Expense", "Personal Services", "Photography")

assign([
    ("937 Printshop", "Print & Copy Shop"),
    ("FEDEX", "Shipping & Logistics"),
    ("USPS", "Postal Service"),
    ("LULU.COM", "Self-Publishing & Printing"),
    ("WRITTEN OUT LOUD", "Writing & Publishing Service"),
], "Expense", "Personal Services", "Printing & Shipping")

assign([
    ("TOWNSHIP OF OLD BRIDGE", "Municipal Government"),
    ("NJ GOV", "State Government Services"),
    ("NJ MOTOR VEHICLE", "Motor Vehicle Administration"),
], "Expense", "Personal Services", "Gov & DMV")

# ============================================================
# SUBSCRIPTIONS
# ============================================================

assign([
    ("Birchbox", "Beauty Subscription Box"),
    ("GUM.CO", "Digital Product Marketplace"),
    ("KINDLE", "E-Book Reading Service"),
    ("New York Times", "News & Journalism Subscription"),
    ("Proactive", "Skincare Subscription"),
    ("SUPERSUMMARY", "Book Summary Service"),
    ("WINXDVD.COM", "DVD/Video Software"),
    ("MISEN", "Direct-to-Consumer Cookware"),
], "Expense", "Subscriptions", "Media & Lifestyle")

# ============================================================
# INCOME
# ============================================================

assign([
    ("PAYMENT", "Bill Payment / Transfer"),
    ("ATM Withdrawal", "ATM Cash Withdrawal"),
], "Income", "Transfers", "Bank Transfer")

assign([
    ("NBPA", "National Basketball Players Assoc."),
    ("Hukn", "Payment Platform"),
    ("Mpon", "Payment Platform"),
    ("ADLB", "Payment Platform"),
    ("CMS", "Centers for Medicare & Medicaid"),
    ("SM", "Payment Platform"),
    ("RCCA", "Organization Payment"),
    ("CTM GROUP INC.", "Business Services Company"),
    ("LMXAC", "Library Consortium"),
    ("RFC MENLO PARK", "Organization Payment"),
    ("R Bailey", "Individual Payment / Transfer"),
], "Income", "Transfers", "Deposit")


# ============================================================
# GENERATE CSV
# ============================================================

def guess_category(merchant):
    """Fallback categorizer for merchants not explicitly mapped."""
    m = merchant.lower()

    if any(w in m for w in ['restaurant', 'grill', 'pizza', 'burger', 'taco',
                            'kebab', 'kabab', 'halal', 'diner', 'cafe', 'kitchen',
                            'bbq', 'chicken', 'sushi', 'ramen', 'noodle',
                            'deli', 'sub ', 'wings', 'falafel', 'gyro',
                            'thai', 'mexican', 'chinese', 'indian', 'italian']):
        return ("Restaurant", "Expense", "Food & Dining", "Restaurants")
    if any(w in m for w in ['bakery', 'boulangerie', 'patisserie', 'bread',
                            'cake', 'pastry', 'donut', 'bagel', 'pretzel']):
        return ("Bakery & Patisserie", "Expense", "Food & Dining", "Bakery & Desserts")
    if any(w in m for w in ['yogurt', 'ice cream', 'gelato', 'frozen',
                            'creamery', 'sundae']):
        return ("Ice Cream & Frozen Dessert", "Expense", "Food & Dining", "Ice Cream & Yogurt")
    if any(w in m for w in ['grocery', 'market', 'supermarket', 'mart',
                            'food', 'farm']):
        return ("Grocery Store", "Expense", "Food & Dining", "Groceries")
    if any(w in m for w in ['coffee', 'tea', 'starbucks', 'dunkin']):
        return ("Coffee & Tea Shop", "Expense", "Food & Dining", "Coffee & Tea")
    if any(w in m for w in ['doordash', 'grubhub', 'uber eat', 'postmate',
                            'deliveroo', 'instacart']):
        return ("Food Delivery Platform", "Expense", "Food & Dining", "Food Delivery")
    if any(w in m for w in ['gas', 'fuel', 'shell', 'exxon', 'chevron',
                            'sunoco', 'bp ', 'valero', 'speedway']):
        return ("Gas Station", "Expense", "Transportation", "Gas & Fuel")
    if any(w in m for w in ['uber', 'lyft', 'taxi', 'cab', 'ride']):
        return ("Ride-Hailing Service", "Expense", "Transportation", "Rideshare")
    if any(w in m for w in ['netflix', 'hulu', 'disney', 'hbo', 'spotify',
                            'youtube', 'streaming', 'prime video']):
        return ("Video Streaming Service", "Expense", "Entertainment", "Streaming Video")
    if any(w in m for w in ['vpn', 'nordvpn', 'express', 'surfshark',
                            'tunnel', 'ghost']):
        return ("Virtual Private Network", "Expense", "Technology", "VPN & Privacy")
    if any(w in m for w in ['hotel', 'inn', 'resort', 'hilton', 'marriott',
                            'hyatt', 'westin', 'sheraton']):
        return ("Hotel & Lodging", "Expense", "Travel", "Hotels & Lodging")
    if any(w in m for w in ['airline', 'airways', 'air ', 'jetblue', 'delta',
                            'united', 'southwest', 'frontier']):
        return ("Commercial Airline", "Expense", "Travel", "Airlines")
    if any(w in m for w in ['medical', 'dental', 'doctor', 'clinic',
                            'hospital', 'health', 'pharma', 'diagnostic']):
        return ("Healthcare Provider", "Expense", "Health & Wellness", "Medical & Dental")

    return ("Retail Store", "Expense", "Shopping", "General Retail")


def main():
    merchants = set()
    with open('combined_transactions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            merchants.add(row['merchant'])

    with open('merchant_category.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['merchant', 'public_category', 'root', 'mid_level', 'leaf'])

        for merchant in sorted(merchants):
            if merchant in CATEGORIES:
                public_cat, root, mid, leaf = CATEGORIES[merchant]
            else:
                public_cat, root, mid, leaf = guess_category(merchant)
            writer.writerow([merchant, public_cat, root, mid, leaf])

    # Stats
    print(f"Total merchants: {len(merchants)}")
    mapped = sum(1 for m in merchants if m in CATEGORIES)
    print(f"Explicitly mapped: {mapped}")
    print(f"Auto-categorized: {len(merchants) - mapped}")

    leaves = set()
    with open('merchant_category.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leaves.add(row['leaf'])

    print(f"\nUnique leaf categories: {len(leaves)}")
    long_leaves = [l for l in leaves if len(l) > 22]
    if long_leaves:
        print(f"Leaves > 22 chars: {long_leaves}")
    else:
        print("All leaf categories <= 22 chars OK")


if __name__ == "__main__":
    main()
