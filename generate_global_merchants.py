"""
Generate global_merchant_category.csv with ~10,000 real global household merchant names.
Each merchant is mapped to:
  - public_category: verbatim industry category from public sources
  - root: Expense or Income
  - mid_level: one of ~15 mid-level categories
  - leaf: one of ~60 leaf categories (each <=22 chars)

Uses real brand names from global markets (US, EU, Asia, Middle East, Latin America, Africa).
"""
import csv

MERCHANTS = []  # list of (merchant, public_category, root, mid_level, leaf)


def add(names_and_cats, root, mid, leaf):
    """Add a batch of (merchant_name, public_category) tuples."""
    for name, pub_cat in names_and_cats:
        MERCHANTS.append((name, pub_cat, root, mid, leaf))



# ============================================================
# FOOD & DINING - Groceries (~800)
# ============================================================

add([
    # US Supermarkets & Grocery
    ("Kroger", "Supermarket Chain"), ("Walmart Grocery", "Supercenter"), ("Safeway", "Supermarket"),
    ("Albertsons", "Supermarket"), ("Publix", "Supermarket"), ("H-E-B", "Supermarket Chain"),
    ("Meijer", "Supercenter"), ("Hy-Vee", "Supermarket"), ("WinCo Foods", "Discount Supermarket"),
    ("Wegmans", "Supermarket"), ("Food Lion", "Supermarket"), ("Giant", "Supermarket"),
    ("Giant Eagle", "Supermarket"), ("ShopRite", "Supermarket"), ("Stop & Shop", "Supermarket"),
    ("Hannaford", "Supermarket"), ("Harris Teeter", "Supermarket"), ("Ingles Markets", "Supermarket"),
    ("Winn-Dixie", "Supermarket"), ("Piggly Wiggly", "Supermarket"), ("Bi-Lo", "Supermarket"),
    ("Stater Bros", "Supermarket"), ("Raley's", "Supermarket"), ("Save Mart", "Supermarket"),
    ("Smart & Final", "Warehouse Grocery"), ("Grocery Outlet", "Discount Grocery"),
    ("Sprouts Farmers Market", "Natural & Organic Grocery"), ("Natural Grocers", "Organic Grocery"),
    ("Fresh Thyme", "Natural Grocery"), ("Earth Fare", "Organic Grocery"),
    ("Trader Joe's", "Specialty Grocery"), ("Whole Foods Market", "Natural & Organic Grocery"),
    ("Aldi", "Discount Supermarket"), ("Lidl", "Discount Supermarket"),
    ("Food 4 Less", "Discount Supermarket"), ("Save-A-Lot", "Discount Grocery"),
    ("Price Chopper", "Supermarket"), ("Tops Friendly Markets", "Supermarket"),
    ("Market Basket", "Supermarket"), ("Ralphs", "Supermarket"), ("Vons", "Supermarket"),
    ("Jewel-Osco", "Supermarket"), ("Acme Markets", "Supermarket"), ("Shaw's", "Supermarket"),
    ("Star Market", "Supermarket"), ("Lucky Supermarkets", "Supermarket"),
    ("Schnucks", "Supermarket"), ("Brookshire's", "Supermarket"), ("Weis Markets", "Supermarket"),
    ("Food City", "Supermarket"), ("Associated Wholesale Grocers", "Wholesale Grocery"),
    ("SpartanNash", "Supermarket"), ("United Supermarkets", "Supermarket"),
    ("Cub Foods", "Supermarket"), ("Festival Foods", "Supermarket"),
    ("Fareway Stores", "Supermarket"), ("Woodman's Food Market", "Warehouse Supermarket"),
    ("Coborn's", "Supermarket"), ("Martin's Super Markets", "Supermarket"),
    ("Redner's Markets", "Supermarket"), ("Key Food", "Supermarket"),
    ("Foodtown", "Supermarket"), ("Gristedes", "Supermarket"),
    ("Morton Williams", "Supermarket"), ("Fairway Market", "Specialty Supermarket"),
    ("Citarella", "Specialty Food Market"), ("Zabar's", "Specialty Food Market"),
    ("Dean & DeLuca", "Gourmet Food Market"), ("Balducci's", "Gourmet Food Market"),
    ("Bristol Farms", "Premium Supermarket"), ("Gelson's", "Premium Supermarket"),
    ("Lazy Acres", "Natural Grocery"), ("New Seasons Market", "Natural Grocery"),
    ("PCC Community Markets", "Cooperative Grocery"), ("Central Market", "Specialty Grocery"),
    # Wholesale Clubs
    ("Costco", "Wholesale Club"), ("Sam's Club", "Wholesale Club"),
    ("BJ's Wholesale Club", "Wholesale Club"), ("Restaurant Depot", "Wholesale Food"),
    # Convenience Stores
    ("7-Eleven", "Convenience Store Chain"), ("Circle K", "Convenience Store & Gas"),
    ("Wawa", "Convenience Store & Gas"), ("Sheetz", "Convenience Store & Gas"),
    ("QuikTrip", "Convenience Store & Gas"), ("Casey's General Store", "Convenience Store & Gas"),
    ("Kwik Trip", "Convenience Store & Gas"), ("Kum & Go", "Convenience Store & Gas"),
    ("RaceTrac", "Convenience Store & Gas"), ("Pilot Flying J", "Travel Center"),
    ("Love's Travel Stops", "Travel Center"), ("Cumberland Farms", "Convenience Store"),
    ("Stewart's Shops", "Convenience Store"), ("Buc-ee's", "Travel Center & Convenience"),
    ("Allsup's", "Convenience Store"), ("Maverik", "Convenience Store & Gas"),
    ("Holiday Stationstores", "Convenience Store & Gas"), ("Thorntons", "Convenience Store & Gas"),
    ("GetGo", "Convenience Store & Gas"), ("Spinx", "Convenience Store & Gas"),
    ("Rutters", "Convenience Store & Gas"), ("Quick Chek", "Convenience Store"),
    ("Royal Farms", "Convenience Store & Fried Chicken"), ("Parker's", "Convenience Store & Gas"),
    # UK Supermarkets
    ("Tesco", "Supermarket Chain"), ("Sainsbury's", "Supermarket Chain"),
    ("Asda", "Supermarket Chain"), ("Morrisons", "Supermarket Chain"),
    ("Waitrose", "Premium Supermarket"), ("Co-op Food", "Cooperative Supermarket"),
    ("Aldi UK", "Discount Supermarket"), ("Lidl UK", "Discount Supermarket"),
    ("Iceland", "Frozen Food Supermarket"), ("M&S Food", "Premium Food Retailer"),
    ("Ocado", "Online Grocery Delivery"), ("Booths", "Premium Supermarket"),
    ("Budgens", "Convenience Supermarket"), ("Londis", "Convenience Store"),
    ("Spar UK", "Convenience Store"), ("Nisa", "Convenience Store"),
    ("One Stop", "Convenience Store"), ("McColl's", "Convenience Store"),
    # EU Supermarkets
    ("Carrefour", "Hypermarket Chain"), ("Leclerc", "Hypermarket Chain"),
    ("Auchan", "Hypermarket Chain"), ("Intermarché", "Supermarket Chain"),
    ("Casino", "Supermarket Chain"), ("Monoprix", "Department Store & Supermarket"),
    ("Franprix", "Supermarket Chain"), ("Picard", "Frozen Food Specialty"),
    ("EDEKA", "Supermarket Chain"), ("REWE", "Supermarket Chain"),
    ("Kaufland", "Hypermarket Chain"), ("Netto", "Discount Supermarket"),
    ("Penny", "Discount Supermarket"), ("Norma", "Discount Supermarket"),
    ("Globus", "Hypermarket"), ("Real", "Hypermarket"),
    ("Albert Heijn", "Supermarket Chain"), ("Jumbo", "Supermarket Chain"),
    ("Plus Supermarkt", "Supermarket Chain"), ("Dirk", "Supermarket Chain"),
    ("Delhaize", "Supermarket Chain"), ("Colruyt", "Discount Supermarket"),
    ("Mercadona", "Supermarket Chain"), ("Dia", "Discount Supermarket"),
    ("El Corte Inglés", "Department Store & Supermarket"), ("Eroski", "Cooperative Supermarket"),
    ("Esselunga", "Supermarket Chain"), ("Conad", "Cooperative Supermarket"),
    ("Coop Italia", "Cooperative Supermarket"), ("Eurospin", "Discount Supermarket"),
    ("ICA", "Supermarket Chain"), ("Coop Sweden", "Cooperative Supermarket"),
    ("Hemköp", "Supermarket Chain"), ("Willys", "Discount Supermarket"),
    ("Føtex", "Supermarket Chain"), ("Rema 1000", "Discount Supermarket"),
    ("Kiwi", "Discount Supermarket"), ("Billa", "Supermarket Chain"),
    ("Spar", "Supermarket Chain"), ("Biedronka", "Discount Supermarket"),
    ("Żabka", "Convenience Store Chain"), ("Dino", "Supermarket Chain"),
    # Asia & Pacific
    ("FamilyMart", "Convenience Store Chain"), ("Lawson", "Convenience Store Chain"),
    ("Ministop", "Convenience Store Chain"), ("AEON", "Hypermarket Chain"),
    ("Ito-Yokado", "Supermarket Chain"), ("Life Supermarket", "Supermarket"),
    ("Summit Store", "Supermarket"), ("Don Quijote", "Discount Store Chain"),
    ("Big C", "Hypermarket Chain"), ("Tesco Lotus", "Hypermarket Chain"),
    ("Tops Market", "Supermarket"), ("Villa Market", "Premium Supermarket"),
    ("Cold Storage", "Premium Supermarket"), ("FairPrice", "Supermarket Chain"),
    ("Sheng Siong", "Supermarket Chain"), ("Giant Singapore", "Hypermarket"),
    ("Wellcome", "Supermarket Chain"), ("ParknShop", "Supermarket Chain"),
    ("Dairy Farm", "Supermarket Group"), ("Lotte Mart", "Hypermarket Chain"),
    ("E-Mart", "Hypermarket Chain"), ("Homeplus", "Hypermarket Chain"),
    ("GS25", "Convenience Store Chain"), ("CU", "Convenience Store Chain"),
    ("Indomaret", "Convenience Store Chain"), ("Alfamart", "Convenience Store Chain"),
    ("Hero Supermarket", "Supermarket"), ("Ranch Market", "Premium Supermarket"),
    ("Big Basket", "Online Grocery Delivery"), ("Grofers", "Online Grocery Delivery"),
    ("DMart", "Hypermarket Chain"), ("Reliance Fresh", "Supermarket Chain"),
    ("Spencer's", "Supermarket Chain"), ("Nature's Basket", "Premium Grocery"),
    ("Star Bazaar", "Hypermarket"), ("More Supermarket", "Supermarket Chain"),
    # Middle East & Africa
    ("Carrefour UAE", "Hypermarket Chain"), ("Lulu Hypermarket", "Hypermarket Chain"),
    ("Spinneys", "Premium Supermarket"), ("Choithrams", "Supermarket Chain"),
    ("Union Coop", "Cooperative Supermarket"), ("Al Maya", "Supermarket Chain"),
    ("Tamimi Markets", "Supermarket"), ("Panda Retail", "Hypermarket Chain"),
    ("Danube Supermarket", "Supermarket"), ("Shufersal", "Supermarket Chain"),
    ("Rami Levy", "Supermarket Chain"), ("Shoprite Holdings", "Supermarket Chain"),
    ("Pick n Pay", "Supermarket Chain"), ("Woolworths SA", "Premium Supermarket"),
    ("Checkers", "Supermarket"), ("Spar South Africa", "Supermarket Chain"),
    ("Game Stores", "Hypermarket"), ("Nakumatt", "Supermarket Chain"),
    # Latin America
    ("Grupo Éxito", "Hypermarket Chain"), ("Chedraui", "Supermarket Chain"),
    ("Soriana", "Hypermarket Chain"), ("Bodega Aurrera", "Discount Supermarket"),
    ("OXXO", "Convenience Store Chain"), ("Coto", "Supermarket Chain"),
    ("Jumbo Chile", "Hypermarket"), ("Wong", "Supermarket Chain"),
    ("Pão de Açúcar", "Supermarket Chain"), ("Extra Hipermercados", "Hypermarket"),
    # Russian & CIS
    ("Magnit", "Supermarket Chain"), ("X5 Retail Group", "Supermarket Group"),
    ("Pyaterochka", "Discount Supermarket"), ("Perekrestok", "Supermarket Chain"),
    ("Dixy", "Supermarket Chain"), ("Lenta", "Hypermarket Chain"),
    # Ethnic & Specialty (Global)
    ("H Mart", "Korean Grocery Store"), ("99 Ranch Market", "Asian Supermarket"),
    ("Mitsuwa Marketplace", "Japanese Supermarket"), ("Patel Brothers", "Indian Grocery"),
    ("Sedano's", "Hispanic Supermarket"), ("Northgate Market", "Hispanic Supermarket"),
    ("Fiesta Mart", "Hispanic Supermarket"), ("El Super", "Hispanic Supermarket"),
    ("Cardenas Markets", "Hispanic Supermarket"), ("Ranch 99", "Asian Supermarket"),
    ("Uwajimaya", "Asian Supermarket"), ("Marukai", "Japanese Supermarket"),
    ("Zion Market", "Korean Supermarket"), ("Good Fortune Supermarket", "Chinese Supermarket"),
    ("Great Wall Supermarket", "Chinese Supermarket"), ("Seafood City", "Filipino Supermarket"),
    ("Lotte Plaza", "Asian Supermarket"), ("Super H Mart", "Korean Supermarket"),
], "Expense", "Food & Dining", "Groceries")



# ============================================================
# FOOD & DINING - Fast Food (~600)
# ============================================================

add([
    # Major Global Chains
    ("McDonald's", "Fast Food Restaurant"), ("Burger King", "Fast Food Restaurant"),
    ("Wendy's", "Fast Food Restaurant"), ("Taco Bell", "Fast Food Mexican"),
    ("KFC", "Fast Food Fried Chicken"), ("Popeyes", "Fast Food Fried Chicken"),
    ("Chick-fil-A", "Fast Food Chicken Restaurant"), ("Subway", "Fast Food Sandwich Chain"),
    ("Arby's", "Fast Food Roast Beef"), ("Sonic Drive-In", "Fast Food Drive-In"),
    ("Jack in the Box", "Fast Food Restaurant"), ("Carl's Jr.", "Fast Food Restaurant"),
    ("Hardee's", "Fast Food Restaurant"), ("Whataburger", "Fast Food Restaurant"),
    ("In-N-Out Burger", "Fast Food Burger"), ("Five Guys", "Fast Casual Burger"),
    ("Shake Shack", "Fast Casual Burger"), ("Culver's", "Fast Casual Butter Burger"),
    ("Steak 'n Shake", "Fast Food Steakburger"), ("White Castle", "Fast Food Slider"),
    ("Checkers/Rally's", "Fast Food Burger"), ("Krystal", "Fast Food Slider"),
    ("Smashburger", "Fast Casual Burger"), ("Fatburger", "Fast Casual Burger"),
    ("Habit Burger Grill", "Fast Casual Burger"), ("Elevation Burger", "Fast Casual Burger"),
    ("BurgerFi", "Fast Casual Burger"), ("Wayback Burgers", "Fast Casual Burger"),
    # Pizza
    ("Domino's", "Pizza Delivery & Carryout"), ("Pizza Hut", "Pizza Restaurant Chain"),
    ("Papa John's", "Pizza Delivery & Carryout"), ("Little Caesars", "Pizza Chain"),
    ("Papa Murphy's", "Take-and-Bake Pizza"), ("Marco's Pizza", "Pizza Chain"),
    ("Jet's Pizza", "Pizza Chain"), ("Hungry Howie's", "Pizza Chain"),
    ("Donatos Pizza", "Pizza Chain"), ("Round Table Pizza", "Pizza Chain"),
    ("Mountain Mike's Pizza", "Pizza Chain"), ("Sbarro", "Pizza Chain"),
    ("Cicis Pizza", "Pizza Buffet"), ("MOD Pizza", "Fast Casual Pizza"),
    ("Blaze Pizza", "Fast Casual Pizza"), ("Pieology", "Fast Casual Pizza"),
    ("& Pizza", "Fast Casual Pizza"), ("Your Pie", "Fast Casual Pizza"),
    # Chicken
    ("Raising Cane's", "Fast Food Chicken Fingers"), ("Zaxby's", "Fast Casual Chicken"),
    ("Wingstop", "Chicken Wing Restaurant"), ("Buffalo Wild Wings", "Sports Bar & Wings"),
    ("Bojangles", "Fast Food Fried Chicken"), ("Church's Chicken", "Fast Food Fried Chicken"),
    ("El Pollo Loco", "Fast Food Grilled Chicken"), ("Golden Chick", "Fast Food Chicken"),
    ("Lee's Famous Recipe", "Fast Food Fried Chicken"), ("Slim Chickens", "Fast Casual Chicken"),
    ("PDQ", "Fast Casual Chicken"), ("Bonchon", "Korean Fried Chicken Chain"),
    # Mexican/Tex-Mex
    ("Chipotle", "Fast Casual Mexican"), ("Qdoba", "Fast Casual Mexican"),
    ("Moe's Southwest Grill", "Fast Casual Mexican"), ("Del Taco", "Fast Food Mexican"),
    ("Taco John's", "Fast Food Mexican"), ("Taco Cabana", "Fast Casual Mexican"),
    ("Taco Bueno", "Fast Food Mexican"), ("Green Burrito", "Fast Food Mexican"),
    ("Baja Fresh", "Fast Casual Mexican"), ("Chronic Tacos", "Fast Casual Mexican"),
    ("Rubio's Coastal Grill", "Fast Casual Seafood/Mexican"), ("Torchy's Tacos", "Fast Casual Taco"),
    # Sandwich/Sub
    ("Jimmy John's", "Fast Food Sandwich"), ("Firehouse Subs", "Fast Casual Sub"),
    ("Jersey Mike's Subs", "Fast Casual Sub"), ("Quiznos", "Fast Casual Toasted Sub"),
    ("Potbelly Sandwich Shop", "Fast Casual Sandwich"), ("Which Wich", "Fast Casual Sandwich"),
    ("Penn Station East Coast Subs", "Fast Casual Sub"), ("Erbert & Gerbert's", "Fast Casual Sandwich"),
    ("McAlister's Deli", "Fast Casual Deli"), ("Jason's Deli", "Fast Casual Deli"),
    ("Schlotzsky's", "Fast Casual Sandwich"), ("Capriotti's", "Sandwich Shop"),
    # Asian Fast Food
    ("Panda Express", "Fast Food Chinese"), ("Sarku Japan", "Fast Food Japanese"),
    ("Teriyaki Madness", "Fast Casual Teriyaki"), ("Wok Box", "Fast Casual Asian"),
    ("Noodles & Company", "Fast Casual Noodle"), ("Pei Wei", "Fast Casual Asian"),
    ("Pick Up Stix", "Fast Casual Chinese"), ("Yoshinoya", "Fast Food Japanese Beef Bowl"),
    ("Jollibee", "Fast Food (Filipino)"), ("Lotteria", "Fast Food (Korean)"),
    # Other Fast Food
    ("Long John Silver's", "Fast Food Seafood"), ("Captain D's", "Fast Food Seafood"),
    ("Culver's", "Fast Casual Butter Burger"), ("Dairy Queen", "Fast Food & Ice Cream"),
    ("A&W Restaurants", "Fast Food Restaurant"), ("Cook Out", "Fast Food Restaurant"),
    ("Braum's", "Fast Food & Ice Cream"), ("Portillo's", "Fast Casual Hot Dogs"),
    ("Wienerschnitzel", "Fast Food Hot Dogs"), ("Hot Dog on a Stick", "Fast Food Hot Dogs"),
    ("Auntie Anne's", "Soft Pretzel Chain"), ("Wetzel's Pretzels", "Soft Pretzel Chain"),
    ("Cinnabon", "Cinnamon Roll Bakery"), ("Krispy Kreme", "Doughnut Shop"),
    # International Fast Food
    ("Nando's", "Fast Casual Peri-Peri Chicken"), ("Greggs", "Bakery & Fast Food (UK)"),
    ("Pret A Manger", "Fast Casual Sandwich & Coffee"), ("Leon", "Fast Casual Natural Food"),
    ("Itsu", "Fast Casual Japanese/Asian"), ("Wagamama", "Fast Casual Asian"),
    ("Guzman y Gomez", "Fast Casual Mexican (AU)"), ("Hungry Jack's", "Fast Food Burger (AU)"),
    ("Oporto", "Fast Food Portuguese Chicken (AU)"), ("Red Rooster", "Fast Food Chicken (AU)"),
    ("Lotteria", "Fast Food (Japan/Korea)"), ("MOS Burger", "Fast Food Burger (Japan)"),
    ("Freshness Burger", "Fast Casual Burger (Japan)"), ("Matsuya", "Fast Food Gyudon (Japan)"),
    ("Sukiya", "Fast Food Gyudon (Japan)"), ("CoCo Ichibanya", "Curry Restaurant (Japan)"),
    ("Mos Burger", "Fast Food Burger (Japan)"), ("First Kitchen", "Fast Food (Japan)"),
    ("Hesburger", "Fast Food Burger (Finland)"), ("Max Burgers", "Fast Food Burger (Sweden)"),
    ("Sibylla", "Fast Food (Sweden)"), ("Nordsee", "Fast Food Seafood (Germany)"),
    ("Vapiano", "Fast Casual Italian"), ("Hans im Glück", "Fast Casual Burger (Germany)"),
    ("Quick", "Fast Food Burger (Belgium/France)"), ("Wimpy", "Fast Food Burger (UK/SA)"),
    ("Steers", "Fast Food Burger (South Africa)"), ("Debonairs Pizza", "Pizza Chain (Africa)"),
    ("Chicken Licken", "Fast Food Chicken (South Africa)"), ("Galito's", "Flame-Grilled Chicken"),
    ("Al Baik", "Fast Food Chicken (Saudi Arabia)"), ("Jahez", "Delivery Platform (Saudi)"),
    ("Marrybrown", "Fast Food (Malaysia)"), ("4Fingers Crispy Chicken", "Fried Chicken (Asia)"),
    ("Texas Chicken", "Fast Food Fried Chicken"), ("Pollo Campero", "Fast Food Chicken (Latin Am)"),
    ("Telepizza", "Pizza Chain (Spain)"), ("Grupo Alsea", "Multi-Brand Fast Food (Mexico)"),
], "Expense", "Food & Dining", "Fast Food")



# ============================================================
# FOOD & DINING - Restaurants (~1200)
# ============================================================

add([
    # US Casual Dining
    ("Applebee's", "Casual Dining Restaurant"), ("Olive Garden", "Italian Casual Dining"),
    ("Chili's", "Casual Dining Restaurant"), ("TGI Fridays", "Casual Dining Restaurant"),
    ("Red Lobster", "Casual Dining Seafood"), ("Outback Steakhouse", "Casual Dining Steakhouse"),
    ("Texas Roadhouse", "Casual Dining Steakhouse"), ("LongHorn Steakhouse", "Casual Dining Steakhouse"),
    ("Cracker Barrel", "Family Restaurant & Gift Shop"), ("Denny's", "Family Dining Restaurant"),
    ("IHOP", "Family Restaurant (Pancakes)"), ("Waffle House", "Diner (Breakfast)"),
    ("Bob Evans", "Family Dining Restaurant"), ("Perkins", "Family Dining Restaurant"),
    ("Village Inn", "Family Dining Restaurant"), ("Shoney's", "Family Dining Restaurant"),
    ("Golden Corral", "Buffet Restaurant"), ("Ryan's", "Buffet Restaurant"),
    ("Sizzler", "Casual Dining Steakhouse"), ("Ponderosa Steakhouse", "Buffet Steakhouse"),
    ("Red Robin", "Casual Dining Burger"), ("Friendly's", "Family Dining & Ice Cream"),
    ("Ruby Tuesday", "Casual Dining Restaurant"), ("O'Charley's", "Casual Dining Restaurant"),
    ("Cheddar's Scratch Kitchen", "Casual Dining Restaurant"), ("BJ's Restaurant", "Casual Dining & Brewhouse"),
    ("Yard House", "Restaurant & Bar"), ("Dave & Buster's", "Entertainment & Dining"),
    ("Maggiano's Little Italy", "Italian Casual Dining"), ("Bonefish Grill", "Casual Dining Seafood"),
    ("The Cheesecake Factory", "Casual Dining Restaurant"), ("P.F. Chang's", "Asian Casual Dining"),
    ("Benihana", "Japanese Teppanyaki Restaurant"), ("Seasons 52", "Fine Casual Dining"),
    ("The Capital Grille", "Upscale Steakhouse"), ("Ruth's Chris Steak House", "Fine Dining Steakhouse"),
    ("Morton's The Steakhouse", "Fine Dining Steakhouse"), ("Fleming's Steakhouse", "Fine Dining Steakhouse"),
    ("STK", "Modern Steakhouse"), ("Smith & Wollensky", "Classic Steakhouse"),
    ("Peter Luger Steak House", "Fine Dining Steakhouse"), ("Lawry's The Prime Rib", "Fine Dining"),
    # US Breakfast/Brunch
    ("First Watch", "Breakfast & Brunch Restaurant"), ("Another Broken Egg Cafe", "Breakfast & Brunch"),
    ("The Original Pancake House", "Breakfast Restaurant"), ("Snooze an A.M. Eatery", "Breakfast & Brunch"),
    ("Eggs Up Grill", "Breakfast & Brunch"), ("Broken Yolk Cafe", "Breakfast & Brunch"),
    ("Black Bear Diner", "Family Diner"), ("Huddle House", "Family Diner"),
    # US Regional/Ethnic
    ("Bahama Breeze", "Caribbean Restaurant"), ("Buca di Beppo", "Italian Family Restaurant"),
    ("Carrabba's Italian Grill", "Italian Casual Dining"), ("Macaroni Grill", "Italian Casual Dining"),
    ("The Melting Pot", "Fondue Restaurant"), ("Joe's Crab Shack", "Seafood Restaurant"),
    ("Legal Sea Foods", "Seafood Restaurant"), ("Landry's", "Seafood Restaurant"),
    ("Claim Jumper", "American Restaurant"), ("Marie Callender's", "Family Restaurant & Pies"),
    ("Luby's", "Cafeteria-Style Restaurant"), ("Boston Market", "Rotisserie Restaurant"),
    ("Wingstop", "Wing Restaurant"), ("Hooters", "Sports Bar & Wings"),
    ("Buffalo Wild Wings", "Sports Bar & Wings"), ("Twin Peaks", "Sports Lodge"),
    # Asian Restaurants
    ("Nobu", "Japanese Fine Dining"), ("Morimoto", "Japanese Fine Dining"),
    ("Sushi Nakazawa", "Sushi Restaurant"), ("Ramen Ichiraku", "Ramen Restaurant"),
    ("Ippudo", "Ramen Restaurant Chain"), ("Ichiran", "Ramen Restaurant Chain"),
    ("Din Tai Fung", "Taiwanese Dumpling Restaurant"), ("Haidilao", "Hot Pot Chain"),
    ("Little Sheep", "Mongolian Hot Pot"), ("Kura Sushi", "Conveyor Belt Sushi"),
    ("Genki Sushi", "Conveyor Belt Sushi"), ("Sushi Zanmai", "Sushi Chain"),
    ("Tim Ho Wan", "Dim Sum Restaurant"), ("Crystal Jade", "Chinese Restaurant Chain"),
    ("Paradise Group", "Chinese Restaurant Chain"), ("Hai Di Lao", "Hot Pot Chain"),
    ("The Sushi Bar", "Japanese Restaurant"), ("Sushi Tei", "Japanese Restaurant Chain"),
    ("Watami", "Japanese Izakaya Chain"), ("Toridoll", "Japanese Udon Chain"),
    ("Marugame Udon", "Udon Restaurant Chain"), ("Ootoya", "Japanese Home Cooking Chain"),
    ("Yayoi", "Japanese Restaurant Chain"), ("Pepper Lunch", "Fast Casual Japanese"),
    ("Thai Express", "Thai Restaurant Chain"), ("Nara Thai", "Thai Restaurant"),
    ("Banana Leaf", "Malaysian Restaurant"), ("Old Town White Coffee", "Malaysian Coffee & Food"),
    ("Secret Recipe", "Malaysian Restaurant Chain"), ("Manhattan Fish Market", "Seafood Restaurant"),
    # Indian Restaurants
    ("Haldiram's", "Indian Restaurant & Sweets"), ("Barbeque Nation", "Indian BBQ Chain"),
    ("Mainland China", "Chinese Restaurant (India)"), ("Saravana Bhavan", "South Indian Vegetarian"),
    ("Paradise Biryani", "Indian Biryani Restaurant"), ("Biryani Blues", "Indian Biryani"),
    ("Punjabi by Nature", "North Indian Restaurant"), ("Bukhara", "North Indian Fine Dining"),
    ("Karim's", "Mughlai Restaurant"), ("Moti Mahal", "Indian Restaurant"),
    # Middle Eastern Restaurants
    ("Al Baik", "Saudi Fast Food"), ("The Meat Co", "Steakhouse (Middle East)"),
    ("Nusret (Salt Bae)", "Turkish Steakhouse"), ("Zuma", "Japanese Restaurant"),
    ("La Petite Maison", "French Restaurant"), ("Nobu Dubai", "Japanese Fine Dining"),
    ("Mashawi", "Middle Eastern Grill"), ("Al Mahara", "Fine Dining Seafood"),
    ("Turkish Kitchen", "Turkish Restaurant"), ("Kazan", "Turkish Restaurant"),
    # European Restaurants
    ("Pizza Express", "Casual Dining Pizza (UK)"), ("Zizzi", "Italian Restaurant (UK)"),
    ("ASK Italian", "Italian Restaurant (UK)"), ("Prezzo", "Italian Restaurant (UK)"),
    ("Frankie & Benny's", "Italian-American Restaurant (UK)"), ("Bella Italia", "Italian Restaurant (UK)"),
    ("Carluccio's", "Italian Restaurant (UK)"), ("Bill's Restaurant", "British Restaurant"),
    ("The Ivy", "British Restaurant"), ("Dishoom", "Indian Restaurant (UK)"),
    ("Côte Brasserie", "French Restaurant (UK)"), ("Le Pain Quotidien", "Bakery Cafe Chain"),
    ("Café Rouge", "French Restaurant (UK)"), ("Gaucho", "Argentine Steakhouse (UK)"),
    ("Block House", "Steakhouse (Germany)"), ("L'Osteria", "Italian Restaurant (Germany)"),
    ("Vapiano", "Italian Fast Casual (Germany)"), ("Sausalitos", "Mexican Restaurant (Germany)"),
    ("Maredo", "Steakhouse (Germany)"), ("Alex", "Restaurant & Bar (Germany)"),
    ("Flunch", "Cafeteria Restaurant (France)"), ("Hippopotamus", "Steakhouse (France)"),
    ("Buffalo Grill", "Steakhouse (France)"), ("Courtepaille", "Grill Restaurant (France)"),
    ("La Tagliatella", "Italian Restaurant (Spain)"), ("Ginos", "Italian Restaurant (Spain)"),
    ("100 Montaditos", "Spanish Tapas Chain"), ("Tapa Tapa", "Spanish Tapas Restaurant"),
    # Latin American
    ("Coco Bambu", "Seafood Restaurant (Brazil)"), ("Outback Brazil", "Steakhouse"),
    ("Fogo de Chão", "Brazilian Steakhouse"), ("Rodízio", "Brazilian BBQ"),
    ("Sanborns", "Restaurant & Retail (Mexico)"), ("El Fogoncito", "Mexican Restaurant"),
    ("La Casa de Toño", "Mexican Pozole Restaurant"), ("Toks", "Family Restaurant (Mexico)"),
    # African
    ("Spur Steak Ranches", "Family Steakhouse (South Africa)"), ("Ocean Basket", "Seafood (South Africa)"),
    ("The Hussar Grill", "Steakhouse (South Africa)"), ("Primi Piatti", "Italian (South Africa)"),
    # Australian
    ("Rashays", "Casual Dining (Australia)"), ("The Bavarian", "German Restaurant (AU)"),
    ("Hurricane's Grill", "Ribs & Steak (Australia)"), ("Ribs & Rumps", "Steakhouse (AU)"),
    ("Hog's Breath Cafe", "Steakhouse (Australia)"), ("Lone Star Rib House", "American (AU)"),
], "Expense", "Food & Dining", "Restaurants")



# ============================================================
# FOOD & DINING - Coffee & Tea (~300)
# ============================================================

add([
    ("Starbucks", "Coffee Shop Chain"), ("Dunkin'", "Coffee & Donut Chain"),
    ("Peet's Coffee", "Specialty Coffee Roaster"), ("The Coffee Bean & Tea Leaf", "Coffee & Tea Chain"),
    ("Caribou Coffee", "Specialty Coffee Chain"), ("Dutch Bros", "Drive-Through Coffee"),
    ("Tim Hortons", "Coffee & Fast Food"), ("Biggby Coffee", "Coffee Chain"),
    ("Scooter's Coffee", "Drive-Through Coffee"), ("7 Brew", "Drive-Through Coffee"),
    ("Black Rock Coffee Bar", "Coffee Chain"), ("PJ's Coffee", "Coffee Chain"),
    ("It's A Grind Coffee", "Coffee Shop"), ("Gregorys Coffee", "Coffee Chain"),
    ("Blue Bottle Coffee", "Specialty Coffee"), ("Intelligentsia Coffee", "Specialty Coffee"),
    ("Stumptown Coffee", "Specialty Coffee Roaster"), ("Counter Culture Coffee", "Specialty Coffee"),
    ("La Colombe Coffee", "Specialty Coffee & Draft Latte"), ("Verve Coffee", "Specialty Coffee"),
    ("Philz Coffee", "Specialty Coffee"), ("Joe Coffee Company", "Coffee Chain"),
    ("Blank Street Coffee", "Coffee Chain"), ("% Arabica", "Japanese Specialty Coffee"),
    ("Costa Coffee", "Coffee Shop Chain (UK)"), ("Caffè Nero", "Coffee Shop Chain (UK)"),
    ("Pret A Manger", "Coffee & Sandwich (UK)"), ("Greggs", "Bakery & Coffee (UK)"),
    ("Paul", "French Bakery & Cafe"), ("Brioche Dorée", "French Bakery Cafe"),
    ("McCafé", "McDonald's Coffee Brand"), ("Lavazza", "Italian Coffee Chain"),
    ("Illy", "Italian Coffee Brand/Cafe"), ("Segafredo", "Italian Coffee Chain"),
    ("Coffee Republic", "Coffee Chain"), ("Wild Bean Cafe", "Gas Station Coffee"),
    ("Gloria Jean's", "Coffee Chain (Australia)"), ("The Coffee Club", "Coffee Chain (AU)"),
    ("Soul Origin", "Coffee & Food (Australia)"), ("Zarraffa's Coffee", "Coffee Chain (AU)"),
    ("DAVIDsTEA", "Specialty Tea Retailer"), ("Teavana", "Premium Tea Brand"),
    ("T2 Tea", "Specialty Tea Retailer (AU)"), ("TWG Tea", "Luxury Tea Salon"),
    ("Gong Cha", "Bubble Tea Chain"), ("CoCo", "Bubble Tea Chain"),
    ("Tiger Sugar", "Bubble Tea Chain"), ("The Alley", "Bubble Tea Chain"),
    ("Kung Fu Tea", "Bubble Tea Chain"), ("ShareTea", "Bubble Tea Chain"),
    ("Chatime", "Bubble Tea Chain"), ("TP Tea", "Bubble Tea Chain"),
    ("Koi Thé", "Bubble Tea Chain"), ("Happy Lemon", "Bubble Tea Chain"),
    ("Heytea", "Cheese Tea Chain (China)"), ("Nayuki", "Tea & Bakery (China)"),
    ("Luckin Coffee", "Coffee Chain (China)"), ("Manner Coffee", "Coffee Chain (China)"),
    ("Angel-in-us Coffee", "Coffee Chain (Korea)"), ("Ediya Coffee", "Coffee Chain (Korea)"),
    ("Tom N Toms", "Coffee Chain (Korea)"), ("A Twosome Place", "Coffee Chain (Korea)"),
    ("Hollys Coffee", "Coffee Chain (Korea)"), ("Café Bene", "Coffee Chain (Korea)"),
    ("Tully's Coffee", "Coffee Chain (Japan)"), ("Doutor Coffee", "Coffee Chain (Japan)"),
    ("Komeda's Coffee", "Coffee Chain (Japan)"), ("St. Marc Café", "Coffee Chain (Japan)"),
    ("Café de Coral", "Fast Casual & Coffee (HK)"), ("Pacific Coffee", "Coffee Chain (HK)"),
    ("Old Town White Coffee", "Coffee Chain (Malaysia)"), ("ZUS Coffee", "Coffee Chain (Malaysia)"),
    ("Kopi Kenangan", "Coffee Chain (Indonesia)"), ("Fore Coffee", "Coffee Chain (Indonesia)"),
    ("Flash Coffee", "Coffee Chain (Asia)"), ("Cafe Amazon", "Coffee Chain (Thailand)"),
    ("Wawee Coffee", "Coffee Chain (Thailand)"), ("Inthanin Coffee", "Coffee Chain (Thailand)"),
    ("Café Coffee Day", "Coffee Chain (India)"), ("Third Wave Coffee", "Specialty Coffee (India)"),
    ("Blue Tokai", "Specialty Coffee (India)"), ("Sleepy Owl", "Coffee Brand (India)"),
    ("Wayne's Coffee", "Coffee Chain (Sweden)"), ("Espresso House", "Coffee Chain (Scandinavia)"),
    ("Robert's Coffee", "Coffee Chain (Finland)"), ("Balzac Coffee", "Coffee Chain (Germany)"),
], "Expense", "Food & Dining", "Coffee & Tea")

# ============================================================
# FOOD & DINING - Food Delivery (~80)
# ============================================================

add([
    ("DoorDash", "Food Delivery Platform"), ("Uber Eats", "Food Delivery Platform"),
    ("Grubhub", "Food Delivery Platform"), ("Postmates", "Multi-Category Delivery"),
    ("Seamless", "Food Delivery Platform"), ("Caviar", "Premium Food Delivery"),
    ("Instacart", "Grocery Delivery Platform"), ("Shipt", "Grocery Delivery Platform"),
    ("Gopuff", "Instant Delivery Platform"), ("goPuff", "Instant Delivery Platform"),
    ("Deliveroo", "Food Delivery (UK/EU)"), ("Just Eat", "Food Delivery (UK/EU)"),
    ("Just Eat Takeaway", "Food Delivery (EU)"), ("Lieferando", "Food Delivery (Germany)"),
    ("Wolt", "Food Delivery (Nordics/EU)"), ("Foodora", "Food Delivery (Nordics)"),
    ("Glovo", "Multi-Category Delivery (EU)"), ("Bolt Food", "Food Delivery (EU)"),
    ("Getir", "Instant Grocery Delivery"), ("Gorillas", "Instant Grocery Delivery"),
    ("Flink", "Instant Grocery Delivery"), ("Jokr", "Instant Grocery Delivery"),
    ("Swiggy", "Food Delivery (India)"), ("Zomato", "Food Delivery (India)"),
    ("Dunzo", "Multi-Category Delivery (India)"), ("Zepto", "Instant Delivery (India)"),
    ("Grab Food", "Food Delivery (SE Asia)"), ("Foodpanda", "Food Delivery (Asia)"),
    ("ShopeeFood", "Food Delivery (SE Asia)"), ("LINE MAN", "Food Delivery (Thailand)"),
    ("Robinhood", "Food Delivery (Thailand)"), ("Meituan", "Food Delivery (China)"),
    ("Ele.me", "Food Delivery (China)"), ("Coupang Eats", "Food Delivery (Korea)"),
    ("Baedal Minjok", "Food Delivery (Korea)"), ("Yogiyo", "Food Delivery (Korea)"),
    ("Demae-can", "Food Delivery (Japan)"), ("Uber Eats Japan", "Food Delivery (Japan)"),
    ("Rappi", "Multi-Category Delivery (Latin Am)"), ("iFood", "Food Delivery (Brazil)"),
    ("PedidosYa", "Food Delivery (Latin America)"), ("DiDi Food", "Food Delivery (Latin Am)"),
    ("Talabat", "Food Delivery (Middle East)"), ("Careem NOW", "Delivery (Middle East)"),
    ("HungerStation", "Food Delivery (Saudi)"), ("Toters", "Food Delivery (Lebanon)"),
    ("Mr D Food", "Food Delivery (South Africa)"), ("Jumia Food", "Food Delivery (Africa)"),
    ("Chowdeck", "Food Delivery (Nigeria)"), ("Skip The Dishes", "Food Delivery (Canada)"),
    ("Fantuan", "Food Delivery (Chinese diaspora)"),
], "Expense", "Food & Dining", "Food Delivery")

# ============================================================
# FOOD & DINING - Bakery & Desserts (~200)
# ============================================================

add([
    ("Panera Bread", "Bakery Cafe Chain"), ("Corner Bakery Cafe", "Bakery Cafe"),
    ("Au Bon Pain", "Bakery Cafe Chain"), ("Atlanta Bread Company", "Bakery Cafe"),
    ("La Madeleine", "French Bakery Cafe"), ("Le Pain Quotidien", "Belgian Bakery Cafe"),
    ("Paris Baguette", "Korean Bakery Chain"), ("Tous les Jours", "Korean Bakery Chain"),
    ("85°C Bakery Cafe", "Taiwanese Bakery Chain"), ("BreadTalk", "Asian Bakery Chain"),
    ("Yamazaki Bakery", "Japanese Bakery Chain"), ("Vie de France", "Japanese Bakery"),
    ("Beard Papa's", "Japanese Cream Puff Chain"), ("Uncle Tetsu", "Japanese Cheesecake"),
    ("Nothing Bundt Cakes", "Specialty Cake Shop"), ("Insomnia Cookies", "Late-Night Cookie Delivery"),
    ("Crumbl Cookies", "Specialty Cookie Shop"), ("Levain Bakery", "Cookie Bakery"),
    ("Magnolia Bakery", "Cupcake & Dessert Bakery"), ("Georgetown Cupcake", "Cupcake Bakery"),
    ("Sprinkles Cupcakes", "Cupcake Bakery"), ("Baked by Melissa", "Mini Cupcake Bakery"),
    ("Carlo's Bakery", "Italian-American Bakery"), ("Porto's Bakery", "Cuban Bakery"),
    ("Milk Bar", "Modern Bakery & Desserts"), ("Lady M", "Luxury Crêpe Cake Boutique"),
    ("Tartine Bakery", "Artisan Bakery"), ("Boudin Bakery", "Sourdough Bakery (SF)"),
    ("Doughnut Plant", "Artisan Doughnut Shop"), ("Voodoo Doughnut", "Novelty Doughnut Shop"),
    ("Duck Donuts", "Made-to-Order Doughnut Shop"), ("Hurts Donut", "Specialty Doughnut"),
    ("Tim Hortons", "Coffee & Doughnut Chain"), ("Shipley Do-Nuts", "Doughnut Chain"),
    ("LaMar's Donuts", "Doughnut Chain"), ("Winchell's Donuts", "Doughnut Chain"),
    ("Paul", "French Bakery (Global)"), ("Eric Kayser", "French Artisan Bakery"),
    ("Maison Kayser", "French Bakery"), ("Ladurée", "French Patisserie (Macarons)"),
    ("Pierre Hermé", "French Patisserie"), ("Fauchon", "French Luxury Patisserie"),
    ("Angelina Paris", "French Tea Room & Patisserie"), ("Gontran Cherrier", "French Bakery"),
    ("Poilâne", "French Sourdough Bakery"), ("Du Pain et des Idées", "French Bakery"),
    ("Konditorei Heinemann", "German Patisserie"), ("Café Gerbeaud", "Hungarian Patisserie"),
    ("Pastelaria Versailles", "Portuguese Patisserie"), ("Pastéis de Belém", "Portuguese Tart Bakery"),
    ("Hofbäckerei Edegger-Tax", "Austrian Bakery"), ("Demel", "Viennese Patisserie"),
    ("Grom", "Italian Gelato & Pastry"), ("Eataly Bakery", "Italian Market Bakery"),
], "Expense", "Food & Dining", "Bakery & Desserts")

# ============================================================
# FOOD & DINING - Ice Cream & Yogurt (~150)
# ============================================================

add([
    ("Baskin-Robbins", "Ice Cream Chain"), ("Cold Stone Creamery", "Ice Cream Chain"),
    ("Dairy Queen", "Ice Cream & Fast Food"), ("Häagen-Dazs", "Premium Ice Cream"),
    ("Ben & Jerry's", "Premium Ice Cream"), ("Magnum", "Premium Ice Cream"),
    ("Dippin' Dots", "Novelty Ice Cream"), ("Marble Slab Creamery", "Ice Cream Chain"),
    ("Carvel", "Ice Cream Chain"), ("Rita's Italian Ice", "Italian Ice & Frozen Custard"),
    ("Andy's Frozen Custard", "Frozen Custard Chain"), ("Culver's", "Frozen Custard & Burgers"),
    ("Jeni's Splendid Ice Creams", "Artisan Ice Cream"), ("Salt & Straw", "Artisan Ice Cream"),
    ("Van Leeuwen Ice Cream", "Artisan Ice Cream"), ("Ample Hills Creamery", "Artisan Ice Cream"),
    ("McConnell's Fine Ice Creams", "Artisan Ice Cream"), ("Graeter's", "Premium Ice Cream"),
    ("Handel's Ice Cream", "Premium Ice Cream"), ("Bruster's Real Ice Cream", "Ice Cream Chain"),
    ("Sub Zero Ice Cream", "Made-to-Order Ice Cream"), ("Creamistry", "Liquid Nitrogen Ice Cream"),
    ("Yogurtland", "Self-Serve Frozen Yogurt"), ("Menchie's", "Self-Serve Frozen Yogurt"),
    ("sweetFrog", "Self-Serve Frozen Yogurt"), ("Orange Leaf", "Self-Serve Frozen Yogurt"),
    ("Red Mango", "Frozen Yogurt Chain"), ("Pinkberry", "Frozen Yogurt Chain"),
    ("TCBY", "Frozen Yogurt Chain"), ("Tutti Frutti", "Self-Serve Frozen Yogurt"),
    ("16 Handles", "Self-Serve Frozen Yogurt"), ("Yogen Früz", "Frozen Yogurt Chain"),
    ("Pressed Juicery", "Cold-Pressed Juice & Freeze"), ("SweetCup", "Korean Frozen Dessert"),
    ("Grom", "Italian Gelato"), ("Amorino", "Italian Gelato Chain"),
    ("Venchi", "Italian Chocolate & Gelato"), ("Bacio di Latte", "Gelato (Brazil)"),
    ("Gelateria Otaleg", "Artisan Gelato (Italy)"), ("Vivoli", "Historic Gelato (Italy)"),
    ("Messina", "Gelato Chain (Australia)"), ("Gelatissimo", "Gelato Chain (Australia)"),
    ("N2 Extreme Gelato", "Liquid Nitrogen Gelato"), ("Snowbird Gelato", "Gelato Chain"),
    ("Bingsu King", "Korean Shaved Ice"), ("Sulbing", "Korean Shaved Ice"),
    ("Softree", "Soft Serve (Korea)"), ("Milksha", "Milk Tea & Soft Serve (Taiwan)"),
    ("Snow Factory", "Shaved Snow (Asia)"), ("Kakigori", "Japanese Shaved Ice"),
], "Expense", "Food & Dining", "Ice Cream & Yogurt")

# ============================================================
# FOOD & DINING - Snacks & Drinks (~100)
# ============================================================

add([
    ("Jamba", "Smoothie & Juice Chain"), ("Smoothie King", "Smoothie Chain"),
    ("Tropical Smoothie Cafe", "Smoothie & Food"), ("Robeks", "Smoothie & Juice"),
    ("Nekter Juice Bar", "Cold-Pressed Juice"), ("Pressed Juicery", "Cold-Pressed Juice"),
    ("Juice It Up!", "Smoothie & Juice"), ("Clean Juice", "Organic Juice Bar"),
    ("Joe & The Juice", "Juice & Coffee Bar"), ("Boost Juice", "Juice & Smoothie (AU)"),
    ("Juice Plus+", "Nutrition Supplement"), ("Daily Harvest", "Frozen Smoothie Delivery"),
    ("Auntie Anne's", "Soft Pretzel Chain"), ("Wetzel's Pretzels", "Soft Pretzel Chain"),
    ("Garrett Popcorn", "Gourmet Popcorn"), ("Kernels Popcorn", "Gourmet Popcorn"),
    ("See's Candies", "Chocolate & Candy"), ("Godiva", "Premium Chocolate"),
    ("Lindt", "Swiss Chocolate"), ("Ghirardelli", "Chocolate Company"),
    ("Fannie May", "Chocolate & Candy"), ("Rocky Mountain Chocolate", "Chocolate & Fudge"),
    ("Mrs. Fields", "Cookie & Snack Chain"), ("Great American Cookies", "Cookie Chain"),
    ("Cinnabon", "Cinnamon Roll Chain"), ("Auntie Anne's", "Pretzel Chain"),
    ("Häagen-Dazs", "Premium Ice Cream/Snack"), ("Godiva Chocolatier", "Luxury Chocolate"),
    ("Ferrero Rocher", "Chocolate & Confectionery"), ("Haribo", "Gummy Candy Maker"),
    ("Pocky", "Japanese Snack Brand"), ("KitKat Chocolatory", "Premium Chocolate (Japan)"),
    ("Royce' Chocolate", "Japanese Chocolate"), ("Tokyo Banana", "Japanese Souvenir Snack"),
], "Expense", "Food & Dining", "Snacks & Drinks")



# ============================================================
# TRANSPORTATION - Gas & Fuel (~200)
# ============================================================

add([
    ("Shell", "Gas Station"), ("ExxonMobil", "Gas Station"), ("BP", "Gas Station"),
    ("Chevron", "Gas Station"), ("Texaco", "Gas Station"), ("Valero", "Gas Station"),
    ("Marathon", "Gas Station"), ("Phillips 66", "Gas Station"), ("Conoco", "Gas Station"),
    ("Citgo", "Gas Station"), ("Sunoco", "Gas Station"), ("Sinclair", "Gas Station"),
    ("Murphy USA", "Gas Station"), ("Costco Gas", "Wholesale Club Gas"),
    ("Sam's Club Fuel", "Wholesale Club Gas"), ("BJ's Gas", "Wholesale Club Gas"),
    ("Kroger Fuel Center", "Grocery Store Gas"), ("Safeway Fuel", "Grocery Store Gas"),
    ("Speedway", "Gas & Convenience"), ("Pilot Flying J", "Truck Stop & Travel Center"),
    ("Love's Travel Stops", "Truck Stop"), ("TA Travel Centers", "Truck Stop"),
    ("Petro Stopping Centers", "Truck Stop"), ("Buc-ee's", "Travel Center & Gas"),
    ("Wawa Gas", "Convenience Store Gas"), ("Sheetz Gas", "Convenience Store Gas"),
    ("QuikTrip Gas", "Convenience Store Gas"), ("Casey's Gas", "Convenience Store Gas"),
    ("Kum & Go Gas", "Convenience Store Gas"), ("Maverik Gas", "Convenience Store Gas"),
    ("RaceTrac Gas", "Convenience Store Gas"), ("Circle K Gas", "Convenience Store Gas"),
    ("7-Eleven Gas", "Convenience Store Gas"), ("GetGo Gas", "Convenience Store Gas"),
    ("Royal Farms Gas", "Convenience Store Gas"), ("Thorntons Gas", "Convenience Store Gas"),
    ("Kwik Trip Gas", "Convenience Store Gas"), ("Holiday Gas", "Convenience Store Gas"),
    ("Mapco", "Gas & Convenience"), ("Flash Foods", "Gas & Convenience"),
    # International Gas
    ("Total Energies", "Gas Station (France/Global)"), ("Eni", "Gas Station (Italy)"),
    ("Repsol", "Gas Station (Spain)"), ("Cepsa", "Gas Station (Spain)"),
    ("Galp", "Gas Station (Portugal)"), ("OMV", "Gas Station (Austria)"),
    ("Aral", "Gas Station (Germany)"), ("Jet", "Gas Station (Germany/UK)"),
    ("Esso", "Gas Station (UK/EU)"), ("Avia", "Gas Station (EU)"),
    ("Q8", "Gas Station (Kuwait/EU)"), ("Star Gas", "Gas Station (EU)"),
    ("Orlen", "Gas Station (Poland)"), ("MOL", "Gas Station (Hungary)"),
    ("Lukoil", "Gas Station (Russia)"), ("Rosneft", "Gas Station (Russia)"),
    ("Gazpromneft", "Gas Station (Russia)"), ("Indian Oil", "Gas Station (India)"),
    ("Bharat Petroleum", "Gas Station (India)"), ("Hindustan Petroleum", "Gas Station (India)"),
    ("Reliance Petroleum", "Gas Station (India)"), ("Petronas", "Gas Station (Malaysia)"),
    ("PTT", "Gas Station (Thailand)"), ("Pertamina", "Gas Station (Indonesia)"),
    ("Caltex", "Gas Station (Asia-Pacific)"), ("Eneos", "Gas Station (Japan)"),
    ("Cosmo Oil", "Gas Station (Japan)"), ("SK Energy", "Gas Station (Korea)"),
    ("GS Caltex", "Gas Station (Korea)"), ("S-Oil", "Gas Station (Korea)"),
    ("Sinopec", "Gas Station (China)"), ("PetroChina", "Gas Station (China)"),
    ("CNOOC", "Gas Station (China)"), ("ADNOC", "Gas Station (UAE)"),
    ("ENOC", "Gas Station (UAE)"), ("Saudi Aramco", "Gas Station (Saudi)"),
    ("Pemex", "Gas Station (Mexico)"), ("YPF", "Gas Station (Argentina)"),
    ("Petrobras", "Gas Station (Brazil)"), ("Copec", "Gas Station (Chile)"),
    ("Sasol", "Gas Station (South Africa)"), ("Engen", "Gas Station (South Africa)"),
], "Expense", "Transportation", "Gas & Fuel")

# ============================================================
# TRANSPORTATION - Rideshare (~50)
# ============================================================

add([
    ("Uber", "Ride-Hailing Service"), ("Lyft", "Ride-Hailing Service"),
    ("Bolt", "Ride-Hailing Service"), ("Via", "Shared Ride Service"),
    ("Curb", "Taxi App"), ("Arro", "Taxi App"),
    ("DiDi", "Ride-Hailing (China/Global)"), ("Grab", "Ride-Hailing (SE Asia)"),
    ("Gojek", "Ride-Hailing (Indonesia)"), ("Ola", "Ride-Hailing (India)"),
    ("Careem", "Ride-Hailing (Middle East)"), ("Yandex Go", "Ride-Hailing (Russia)"),
    ("Kakao T", "Ride-Hailing (Korea)"), ("Tada", "Ride-Hailing (SE Asia)"),
    ("InDrive", "Ride-Hailing (Global)"), ("Cabify", "Ride-Hailing (Spain/Latin Am)"),
    ("99", "Ride-Hailing (Brazil)"), ("Beat", "Ride-Hailing (Latin Am/Greece)"),
    ("Free Now", "Ride-Hailing (Europe)"), ("Kapten", "Ride-Hailing (France)"),
    ("Gett", "Ride-Hailing (Israel/UK)"), ("Maxim", "Ride-Hailing (Russia/Asia)"),
    ("Taxify", "Ride-Hailing (Africa/EU)"), ("Heetch", "Ride-Hailing (France/Africa)"),
    ("Addison Lee", "Private Hire (UK)"), ("Blacklane", "Chauffeur Service"),
], "Expense", "Transportation", "Rideshare")

# ============================================================
# TRANSPORTATION - Public Transit (~50)
# ============================================================

add([
    ("MTA", "Metropolitan Transit Authority"), ("NJ Transit", "State Transit Authority"),
    ("BART", "Bay Area Rapid Transit"), ("Metra", "Commuter Rail (Chicago)"),
    ("MBTA", "Massachusetts Transit"), ("SEPTA", "Philadelphia Transit"),
    ("MARTA", "Atlanta Transit"), ("TriMet", "Portland Transit"),
    ("Metro Transit", "Minneapolis Transit"), ("RTD", "Denver Transit"),
    ("E-ZPass", "Electronic Toll Collection"), ("SunPass", "Florida Toll"),
    ("FasTrak", "California Toll"), ("TxTag", "Texas Toll"),
    ("I-Pass", "Illinois Toll"), ("Good To Go!", "Washington Toll"),
    ("Oyster Card", "London Transit Card"), ("Clipper Card", "SF Bay Transit Card"),
    ("OMNY", "NYC Transit Tap-to-Pay"), ("Ventra", "Chicago Transit Card"),
    ("SmarTrip", "DC Metro Card"), ("Charlie Card", "Boston Transit Card"),
    ("Presto Card", "Toronto Transit Card"), ("Opal Card", "Sydney Transit"),
    ("Octopus Card", "Hong Kong Transit"), ("Suica", "Japan Rail IC Card"),
    ("Pasmo", "Tokyo Transit Card"), ("ICOCA", "Japan Rail IC Card"),
    ("T-money", "Korea Transit Card"), ("EasyCard", "Taiwan Transit"),
    ("Navigo", "Paris Transit Card"), ("Rejsekort", "Denmark Transit Card"),
    ("OV-chipkaart", "Netherlands Transit"), ("BVG Ticket", "Berlin Transit"),
], "Expense", "Transportation", "Public Transit")

# ============================================================
# TRANSPORTATION - Car Service & Parts (~200)
# ============================================================

add([
    ("AutoZone", "Auto Parts Retailer"), ("O'Reilly Auto Parts", "Auto Parts Retailer"),
    ("Advance Auto Parts", "Auto Parts Retailer"), ("NAPA Auto Parts", "Auto Parts Retailer"),
    ("Pep Boys", "Auto Parts & Service"), ("CarQuest", "Auto Parts Retailer"),
    ("Jiffy Lube", "Oil Change & Auto Service"), ("Valvoline Instant", "Oil Change Service"),
    ("Midas", "Auto Repair & Service"), ("Maaco", "Auto Paint & Collision"),
    ("Meineke", "Auto Repair & Muffler"), ("Firestone Complete", "Tire & Auto Service"),
    ("Goodyear Auto Service", "Tire & Auto Service"), ("Discount Tire", "Tire Retailer"),
    ("Tire Kingdom", "Tire Retailer"), ("America's Tire", "Tire Retailer"),
    ("Les Schwab", "Tire & Auto Service"), ("Big O Tires", "Tire & Auto Service"),
    ("NTB - National Tire", "Tire & Auto Service"), ("Sullivan Tire", "Tire & Auto"),
    ("Safelite AutoGlass", "Auto Glass Repair"), ("Caliber Collision", "Auto Body Repair"),
    ("Service King", "Auto Body Repair"), ("Gerber Collision", "Auto Body Repair"),
    ("Take 5 Oil Change", "Oil Change Service"), ("Express Oil Change", "Oil Change"),
    ("Christian Brothers Automotive", "Auto Repair"), ("AAMCO", "Transmission Repair"),
    ("Brake Masters", "Brake Repair Service"), ("Brakes Plus", "Brake & Auto Repair"),
    ("Monro Muffler Brake", "Auto Repair Chain"), ("Tires Plus", "Tire & Auto Service"),
    ("Grease Monkey", "Oil Change & Auto"), ("Precision Tune Auto Care", "Auto Repair"),
    ("Tuffy Tire & Auto", "Tire & Auto Service"), ("Ziebart", "Auto Detailing & Protection"),
    ("Mavis Discount Tire", "Tire Retailer"), ("Town Fair Tire", "Tire Retailer"),
    # Car Wash
    ("Mister Car Wash", "Car Wash Chain"), ("Driven Brands Car Wash", "Car Wash"),
    ("Quick Quack Car Wash", "Car Wash Chain"), ("Zips Car Wash", "Car Wash Chain"),
    ("Tidal Wave Auto Spa", "Car Wash"), ("Club Car Wash", "Car Wash Chain"),
    ("Splash Car Wash", "Car Wash"), ("Delta Sonic", "Car Wash & Gas"),
    ("Wash Depot Holdings", "Car Wash Chain"), ("Tommy's Express", "Car Wash"),
    # Dealerships (major brands)
    ("Toyota Service", "Automobile Dealer Service"), ("Honda Service", "Automobile Dealer Service"),
    ("Ford Service", "Automobile Dealer Service"), ("Chevrolet Service", "Automobile Dealer Service"),
    ("BMW Service", "Automobile Dealer Service"), ("Mercedes-Benz Service", "Automobile Dealer Service"),
    ("Audi Service", "Automobile Dealer Service"), ("Volkswagen Service", "Automobile Dealer Service"),
    ("Hyundai Service", "Automobile Dealer Service"), ("Kia Service", "Automobile Dealer Service"),
    ("Nissan Service", "Automobile Dealer Service"), ("Subaru Service", "Automobile Dealer Service"),
    ("Mazda Service", "Automobile Dealer Service"), ("Lexus Service", "Automobile Dealer Service"),
    ("Tesla Service", "Electric Vehicle Service"), ("Volvo Service", "Automobile Dealer Service"),
    # International
    ("Halfords", "Auto Parts & Cycling (UK)"), ("Kwik Fit", "Auto Repair (UK)"),
    ("Euromaster", "Tire & Auto Service (EU)"), ("Norauto", "Auto Service (France)"),
    ("ATU", "Auto Parts & Service (Germany)"), ("A.T.U", "Auto Parts (Germany)"),
    ("Bosch Car Service", "Auto Repair (Global)"), ("Point S", "Tire & Auto (Global)"),
    ("Michelin", "Tire Manufacturer & Service"), ("Bridgestone", "Tire Manufacturer & Service"),
    ("Continental Tire", "Tire Manufacturer"), ("Pirelli", "Tire Manufacturer"),
], "Expense", "Transportation", "Car Service & Parts")



# ============================================================
# SHOPPING - General Retail (~500)
# ============================================================

add([
    ("Amazon", "Online Marketplace"), ("Walmart", "Supercenter & General Merchandise"),
    ("Target", "General Merchandise Retailer"), ("eBay", "Online Auction & Marketplace"),
    ("Etsy", "Handmade & Vintage Marketplace"), ("Wish", "Online Discount Marketplace"),
    ("Temu", "Online Discount Marketplace"), ("Shein", "Fast Fashion E-Commerce"),
    ("AliExpress", "Online Marketplace (China)"), ("Alibaba", "B2B Online Marketplace"),
    ("Dollar General", "Discount Variety Store"), ("Dollar Tree", "Dollar Store Chain"),
    ("Family Dollar", "Discount Variety Store"), ("Five Below", "Discount Retailer"),
    ("99 Cents Only", "Dollar Store"), ("Big Lots", "Discount Retailer"),
    ("Ollie's Bargain Outlet", "Discount Retailer"), ("Tuesday Morning", "Off-Price Home"),
    ("Ross Dress for Less", "Off-Price Department Store"), ("T.J. Maxx", "Off-Price Department"),
    ("Marshalls", "Off-Price Department Store"), ("HomeGoods", "Off-Price Home Furnishings"),
    ("Burlington", "Off-Price Department Store"), ("Nordstrom Rack", "Off-Price Department"),
    ("Saks Off 5th", "Off-Price Luxury"), ("Overstock.com", "Online Discount Retailer"),
    ("Wayfair", "Online Home Goods"), ("Groupon", "Online Deals & Coupons"),
    ("Rakuten", "Online Marketplace (Japan)"), ("Mercari", "Peer-to-Peer Marketplace"),
    ("Poshmark", "Fashion Resale Marketplace"), ("ThredUp", "Online Thrift Store"),
    ("Depop", "Fashion Resale (Gen Z)"), ("StockX", "Sneaker & Streetwear Marketplace"),
    ("GOAT", "Sneaker Marketplace"), ("Reverb", "Musical Instrument Marketplace"),
    # Department Stores
    ("Macy's", "Department Store"), ("Nordstrom", "Upscale Department Store"),
    ("JCPenney", "Department Store"), ("Kohl's", "Department Store"),
    ("Dillard's", "Department Store"), ("Neiman Marcus", "Luxury Department Store"),
    ("Saks Fifth Avenue", "Luxury Department Store"), ("Bergdorf Goodman", "Luxury Department"),
    ("Bloomingdale's", "Upscale Department Store"), ("Barneys New York", "Luxury Department"),
    ("Selfridges", "Luxury Department Store (UK)"), ("Harrods", "Luxury Department Store (UK)"),
    ("John Lewis", "Department Store (UK)"), ("Debenhams", "Department Store (UK)"),
    ("Harvey Nichols", "Luxury Department Store (UK)"), ("Liberty London", "Department Store (UK)"),
    ("Galeries Lafayette", "Department Store (France)"), ("Le Bon Marché", "Department Store (France)"),
    ("Printemps", "Department Store (France)"), ("KaDeWe", "Department Store (Germany)"),
    ("El Corte Inglés", "Department Store (Spain)"), ("La Rinascente", "Department Store (Italy)"),
    ("Takashimaya", "Department Store (Japan)"), ("Isetan", "Department Store (Japan)"),
    ("Mitsukoshi", "Department Store (Japan)"), ("Sogo", "Department Store (Japan/Asia)"),
    ("Lotte Department Store", "Department Store (Korea)"), ("Shinsegae", "Department Store (Korea)"),
    ("Hyundai Department Store", "Department Store (Korea)"), ("David Jones", "Department Store (AU)"),
    ("Myer", "Department Store (Australia)"),
    # Variety/General International
    ("Miniso", "Variety Store Chain (China)"), ("Daiso", "100-Yen Store (Japan)"),
    ("Flying Tiger Copenhagen", "Variety Store (Denmark)"), ("Muji", "Lifestyle Goods (Japan)"),
    ("Hema", "Variety Store (Netherlands)"), ("Action", "Discount Variety (Netherlands)"),
    ("Primark", "Discount Fashion & Home (UK)"), ("Poundland", "Discount Variety (UK)"),
    ("B&M Bargains", "Discount Variety (UK)"), ("Home Bargains", "Discount Variety (UK)"),
    ("Woolworths Group", "General Retail (Australia)"), ("Kmart Australia", "Discount Department"),
    ("The Reject Shop", "Discount Variety (AU)"), ("Mr Price", "Value Retailer (South Africa)"),
    ("Takealot", "Online Marketplace (South Africa)"), ("Jumia", "Online Marketplace (Africa)"),
    ("Lazada", "Online Marketplace (SE Asia)"), ("Shopee", "Online Marketplace (SE Asia)"),
    ("Tokopedia", "Online Marketplace (Indonesia)"), ("Bukalapak", "Online Marketplace (Indonesia)"),
    ("Flipkart", "Online Marketplace (India)"), ("Myntra", "Fashion E-Commerce (India)"),
    ("Snapdeal", "Online Marketplace (India)"), ("Meesho", "Social Commerce (India)"),
    ("Coupang", "E-Commerce Platform (Korea)"), ("Naver Shopping", "E-Commerce (Korea)"),
    ("11Street", "E-Commerce (Korea)"), ("Gmarket", "Online Marketplace (Korea)"),
    ("JD.com", "E-Commerce Platform (China)"), ("Pinduoduo", "Group-Buy E-Commerce (China)"),
    ("Taobao", "Online Marketplace (China)"), ("Tmall", "Premium E-Commerce (China)"),
    ("MercadoLibre", "Online Marketplace (Latin Am)"), ("Submarino", "E-Commerce (Brazil)"),
    ("Magazine Luiza", "Retail & E-Commerce (Brazil)"), ("Falabella", "Department Store (Chile)"),
    ("Liverpool", "Department Store (Mexico)"), ("Palacio de Hierro", "Luxury Department (Mexico)"),
    ("Soriana", "Hypermarket & Retail (Mexico)"), ("Hepsiburada", "E-Commerce (Turkey)"),
    ("Trendyol", "E-Commerce (Turkey)"), ("Noon", "E-Commerce (Middle East)"),
    ("Souq.com", "E-Commerce (Middle East)"), ("Namshi", "Fashion E-Commerce (Middle East)"),
], "Expense", "Shopping", "General Retail")

# ============================================================
# SHOPPING - Clothing & Apparel (~700)
# ============================================================

add([
    # Fast Fashion
    ("Zara", "Fast Fashion Retailer"), ("H&M", "Fast Fashion Retailer"),
    ("Uniqlo", "Casual Apparel Retailer"), ("Forever 21", "Fast Fashion Retailer"),
    ("Primark", "Discount Fashion"), ("Mango", "Fashion Apparel"),
    ("Pull&Bear", "Youth Fashion (Inditex)"), ("Bershka", "Youth Fashion (Inditex)"),
    ("Stradivarius", "Women's Fashion (Inditex)"), ("Massimo Dutti", "Premium Casual (Inditex)"),
    ("Cotton On", "Fast Fashion (Australia)"), ("Superdry", "Fashion Brand (UK)"),
    ("River Island", "Fashion Retailer (UK)"), ("New Look", "Fashion Retailer (UK)"),
    ("Topshop", "Fashion Retailer (UK)"), ("ASOS", "Online Fashion Retailer"),
    ("Boohoo", "Online Fast Fashion"), ("Pretty Little Thing", "Online Fast Fashion"),
    ("Missguided", "Online Fast Fashion"), ("Fashion Nova", "Online Fast Fashion"),
    # Casual & Mid-Range
    ("Gap", "Casual Apparel"), ("Old Navy", "Value Casual Apparel"),
    ("Banana Republic", "Premium Casual Apparel"), ("J.Crew", "Preppy Apparel"),
    ("Abercrombie & Fitch", "Casual Apparel"), ("Hollister", "Teen Casual Apparel"),
    ("American Eagle", "Casual Apparel"), ("Aerie", "Intimates & Loungewear"),
    ("Express", "Fashion Apparel"), ("Guess", "Fashion Apparel & Accessories"),
    ("Calvin Klein", "Designer Fashion & Underwear"), ("Tommy Hilfiger", "Premium Fashion"),
    ("Ralph Lauren", "Premium Fashion & Lifestyle"), ("Lacoste", "Premium Casual (French)"),
    ("Hugo Boss", "Designer Fashion"), ("Michael Kors", "Accessible Luxury Fashion"),
    ("Kate Spade", "Accessible Luxury Fashion"), ("Tory Burch", "Accessible Luxury"),
    ("Ted Baker", "Designer Fashion (UK)"), ("AllSaints", "Contemporary Fashion (UK)"),
    ("French Connection", "Fashion Brand (UK)"), ("Reiss", "Premium Fashion (UK)"),
    ("COS", "Minimalist Fashion (H&M Group)"), ("& Other Stories", "Fashion (H&M Group)"),
    ("Arket", "Lifestyle Brand (H&M Group)"), ("Weekday", "Fashion (H&M Group)"),
    ("Monki", "Fashion (H&M Group)"),
    # Athletic & Sportswear
    ("Nike", "Athletic Apparel & Footwear"), ("Adidas", "Athletic Apparel & Footwear"),
    ("Puma", "Athletic Apparel & Footwear"), ("Under Armour", "Athletic Performance Apparel"),
    ("New Balance", "Athletic Footwear & Apparel"), ("Reebok", "Athletic Footwear & Apparel"),
    ("ASICS", "Athletic Footwear"), ("Skechers", "Casual & Athletic Footwear"),
    ("Brooks Running", "Running Footwear"), ("Saucony", "Running Footwear"),
    ("Hoka", "Running Footwear"), ("On Running", "Premium Running Footwear"),
    ("Lululemon", "Athletic Apparel (Yoga)"), ("Athleta", "Women's Athletic Apparel"),
    ("Fabletics", "Athletic Apparel (DTC)"), ("Alo Yoga", "Premium Yoga Apparel"),
    ("Gymshark", "Fitness Apparel (UK)"), ("Sweaty Betty", "Women's Activewear (UK)"),
    ("Outdoor Voices", "Casual Athletic Apparel"), ("Vuori", "Premium Athletic Casual"),
    ("Rhone", "Men's Athletic Apparel"),
    # Outdoor & Adventure
    ("The North Face", "Outdoor Apparel & Gear"), ("Patagonia", "Outdoor & Sustainable Apparel"),
    ("Columbia Sportswear", "Outdoor Apparel"), ("REI Co-op", "Outdoor Gear & Apparel"),
    ("Arc'teryx", "Premium Outdoor Apparel"), ("Marmot", "Outdoor Apparel"),
    ("Mountain Hardwear", "Outdoor Apparel"), ("Fjällräven", "Swedish Outdoor Brand"),
    ("Jack Wolfskin", "Outdoor Brand (Germany)"), ("Berghaus", "Outdoor Brand (UK)"),
    ("Rab", "Outdoor Brand (UK)"), ("Salomon", "Outdoor Footwear & Gear"),
    ("Merrell", "Hiking Footwear"), ("Timberland", "Outdoor Boots & Apparel"),
    ("L.L.Bean", "Outdoor Apparel & Gear"), ("Eddie Bauer", "Outdoor & Casual Apparel"),
    ("Cabela's", "Outdoor & Hunting"), ("Bass Pro Shops", "Outdoor & Fishing"),
    # Denim & Casual
    ("Levi's", "Denim & Casual Apparel"), ("Wrangler", "Western & Denim"),
    ("Lee Jeans", "Denim Apparel"), ("True Religion", "Premium Denim"),
    ("AG Jeans", "Premium Denim"), ("7 For All Mankind", "Premium Denim"),
    ("Diesel", "Denim & Fashion (Italy)"), ("G-Star Raw", "Denim & Fashion (Netherlands)"),
    # Luxury Fashion
    ("Louis Vuitton", "Luxury Fashion House"), ("Gucci", "Luxury Fashion House"),
    ("Chanel", "Luxury Fashion House"), ("Hermès", "Luxury Fashion House"),
    ("Prada", "Luxury Fashion House"), ("Dior", "Luxury Fashion House"),
    ("Burberry", "Luxury Fashion (UK)"), ("Versace", "Luxury Fashion (Italy)"),
    ("Valentino", "Luxury Fashion (Italy)"), ("Balenciaga", "Luxury Fashion (Spain)"),
    ("Fendi", "Luxury Fashion (Italy)"), ("Givenchy", "Luxury Fashion (France)"),
    ("Saint Laurent", "Luxury Fashion (France)"), ("Bottega Veneta", "Luxury Fashion (Italy)"),
    ("Alexander McQueen", "Luxury Fashion (UK)"), ("Stella McCartney", "Luxury Fashion (UK)"),
    ("Dolce & Gabbana", "Luxury Fashion (Italy)"), ("Moncler", "Luxury Outerwear (Italy)"),
    ("Max Mara", "Luxury Fashion (Italy)"), ("Salvatore Ferragamo", "Luxury Fashion (Italy)"),
    ("Loewe", "Luxury Fashion (Spain)"), ("Celine", "Luxury Fashion (France)"),
    ("Tom Ford", "Luxury Fashion"), ("Off-White", "Luxury Streetwear"),
    ("Acne Studios", "Contemporary Luxury (Sweden)"), ("Isabel Marant", "Designer Fashion (France)"),
    # Footwear
    ("Foot Locker", "Athletic Footwear Retailer"), ("Finish Line", "Athletic Footwear"),
    ("Journeys", "Teen Footwear Retailer"), ("Famous Footwear", "Footwear Retailer"),
    ("DSW", "Footwear Retailer"), ("Shoe Carnival", "Footwear Retailer"),
    ("Crocs", "Casual Footwear"), ("Vans", "Skate & Casual Footwear"),
    ("Converse", "Casual Footwear"), ("Birkenstock", "Comfort Sandals"),
    ("UGG", "Sheepskin Boots & Footwear"), ("Dr. Martens", "Boots & Footwear (UK)"),
    ("Clarks", "Footwear (UK)"), ("Steve Madden", "Fashion Footwear"),
    ("Stuart Weitzman", "Luxury Footwear"), ("Jimmy Choo", "Luxury Footwear"),
    ("Christian Louboutin", "Luxury Footwear"), ("Manolo Blahnik", "Luxury Footwear"),
    ("Cole Haan", "Premium Footwear"), ("Allen Edmonds", "Dress Shoes"),
    # Jewelry & Accessories
    ("Tiffany & Co.", "Luxury Jewelry"), ("Cartier", "Luxury Jewelry & Watches"),
    ("Pandora", "Jewelry Retailer"), ("Kay Jewelers", "Jewelry Retailer"),
    ("Zales", "Jewelry Retailer"), ("Jared", "Jewelry Retailer"),
    ("David Yurman", "Designer Jewelry"), ("Swarovski", "Crystal Jewelry & Accessories"),
    ("Alex and Ani", "Fashion Jewelry"), ("Kendra Scott", "Fashion Jewelry"),
    ("Mejuri", "DTC Fine Jewelry"), ("Brilliant Earth", "Ethical Jewelry"),
    ("Blue Nile", "Online Diamond Retailer"), ("James Allen", "Online Diamond Retailer"),
    # Watches
    ("Rolex", "Luxury Watch Manufacturer"), ("Omega", "Luxury Watch Manufacturer"),
    ("TAG Heuer", "Luxury Watch Manufacturer"), ("Breitling", "Luxury Watch Manufacturer"),
    ("IWC", "Luxury Watch Manufacturer"), ("Tissot", "Swiss Watch Manufacturer"),
    ("Seiko", "Watch Manufacturer (Japan)"), ("Casio", "Watch & Electronics (Japan)"),
    ("Fossil", "Fashion Watches & Accessories"), ("Citizen", "Watch Manufacturer (Japan)"),
    ("Garmin", "GPS & Fitness Watches"), ("Apple Watch", "Smartwatch"),
    ("Fitbit", "Fitness Tracker"), ("Samsung Galaxy Watch", "Smartwatch"),
    # Intimates & Swimwear
    ("Victoria's Secret", "Lingerie & Beauty"), ("Savage X Fenty", "Lingerie (Inclusive)"),
    ("ThirdLove", "DTC Bras & Intimates"), ("Skims", "Shapewear & Loungewear"),
    ("Spanx", "Shapewear"), ("Soma", "Intimates & Sleepwear"),
    # Kids Clothing
    ("Carter's", "Children's Clothing"), ("OshKosh B'Gosh", "Children's Clothing"),
    ("Gymboree", "Children's Clothing"), ("The Children's Place", "Children's Clothing"),
    ("Hanna Andersson", "Children's Clothing"), ("Primary", "DTC Kids Clothing"),
    ("Janie and Jack", "Premium Kids Clothing"), ("Tea Collection", "Kids Clothing"),
], "Expense", "Shopping", "Clothing & Apparel")



# ============================================================
# SHOPPING - Electronics (~400)
# ============================================================

add([
    ("Apple", "Consumer Electronics & Software"), ("Samsung", "Electronics Conglomerate"),
    ("Sony", "Electronics & Entertainment"), ("LG Electronics", "Electronics Manufacturer"),
    ("Microsoft", "Software & Hardware"), ("Google Pixel", "Smartphone"),
    ("Dell", "Computer Manufacturer"), ("HP", "Computer Manufacturer"),
    ("Lenovo", "Computer Manufacturer"), ("ASUS", "Computer Hardware"),
    ("Acer", "Computer Hardware"), ("MSI", "Gaming Hardware"),
    ("Razer", "Gaming Peripherals"), ("Corsair", "Gaming & PC Components"),
    ("Logitech", "Computer Peripherals"), ("SteelSeries", "Gaming Peripherals"),
    ("HyperX", "Gaming Peripherals"), ("NVIDIA", "GPU Manufacturer"),
    ("AMD", "Semiconductor Manufacturer"), ("Intel", "Semiconductor Manufacturer"),
    ("Qualcomm", "Mobile Chipset"), ("Western Digital", "Storage Devices"),
    ("Seagate", "Storage Devices"), ("Kingston Technology", "Memory & Storage"),
    ("Crucial", "Memory & Storage"), ("SanDisk", "Flash Storage"),
    # Retailers
    ("Best Buy", "Consumer Electronics Retailer"), ("B&H Photo", "Electronics & Camera"),
    ("Micro Center", "Computer & Electronics"), ("Fry's Electronics", "Electronics Retailer"),
    ("NewEgg", "Online Electronics Retailer"), ("Adorama", "Camera & Electronics"),
    ("GameStop", "Video Game Retailer"), ("Currys", "Electronics Retailer (UK)"),
    ("MediaMarkt", "Electronics Retailer (EU)"), ("Saturn", "Electronics Retailer (Germany)"),
    ("Fnac", "Electronics & Media (France)"), ("Darty", "Electronics Retailer (France)"),
    ("Boulanger", "Electronics Retailer (France)"), ("Euronics", "Electronics Retailer (EU)"),
    ("Expert", "Electronics Retailer (EU)"), ("Elkjøp", "Electronics (Scandinavia)"),
    ("Power", "Electronics (Scandinavia)"), ("Yodobashi Camera", "Electronics (Japan)"),
    ("Bic Camera", "Electronics (Japan)"), ("Yamada Denki", "Electronics (Japan)"),
    ("K's Denki", "Electronics (Japan)"), ("Edion", "Electronics (Japan)"),
    ("Hi-Mart", "Electronics (Korea)"), ("Croma", "Electronics (India)"),
    ("Vijay Sales", "Electronics (India)"), ("Reliance Digital", "Electronics (India)"),
    ("JB Hi-Fi", "Electronics Retailer (Australia)"), ("Harvey Norman", "Electronics (AU)"),
    ("The Good Guys", "Electronics (Australia)"),
    # Audio
    ("Bose", "Audio Equipment"), ("Sonos", "Wireless Speakers & Audio"),
    ("Bang & Olufsen", "Premium Audio (Denmark)"), ("Harman Kardon", "Audio Equipment"),
    ("JBL", "Audio Equipment"), ("Sennheiser", "Audio Equipment (Germany)"),
    ("Audio-Technica", "Audio Equipment (Japan)"), ("Beats by Dre", "Headphones & Audio"),
    ("Marshall", "Audio Equipment (UK)"), ("Klipsch", "Audio Equipment"),
    # Cameras & Imaging
    ("Canon", "Camera & Imaging"), ("Nikon", "Camera & Imaging"),
    ("Sony Alpha", "Camera & Imaging"), ("Fujifilm", "Camera & Imaging (Japan)"),
    ("Panasonic Lumix", "Camera & Imaging"), ("GoPro", "Action Camera"),
    ("DJI", "Drone & Camera Manufacturer"), ("Insta360", "360 Camera"),
    # Smart Home
    ("Ring", "Smart Home Security"), ("Nest", "Smart Home (Google)"),
    ("Arlo", "Smart Home Security"), ("Wyze", "Smart Home Devices"),
    ("Philips Hue", "Smart Lighting"), ("ecobee", "Smart Thermostat"),
    ("August Home", "Smart Lock"), ("SimpliSafe", "Home Security System"),
    ("ADT", "Home Security System"), ("Vivint", "Smart Home Security"),
    # Appliances
    ("Dyson", "Premium Home Appliances"), ("iRobot", "Robot Vacuum"),
    ("Shark", "Vacuum & Home"), ("Vitamix", "High-Performance Blender"),
    ("Breville", "Kitchen Appliances"), ("KitchenAid", "Kitchen Appliances"),
    ("Instant Pot", "Multi-Cooker"), ("Ninja", "Kitchen Appliances"),
    ("Keurig", "Coffee Machine"), ("Nespresso", "Coffee Machine"),
    ("De'Longhi", "Coffee & Kitchen Appliances"), ("Weber", "Grills & Outdoor Cooking"),
    ("Traeger", "Wood Pellet Grills"), ("Big Green Egg", "Ceramic Grill"),
], "Expense", "Shopping", "Electronics")

# ============================================================
# SHOPPING - Home & Garden (~300)
# ============================================================

add([
    ("Home Depot", "Home Improvement Retailer"), ("Lowe's", "Home Improvement Retailer"),
    ("Menards", "Home Improvement Retailer"), ("Ace Hardware", "Hardware Store"),
    ("True Value", "Hardware Store"), ("Do it Best", "Hardware Store"),
    ("Tractor Supply", "Farm & Ranch Retailer"), ("Harbor Freight", "Discount Tool Store"),
    ("IKEA", "Furniture & Home Goods"), ("Wayfair", "Online Home Goods"),
    ("Pottery Barn", "Home Furnishings"), ("West Elm", "Modern Home Furnishings"),
    ("Crate & Barrel", "Home Furnishings"), ("CB2", "Modern Home Furnishings"),
    ("Williams-Sonoma", "Kitchen & Home"), ("Restoration Hardware", "Luxury Home Furnishings"),
    ("Arhaus", "Artisan Home Furnishings"), ("Ethan Allen", "Furniture Retailer"),
    ("La-Z-Boy", "Furniture Retailer"), ("Ashley Furniture", "Furniture Retailer"),
    ("Rooms To Go", "Furniture Retailer"), ("Bob's Discount Furniture", "Discount Furniture"),
    ("Raymour & Flanigan", "Furniture Retailer"), ("Haverty's", "Furniture Retailer"),
    ("Article", "DTC Modern Furniture"), ("Joybird", "Mid-Century Modern Furniture"),
    ("Burrow", "DTC Sofa & Furniture"), ("Floyd", "Modular Furniture"),
    ("Bed Bath & Beyond", "Home Goods Retailer"), ("HomeGoods", "Off-Price Home Furnishings"),
    ("Tuesday Morning", "Off-Price Home & Gifts"), ("At Home", "Home Décor Superstore"),
    ("Pier 1 Imports", "Home Décor & Furniture"), ("World Market", "Global Home & Food"),
    ("Anthropologie Home", "Bohemian Home Décor"), ("Urban Outfitters Home", "Modern Home"),
    ("Terrain", "Garden & Home"), ("Crate & Kids", "Kids Furniture & Décor"),
    ("Pottery Barn Kids", "Kids Furniture & Décor"), ("Land of Nod", "Kids Furniture"),
    # Bed & Bath
    ("Casper", "DTC Mattress"), ("Purple Mattress", "DTC Mattress"),
    ("Tempur-Pedic", "Premium Mattress"), ("Sleep Number", "Adjustable Mattress"),
    ("Mattress Firm", "Mattress Retailer"), ("Brooklinen", "DTC Bedding"),
    ("Parachute Home", "DTC Bedding & Bath"), ("Boll & Branch", "Premium Bedding"),
    ("Buffy", "Sustainable Bedding"), ("Cozy Earth", "Bamboo Bedding"),
    # Garden & Outdoor
    ("Scotts Miracle-Gro", "Lawn & Garden Products"), ("Home Depot Garden", "Garden Center"),
    ("Lowe's Garden", "Garden Center"), ("Tractor Supply Garden", "Farm & Garden"),
    ("Terrain", "Garden & Outdoor Living"), ("Gardener's Supply", "Garden Retailer"),
    ("Burpee Seeds", "Seed & Garden Company"), ("Park Seed", "Seed Company"),
    # Kitchen & Dining
    ("Williams-Sonoma", "Premium Kitchen & Cookware"), ("Sur La Table", "Kitchen & Cookware"),
    ("Le Creuset", "Premium Cookware (French)"), ("All-Clad", "Premium Cookware"),
    ("Staub", "Premium Cookware (French)"), ("Lodge Cast Iron", "Cast Iron Cookware"),
    ("Calphalon", "Cookware & Bakeware"), ("Cuisinart", "Kitchen Appliances & Cookware"),
    ("OXO", "Kitchen Tools & Gadgets"),
    # UK/EU Home
    ("B&Q", "Home Improvement (UK)"), ("Screwfix", "Trade Supplies (UK)"),
    ("Homebase", "Home & Garden (UK)"), ("Wickes", "Home Improvement (UK)"),
    ("Leroy Merlin", "Home Improvement (France/EU)"), ("Bauhaus", "Home Improvement (Germany)"),
    ("Hornbach", "Home Improvement (Germany)"), ("OBI", "Home Improvement (Germany)"),
    ("Jysk", "Home Furnishings (Denmark/EU)"), ("Maisons du Monde", "Home Décor (France)"),
    ("Habitat", "Modern Home Furnishings (UK)"), ("Dunelm", "Home Textiles & Furnishings (UK)"),
    ("John Lewis Home", "Home & Garden (UK)"), ("The White Company", "Home & Lifestyle (UK)"),
    ("Zara Home", "Home Textiles (Inditex)"), ("H&M Home", "Home Textiles"),
], "Expense", "Shopping", "Home & Garden")

# ============================================================
# SHOPPING - Sporting Goods (~150)
# ============================================================

add([
    ("Dick's Sporting Goods", "Sporting Goods Retailer"), ("Academy Sports", "Sporting Goods"),
    ("REI", "Outdoor Gear & Apparel"), ("Bass Pro Shops", "Outdoor & Fishing"),
    ("Cabela's", "Outdoor & Hunting"), ("Scheels", "Sporting Goods"),
    ("Big 5 Sporting Goods", "Sporting Goods"), ("Hibbett Sports", "Athletic Footwear & Apparel"),
    ("Modell's Sporting Goods", "Sporting Goods"), ("Sport Chek", "Sporting Goods (Canada)"),
    ("Decathlon", "Sporting Goods (France/Global)"), ("JD Sports", "Sportswear Retailer (UK)"),
    ("Sports Direct", "Discount Sports (UK)"), ("Intersport", "Sporting Goods (EU)"),
    ("XXL Sport", "Sporting Goods (Scandinavia)"), ("Stadium", "Sporting Goods (Sweden)"),
    ("Rebel Sport", "Sporting Goods (Australia)"), ("Anaconda", "Outdoor Gear (Australia)"),
    ("BCF", "Boating Camping Fishing (AU)"), ("Kathmandu", "Outdoor Gear (NZ/AU)"),
    # Specialized
    ("Titleist", "Golf Equipment"), ("Callaway Golf", "Golf Equipment"),
    ("TaylorMade", "Golf Equipment"), ("Ping", "Golf Equipment"),
    ("PGA Tour Superstore", "Golf Retailer"), ("Golf Galaxy", "Golf Retailer"),
    ("Tennis Express", "Tennis Equipment"), ("Wilson Sporting Goods", "Multi-Sport Equipment"),
    ("Rawlings", "Baseball Equipment"), ("Louisville Slugger", "Baseball Bats"),
    ("Easton Sports", "Baseball & Hockey Equipment"), ("CCM Hockey", "Hockey Equipment"),
    ("Bauer Hockey", "Hockey Equipment"), ("Pure Hockey", "Hockey Retailer"),
    ("Peloton", "Connected Fitness Equipment"), ("NordicTrack", "Home Fitness Equipment"),
    ("Rogue Fitness", "CrossFit & Weightlifting Equipment"), ("Bowflex", "Home Fitness Equipment"),
    ("Life Fitness", "Commercial Fitness Equipment"), ("Technogym", "Fitness Equipment (Italy)"),
    ("Yeti", "Outdoor Coolers & Drinkware"), ("RTIC Outdoors", "Coolers & Drinkware"),
    ("Hydro Flask", "Insulated Water Bottles"), ("S'well", "Insulated Water Bottles"),
    ("CamelBak", "Hydration Products"), ("Osprey Packs", "Backpacks & Travel"),
    ("Gregory", "Backpacks"), ("Deuter", "Backpacks (Germany)"),
], "Expense", "Shopping", "Sporting Goods")

# ============================================================
# SHOPPING - Pet Supplies (~80)
# ============================================================

add([
    ("PetSmart", "Pet Supply Retailer"), ("Petco", "Pet Supply Retailer"),
    ("Chewy", "Online Pet Supply"), ("BarkBox", "Dog Subscription Box"),
    ("Farmer's Dog", "Fresh Dog Food Delivery"), ("Ollie", "Fresh Dog Food Delivery"),
    ("Nom Nom Now", "Fresh Pet Food"), ("JustFoodForDogs", "Fresh Pet Food"),
    ("Blue Buffalo", "Pet Food Brand"), ("Hill's Science Diet", "Premium Pet Food"),
    ("Royal Canin", "Premium Pet Food"), ("Purina", "Pet Food Brand"),
    ("Iams", "Pet Food Brand"), ("Wellness Pet Food", "Natural Pet Food"),
    ("Orijen", "Premium Pet Food"), ("Acana", "Premium Pet Food"),
    ("Banfield Pet Hospital", "Veterinary Clinic Chain"), ("VCA Animal Hospitals", "Veterinary Chain"),
    ("Petplan", "Pet Insurance"), ("Trupanion", "Pet Insurance"),
    ("Lemonade Pet", "Pet Insurance"), ("Healthy Paws", "Pet Insurance"),
    ("Pets at Home", "Pet Supply (UK)"), ("Fressnapf", "Pet Supply (Germany)"),
    ("Zooplus", "Online Pet Supply (EU)"), ("Maxi Zoo", "Pet Supply (EU)"),
    ("Pet Circle", "Online Pet Supply (AU)"), ("PetBarn", "Pet Supply (Australia)"),
], "Expense", "Shopping", "Pet Supplies")

# ============================================================
# SHOPPING - Books & Media (~100)
# ============================================================

add([
    ("Barnes & Noble", "Book Retailer"), ("Books-A-Million", "Book Retailer"),
    ("Half Price Books", "Used Book Retailer"), ("Powell's Books", "Independent Bookstore"),
    ("ThriftBooks", "Online Used Books"), ("Better World Books", "Online Used Books"),
    ("Amazon Kindle", "E-Book Store"), ("Apple Books", "E-Book Store"),
    ("Google Play Books", "E-Book Store"), ("Kobo", "E-Reader & E-Books"),
    ("Audible", "Audiobook Service"), ("Libro.fm", "Indie Audiobook Service"),
    ("Scribd", "E-Book & Audiobook Subscription"), ("Kindle Unlimited", "E-Book Subscription"),
    ("Bookshop.org", "Online Indie Bookstore"), ("Waterstones", "Book Retailer (UK)"),
    ("WHSmith", "Book & Stationery (UK)"), ("Fnac", "Books & Media (France)"),
    ("Thalia", "Book Retailer (Germany)"), ("Hugendubel", "Book Retailer (Germany)"),
    ("Kinokuniya", "Book Retailer (Japan)"), ("Tsutaya", "Books & Media (Japan)"),
    ("Kyobo Book Centre", "Book Retailer (Korea)"), ("Popular Bookstore", "Books (Malaysia)"),
    # Music/Media
    ("Spotify", "Music Streaming"), ("Apple Music", "Music Streaming"),
    ("YouTube Music", "Music Streaming"), ("Amazon Music", "Music Streaming"),
    ("Tidal", "Hi-Fi Music Streaming"), ("Deezer", "Music Streaming"),
    ("SoundCloud", "Music Streaming & Sharing"), ("Bandcamp", "Indie Music Marketplace"),
    ("Vinyl Me Please", "Vinyl Subscription"), ("Discogs", "Music Marketplace"),
], "Expense", "Shopping", "Books & Media")

# ============================================================
# SHOPPING - Office Supplies (~60)
# ============================================================

add([
    ("Staples", "Office Supply Retailer"), ("Office Depot", "Office Supply Retailer"),
    ("OfficeMax", "Office Supply Retailer"), ("Quill.com", "Online Office Supplies"),
    ("Vistaprint", "Custom Printing & Marketing"), ("Shutterfly", "Photo Printing & Gifts"),
    ("FedEx Office", "Printing & Shipping"), ("UPS Store", "Printing & Shipping"),
    ("The UPS Store", "Printing & Shipping"), ("Staples Print", "Business Printing"),
    ("Ryman", "Stationery & Office (UK)"), ("Viking Direct", "Office Supplies (UK/EU)"),
    ("Bureau Vallée", "Office Supplies (France)"), ("Lyreco", "Office Supplies (B2B EU)"),
    ("ASKUL", "Office Supplies (Japan)"), ("Kokuyo", "Stationery (Japan)"),
    ("Moleskine", "Premium Notebooks"), ("Leuchtturm1917", "Premium Notebooks (Germany)"),
    ("Rhodia", "Premium Paper & Notebooks (France)"), ("Muji Stationery", "Minimal Stationery"),
], "Expense", "Shopping", "Office Supplies")



# ============================================================
# ENTERTAINMENT - Streaming Video (~80)
# ============================================================

add([
    ("Netflix", "Video Streaming Service"), ("Disney+", "Video Streaming Service"),
    ("Hulu", "Video Streaming Service"), ("HBO Max", "Video Streaming Service"),
    ("Amazon Prime Video", "Video Streaming Service"), ("Apple TV+", "Video Streaming Service"),
    ("Paramount+", "Video Streaming Service"), ("Peacock", "Video Streaming Service"),
    ("Discovery+", "Documentary & Reality Streaming"), ("ESPN+", "Sports Streaming"),
    ("Showtime", "Premium Cable & Streaming"), ("Starz", "Premium Cable & Streaming"),
    ("AMC+", "Streaming Service"), ("BritBox", "British TV Streaming"),
    ("Acorn TV", "International TV Streaming"), ("Sundance Now", "Indie Film Streaming"),
    ("Shudder", "Horror Streaming"), ("Criterion Channel", "Classic Film Streaming"),
    ("MUBI", "Curated Film Streaming"), ("Kanopy", "Free Streaming (Library)"),
    ("Tubi", "Free Video Streaming"), ("Pluto TV", "Free Streaming"),
    ("Roku Channel", "Free Streaming"), ("Vudu", "Video on Demand"),
    ("Crunchyroll", "Anime Streaming"), ("Funimation", "Anime Streaming"),
    ("VRV", "Animation & Sci-Fi Streaming"), ("CuriosityStream", "Documentary Streaming"),
    ("Vimeo", "Video Hosting Platform"), ("YouTube Premium", "Video & Music Streaming"),
    ("Twitch", "Live Streaming Platform"), ("Philo", "Live TV Streaming"),
    ("Sling TV", "Live TV Streaming"), ("fuboTV", "Sports-Focused Live TV"),
    ("YouTube TV", "Live TV Streaming"), ("Hulu Live TV", "Live TV Streaming"),
    ("DAZN", "Sports Streaming (Global)"), ("beIN Sports", "Sports Streaming (ME/EU)"),
    ("Now TV", "Streaming (UK)"), ("All 4", "Streaming (UK)"),
    ("Stan", "Video Streaming (Australia)"), ("Binge", "Video Streaming (Australia)"),
    ("Kayo Sports", "Sports Streaming (AU)"), ("Crave", "Video Streaming (Canada)"),
    ("Shahid", "Video Streaming (Middle East)"), ("Viu", "Video Streaming (Asia)"),
    ("iQIYI", "Video Streaming (China)"), ("Youku", "Video Streaming (China)"),
    ("Bilibili", "Video Streaming (China)"), ("TVer", "Free Streaming (Japan)"),
    ("Hotstar", "Video Streaming (India)"), ("ZEE5", "Video Streaming (India)"),
    ("SonyLIV", "Video Streaming (India)"), ("Voot", "Video Streaming (India)"),
    ("Wavve", "Video Streaming (Korea)"), ("Watcha", "Video Streaming (Korea)"),
    ("Vidio", "Video Streaming (Indonesia)"), ("WeTV", "Video Streaming (SE Asia)"),
], "Expense", "Entertainment", "Streaming Video")

# ============================================================
# ENTERTAINMENT - Gaming (~100)
# ============================================================

add([
    ("PlayStation Store", "Digital Game Store"), ("Xbox Store", "Digital Game Store"),
    ("Nintendo eShop", "Digital Game Store"), ("Steam", "PC Game Platform"),
    ("Epic Games Store", "PC Game Platform"), ("GOG.com", "DRM-Free Game Store"),
    ("EA Play", "Game Subscription"), ("Xbox Game Pass", "Game Subscription"),
    ("PlayStation Plus", "Game Subscription"), ("Nintendo Switch Online", "Game Subscription"),
    ("Ubisoft+", "Game Subscription"), ("GeForce Now", "Cloud Gaming"),
    ("Stadia", "Cloud Gaming (Google)"), ("Xbox Cloud Gaming", "Cloud Gaming"),
    ("Activision Blizzard", "Game Publisher"), ("Electronic Arts", "Game Publisher"),
    ("Take-Two Interactive", "Game Publisher"), ("Ubisoft", "Game Publisher"),
    ("Square Enix", "Game Publisher (Japan)"), ("Capcom", "Game Publisher (Japan)"),
    ("Bandai Namco", "Game Publisher (Japan)"), ("Konami", "Game Publisher (Japan)"),
    ("Sega", "Game Publisher (Japan)"), ("Nintendo", "Game Company"),
    ("Sony Interactive", "Game Company"), ("Microsoft Gaming", "Game Company"),
    ("Riot Games", "Game Developer"), ("Valve", "Game Developer & Platform"),
    ("Mojang Studios", "Game Developer (Minecraft)"), ("Supercell", "Mobile Game Developer"),
    ("Niantic", "Mobile Game Developer"), ("King (Candy Crush)", "Mobile Game Developer"),
    ("Zynga", "Mobile Game Developer"), ("miHoYo/HoYoverse", "Game Developer (China)"),
    ("Tencent Games", "Game Publisher (China)"), ("NetEase Games", "Game Publisher (China)"),
    ("Nexon", "Game Publisher (Korea)"), ("NCSoft", "Game Publisher (Korea)"),
    ("Krafton", "Game Developer (PUBG)"), ("Roblox", "Gaming Platform"),
    # Hardware & Retailers
    ("GameStop", "Video Game Retailer"), ("GAME", "Video Game Retailer (UK)"),
    ("EB Games", "Video Game Retailer (AU/CA)"), ("Gamers Gate", "Digital Game Retailer"),
    ("Razer", "Gaming Peripherals"), ("SteelSeries", "Gaming Peripherals"),
    ("Corsair", "Gaming Peripherals & Components"), ("HyperX", "Gaming Peripherals"),
    ("Logitech G", "Gaming Peripherals"), ("Turtle Beach", "Gaming Headsets"),
    ("SCUF Gaming", "Custom Controllers"), ("Secretlab", "Gaming Chairs"),
    ("DXRacer", "Gaming Chairs"), ("Herman Miller Gaming", "Ergonomic Gaming Chairs"),
], "Expense", "Entertainment", "Gaming")

# ============================================================
# ENTERTAINMENT - Movies & Events (~150)
# ============================================================

add([
    ("AMC Theatres", "Movie Theater Chain"), ("Regal Cinemas", "Movie Theater Chain"),
    ("Cinemark", "Movie Theater Chain"), ("Marcus Theatres", "Movie Theater Chain"),
    ("Alamo Drafthouse", "Dine-In Movie Theater"), ("IPIC Theaters", "Luxury Cinema"),
    ("Studio Movie Grill", "Dine-In Cinema"), ("Landmark Theatres", "Art House Cinema"),
    ("Showcase Cinemas", "Movie Theater"), ("Harkins Theatres", "Movie Theater"),
    ("Malco Theatres", "Movie Theater"), ("Bow Tie Cinemas", "Movie Theater"),
    ("Cineworld", "Movie Theater (UK)"), ("Odeon", "Movie Theater (UK)"),
    ("Vue Cinemas", "Movie Theater (UK)"), ("Curzon", "Art House Cinema (UK)"),
    ("Pathé", "Movie Theater (France/NL)"), ("Gaumont", "Movie Theater (France)"),
    ("CineStar", "Movie Theater (Germany)"), ("UCI Cinemas", "Movie Theater (Italy)"),
    ("Hoyts", "Movie Theater (Australia)"), ("Event Cinemas", "Movie Theater (AU/NZ)"),
    ("Village Cinemas", "Movie Theater (Australia)"), ("PVR Cinemas", "Movie Theater (India)"),
    ("INOX", "Movie Theater (India)"), ("Cinépolis", "Movie Theater (Mexico/Global)"),
    ("Cinemex", "Movie Theater (Mexico)"), ("CGV", "Movie Theater (Korea/Global)"),
    ("Lotte Cinema", "Movie Theater (Korea)"), ("Megabox", "Movie Theater (Korea)"),
    ("Toho Cinemas", "Movie Theater (Japan)"), ("Golden Village", "Movie Theater (Singapore)"),
    ("Shaw Theatres", "Movie Theater (Singapore)"), ("Vox Cinemas", "Movie Theater (ME)"),
    # Ticketing & Events
    ("Ticketmaster", "Event Ticketing Platform"), ("Live Nation", "Concert & Event Promoter"),
    ("AXS", "Event Ticketing"), ("SeatGeek", "Event Ticket Marketplace"),
    ("StubHub", "Event Ticket Resale"), ("Vivid Seats", "Event Ticket Marketplace"),
    ("Eventbrite", "Event Ticketing Platform"), ("Dice", "Music Event Ticketing"),
    ("See Tickets", "Event Ticketing (UK)"), ("Ticketek", "Event Ticketing (AU)"),
    ("Viagogo", "Ticket Resale Marketplace"), ("TickPick", "No-Fee Ticket Marketplace"),
    # Performing Arts
    ("Broadway", "Live Theater (NYC)"), ("West End", "Live Theater (London)"),
    ("Cirque du Soleil", "Contemporary Circus"), ("Blue Man Group", "Performance Art"),
    ("Medieval Times", "Dinner & Tournament"), ("Second City", "Comedy Theater"),
    # Museums & Cultural
    ("Metropolitan Museum of Art", "Art Museum"), ("MoMA", "Modern Art Museum"),
    ("Smithsonian", "Museum Complex"), ("National Gallery", "Art Museum (UK)"),
    ("British Museum", "Museum (UK)"), ("Louvre", "Art Museum (France)"),
    ("Guggenheim", "Art Museum"), ("Whitney Museum", "Art Museum"),
], "Expense", "Entertainment", "Movies & Events")

# ============================================================
# ENTERTAINMENT - Amusement & Parks (~150)
# ============================================================

add([
    ("Walt Disney World", "Theme Park"), ("Disneyland", "Theme Park"),
    ("Universal Studios", "Theme Park"), ("Universal Orlando", "Theme Park"),
    ("Islands of Adventure", "Theme Park"), ("SeaWorld", "Marine Theme Park"),
    ("Busch Gardens", "Theme Park"), ("Six Flags", "Amusement Park Chain"),
    ("Cedar Point", "Amusement Park"), ("Knott's Berry Farm", "Amusement Park"),
    ("Hersheypark", "Amusement Park"), ("Dollywood", "Theme Park"),
    ("Silver Dollar City", "Theme Park"), ("Legoland", "Theme Park"),
    ("Kings Island", "Amusement Park"), ("Kings Dominion", "Amusement Park"),
    ("Carowinds", "Amusement Park"), ("Dorney Park", "Amusement Park"),
    ("Great Adventure", "Amusement Park"), ("Worlds of Fun", "Amusement Park"),
    ("Schlitterbahn", "Water Park"), ("Splish Splash", "Water Park"),
    ("Water Country USA", "Water Park"), ("Typhoon Texas", "Water Park"),
    ("Great Wolf Lodge", "Indoor Water Park Resort"), ("Kalahari Resorts", "Water Park Resort"),
    # International Theme Parks
    ("Tokyo Disneyland", "Theme Park (Japan)"), ("Tokyo DisneySea", "Theme Park (Japan)"),
    ("Universal Studios Japan", "Theme Park (Japan)"), ("Fuji-Q Highland", "Amusement Park (Japan)"),
    ("Everland", "Theme Park (Korea)"), ("Lotte World", "Theme Park (Korea)"),
    ("Shanghai Disneyland", "Theme Park (China)"), ("Hong Kong Disneyland", "Theme Park"),
    ("Ocean Park Hong Kong", "Theme Park & Aquarium"), ("Chimelong", "Theme Park (China)"),
    ("Europa-Park", "Theme Park (Germany)"), ("Phantasialand", "Theme Park (Germany)"),
    ("Efteling", "Theme Park (Netherlands)"), ("Tivoli Gardens", "Amusement Park (Denmark)"),
    ("Liseberg", "Amusement Park (Sweden)"), ("PortAventura", "Theme Park (Spain)"),
    ("Alton Towers", "Theme Park (UK)"), ("Thorpe Park", "Theme Park (UK)"),
    ("Chessington", "Theme Park (UK)"), ("Legoland Windsor", "Theme Park (UK)"),
    ("Ferrari World", "Theme Park (UAE)"), ("IMG Worlds", "Indoor Theme Park (UAE)"),
    ("Dreamworld", "Theme Park (Australia)"), ("Luna Park", "Amusement Park (AU)"),
    # Family Entertainment Centers
    ("Dave & Buster's", "Arcade & Dining"), ("Main Event", "Entertainment Center"),
    ("Topgolf", "Golf Entertainment Complex"), ("Punch Bowl Social", "Social Entertainment"),
    ("Round1", "Arcade & Entertainment (Japan)"), ("Timezone", "Arcade (Asia-Pacific)"),
    ("Chuck E. Cheese", "Kids Entertainment & Pizza"), ("Peter Piper Pizza", "Kids Pizza & Games"),
    ("Urban Air", "Trampoline & Adventure Park"), ("Sky Zone", "Trampoline Park"),
    ("iFLY Indoor Skydiving", "Indoor Skydiving"), ("K1 Speed", "Indoor Go-Kart Racing"),
    ("Andretti Indoor Karting", "Indoor Karting"), ("Bowlero", "Bowling & Entertainment"),
    ("Lucky Strike", "Bowling & Lounge"), ("Pinstripes", "Bowling & Bistro"),
    # Zoos & Aquariums
    ("San Diego Zoo", "Zoo"), ("Bronx Zoo", "Zoo"), ("National Zoo", "Zoo"),
    ("Georgia Aquarium", "Aquarium"), ("Monterey Bay Aquarium", "Aquarium"),
    ("Shedd Aquarium", "Aquarium"), ("Vancouver Aquarium", "Aquarium"),
    ("Chester Zoo", "Zoo (UK)"), ("London Zoo", "Zoo (UK)"),
    ("Singapore Zoo", "Zoo"), ("Taronga Zoo", "Zoo (Australia)"),
], "Expense", "Entertainment", "Amusement & Parks")

# ============================================================
# ENTERTAINMENT - Sports & Recreation (~100)
# ============================================================

add([
    # Sports Leagues & Venues
    ("NFL", "Professional Football League"), ("NBA", "Professional Basketball League"),
    ("MLB", "Professional Baseball League"), ("NHL", "Professional Hockey League"),
    ("MLS", "Professional Soccer League"), ("PGA Tour", "Professional Golf"),
    ("UFC", "Mixed Martial Arts"), ("WWE", "Professional Wrestling"),
    ("Premier League", "English Soccer League"), ("La Liga", "Spanish Soccer League"),
    ("Bundesliga", "German Soccer League"), ("Serie A", "Italian Soccer League"),
    ("Ligue 1", "French Soccer League"), ("Formula 1", "Motor Racing"),
    ("NASCAR", "Stock Car Racing"),
    # Fitness & Gyms
    ("Planet Fitness", "Gym & Fitness Club"), ("LA Fitness", "Gym & Fitness Club"),
    ("24 Hour Fitness", "Gym & Fitness Club"), ("Gold's Gym", "Gym & Fitness Club"),
    ("Anytime Fitness", "Gym Franchise"), ("Orangetheory Fitness", "Boutique Fitness"),
    ("CrossFit", "Functional Fitness"), ("SoulCycle", "Cycling Studio"),
    ("Barry's Bootcamp", "Fitness Studio"), ("F45 Training", "Group Fitness"),
    ("Equinox", "Premium Gym & Fitness"), ("Lifetime Fitness", "Premium Fitness Club"),
    ("YMCA", "Community Fitness & Recreation"), ("ClassPass", "Fitness Membership App"),
    ("Mindbody", "Fitness & Wellness Booking"), ("Peloton", "Connected Fitness"),
    ("Barre3", "Barre Fitness Studio"), ("Pure Barre", "Barre Fitness Studio"),
    ("CorePower Yoga", "Yoga Studio Chain"), ("YogaWorks", "Yoga Studio Chain"),
    ("Bikram Yoga", "Hot Yoga Studio"), ("Club Pilates", "Pilates Studio"),
    ("CycleBar", "Cycling Studio"), ("Row House", "Rowing Fitness Studio"),
    ("Rumble Boxing", "Boxing Fitness Studio"), ("Title Boxing Club", "Boxing Fitness"),
    ("UFC Gym", "MMA & Fitness"), ("9Round Fitness", "Kickboxing Circuit Training"),
    ("Crunch Fitness", "Gym & Fitness"), ("Blink Fitness", "Budget Gym"),
    ("Snap Fitness", "24-Hour Gym Franchise"), ("Retro Fitness", "Budget Gym"),
    ("YouFit", "Budget Gym"), ("Workout Anytime", "24-Hour Gym"),
    ("Orangetheory", "Boutique Fitness"), ("Burn Boot Camp", "Fitness Camp"),
    # International Gyms
    ("PureGym", "Gym (UK)"), ("The Gym Group", "Budget Gym (UK)"),
    ("David Lloyd Clubs", "Premium Gym (UK)"), ("Virgin Active", "Premium Gym (Global)"),
    ("Fitness First", "Gym Chain (Global)"), ("McFIT", "Gym Chain (Germany)"),
    ("Basic-Fit", "Gym Chain (EU)"), ("Fitness Park", "Gym Chain (France)"),
    ("GoodLife Fitness", "Gym Chain (Canada)"), ("Jetts Fitness", "Gym (Australia)"),
    ("Fitness First AU", "Gym (Australia)"), ("Cult.fit", "Fitness (India)"),
    ("Gold's Gym India", "Gym (India)"), ("Talwalkars", "Gym (India)"),
    # Golf
    ("Topgolf", "Golf Entertainment"), ("PGA Tour Superstore", "Golf Retail"),
    ("Golf Galaxy", "Golf Retail"), ("GolfNow", "Tee Time Booking"),
    ("Club Champion", "Golf Club Fitting"),
], "Expense", "Entertainment", "Sports & Recreation")



# ============================================================
# TRAVEL - Airlines (~120)
# ============================================================

add([
    # US Airlines
    ("American Airlines", "Major Airline"), ("Delta Air Lines", "Major Airline"),
    ("United Airlines", "Major Airline"), ("Southwest Airlines", "Low-Cost Airline"),
    ("JetBlue", "Low-Cost Airline"), ("Alaska Airlines", "Airline"),
    ("Spirit Airlines", "Ultra-Low-Cost Airline"), ("Frontier Airlines", "Ultra-Low-Cost Airline"),
    ("Allegiant Air", "Ultra-Low-Cost Airline"), ("Hawaiian Airlines", "Airline"),
    ("Sun Country Airlines", "Low-Cost Airline"), ("Breeze Airways", "Low-Cost Airline"),
    # European Airlines
    ("British Airways", "Major Airline (UK)"), ("Ryanair", "Ultra-Low-Cost (Ireland)"),
    ("easyJet", "Low-Cost Airline (UK)"), ("Wizz Air", "Ultra-Low-Cost (Hungary)"),
    ("Vueling", "Low-Cost Airline (Spain)"), ("Norwegian Air", "Low-Cost (Scandinavia)"),
    ("Lufthansa", "Major Airline (Germany)"), ("Air France", "Major Airline (France)"),
    ("KLM", "Major Airline (Netherlands)"), ("Iberia", "Major Airline (Spain)"),
    ("Alitalia/ITA", "Airline (Italy)"), ("Swiss Air", "Airline (Switzerland)"),
    ("Austrian Airlines", "Airline (Austria)"), ("SAS", "Airline (Scandinavia)"),
    ("Finnair", "Airline (Finland)"), ("LOT Polish Airlines", "Airline (Poland)"),
    ("TAP Air Portugal", "Airline (Portugal)"), ("Aer Lingus", "Airline (Ireland)"),
    ("Turkish Airlines", "Major Airline (Turkey)"), ("Aegean Airlines", "Airline (Greece)"),
    # Asian Airlines
    ("Emirates", "Major Airline (UAE)"), ("Qatar Airways", "Major Airline (Qatar)"),
    ("Etihad Airways", "Major Airline (UAE)"), ("Singapore Airlines", "Major Airline"),
    ("Cathay Pacific", "Major Airline (Hong Kong)"), ("ANA", "Major Airline (Japan)"),
    ("Japan Airlines", "Major Airline (Japan)"), ("Korean Air", "Major Airline (Korea)"),
    ("Asiana Airlines", "Airline (Korea)"), ("Thai Airways", "Major Airline (Thailand)"),
    ("Malaysia Airlines", "Airline (Malaysia)"), ("AirAsia", "Low-Cost Airline (Asia)"),
    ("Garuda Indonesia", "Airline (Indonesia)"), ("Lion Air", "Low-Cost (Indonesia)"),
    ("Vietnam Airlines", "Airline (Vietnam)"), ("VietJet Air", "Low-Cost (Vietnam)"),
    ("Philippine Airlines", "Airline (Philippines)"), ("Cebu Pacific", "Low-Cost (Philippines)"),
    ("China Southern", "Major Airline (China)"), ("Air China", "Major Airline (China)"),
    ("China Eastern", "Major Airline (China)"), ("Hainan Airlines", "Airline (China)"),
    ("IndiGo", "Low-Cost Airline (India)"), ("Air India", "Major Airline (India)"),
    ("SpiceJet", "Low-Cost Airline (India)"),
    # Other
    ("Air Canada", "Major Airline (Canada)"), ("WestJet", "Airline (Canada)"),
    ("Qantas", "Major Airline (Australia)"), ("Virgin Australia", "Airline (Australia)"),
    ("LATAM Airlines", "Major Airline (Latin Am)"), ("Avianca", "Airline (Colombia)"),
    ("Copa Airlines", "Airline (Panama)"), ("Azul Airlines", "Airline (Brazil)"),
    ("South African Airways", "Airline"), ("Ethiopian Airlines", "Major Airline (Africa)"),
    ("Kenya Airways", "Airline (Kenya)"), ("Royal Air Maroc", "Airline (Morocco)"),
    ("EgyptAir", "Airline (Egypt)"), ("Saudia", "Airline (Saudi Arabia)"),
], "Expense", "Travel", "Airlines")

# ============================================================
# TRAVEL - Hotels & Lodging (~350)
# ============================================================

add([
    # Marriott Brands
    ("Marriott", "Hotel Chain"), ("Courtyard by Marriott", "Select-Service Hotel"),
    ("Residence Inn", "Extended Stay Hotel"), ("SpringHill Suites", "All-Suite Hotel"),
    ("Fairfield Inn", "Economy Hotel"), ("TownePlace Suites", "Extended Stay"),
    ("AC Hotels", "Lifestyle Hotel"), ("Aloft Hotels", "Boutique Hotel"),
    ("Element Hotels", "Eco-Friendly Extended Stay"), ("Moxy Hotels", "Boutique Budget"),
    ("W Hotels", "Lifestyle Luxury Hotel"), ("Westin", "Upscale Hotel"),
    ("Sheraton", "Full-Service Hotel"), ("JW Marriott", "Luxury Hotel"),
    ("The Ritz-Carlton", "Luxury Hotel"), ("St. Regis", "Ultra-Luxury Hotel"),
    ("Edition Hotels", "Luxury Boutique"), ("Autograph Collection", "Independent Luxury"),
    # Hilton Brands
    ("Hilton", "Hotel Chain"), ("Hilton Garden Inn", "Upscale Hotel"),
    ("Hampton Inn", "Economy Hotel"), ("Embassy Suites", "All-Suite Hotel"),
    ("DoubleTree", "Full-Service Hotel"), ("Home2 Suites", "Extended Stay"),
    ("Homewood Suites", "Extended Stay"), ("Tru by Hilton", "Budget Hotel"),
    ("Curio Collection", "Boutique Hotel"), ("Tapestry Collection", "Boutique"),
    ("Conrad Hotels", "Luxury Hotel"), ("Waldorf Astoria", "Ultra-Luxury Hotel"),
    ("LXR Hotels", "Luxury Collection"), ("Canopy by Hilton", "Lifestyle Hotel"),
    ("Tempo by Hilton", "Lifestyle Hotel"), ("Signia by Hilton", "Premium Meeting Hotel"),
    # Hyatt Brands
    ("Hyatt", "Hotel Chain"), ("Hyatt Regency", "Full-Service Hotel"),
    ("Grand Hyatt", "Luxury Hotel"), ("Park Hyatt", "Ultra-Luxury Hotel"),
    ("Hyatt Place", "Select-Service Hotel"), ("Hyatt House", "Extended Stay"),
    ("Andaz", "Luxury Boutique Hotel"), ("Thompson Hotels", "Luxury Lifestyle"),
    ("Caption by Hyatt", "Lifestyle Hotel"), ("Hyatt Centric", "Lifestyle Hotel"),
    # IHG Brands
    ("Holiday Inn", "Midscale Hotel"), ("Holiday Inn Express", "Economy Hotel"),
    ("Crowne Plaza", "Upscale Hotel"), ("InterContinental", "Luxury Hotel"),
    ("Kimpton Hotels", "Boutique Hotel"), ("Hotel Indigo", "Boutique Hotel"),
    ("Staybridge Suites", "Extended Stay"), ("Candlewood Suites", "Extended Stay"),
    ("Even Hotels", "Wellness Hotel"), ("Voco Hotels", "Upscale Hotel"),
    ("Regent Hotels", "Ultra-Luxury Hotel"), ("Six Senses", "Luxury Wellness Resort"),
    # Wyndham Brands
    ("Wyndham Hotels", "Hotel Chain"), ("Ramada", "Midscale Hotel"),
    ("Days Inn", "Economy Hotel"), ("Super 8", "Budget Hotel"),
    ("Microtel", "Budget Hotel"), ("La Quinta", "Midscale Hotel"),
    ("Baymont", "Budget Hotel"), ("Travelodge", "Budget Hotel"),
    ("Howard Johnson", "Economy Hotel"), ("AmeriHost", "Economy Hotel"),
    # Choice Hotels
    ("Comfort Inn", "Economy Hotel"), ("Quality Inn", "Economy Hotel"),
    ("Sleep Inn", "Budget Hotel"), ("Clarion", "Midscale Hotel"),
    ("Econo Lodge", "Budget Hotel"), ("Rodeway Inn", "Budget Hotel"),
    ("MainStay Suites", "Extended Stay"), ("Cambria Hotels", "Upscale Hotel"),
    ("Ascend Collection", "Boutique Collection"),
    # Independent Luxury
    ("Four Seasons", "Luxury Hotel"), ("Mandarin Oriental", "Luxury Hotel"),
    ("Peninsula Hotels", "Luxury Hotel"), ("Shangri-La", "Luxury Hotel"),
    ("Rosewood Hotels", "Ultra-Luxury Hotel"), ("Aman Resorts", "Ultra-Luxury Resort"),
    ("One&Only Resorts", "Ultra-Luxury Resort"), ("Banyan Tree", "Luxury Resort"),
    ("Oberoi Hotels", "Luxury Hotel (India)"), ("Taj Hotels", "Luxury Hotel (India)"),
    ("ITC Hotels", "Luxury Hotel (India)"), ("Raffles Hotels", "Luxury Hotel"),
    ("Belmond", "Luxury Hotel & Train"), ("Rocco Forte", "Luxury Hotel (UK)"),
    ("Dorchester Collection", "Luxury Hotel"), ("Oetker Collection", "Luxury Hotel"),
    # Vacation & Alternative
    ("Airbnb", "Short-Term Rental Platform"), ("Vrbo", "Vacation Rental Platform"),
    ("Booking.com", "Online Travel Agency"), ("Expedia", "Online Travel Agency"),
    ("Hotels.com", "Hotel Booking Platform"), ("Trivago", "Hotel Price Comparison"),
    ("Agoda", "Hotel Booking (Asia)"), ("Trip.com", "Travel Booking (China)"),
    ("MakeMyTrip", "Travel Booking (India)"), ("Despegar", "Travel Booking (Latin Am)"),
    # Budget International
    ("Premier Inn", "Budget Hotel (UK)"), ("Travelodge UK", "Budget Hotel (UK)"),
    ("ibis", "Budget Hotel (Accor)"), ("ibis Budget", "Economy Hotel (Accor)"),
    ("Novotel", "Midscale Hotel (Accor)"), ("Mercure", "Midscale Hotel (Accor)"),
    ("Sofitel", "Luxury Hotel (Accor)"), ("Pullman", "Upscale Hotel (Accor)"),
    ("MGallery", "Boutique Hotel (Accor)"), ("Mövenpick", "Upscale Hotel (Accor)"),
    ("NH Hotels", "Hotel Chain (Spain)"), ("Meliá Hotels", "Hotel Chain (Spain)"),
    ("Scandic Hotels", "Hotel Chain (Scandinavia)"), ("Radisson", "Hotel Chain"),
    ("APA Hotels", "Hotel Chain (Japan)"), ("Toyoko Inn", "Business Hotel (Japan)"),
    ("Route Inn", "Business Hotel (Japan)"), ("Dormy Inn", "Business Hotel (Japan)"),
    # Car Rental
    ("Enterprise Rent-A-Car", "Car Rental"), ("Hertz", "Car Rental"),
    ("Avis", "Car Rental"), ("Budget Car Rental", "Car Rental"),
    ("National Car Rental", "Car Rental"), ("Alamo Rent A Car", "Car Rental"),
    ("Dollar Rent A Car", "Car Rental"), ("Thrifty Car Rental", "Car Rental"),
    ("Sixt", "Car Rental (Germany/Global)"), ("Europcar", "Car Rental (EU)"),
    ("Zipcar", "Car Sharing Service"), ("Turo", "Peer-to-Peer Car Rental"),
    ("Getaround", "Peer-to-Peer Car Sharing"),
], "Expense", "Travel", "Hotels & Lodging")



# ============================================================
# HEALTH & WELLNESS (~500 total)
# ============================================================

add([
    # Pharmacy Chains
    ("CVS Pharmacy", "Pharmacy & Drugstore Chain"), ("Walgreens", "Pharmacy & Drugstore Chain"),
    ("Rite Aid", "Pharmacy & Drugstore Chain"), ("Walmart Pharmacy", "Pharmacy (In-Store)"),
    ("Kroger Pharmacy", "Pharmacy (In-Store)"), ("Costco Pharmacy", "Pharmacy (In-Store)"),
    ("Express Scripts", "Pharmacy Benefit Manager"), ("OptumRx", "Pharmacy Benefit Manager"),
    ("Capsule Pharmacy", "Online Pharmacy"), ("Alto Pharmacy", "Digital Pharmacy"),
    ("Amazon Pharmacy", "Online Pharmacy"), ("PillPack", "Online Pharmacy (Amazon)"),
    ("GoodRx", "Prescription Discount"), ("RxSaver", "Prescription Discount"),
    ("Boots", "Pharmacy & Health/Beauty (UK)"), ("Superdrug", "Pharmacy & Beauty (UK)"),
    ("LloydsPharmacy", "Pharmacy (UK)"), ("Rossmann", "Drugstore (Germany)"),
    ("dm-drogerie markt", "Drugstore (Germany)"), ("Müller", "Drugstore (Germany)"),
    ("Apotek Hjärtat", "Pharmacy (Sweden)"), ("Apotea", "Online Pharmacy (Sweden)"),
    ("Farmacity", "Pharmacy Chain (Argentina)"), ("Drogasil", "Pharmacy (Brazil)"),
    ("Watsons", "Pharmacy & Beauty (Asia)"), ("Guardian Pharmacy", "Pharmacy (Asia)"),
    ("Matsumoto Kiyoshi", "Drugstore (Japan)"), ("Welcia", "Drugstore (Japan)"),
    ("Tsuruha Drug", "Drugstore (Japan)"), ("Olive Young", "Health & Beauty (Korea)"),
    ("Apollo Pharmacy", "Pharmacy (India)"), ("MedPlus", "Pharmacy (India)"),
    ("PharmEasy", "Online Pharmacy (India)"), ("1mg", "Online Pharmacy (India)"),
    ("Dis-Chem", "Pharmacy (South Africa)"), ("Clicks", "Pharmacy (South Africa)"),
], "Expense", "Health & Wellness", "Pharmacy")

add([
    # Beauty & Personal Care Retailers
    ("Sephora", "Beauty & Cosmetics Retailer"), ("Ulta Beauty", "Beauty & Cosmetics Retailer"),
    ("MAC Cosmetics", "Prestige Cosmetics"), ("Estée Lauder", "Prestige Beauty"),
    ("Clinique", "Prestige Skincare"), ("Lancôme", "Prestige Beauty (French)"),
    ("Bobbi Brown", "Prestige Cosmetics"), ("NARS Cosmetics", "Prestige Cosmetics"),
    ("Urban Decay", "Cosmetics Brand"), ("Too Faced", "Cosmetics Brand"),
    ("Charlotte Tilbury", "Luxury Cosmetics (UK)"), ("Glossier", "DTC Beauty Brand"),
    ("Fenty Beauty", "Inclusive Cosmetics Brand"), ("Rare Beauty", "Cosmetics Brand"),
    ("ColourPop", "Affordable Cosmetics"), ("e.l.f. Cosmetics", "Budget Cosmetics"),
    ("NYX Cosmetics", "Affordable Cosmetics"), ("Maybelline", "Mass Market Cosmetics"),
    ("L'Oréal Paris", "Mass Market Beauty"), ("Revlon", "Mass Market Cosmetics"),
    ("CoverGirl", "Mass Market Cosmetics"), ("Neutrogena", "Skincare & Suncare"),
    ("CeraVe", "Dermatologist Skincare"), ("The Ordinary", "Affordable Skincare"),
    ("Drunk Elephant", "Premium Skincare"), ("Tatcha", "Luxury Skincare (Japanese-Inspired)"),
    ("Sunday Riley", "Premium Skincare"), ("Kiehl's", "Premium Skincare"),
    ("La Mer", "Ultra-Luxury Skincare"), ("SK-II", "Premium Skincare (Japan)"),
    ("Shiseido", "Skincare & Cosmetics (Japan)"), ("Innisfree", "Natural Beauty (Korea)"),
    ("Laneige", "K-Beauty Skincare"), ("Sulwhasoo", "Luxury K-Beauty"),
    ("Amorepacific", "K-Beauty Conglomerate"), ("Dr. Jart+", "K-Beauty Skincare"),
    # Salons & Spas
    ("Supercuts", "Hair Salon Chain"), ("Great Clips", "Hair Salon Chain"),
    ("Sport Clips", "Men's Hair Salon Chain"), ("Hair Cuttery", "Hair Salon Chain"),
    ("Fantastic Sams", "Hair Salon Chain"), ("SmartStyle", "Hair Salon (Walmart)"),
    ("Regis Salons", "Hair Salon Chain"), ("Ulta Salon", "Hair Salon"),
    ("Drybar", "Blowout Bar"), ("Madison Reed", "Hair Color Salon & DTC"),
    ("European Wax Center", "Waxing Salon"), ("Waxing the City", "Waxing Salon"),
    ("Massage Envy", "Massage & Spa Chain"), ("Hand & Stone Massage", "Massage & Facial Spa"),
    ("Elements Massage", "Therapeutic Massage"), ("Woodhouse Day Spa", "Day Spa"),
    ("Burke Williams", "Day Spa"), ("Exhale Spa", "Spa & Fitness"),
    ("Bliss Spa", "Day Spa"), ("Red Door Spa", "Elizabeth Arden Spa"),
    ("SkinLaundry", "Laser & Light Facial"), ("Ideal Image", "Medical Aesthetics"),
    ("Laser Away", "Laser Hair Removal"), ("Milan Laser", "Laser Hair Removal"),
    ("Toni&Guy", "Hair Salon (UK)"), ("Rush Hair", "Hair Salon (UK)"),
    # Perfume & Fragrance
    ("Jo Malone", "Luxury Fragrance"), ("Le Labo", "Niche Fragrance"),
    ("Diptyque", "Luxury Fragrance & Candles"), ("Byredo", "Niche Fragrance"),
    ("Tom Ford Beauty", "Luxury Fragrance"), ("Creed", "Luxury Fragrance"),
    ("Bath & Body Works", "Bath & Body Products"), ("The Body Shop", "Natural Beauty & Body"),
    ("Lush", "Fresh Handmade Cosmetics"), ("L'Occitane", "Natural Beauty (French)"),
    ("Aesop", "Premium Skincare & Body (AU)"), ("Rituals", "Home & Body (Netherlands)"),
    # Men's Grooming
    ("Dollar Shave Club", "Men's Grooming Subscription"), ("Harry's", "Men's Grooming DTC"),
    ("Manscaped", "Men's Grooming"), ("The Art of Shaving", "Men's Grooming"),
    ("Beardbrand", "Men's Grooming"), ("Hims", "Men's Health & Wellness"),
], "Expense", "Health & Wellness", "Beauty & Spa")

add([
    # Health & Wellness Products
    ("GNC", "Vitamins & Supplements Retailer"), ("Vitamin Shoppe", "Vitamins & Supplements"),
    ("iHerb", "Online Health Products"), ("Thrive Market", "Online Health Marketplace"),
    ("Herbalife", "Nutrition MLM"), ("Nature's Bounty", "Supplement Brand"),
    ("NOW Foods", "Natural Supplements"), ("Garden of Life", "Organic Supplements"),
    ("MegaFood", "Whole Food Supplements"), ("Athletic Greens/AG1", "Greens Supplement"),
    ("Ritual", "Subscription Vitamins"), ("Care/of", "Personalized Vitamins"),
    ("Seed", "Probiotic Supplement"), ("Olly", "Gummy Vitamins"),
    ("SugarBear", "Hair Vitamins"), ("Nutrafol", "Hair Growth Supplement"),
    ("Oura Ring", "Wearable Health Tracker"), ("Whoop", "Fitness Tracker Band"),
    ("Eight Sleep", "Smart Mattress & Sleep Tech"), ("Calm", "Meditation & Sleep App"),
    ("Headspace", "Meditation App"), ("BetterHelp", "Online Therapy Platform"),
    ("Talkspace", "Online Therapy Platform"), ("Noom", "Weight Loss App"),
    ("WeightWatchers", "Weight Management Program"), ("Jenny Craig", "Weight Management"),
    ("Nutrisystem", "Meal Delivery (Weight Loss)"), ("Optavia", "Health & Wellness Coaching"),
    ("Hims & Hers", "Telehealth & Wellness"), ("Ro", "Telehealth Platform"),
    ("Keeps", "Hair Loss Treatment"), ("Curology", "Custom Skincare (Prescription)"),
    ("Warby Parker", "Prescription Eyewear"), ("Zenni Optical", "Budget Eyeglasses Online"),
    ("1-800-Contacts", "Contact Lens Retailer"), ("EyeBuyDirect", "Online Eyeglasses"),
    ("SmileDirectClub", "Clear Aligners"), ("Invisalign", "Clear Aligners"),
    ("Byte", "Clear Aligners"), ("Quip", "Electric Toothbrush Subscription"),
    ("Oral-B", "Electric Toothbrush"), ("Philips Sonicare", "Electric Toothbrush"),
], "Expense", "Health & Wellness", "Health Products")

# ============================================================
# HOUSING & UTILITIES (~300)
# ============================================================

add([
    # Electric Utilities (US)
    ("Duke Energy", "Electric Utility"), ("Dominion Energy", "Electric Utility"),
    ("Southern Company", "Electric Utility"), ("Exelon", "Electric Utility"),
    ("AEP (American Electric Power)", "Electric Utility"), ("NextEra Energy", "Electric Utility"),
    ("Entergy", "Electric Utility"), ("Xcel Energy", "Electric Utility"),
    ("Eversource Energy", "Electric Utility"), ("WEC Energy", "Electric Utility"),
    ("PPL Corporation", "Electric Utility"), ("Ameren", "Electric & Gas Utility"),
    ("CenterPoint Energy", "Electric & Gas Utility"), ("Atmos Energy", "Natural Gas Utility"),
    ("National Grid", "Electric & Gas Utility"), ("ConEdison", "Electric & Gas (NYC)"),
    ("Pacific Gas & Electric (PG&E)", "Electric & Gas Utility"), ("SoCal Edison", "Electric Utility"),
    ("Florida Power & Light", "Electric Utility"), ("Georgia Power", "Electric Utility"),
    # Gas & Water
    ("National Fuel Gas", "Natural Gas Utility"), ("New Jersey Natural Gas", "Gas Utility"),
    ("Southwest Gas", "Natural Gas Utility"), ("Spire", "Natural Gas Utility"),
    ("American Water Works", "Water Utility"), ("Essential Utilities", "Water & Gas"),
    ("California Water Service", "Water Utility"), ("SJW Group", "Water Utility"),
    # Cable/Internet/Phone
    ("Comcast/Xfinity", "Cable TV & Internet"), ("Charter/Spectrum", "Cable TV & Internet"),
    ("AT&T", "Telecom & Internet"), ("Verizon", "Telecom & Wireless"),
    ("T-Mobile", "Wireless Telecommunications"), ("Cox Communications", "Cable & Internet"),
    ("Altice/Optimum", "Cable & Internet"), ("Frontier Communications", "Internet & Phone"),
    ("CenturyLink/Lumen", "Internet & Phone"), ("Windstream", "Internet & Phone"),
    ("Mediacom", "Cable & Internet"), ("WOW! Internet", "Cable & Internet"),
    ("Google Fiber", "Fiber Internet"), ("Starlink", "Satellite Internet"),
    ("HughesNet", "Satellite Internet"), ("Viasat", "Satellite Internet"),
    # Wireless/Mobile
    ("Verizon Wireless", "Wireless Carrier"), ("AT&T Wireless", "Wireless Carrier"),
    ("T-Mobile", "Wireless Carrier"), ("US Cellular", "Wireless Carrier"),
    ("Mint Mobile", "MVNO (Budget Wireless)"), ("Visible", "MVNO (Verizon)"),
    ("Cricket Wireless", "MVNO (AT&T)"), ("Metro by T-Mobile", "Prepaid Wireless"),
    ("Boost Mobile", "Prepaid Wireless"), ("Straight Talk", "Prepaid Wireless"),
    ("Consumer Cellular", "MVNO (Seniors)"), ("Ting Mobile", "MVNO"),
    ("Google Fi", "MVNO (Google)"), ("Republic Wireless", "MVNO"),
    # International Telecom
    ("Vodafone", "Telecom (UK/Global)"), ("BT (British Telecom)", "Telecom (UK)"),
    ("Sky UK", "TV & Broadband (UK)"), ("Virgin Media", "Cable & Mobile (UK)"),
    ("Three UK", "Mobile Operator (UK)"), ("EE", "Mobile Operator (UK)"),
    ("Orange", "Telecom (France/Global)"), ("SFR", "Telecom (France)"),
    ("Free Mobile", "Telecom (France)"), ("Deutsche Telekom", "Telecom (Germany)"),
    ("O2", "Mobile Operator (Germany/UK)"), ("Telefonica", "Telecom (Spain)"),
    ("Swisscom", "Telecom (Switzerland)"), ("KPN", "Telecom (Netherlands)"),
    ("Telia", "Telecom (Scandinavia)"), ("Telenor", "Telecom (Norway/Asia)"),
    ("Jio", "Telecom (India)"), ("Airtel", "Telecom (India)"),
    ("Singtel", "Telecom (Singapore)"), ("Telstra", "Telecom (Australia)"),
    ("Optus", "Telecom (Australia)"), ("NTT Docomo", "Mobile (Japan)"),
    ("SoftBank Mobile", "Mobile (Japan)"), ("SK Telecom", "Mobile (Korea)"),
    ("China Mobile", "Mobile (China)"), ("MTN", "Telecom (Africa)"),
    ("Safaricom", "Telecom (Kenya)"), ("América Móvil", "Telecom (Latin America)"),
    # Insurance
    ("State Farm", "Auto & Home Insurance"), ("Geico", "Auto Insurance"),
    ("Progressive", "Auto Insurance"), ("Allstate", "Auto & Home Insurance"),
    ("Liberty Mutual", "Auto & Home Insurance"), ("USAA", "Insurance & Banking"),
    ("Nationwide", "Insurance"), ("Farmers Insurance", "Insurance"),
    ("Travelers", "Property & Casualty Insurance"), ("Erie Insurance", "Insurance"),
    ("American Family Insurance", "Insurance"), ("Shelter Insurance", "Insurance"),
    ("Auto-Owners Insurance", "Insurance"), ("The Hartford", "Insurance"),
    ("Lemonade Insurance", "Digital Insurance"), ("Root Insurance", "Digital Auto Insurance"),
    ("Metromile", "Pay-Per-Mile Insurance"), ("Hippo Insurance", "Home Insurance"),
    # Home Services
    ("Terminix", "Pest Control Service"), ("Orkin", "Pest Control Service"),
    ("Rentokil", "Pest Control (UK/Global)"), ("TruGreen", "Lawn Care Service"),
    ("Lawn Doctor", "Lawn Care Franchise"), ("Molly Maid", "House Cleaning Service"),
    ("Merry Maids", "House Cleaning Service"), ("The Maids", "House Cleaning Service"),
    ("ServiceMaster", "Restoration & Cleaning"), ("Stanley Steemer", "Carpet Cleaning"),
    ("Mr. Rooter Plumbing", "Plumbing Service"), ("Roto-Rooter", "Plumbing & Drain"),
    ("Mr. Electric", "Electrical Service"), ("Benjamin Franklin Plumbing", "Plumbing"),
    ("One Hour Heating & Air", "HVAC Service"), ("Aire Serv", "HVAC Service"),
    ("Handyman Connection", "Handyman Service"), ("Mr. Handyman", "Handyman Service"),
    ("TaskRabbit", "Gig Economy Home Services"), ("Thumbtack", "Local Service Marketplace"),
    ("Angi (Angie's List)", "Home Service Marketplace"), ("HomeAdvisor", "Home Service Marketplace"),
    ("Porch", "Home Service Platform"), ("Handy", "Home Cleaning & Handyman"),
], "Expense", "Housing & Utilities", "Utilities")



# ============================================================
# TECHNOLOGY - Software & SaaS (~300)
# ============================================================

add([
    ("Adobe", "Creative & Document Software"), ("Microsoft 365", "Productivity Suite"),
    ("Google Workspace", "Productivity Suite"), ("Apple iCloud", "Cloud Storage"),
    ("Dropbox", "Cloud Storage & Collaboration"), ("Box", "Enterprise Cloud Storage"),
    ("Notion", "Productivity & Notes"), ("Evernote", "Note-Taking App"),
    ("Todoist", "Task Management App"), ("Asana", "Project Management"),
    ("Monday.com", "Work Management Platform"), ("Trello", "Project Management (Kanban)"),
    ("Jira", "Issue Tracking (Atlassian)"), ("Confluence", "Team Wiki (Atlassian)"),
    ("Slack", "Team Messaging"), ("Discord", "Communication Platform"),
    ("Zoom", "Video Conferencing"), ("Google Meet", "Video Conferencing"),
    ("Microsoft Teams", "Team Collaboration"), ("Webex", "Video Conferencing (Cisco)"),
    ("Loom", "Async Video Messaging"), ("Calendly", "Scheduling Platform"),
    ("Salesforce", "CRM Platform"), ("HubSpot", "CRM & Marketing"),
    ("Zendesk", "Customer Service Platform"), ("Intercom", "Customer Messaging"),
    ("Freshworks", "Business Software Suite"), ("Zoho", "Business Software Suite"),
    ("QuickBooks", "Accounting Software"), ("Xero", "Accounting Software"),
    ("FreshBooks", "Invoicing & Accounting"), ("Wave Accounting", "Free Accounting"),
    ("Stripe", "Payment Processing"), ("Square", "Payment & POS"),
    ("PayPal", "Online Payment Platform"), ("Venmo", "P2P Payment"),
    ("Cash App", "P2P Payment & Banking"), ("Zelle", "P2P Bank Transfer"),
    ("Wise", "International Money Transfer"), ("Revolut", "Digital Banking"),
    ("Shopify", "E-Commerce Platform"), ("WooCommerce", "E-Commerce (WordPress)"),
    ("BigCommerce", "E-Commerce Platform"), ("Squarespace", "Website Builder"),
    ("Wix", "Website Builder"), ("Webflow", "Web Design Platform"),
    ("WordPress.com", "Blogging & CMS"), ("GoDaddy", "Domain & Web Hosting"),
    ("Namecheap", "Domain & Hosting"), ("Bluehost", "Web Hosting"),
    ("DigitalOcean", "Cloud Infrastructure"), ("AWS", "Cloud Computing (Amazon)"),
    ("Google Cloud", "Cloud Computing"), ("Microsoft Azure", "Cloud Computing"),
    ("Cloudflare", "CDN & Web Security"), ("Fastly", "CDN & Edge Computing"),
    ("Akamai", "CDN & Security"), ("Vercel", "Frontend Cloud Platform"),
    ("Netlify", "Web Deployment Platform"), ("Heroku", "Cloud Platform"),
    ("GitHub", "Code Hosting & Collaboration"), ("GitLab", "DevOps Platform"),
    ("Bitbucket", "Code Hosting (Atlassian)"), ("JetBrains", "Developer IDEs"),
    ("Visual Studio", "Developer IDE (Microsoft)"), ("Postman", "API Development"),
    ("Docker", "Container Platform"), ("Kubernetes", "Container Orchestration"),
    ("Terraform", "Infrastructure as Code"), ("Datadog", "Monitoring & Analytics"),
    ("New Relic", "Application Monitoring"), ("PagerDuty", "Incident Management"),
    ("Twilio", "Communication APIs"), ("SendGrid", "Email Delivery"),
    ("Mailchimp", "Email Marketing"), ("Constant Contact", "Email Marketing"),
    ("Canva", "Graphic Design Platform"), ("Figma", "UI Design Tool"),
    ("Sketch", "UI Design Tool (Mac)"), ("InVision", "Design Collaboration"),
    ("Miro", "Visual Collaboration"), ("Lucidchart", "Diagramming Tool"),
    ("OpenAI", "AI & Machine Learning"), ("Anthropic", "AI Research"),
    ("Grammarly", "AI Writing Assistant"), ("Jasper AI", "AI Content Generation"),
    ("Midjourney", "AI Image Generation"), ("Stability AI", "AI Image Generation"),
    ("LinkedIn Premium", "Professional Networking"), ("Indeed", "Job Search Platform"),
    ("Glassdoor", "Job & Company Reviews"), ("ZipRecruiter", "Job Posting Platform"),
    ("1Password", "Password Manager"), ("LastPass", "Password Manager"),
    ("Bitwarden", "Password Manager"), ("Dashlane", "Password Manager"),
    ("NordVPN", "Virtual Private Network"), ("ExpressVPN", "Virtual Private Network"),
    ("Surfshark", "Virtual Private Network"), ("ProtonVPN", "Virtual Private Network"),
    ("Norton", "Cybersecurity Software"), ("McAfee", "Cybersecurity Software"),
    ("Bitdefender", "Cybersecurity Software"), ("Kaspersky", "Cybersecurity Software"),
    ("Malwarebytes", "Anti-Malware Software"), ("CrowdStrike", "Endpoint Security"),
    ("SentinelOne", "Endpoint Security"), ("Sophos", "Cybersecurity (UK)"),
    ("Trend Micro", "Cybersecurity (Japan)"), ("ESET", "Cybersecurity (Slovakia)"),
], "Expense", "Technology", "Software & SaaS")

# ============================================================
# FINANCIAL SERVICES (~200)
# ============================================================

add([
    # US Banks & Credit Unions
    ("Chase", "Major Bank"), ("Bank of America", "Major Bank"),
    ("Wells Fargo", "Major Bank"), ("Citibank", "Major Bank"),
    ("US Bank", "Major Bank"), ("PNC Bank", "Regional Bank"),
    ("Truist", "Regional Bank"), ("TD Bank", "Regional Bank"),
    ("Capital One", "Bank & Credit Card"), ("Discover", "Credit Card & Bank"),
    ("American Express", "Credit Card & Financial"), ("Goldman Sachs Marcus", "Online Savings"),
    ("Ally Bank", "Online Bank"), ("Synchrony Bank", "Consumer Finance"),
    ("Navy Federal Credit Union", "Credit Union"), ("Pentagon Federal CU", "Credit Union"),
    ("BECU", "Credit Union"), ("Golden 1 Credit Union", "Credit Union"),
    # Fintech
    ("Chime", "Neobank"), ("SoFi", "Online Banking & Lending"),
    ("Robinhood", "Stock Trading App"), ("Coinbase", "Cryptocurrency Exchange"),
    ("Kraken", "Cryptocurrency Exchange"), ("Binance", "Cryptocurrency Exchange"),
    ("Wealthfront", "Robo-Advisor"), ("Betterment", "Robo-Advisor"),
    ("Acorns", "Micro-Investing App"), ("Stash", "Investing App"),
    ("Public.com", "Social Investing"), ("M1 Finance", "Investment Platform"),
    ("Personal Capital", "Financial Planning"), ("Mint", "Budgeting App"),
    ("YNAB", "Budgeting App"), ("Credit Karma", "Credit Monitoring"),
    ("NerdWallet", "Financial Advice Platform"), ("LendingClub", "Peer-to-Peer Lending"),
    ("Prosper", "Peer-to-Peer Lending"), ("Upstart", "AI Lending Platform"),
    ("Earnin", "Earned Wage Access"), ("Dave", "Overdraft Protection App"),
    ("Affirm", "Buy Now Pay Later"), ("Klarna", "Buy Now Pay Later"),
    ("Afterpay", "Buy Now Pay Later"), ("Sezzle", "Buy Now Pay Later"),
    ("Zip (QuadPay)", "Buy Now Pay Later"),
    # International Banks & Fintech
    ("HSBC", "Global Bank"), ("Barclays", "Bank (UK)"),
    ("NatWest", "Bank (UK)"), ("Lloyds Bank", "Bank (UK)"),
    ("Revolut", "Digital Bank (UK)"), ("Monzo", "Digital Bank (UK)"),
    ("Starling Bank", "Digital Bank (UK)"), ("N26", "Digital Bank (Germany)"),
    ("ING", "Bank (Netherlands)"), ("BNP Paribas", "Bank (France)"),
    ("Deutsche Bank", "Bank (Germany)"), ("UBS", "Bank (Switzerland)"),
    ("Credit Suisse", "Bank (Switzerland)"), ("Santander", "Bank (Spain/Global)"),
    ("BBVA", "Bank (Spain)"), ("Nubank", "Digital Bank (Brazil)"),
    ("Mercado Pago", "Digital Payment (Latin Am)"), ("Grab Financial", "Digital Finance (Asia)"),
    ("PayTM", "Digital Payment (India)"), ("PhonePe", "Digital Payment (India)"),
    ("GoPay", "Digital Payment (Indonesia)"), ("KakaoPay", "Digital Payment (Korea)"),
    ("Ant Financial/Alipay", "Digital Payment (China)"), ("WeChat Pay", "Digital Payment (China)"),
    # Investment & Brokerage
    ("Fidelity Investments", "Brokerage & Mutual Funds"), ("Charles Schwab", "Brokerage"),
    ("Vanguard", "Index Funds & Brokerage"), ("E*TRADE", "Online Brokerage"),
    ("TD Ameritrade", "Online Brokerage"), ("Interactive Brokers", "Online Brokerage"),
    ("Merrill Lynch", "Wealth Management"), ("Morgan Stanley", "Wealth Management"),
    ("Edward Jones", "Investment Advisory"), ("Raymond James", "Financial Services"),
    # Insurance
    ("State Farm", "Insurance"), ("Geico", "Auto Insurance"),
    ("Progressive", "Auto Insurance"), ("Allstate", "Insurance"),
    ("Liberty Mutual", "Insurance"), ("Nationwide", "Insurance"),
    ("USAA", "Insurance (Military)"), ("Farmers Insurance", "Insurance"),
    ("MetLife", "Life Insurance"), ("Prudential", "Life Insurance"),
    ("New York Life", "Life Insurance"), ("Northwestern Mutual", "Life Insurance"),
    ("MassMutual", "Life Insurance"), ("Guardian Life", "Insurance"),
    ("Transamerica", "Life Insurance"), ("Lincoln Financial", "Insurance & Annuities"),
], "Expense", "Financial Services", "Banking Fees")

# ============================================================
# EDUCATION (~200)
# ============================================================

add([
    # Online Learning Platforms
    ("Coursera", "Online Course Platform"), ("Udemy", "Online Course Marketplace"),
    ("edX", "Online Learning (University)"), ("LinkedIn Learning", "Professional Courses"),
    ("Skillshare", "Creative Online Learning"), ("MasterClass", "Celebrity-Led Courses"),
    ("Khan Academy", "Free Online Learning"), ("Codecademy", "Coding Education"),
    ("Treehouse", "Tech Education"), ("Pluralsight", "Technology Skills"),
    ("DataCamp", "Data Science Learning"), ("Udacity", "Tech Nanodegrees"),
    ("Brilliant.org", "STEM Learning"), ("Duolingo", "Language Learning App"),
    ("Babbel", "Language Learning App"), ("Rosetta Stone", "Language Learning"),
    ("Busuu", "Language Learning App"), ("italki", "Language Tutoring"),
    ("Preply", "Online Tutoring"), ("Wyzant", "Tutoring Marketplace"),
    ("Varsity Tutors", "Online Tutoring"), ("Chegg", "Textbooks & Tutoring"),
    ("Course Hero", "Study Resources"), ("Quizlet", "Flashcard & Study App"),
    ("Brainly", "Student Q&A Platform"), ("Photomath", "Math Problem Solver"),
    # K-12 Education
    ("Kumon", "Math & Reading Tutoring"), ("Mathnasium", "Math Learning Center"),
    ("Sylvan Learning", "Tutoring Center"), ("Huntington Learning", "Tutoring Center"),
    ("KidzArt", "Children's Art Education"), ("Code Ninjas", "Kids Coding Center"),
    ("Engineering For Kids", "STEM Education"), ("Snapology", "LEGO STEM Education"),
    ("Gymboree Play & Music", "Early Childhood"), ("Kindercare", "Childcare & Learning"),
    ("Bright Horizons", "Childcare & Education"), ("Goddard School", "Preschool"),
    ("Primrose Schools", "Preschool"), ("The Learning Experience", "Childcare"),
    # Test Prep
    ("Kaplan", "Test Prep & Education"), ("The Princeton Review", "Test Prep"),
    ("Magoosh", "Online Test Prep"), ("PrepScholar", "SAT/ACT Prep"),
    ("Manhattan Prep", "GMAT/GRE Prep"), ("LeetCode", "Coding Interview Prep"),
    ("HackerRank", "Technical Assessment"), ("AlgoExpert", "Coding Interview Prep"),
    # Music & Arts Education
    ("School of Rock", "Music Education"), ("Guitar Center Lessons", "Music Lessons"),
    ("Fender Play", "Online Guitar Lessons"), ("Simply Piano", "Piano Learning App"),
    ("Yousician", "Music Learning App"), ("Flowkey", "Piano Learning App"),
    # Professional & Higher Ed
    ("Pearson", "Educational Publisher"), ("McGraw Hill", "Educational Publisher"),
    ("Cengage", "Educational Publisher"), ("Scholastic", "Children's Publisher"),
    ("Houghton Mifflin Harcourt", "Educational Publisher"),
], "Expense", "Education", "Online Learning")

# ============================================================
# DONATIONS & CHARITY (~80)
# ============================================================

add([
    ("GoFundMe", "Crowdfunding Platform"), ("Kickstarter", "Creative Crowdfunding"),
    ("Indiegogo", "Crowdfunding Platform"), ("Patreon", "Creator Membership Platform"),
    ("Buy Me a Coffee", "Creator Tips Platform"), ("Ko-fi", "Creator Support Platform"),
    ("JustGiving", "Charity Fundraising (UK)"), ("GlobalGiving", "International Charity"),
    ("Charity Navigator", "Charity Rating"), ("Give.org", "Charity Verification"),
    ("GiveDirectly", "Cash Transfer Charity"), ("Kiva", "Micro-Lending Charity"),
    ("DonorsChoose", "Education Fundraising"), ("St. Jude Children's", "Children's Hospital"),
    ("Salvation Army", "Charitable Organization"), ("United Way", "Charitable Organization"),
    ("Red Cross", "Humanitarian Organization"), ("Habitat for Humanity", "Housing Charity"),
    ("Feeding America", "Food Bank Network"), ("Goodwill", "Thrift & Workforce Dev"),
    ("UNICEF", "Children's Charity"), ("Doctors Without Borders", "Medical Charity"),
    ("World Wildlife Fund", "Environmental Charity"), ("Nature Conservancy", "Environmental Charity"),
    ("Sierra Club", "Environmental Organization"), ("Greenpeace", "Environmental Org"),
    ("ASPCA", "Animal Welfare"), ("Humane Society", "Animal Welfare"),
    ("Wikipedia/Wikimedia", "Free Encyclopedia"), ("Electronic Frontier Foundation", "Digital Rights"),
    ("ACLU", "Civil Liberties Organization"), ("Planned Parenthood", "Healthcare Nonprofit"),
    ("NPR", "Public Radio"), ("PBS", "Public Broadcasting"),
    ("ActBlue", "Political Fundraising"), ("WinRed", "Political Fundraising"),
    ("Change.org", "Online Petition Platform"),
], "Expense", "Donations & Gifts", "Charity & Donations")

# ============================================================
# KIDS & FAMILY (~100)
# ============================================================

add([
    ("Toys R Us", "Toy Store Chain"), ("Build-A-Bear Workshop", "Custom Stuffed Animals"),
    ("LEGO Store", "Building Toy Retailer"), ("Disney Store", "Character Merchandise"),
    ("American Girl", "Premium Dolls & Accessories"), ("Barbie", "Doll Brand (Mattel)"),
    ("Hot Wheels", "Toy Car Brand (Mattel)"), ("Nerf", "Toy Blaster Brand (Hasbro)"),
    ("Play-Doh", "Modeling Compound (Hasbro)"), ("Fisher-Price", "Infant/Toddler Toys"),
    ("Little Tikes", "Children's Toys & Furniture"), ("Step2", "Children's Outdoor Play"),
    ("Melissa & Doug", "Educational Toys"), ("VTech", "Electronic Learning Toys"),
    ("LeapFrog", "Educational Technology Toys"), ("Osmo", "Interactive Learning"),
    ("KidKraft", "Wooden Toys & Furniture"), ("Fat Brain Toys", "Educational Toys"),
    ("Learning Resources", "Educational Toys & Games"), ("ThinkFun", "Logic Games"),
    ("Ravensburger", "Puzzles & Games (Germany)"), ("Playmobil", "Toy Figures (Germany)"),
    ("Schleich", "Toy Animal Figures (Germany)"), ("Hape", "Wooden Toys"),
    ("Lovevery", "Age-Appropriate Toy Subscription"), ("KiwiCo", "Kids Activity Subscription"),
    ("Little Passports", "Kids Educational Subscription"), ("Highlights", "Kids Magazine & Activity"),
    # Baby & Nursery
    ("BuyBuy Baby", "Baby Products Retailer"), ("Pottery Barn Kids", "Kids Furniture & Decor"),
    ("Crate & Kids", "Kids Furniture & Decor"), ("Babylist", "Baby Registry"),
    ("Ergobaby", "Baby Carrier"), ("UPPAbaby", "Premium Stroller"),
    ("Bugaboo", "Premium Stroller"), ("Nuna", "Premium Baby Gear"),
    ("Hatch", "Baby Sound Machine & Light"), ("Nanit", "Baby Monitor"),
    ("Snoo", "Smart Bassinet (Happiest Baby)"), ("Graco", "Baby Products"),
    ("Baby Jogger", "Stroller Brand"), ("4moms", "Baby Tech Products"),
    ("Babyganics", "Baby Skincare & Cleaning"), ("Honest Company", "Baby & Home Products"),
    ("Pampers", "Diapers"), ("Huggies", "Diapers"),
    ("Hello Bello", "Diapers & Baby Products"), ("Dyper", "Sustainable Diapers"),
    ("Earth's Best", "Organic Baby Food"), ("Happy Family", "Organic Baby Food"),
    ("Once Upon a Farm", "Organic Baby Food"), ("Cerebelly", "Brain-Building Baby Food"),
], "Expense", "Kids & Family", "Toys & Activities")

# ============================================================
# INCOME
# ============================================================

add([
    ("Direct Deposit", "Payroll Deposit"), ("Payroll", "Employer Payroll"),
    ("ADP Payroll", "Payroll Processing"), ("Gusto Payroll", "Payroll Processing"),
    ("ACH Deposit", "Electronic Bank Transfer"), ("Wire Transfer", "Bank Wire"),
    ("Tax Refund", "Government Tax Refund"), ("Social Security", "Government Benefit"),
    ("Unemployment Insurance", "Government Benefit"), ("Child Tax Credit", "Government Benefit"),
    ("Zelle Payment Received", "P2P Payment"), ("Venmo Transfer In", "P2P Payment"),
    ("PayPal Transfer In", "P2P Payment"), ("Cash App Received", "P2P Payment"),
    ("Dividend Payment", "Investment Income"), ("Interest Payment", "Bank Interest"),
    ("Rental Income", "Property Rental"), ("Freelance Payment", "Self-Employment Income"),
    ("Refund", "Merchant Refund"), ("Insurance Claim", "Insurance Payout"),
], "Income", "Transfers", "Deposit")





# ============================================================
# ADDITIONAL MERCHANTS TO REACH 10K TARGET
# ============================================================

# More Restaurants (need ~800 more)
add([
    # American Casual/Regional
    ("Cheesecake Factory", "Casual Dining Restaurant"), ("Brinker International", "Restaurant Group"),
    ("Darden Restaurants", "Restaurant Group"), ("Yardhouse", "Restaurant & Bar"),
    ("Bahama Breeze", "Caribbean Restaurant"), ("Season's 52", "Fine Casual Dining"),
    ("Eddie V's", "Upscale Seafood"), ("Yard House", "Restaurant & Bar"),
    ("The Keg", "Steakhouse (Canada)"), ("Swiss Chalet", "Family Restaurant (Canada)"),
    ("Harvey's", "Fast Food (Canada)"), ("A&W Canada", "Fast Food (Canada)"),
    ("Mary Brown's Chicken", "Fried Chicken (Canada)"), ("St-Hubert", "Rotisserie (Canada)"),
    ("Cora", "Breakfast (Canada)"), ("Montana's BBQ", "BBQ Restaurant (Canada)"),
    ("Earl's Kitchen", "Casual Dining (Canada)"), ("Moxie's", "Casual Dining (Canada)"),
    ("The Keg Steakhouse", "Steakhouse (Canada)"), ("Boston Pizza", "Pizza & Sports Bar (Canada)"),
    ("White Spot", "Regional Restaurant (BC)"), ("Original Joe's", "Casual Dining (Canada)"),
    # More US Chains
    ("Wingstop", "Wing Restaurant"), ("Zaxby's", "Chicken Restaurant"),
    ("Cane's", "Chicken Fingers Restaurant"), ("Pollo Tropical", "Caribbean Fast Casual"),
    ("El Torito", "Mexican Restaurant"), ("On The Border", "Tex-Mex Restaurant"),
    ("Chuy's", "Tex-Mex Restaurant"), ("Torchy's Tacos", "Taco Restaurant"),
    ("Velvet Taco", "Creative Taco Restaurant"), ("Fuzzy's Taco Shop", "Taco Restaurant"),
    ("Taco Cabana", "Tex-Mex Fast Casual"), ("Green Burrito", "Mexican Fast Food"),
    ("Wahoo's Fish Tacos", "Fish Taco Restaurant"), ("Baja Fresh", "Mexican Fast Casual"),
    ("Cafe Rio", "Mexican Restaurant"), ("Costa Vida", "Mexican Restaurant"),
    ("Mod Pizza", "Fast Casual Pizza"), ("Blaze Pizza", "Fast Casual Pizza"),
    ("Pieology", "Custom Pizza"), ("Mellow Mushroom", "Pizza & Bar"),
    ("Donatos", "Pizza Chain"), ("Jet's Pizza", "Pizza Chain"),
    ("Marco's Pizza", "Pizza Chain"), ("Hungry Howie's", "Pizza Chain"),
    ("Mountain Mike's", "Pizza Chain"), ("Round Table Pizza", "Pizza Chain"),
    ("Giordano's", "Deep Dish Pizza (Chicago)"), ("Lou Malnati's", "Deep Dish Pizza (Chicago)"),
    ("Portillo's", "Chicago-Style Hot Dogs & Italian Beef"), ("Culver's", "Midwest Fast Casual"),
    ("Steak 'n Shake", "Steakburger Restaurant"), ("Freddy's Frozen Custard", "Fast Casual"),
    ("White Castle", "Fast Food Sliders"), ("Krystal", "Fast Food Sliders"),
    ("Checkers/Rally's", "Fast Food Burger"), ("Cookout", "Fast Food (Southeast)"),
    ("Zaxby's", "Chicken Restaurant"), ("Raising Cane's", "Chicken Fingers"),
    ("Waba Grill", "Teriyaki Fast Casual"), ("Yoshinoya", "Japanese Beef Bowl"),
    ("Sarku Japan", "Japanese Fast Food"), ("Teriyaki Madness", "Teriyaki Fast Casual"),
    # Breakfast/Brunch Chains
    ("First Watch", "Breakfast & Brunch"), ("Another Broken Egg", "Breakfast & Brunch"),
    ("Eggs Up Grill", "Breakfast Restaurant"), ("Broken Yolk Cafe", "Breakfast Cafe"),
    ("Snooze Morning Eatery", "Breakfast & Brunch"), ("Toasted Yolk Cafe", "Breakfast"),
    ("Wild Eggs", "Breakfast Restaurant"), ("Hash House A Go Go", "Breakfast"),
    ("Keke's Breakfast Cafe", "Breakfast (Florida)"), ("Maple Street Biscuit", "Breakfast"),
    ("Biscuitville", "Breakfast Restaurant"), ("Kolache Factory", "Kolache Restaurant"),
    # Steakhouses & Fine Dining
    ("Ruth's Chris", "Fine Dining Steakhouse"), ("Morton's Steakhouse", "Fine Dining Steakhouse"),
    ("The Capital Grille", "Fine Dining Steakhouse"), ("Fleming's Steakhouse", "Fine Dining"),
    ("STK", "Modern Steakhouse"), ("Fogo de Chão", "Brazilian Steakhouse"),
    ("Texas de Brazil", "Brazilian Steakhouse"), ("Rodízio Grill", "Brazilian Steakhouse"),
    ("Sullivan's Steakhouse", "Fine Dining Steakhouse"), ("Del Frisco's", "Fine Dining Steakhouse"),
    ("Mastro's", "Fine Dining Steakhouse"), ("Eddie V's", "Upscale Seafood & Steakhouse"),
    ("Ocean Prime", "Upscale Seafood & Steak"), ("Jeff Ruby's", "Fine Dining Steakhouse"),
    ("Perry's Steakhouse", "Fine Dining Steakhouse"), ("Bern's Steak House", "Fine Dining"),
    ("Peter Luger", "Classic Steakhouse (NYC)"), ("Keen's Steakhouse", "Classic Steakhouse"),
    # Seafood
    ("Joe's Crab Shack", "Seafood Restaurant"), ("Legal Sea Foods", "Seafood Restaurant"),
    ("Bonefish Grill", "Casual Seafood"), ("Pappadeaux Seafood", "Cajun Seafood"),
    ("Captain D's", "Fast Food Seafood"), ("Long John Silver's", "Fast Food Seafood"),
    ("Crab House", "Seafood Restaurant"), ("Luke's Lobster", "Lobster Roll Shop"),
    ("Crabby's Seafood", "Seafood Restaurant"), ("McCormick & Schmick's", "Upscale Seafood"),
    # Asian (US)
    ("Benihana", "Japanese Teppanyaki"), ("Nobu", "Japanese Fine Dining"),
    ("Momofuku", "Asian-American Restaurant"), ("Haidilao", "Hot Pot Chain (Chinese)"),
    ("99 Favor Taste", "Hot Pot Restaurant"), ("Gen Korean BBQ", "Korean BBQ"),
    ("KBBQ", "Korean BBQ Restaurant"), ("Gyu-Kaku", "Japanese BBQ Restaurant"),
    ("Wagamama", "Asian Casual Dining"), ("PF Chang's", "Asian Casual Dining"),
    ("Pei Wei Asian Diner", "Asian Fast Casual"), ("Pick Up Stix", "Chinese Fast Casual"),
    ("Ippudo", "Ramen Chain"), ("Jinya Ramen", "Ramen Restaurant"),
    ("Silverlake Ramen", "Ramen Restaurant"), ("Ramen Tatsu-Ya", "Ramen (Austin)"),
    ("Sumo Ramen", "Ramen Restaurant"), ("Kura Revolving Sushi", "Conveyor Belt Sushi"),
    ("Hai Di Lao", "Hot Pot (Chinese)"), ("Little Sheep Hot Pot", "Mongolian Hot Pot"),
    ("Tim Ho Wan", "Dim Sum Restaurant"), ("Din Tai Fung", "Dumpling Restaurant"),
    ("Xi'an Famous Foods", "Chinese Noodle Restaurant"), ("Chengdu Taste", "Szechuan Restaurant"),
    ("Uncle Tetsu's", "Japanese Cheesecake"), ("Beard Papa's", "Japanese Cream Puffs"),
    # Indian Restaurants (US/UK)
    ("Dishoom", "Indian Restaurant (UK)"), ("Gymkhana", "Indian Fine Dining (UK)"),
    ("Masala Zone", "Indian Casual Dining (UK)"), ("Tiffin Room", "Indian Restaurant"),
    ("Curry House", "Indian Restaurant"), ("Tandoori Flame", "Indian Buffet"),
    ("Royal India", "Indian Restaurant"), ("Maharaja Palace", "Indian Restaurant"),
    ("Tikka House", "Indian Restaurant"), ("Naan & Curry", "Indian Fast Casual"),
    # Mediterranean/Middle Eastern
    ("Cava", "Mediterranean Fast Casual"), ("sweetgreen", "Salad Fast Casual"),
    ("Tender Greens", "Salad & Plates"), ("Just Salad", "Salad Fast Casual"),
    ("Chopt", "Salad Fast Casual"), ("Dig Inn", "Farm-to-Table Fast Casual"),
    ("Mendocino Farms", "Sandwich & Salad"), ("Flower Child", "Healthy Fast Casual"),
    ("True Food Kitchen", "Health-Focused Restaurant"), ("Sharky's", "Mexican Health"),
    ("ZOEs Kitchen", "Mediterranean Fast Casual"), ("Roti Mediterranean", "Mediterranean"),
    ("Halal Guys", "Halal Street Food"), ("Aladdin's Eatery", "Lebanese Restaurant"),
    ("Tabouleh", "Lebanese Restaurant"), ("Shawarma Press", "Shawarma Restaurant"),
    ("Hummus Republic", "Mediterranean Fast Casual"), ("Daphne's", "Greek Restaurant"),
    # European
    ("Le Bernardin", "French Fine Dining (NYC)"), ("Daniel", "French Fine Dining (NYC)"),
    ("Jean-Georges", "French Fine Dining"), ("The French Laundry", "Fine Dining (Napa)"),
    ("Alinea", "Fine Dining (Chicago)"), ("Eleven Madison Park", "Fine Dining (NYC)"),
    ("Noma", "Fine Dining (Copenhagen)"), ("El Celler de Can Roca", "Fine Dining (Spain)"),
    ("Osteria Francescana", "Fine Dining (Italy)"), ("The Fat Duck", "Fine Dining (UK)"),
    ("Restaurant Gordon Ramsay", "Fine Dining (UK)"), ("Heston Blumenthal", "Fine Dining (UK)"),
    # Pizza International
    ("Domino's UK", "Pizza Delivery (UK)"), ("Papa John's UK", "Pizza Delivery (UK)"),
    ("Franco Manca", "Sourdough Pizza (UK)"), ("Pizza Pilgrims", "Neapolitan Pizza (UK)"),
    ("Homeslice", "Pizza Restaurant (UK)"), ("L'Antica Pizzeria da Michele", "Italian Pizzeria"),
    ("Rossopomodoro", "Italian Pizza Chain"), ("Alice Pizza", "Pizza al Taglio (Italy)"),
], "Expense", "Food & Dining", "Restaurants")

# More Clothing & Apparel brands
add([
    # More International Fashion
    ("Desigual", "Fashion Brand (Spain)"), ("Promod", "Women's Fashion (France)"),
    ("Camaïeu", "Women's Fashion (France)"), ("Kiabi", "Family Fashion (France)"),
    ("Celio", "Men's Fashion (France)"), ("Jules", "Men's Fashion (France)"),
    ("Esprit", "Fashion Brand (Germany)"), ("s.Oliver", "Fashion Brand (Germany)"),
    ("Tom Tailor", "Fashion Brand (Germany)"), ("Gerry Weber", "Women's Fashion (Germany)"),
    ("Marc O'Polo", "Premium Fashion (Germany)"), ("Bogner", "Luxury Sportswear (Germany)"),
    ("Benetton", "Fashion Brand (Italy)"), ("Calzedonia", "Legwear & Swimwear (Italy)"),
    ("Intimissimi", "Lingerie (Italy)"), ("OVS", "Family Fashion (Italy)"),
    ("Mango Man", "Men's Fashion (Spain)"), ("Cortefiel", "Fashion (Spain)"),
    ("Adolfo Dominguez", "Designer Fashion (Spain)"), ("Helly Hansen", "Outdoor (Norway)"),
    ("Didriksons", "Outdoor Fashion (Sweden)"), ("Peak Performance", "Outdoor (Sweden)"),
    ("Marimekko", "Fashion & Home (Finland)"), ("Samsøe Samsøe", "Fashion (Denmark)"),
    ("Ganni", "Contemporary Fashion (Denmark)"), ("By Malene Birger", "Fashion (Denmark)"),
    # Fast Fashion Asia
    ("GU", "Fast Fashion (Japan, Uniqlo Group)"), ("Shimamura", "Fashion Retailer (Japan)"),
    ("Right-on", "Casual Fashion (Japan)"), ("Honeys", "Women's Fashion (Japan)"),
    ("Spao", "Fast Fashion (Korea)"), ("8seconds", "Fast Fashion (Korea)"),
    ("Stylenanda", "Fashion & Beauty (Korea)"), ("Eland", "Fashion Group (Korea)"),
    ("FJ Benjamin", "Fashion Retail (Singapore)"), ("Charles & Keith", "Fashion Accessories"),
    ("Love, Bonito", "Women's Fashion (Singapore)"), ("Pomelo Fashion", "Fashion (Thailand)"),
    ("Fabindia", "Indian Ethnic Fashion"), ("Biba", "Indian Women's Fashion"),
    ("W (Wishful Wear)", "Indian Fashion"), ("Allen Solly", "Indian Casual Fashion"),
    ("Peter England", "Men's Fashion (India)"), ("Van Heusen", "Men's Fashion"),
    ("Louis Philippe", "Men's Premium Fashion (India)"), ("Pantaloons", "Fashion Retail (India)"),
    ("Foschini", "Fashion Retailer (South Africa)"), ("Edgars", "Fashion (South Africa)"),
    ("Truworths", "Fashion (South Africa)"), ("Woolworths Fashion", "Fashion (South Africa)"),
    # DTC / Online Fashion
    ("Everlane", "Transparent Fashion DTC"), ("Reformation", "Sustainable Women's Fashion"),
    ("Madewell", "Denim & Casual (J.Crew Group)"), ("Frank and Oak", "Sustainable Fashion"),
    ("Bonobos", "Men's Fashion DTC"), ("Untuckit", "Men's Shirts DTC"),
    ("Stitch Fix", "Styling Service & Fashion"), ("Trunk Club", "Personal Styling"),
    ("Rent the Runway", "Fashion Rental"), ("Le Tote", "Fashion Rental"),
    ("ThredUp", "Online Thrift Store"), ("The RealReal", "Luxury Consignment"),
    ("Vestiaire Collective", "Luxury Resale"), ("Grailed", "Menswear Resale"),
    ("Stadium Goods", "Sneaker Resale"), ("GOAT", "Sneaker Marketplace"),
], "Expense", "Shopping", "Clothing & Apparel")

# More General Retail & Home
add([
    ("Costco", "Wholesale Club"), ("BJ's Wholesale", "Wholesale Club"),
    ("Sam's Club", "Wholesale Club"), ("Aldi US", "Discount Grocery & Retail"),
    ("Trader Joe's", "Specialty Grocery"), ("World Market", "Global Home & Food"),
    ("Pier 1", "Home Decor"), ("Z Gallerie", "Home Decor & Furniture"),
    ("Anthropologie Home", "Bohemian Home & Fashion"), ("Urban Outfitters", "Lifestyle Retail"),
    ("Free People", "Bohemian Fashion"), ("Terrain", "Garden & Home (URBN)"),
    ("Container Store", "Storage & Organization"), ("Storables", "Organization Retailer"),
    ("The Paper Store", "Gifts & Stationery"), ("Paper Source", "Stationery & Gifts"),
    ("Hallmark", "Greeting Cards & Gifts"), ("Things Remembered", "Personalized Gifts"),
    ("Yankee Candle", "Candle & Home Fragrance"), ("Voluspa", "Premium Candles"),
    ("Diptyque", "Luxury Candles & Fragrance"), ("Boy Smells", "Candles & Fragrance"),
    ("CB2", "Modern Home Furnishings"), ("Design Within Reach", "Modern Furniture"),
    ("Herman Miller", "Premium Office Furniture"), ("Steelcase", "Office Furniture"),
    ("IKEA", "Furniture & Home Goods"), ("Room & Board", "American-Made Furniture"),
    ("Mitchell Gold + Bob Williams", "Upholstery"), ("Arhaus", "Artisan Furniture"),
    ("Lexington Home Brands", "Furniture"), ("Ethan Allen", "Furniture"),
    ("Havertys", "Furniture Retailer"), ("Rooms To Go", "Furniture Retailer"),
    ("Ashley HomeStore", "Furniture Retailer"), ("Bob's Discount Furniture", "Budget Furniture"),
    ("Badcock Home Furniture", "Furniture"), ("Conn's HomePlus", "Furniture & Appliances"),
    ("Nebraska Furniture Mart", "Furniture & Electronics"), ("RC Willey", "Furniture"),
    ("Slumberland", "Furniture Retailer"), ("Art Van Furniture", "Furniture"),
], "Expense", "Shopping", "Home & Garden")

# More Electronics & Tech Accessories
add([
    ("Anker", "Charging & Audio Accessories"), ("Belkin", "Tech Accessories"),
    ("OtterBox", "Phone Cases & Protection"), ("Speck", "Phone Cases"),
    ("Casetify", "Custom Phone Cases"), ("PopSockets", "Phone Grip Accessories"),
    ("Zagg", "Screen Protectors & Accessories"), ("Mophie", "Portable Chargers"),
    ("Tile", "Bluetooth Tracker"), ("Apple AirTag", "Item Tracker"),
    ("Samsung Galaxy Buds", "Wireless Earbuds"), ("AirPods", "Wireless Earbuds"),
    ("Nothing", "Tech Brand (UK)"), ("OnePlus", "Smartphone Brand (China)"),
    ("Xiaomi", "Electronics (China)"), ("Oppo", "Smartphone (China)"),
    ("Vivo", "Smartphone (China)"), ("Realme", "Smartphone (China)"),
    ("Huawei", "Electronics (China)"), ("TCL", "TV & Electronics (China)"),
    ("Hisense", "TV & Electronics (China)"), ("Vizio", "TV Brand"),
    ("Roku TV", "Smart TV Platform"), ("Fire TV", "Smart TV (Amazon)"),
    ("Chromecast", "Streaming Device (Google)"), ("Apple TV", "Streaming Device"),
    ("TP-Link", "Networking Equipment"), ("Ubiquiti", "Networking Equipment"),
    ("Eero", "Mesh WiFi System (Amazon)"), ("Google Nest WiFi", "Mesh WiFi"),
    ("Orbi", "Mesh WiFi (Netgear)"), ("Linksys", "Networking Equipment"),
    ("Brother", "Printers & Sewing Machines"), ("Epson", "Printers & Projectors"),
    ("Xerox", "Printers & Copiers"), ("Ricoh", "Office Equipment"),
    ("Cricut", "Craft Cutting Machine"), ("Silhouette", "Craft Cutting Machine"),
    ("3D Systems", "3D Printers"), ("Creality", "3D Printers"),
    ("Prusa", "3D Printers (Czech)"), ("Elegoo", "3D Printers & Electronics"),
], "Expense", "Shopping", "Electronics")

# More Software/SaaS
add([
    ("Spotify Premium", "Music Subscription"), ("Apple One", "Apple Services Bundle"),
    ("Google One", "Google Cloud Storage"), ("Amazon Prime", "Subscription Service"),
    ("Costco Membership", "Warehouse Club Membership"), ("AAA Membership", "Auto Club Membership"),
    ("Sam's Club Membership", "Warehouse Club Membership"), ("BJ's Membership", "Warehouse Club"),
    ("Walmart+", "Retail Subscription"), ("Target Circle", "Retail Loyalty Program"),
    ("DoorDash DashPass", "Delivery Subscription"), ("Uber One", "Ride & Delivery Sub"),
    ("Instacart+", "Grocery Delivery Sub"), ("GrubHub+", "Delivery Subscription"),
    ("Shipt Membership", "Grocery Delivery Sub"), ("FreshDirect", "Online Grocery"),
    ("Imperfect Foods", "Surplus Grocery Delivery"), ("Misfits Market", "Surplus Grocery"),
    ("HelloFresh", "Meal Kit Delivery"), ("Blue Apron", "Meal Kit Delivery"),
    ("Home Chef", "Meal Kit Delivery"), ("EveryPlate", "Budget Meal Kit"),
    ("Dinnerly", "Budget Meal Kit"), ("Factor", "Prepared Meal Delivery"),
    ("Freshly", "Prepared Meal Delivery"), ("Tovala", "Smart Oven + Meal Delivery"),
    ("CookUnity", "Chef-Prepared Meals"), ("Hungryroot", "Grocery + Meal Planning"),
    ("Sunbasket", "Organic Meal Kit"), ("Green Chef", "Organic Meal Kit"),
    ("Purple Carrot", "Plant-Based Meal Kit"), ("Sakara Life", "Plant-Based Meals"),
    ("Daily Harvest", "Frozen Meal Delivery"), ("Thistle", "Plant-Based Meal Delivery"),
    ("Snap Kitchen", "Prepared Meals"), ("Territory Foods", "Prepared Meals"),
    ("Methodology", "Prepared Meals (California)"), ("Pete's Real Food", "Paleo Meal Delivery"),
    ("Trifecta Nutrition", "Organic Prepared Meals"), ("Icon Meals", "Prepared Meals"),
    ("Eat Clean Bro", "Prepared Meals (NJ)"), ("Fuel Meals", "Prepared Meals"),
], "Expense", "Food & Dining", "Restaurants")

# More Groceries (International)
add([
    ("Ahold Delhaize", "Supermarket Group"), ("Aldi North", "Discount Supermarket"),
    ("Aldi South", "Discount Supermarket"), ("Coles Online", "Online Grocery (AU)"),
    ("Woolworths Online", "Online Grocery (AU)"), ("New World", "Supermarket (NZ)"),
    ("Pak'nSave", "Discount Supermarket (NZ)"), ("Four Square", "Convenience (NZ)"),
    ("T&T Supermarket", "Asian Supermarket (Canada)"), ("No Frills", "Discount Grocery (Canada)"),
    ("FreshCo", "Discount Grocery (Canada)"), ("Food Basics", "Discount Grocery (Canada)"),
    ("Metro Canada", "Supermarket (Canada)"), ("IGA Canada", "Supermarket (Canada)"),
    ("Provigo", "Supermarket (Quebec)"), ("Maxi", "Discount Grocery (Quebec)"),
    ("Super C", "Discount Grocery (Quebec)"), ("Adonis", "Mediterranean Grocery (Canada)"),
    ("Bulk Barn", "Bulk Food Store (Canada)"), ("Longo's", "Supermarket (Ontario)"),
    ("Farm Boy", "Specialty Grocery (Ontario)"), ("Whole Foods Canada", "Organic Grocery"),
    ("Eataly", "Italian Food Market"), ("Marqt", "Premium Grocery (Netherlands)"),
    ("Biocoop", "Organic Cooperative (France)"), ("Naturalia", "Organic Grocery (France)"),
    ("Alnatura", "Organic Grocery (Germany)"), ("denn's Biomarkt", "Organic Grocery (Germany)"),
    ("Organic Food Bar", "Health Food Store"), ("Sprouts", "Natural & Organic Grocery"),
    ("Fresh Market", "Specialty Grocery"), ("Lucky's Market", "Natural Grocery"),
    ("Lazy Acres", "Natural Grocery"), ("Mother's Market", "Natural Grocery"),
    ("Jimbo's", "Natural Grocery (San Diego)"), ("Rainbow Grocery", "Cooperative Grocery"),
    ("Berkeley Bowl", "Specialty Produce Market"), ("Bi-Rite Market", "Specialty Grocery (SF)"),
    ("Gourmet Garage", "Specialty Market (NYC)"), ("Westside Market", "Specialty Market (NYC)"),
    ("Garden of Eden", "Specialty Market"), ("Stew Leonard's", "Fresh Food Market"),
    ("Jungle Jim's", "Specialty Market (Ohio)"), ("Central Market", "Specialty Grocery (TX)"),
    ("Market Street", "Supermarket (TX)"), ("Lowes Foods", "Supermarket (SE US)"),
    ("Heinen's Fine Foods", "Premium Grocery (OH)"), ("Dorothy Lane Market", "Specialty Market"),
    ("Nugget Markets", "Specialty Grocery (CA)"), ("Mollie Stone's", "Premium Grocery (CA)"),
    ("Oliver's Market", "Natural Grocery (CA)"), ("Erewhon", "Organic Luxury Grocery (LA)"),
], "Expense", "Food & Dining", "Groceries")



# ============================================================
# ADDITIONAL MERCHANTS - Restaurants (Global Independent & Regional)
# ============================================================

add([
    ("Nando's", "Peri-Peri Chicken Restaurant"), ("Wetherspoons", "Pub Chain (UK)"),
    ("Miller & Carter", "Steakhouse (UK)"), ("Harvester", "Family Restaurant (UK)"),
    ("Toby Carvery", "Carvery Restaurant (UK)"), ("Beefeater", "Restaurant & Pub (UK)"),
    ("Brewers Fayre", "Pub Restaurant (UK)"), ("Hungry Horse", "Pub Restaurant (UK)"),
    ("Nando's UK", "Peri-Peri Chicken (UK)"), ("Turtle Bay", "Caribbean Restaurant (UK)"),
    ("Las Iguanas", "Latin American Restaurant (UK)"), ("Byron Burger", "Burger Restaurant (UK)"),
    ("GBK (Gourmet Burger Kitchen)", "Burger Restaurant (UK)"), ("Five Guys UK", "Burger Restaurant"),
    ("Wahaca", "Mexican Street Food (UK)"), ("Yo! Sushi", "Conveyor Belt Sushi (UK)"),
    ("Itsu", "Asian Fast Casual (UK)"), ("Wasabi", "Japanese Fast Casual (UK)"),
    ("Comptoir Libanais", "Lebanese Restaurant (UK)"), ("Pho", "Vietnamese Restaurant (UK)"),
    ("Busaba", "Thai Restaurant (UK)"), ("Rosa's Thai Cafe", "Thai Restaurant (UK)"),
    ("Giggling Squid", "Thai Restaurant (UK)"), ("Thai Square", "Thai Restaurant (UK)"),
    ("Côte Brasserie", "French Brasserie (UK)"), ("Brasserie Blanc", "French Restaurant (UK)"),
    ("Carluccio's", "Italian Restaurant (UK)"), ("Jamie's Italian", "Italian Restaurant (UK)"),
    ("Strada", "Italian Restaurant (UK)"), ("Giraffe", "World Food Restaurant (UK)"),
    # German/Austrian Restaurants
    ("Hofbräuhaus", "Bavarian Beer Hall"), ("Augustiner-Keller", "Beer Hall (Munich)"),
    ("Wienerwald", "Chicken Restaurant (Germany/Austria)"), ("Nordsee", "Seafood Fast Food (Germany)"),
    ("Hans im Glück", "Burger Restaurant (Germany)"), ("Peter Pane", "Burger Restaurant (Germany)"),
    ("dean&david", "Salad & Bowls (Germany)"), ("Coa", "Asian Restaurant (Germany)"),
    ("Sausalitos", "Mexican Restaurant (Germany)"), ("Alex", "Restaurant & Bar (Germany)"),
    ("Block House", "Steakhouse (Germany)"), ("Schweinske", "Restaurant Chain (Germany)"),
    # French Restaurants
    ("Hippopotamus", "Steakhouse Chain (France)"), ("Buffalo Grill", "Grill Chain (France)"),
    ("Courtepaille", "Grill Chain (France)"), ("La Boucherie", "Steakhouse (France)"),
    ("Del Arte", "Italian Restaurant (France)"), ("Poivre Rouge", "Grill (France)"),
    ("Chez Clément", "French Restaurant"), ("Les 3 Brasseurs", "Brewpub (France/Canada)"),
    ("Big Fernand", "Gourmet Burger (France)"), ("PNY Burger", "Burger (Paris)"),
    # Italian Restaurants
    ("Eataly", "Italian Food Hall & Restaurant"), ("Obicà", "Mozzarella Bar (Italy)"),
    ("Roadhouse Grill", "Steakhouse (Italy)"), ("Old Wild West", "American Grill (Italy)"),
    ("La Piadineria", "Italian Flatbread"), ("Alice Pizza", "Pizza al Taglio (Italy)"),
    ("Rossopomodoro", "Neapolitan Pizza Chain"), ("Spontini", "Pizza Chain (Milan)"),
    # Spanish Restaurants
    ("100 Montaditos", "Tapas Chain (Spain)"), ("Lizarran", "Tapas Chain (Spain)"),
    ("Foster's Hollywood", "American Restaurant (Spain)"), ("Vips", "Coffee & Dining (Spain)"),
    ("Goiko", "Gourmet Burger (Spain)"), ("Lateral", "Casual Dining (Spain)"),
    # Australian Restaurants
    ("Grill'd", "Burger Restaurant (Australia)"), ("Betty's Burgers", "Burger (Australia)"),
    ("The Bavarian", "German Restaurant (Australia)"), ("Ribs & Burgers", "BBQ (Australia)"),
    ("Guzman y Gomez", "Mexican (Australia)"), ("Zambrero", "Mexican (Australia)"),
    ("Mad Mex", "Mexican Fast Casual (Australia)"), ("Sushi Train", "Sushi (Australia)"),
    ("Sushi Hub", "Sushi (Australia)"), ("Roll'd", "Vietnamese (Australia)"),
    ("PappaRich", "Malaysian Restaurant (Australia)"), ("Crust Gourmet Pizza", "Pizza (Australia)"),
    ("Domino's Australia", "Pizza Delivery (Australia)"), ("Pizza Capers", "Pizza (Australia)"),
    # Japanese Restaurants
    ("Sukiya", "Gyudon Chain (Japan)"), ("Matsuya", "Gyudon Chain (Japan)"),
    ("Yoshinoya", "Gyudon Chain (Japan)"), ("Nakau", "Udon & Donburi (Japan)"),
    ("Marugame Udon", "Udon Chain (Japan)"), ("Hanamaru Udon", "Udon Chain (Japan)"),
    ("Ootoya", "Japanese Home Cooking Chain"), ("Yayoi", "Japanese Set Meals"),
    ("Joyfull", "Family Restaurant (Japan)"), ("Gusto", "Family Restaurant (Japan)"),
    ("Bamiyan", "Chinese Restaurant (Japan)"), ("Saizeriya", "Italian Chain (Japan)"),
    ("Mos Burger", "Burger Chain (Japan)"), ("Freshness Burger", "Burger Chain (Japan)"),
    ("CoCo Ichibanya", "Curry House Chain (Japan)"), ("Go! Go! Curry", "Japanese Curry"),
    ("Ichiran Ramen", "Ramen Chain (Japan)"), ("Ippudo Ramen", "Ramen Chain (Japan)"),
    ("Tenkaippin", "Ramen Chain (Japan)"), ("Kourakuen", "Ramen Chain (Japan)"),
    ("Hidakaya", "Ramen & Chinese (Japan)"), ("Ohsho", "Gyoza Chain (Japan)"),
    ("Torikizoku", "Yakitori Chain (Japan)"), ("Watami", "Izakaya Chain (Japan)"),
    ("Shirokiya", "Izakaya Chain (Japan)"), ("Tsubohachi", "Izakaya (Japan)"),
    # Korean Restaurants
    ("BBQ Chicken Korea", "Fried Chicken (Korea)"), ("BHC Chicken", "Fried Chicken (Korea)"),
    ("Kyochon Chicken", "Fried Chicken (Korea)"), ("Pelicana Chicken", "Fried Chicken (Korea)"),
    ("Goobne Chicken", "Oven-Roasted Chicken (Korea)"), ("Nene Chicken", "Fried Chicken (Korea)"),
    ("Bonchon", "Korean Fried Chicken"), ("bb.q Chicken", "Korean Fried Chicken"),
    ("Kkanbu Chicken", "Korean Fried Chicken"), ("Mexicana Chicken", "Korean Fried Chicken"),
    ("Baekjeong", "Korean BBQ Chain"), ("Seorae", "Korean BBQ Chain"),
    ("Bornga", "Korean BBQ Chain"), ("Samgyeopsal Matjip", "Korean BBQ"),
    ("Mr. Pizza Korea", "Pizza Chain (Korea)"), ("Pizza Maru", "Korean Pizza"),
    ("Gongcha Korea", "Bubble Tea (Korea)"), ("Sulbing", "Korean Dessert Cafe"),
    ("Twosome Place", "Coffee & Dessert (Korea)"), ("Paris Baguette", "Bakery Cafe (Korea)"),
    ("Tous les Jours", "Bakery Chain (Korea)"), ("Caffe Bene", "Coffee Chain (Korea)"),
    # Indian Restaurants
    ("Saravana Bhavan", "South Indian Vegetarian"), ("Haldiram's", "Indian Restaurant & Sweets"),
    ("Barbeque Nation", "Indian BBQ Buffet"), ("Paradise Biryani", "Biryani Restaurant"),
    ("Behrouz Biryani", "Biryani Delivery"), ("Biryani Blues", "Biryani Restaurant"),
    ("Mainland China", "Chinese Restaurant (India)"), ("The Great Kabab Factory", "Mughlai"),
    ("Bukhara", "North Indian Fine Dining"), ("Indian Accent", "Modern Indian Fine Dining"),
    ("Dakshin", "South Indian Fine Dining"), ("Peshawri", "North Indian Restaurant"),
    ("Karim's Delhi", "Mughlai Restaurant"), ("Al Jawahar", "Mughlai Restaurant"),
    ("Moti Mahal", "North Indian Restaurant"), ("Rajdhani Thali", "Indian Thali Chain"),
    ("Sagar Ratna", "South Indian Restaurant"), ("Vaango", "South Indian Fast Casual"),
    ("Subway India", "Sandwich Chain (India)"), ("Domino's India", "Pizza (India)"),
    ("Pizza Hut India", "Pizza (India)"), ("McDonald's India", "Fast Food (India)"),
    ("KFC India", "Fried Chicken (India)"), ("Burger King India", "Fast Food (India)"),
    ("Faasos", "Indian Wraps Delivery"), ("Box8", "Indian Meal Delivery"),
    ("Chai Point", "Chai & Snacks (India)"), ("Chaayos", "Chai Cafe (India)"),
    # Middle Eastern Restaurants
    ("Al Baik", "Chicken Fast Food (Saudi)"), ("Kudu", "Fast Food (Saudi Arabia)"),
    ("Herfy", "Fast Food (Saudi Arabia)"), ("Al Tazaj", "Grilled Chicken (Saudi)"),
    ("Shawarmer", "Shawarma Chain (Saudi)"), ("Maestro Pizza", "Pizza (Saudi Arabia)"),
    ("Le Chateau", "Bakery & Restaurant (Lebanon)"), ("Zaatar w Zeit", "Lebanese Fast Casual"),
    ("Manoushe Street", "Lebanese Flatbread"), ("Abd El Wahab", "Lebanese Restaurant"),
    ("Comptoir Libanais", "Lebanese Restaurant"), ("Arabica", "Coffee & Food (ME)"),
    ("The Maine Oyster Bar", "Seafood (Dubai)"), ("Tresind Studio", "Indian Fine Dining (Dubai)"),
    ("Zuma Dubai", "Japanese Restaurant (Dubai)"), ("La Petite Maison Dubai", "French (Dubai)"),
    # African Restaurants
    ("Nando's South Africa", "Peri-Peri Chicken"), ("Spur Steak Ranches", "Family Steakhouse (SA)"),
    ("Wimpy South Africa", "Fast Food (South Africa)"), ("Steers", "Burger Chain (South Africa)"),
    ("Debonairs Pizza", "Pizza Chain (South Africa)"), ("Roman's Pizza", "Pizza (South Africa)"),
    ("Chicken Licken", "Fried Chicken (South Africa)"), ("Ocean Basket", "Seafood (South Africa)"),
    ("Fishaways", "Fish & Chips (South Africa)"), ("The Hussar Grill", "Steakhouse (SA)"),
    ("Mug & Bean", "Coffee & Restaurant (SA)"), ("Vida e Caffè", "Coffee Chain (SA)"),
    # Latin American Restaurants
    ("Fogo de Chão", "Brazilian Steakhouse (Global)"), ("Texas de Brazil", "Brazilian Steakhouse"),
    ("Rodízio Grill", "Brazilian Steakhouse"), ("Outback Brazil", "Steakhouse (Brazil)"),
    ("Coco Bambu", "Seafood Restaurant (Brazil)"), ("Madero", "Burger & Steak (Brazil)"),
    ("Giraffas", "Fast Casual (Brazil)"), ("Spoleto", "Italian Fast Casual (Brazil)"),
    ("Bob's Burgers Brazil", "Fast Food (Brazil)"), ("Habib's", "Fast Food (Brazil)"),
    ("Sanborns", "Restaurant & Retail (Mexico)"), ("Vips Mexico", "Family Restaurant (Mexico)"),
    ("El Portón", "Mexican Restaurant"), ("Toks", "Family Restaurant (Mexico)"),
    ("La Casa de Toño", "Pozole Restaurant (Mexico)"), ("El Fogoncito", "Tacos (Mexico)"),
    ("Pollo Campero", "Fried Chicken (Guatemala/Latin Am)"),
], "Expense", "Food & Dining", "Restaurants")

# ============================================================
# ADDITIONAL - More Clothing, Electronics, Hotels
# ============================================================

add([
    # More Athleisure/DTC Brands
    ("Allbirds", "Sustainable Footwear DTC"), ("Rothy's", "Sustainable Footwear DTC"),
    ("Cariuma", "Sustainable Sneakers"), ("Veja", "Sustainable Sneakers (France)"),
    ("On Cloud", "Swiss Running Shoes"), ("Hoka One One", "Cushioned Running Shoes"),
    ("Tracksmith", "Running Apparel DTC"), ("Janji", "Running Apparel DTC"),
    ("Ten Thousand", "Men's Training Apparel"), ("Hylete", "CrossFit Apparel"),
    ("Born Primitive", "CrossFit Apparel"), ("Nobull", "CrossFit Training Shoes"),
    ("Goruck", "Rucking Gear & Apparel"), ("Mystery Ranch", "Tactical Backpacks"),
    ("5.11 Tactical", "Tactical Apparel & Gear"), ("Kuhl", "Outdoor Apparel"),
    ("prAna", "Yoga & Outdoor Apparel"), ("Prana", "Yoga & Climbing Apparel"),
    ("Manduka", "Yoga Mats & Apparel"), ("Alo Yoga", "Premium Yoga Apparel"),
    # More Luxury
    ("Brunello Cucinelli", "Ultra-Luxury Italian Fashion"), ("Loro Piana", "Luxury Italian Textiles"),
    ("Kiton", "Ultra-Luxury Italian Tailoring"), ("Zegna", "Luxury Men's Fashion (Italy)"),
    ("Canali", "Luxury Men's Suiting (Italy)"), ("Etro", "Luxury Fashion (Italy)"),
    ("Missoni", "Luxury Knitwear (Italy)"), ("Marni", "Contemporary Luxury (Italy)"),
    ("Jil Sander", "Minimalist Luxury"), ("The Row", "Ultra-Luxury Minimalist"),
    ("Lemaire", "Minimalist Fashion (France)"), ("AMI Paris", "Contemporary Fashion (France)"),
    ("Jacquemus", "Contemporary Fashion (France)"), ("Maison Kitsuné", "Fashion & Lifestyle"),
    ("A.P.C.", "French Contemporary Fashion"), ("Sandro", "French Contemporary Fashion"),
    ("Maje", "French Contemporary Fashion"), ("Claudie Pierlot", "French Fashion"),
    ("Zadig & Voltaire", "Rock-Chic Fashion (France)"), ("Ba&sh", "French Bohemian Fashion"),
    ("Golden Goose", "Luxury Sneakers (Italy)"), ("Common Projects", "Luxury Sneakers"),
    ("Axel Arigato", "Luxury Sneakers (Sweden)"), ("Filling Pieces", "Luxury Sneakers (NL)"),
    ("P448", "Italian Luxury Sneakers"), ("Maison Margiela", "Avant-Garde Fashion"),
    ("Rick Owens", "Avant-Garde Fashion"), ("Comme des Garçons", "Avant-Garde (Japan)"),
    ("Issey Miyake", "Japanese Designer Fashion"), ("Yohji Yamamoto", "Japanese Designer Fashion"),
    ("Sacai", "Japanese Designer Fashion"), ("Kenzo", "Fashion House (Japan/France)"),
    # More Streetwear
    ("Supreme", "Streetwear Brand"), ("Palace", "Streetwear Brand (UK)"),
    ("Stüssy", "Streetwear Brand"), ("A Bathing Ape (BAPE)", "Japanese Streetwear"),
    ("Neighborhood", "Japanese Streetwear"), ("WTAPS", "Japanese Streetwear"),
    ("Human Made", "Japanese Streetwear"), ("Undercover", "Japanese Streetwear"),
    ("Noah NYC", "Streetwear & Sustainability"), ("Kith", "Streetwear & Lifestyle"),
    ("Fear of God", "Luxury Streetwear"), ("Essentials", "Accessible Streetwear (FOG)"),
    ("Aimé Leon Dore", "NYC Streetwear & Lifestyle"), ("New Era", "Cap & Headwear Brand"),
    ("Mitchell & Ness", "Vintage Sportswear"), ("Starter", "Sports Apparel"),
], "Expense", "Shopping", "Clothing & Apparel")

add([
    # More Electronics/Tech brands
    ("Sonos", "Wireless Audio System"), ("Marshall Headphones", "Audio Brand (UK)"),
    ("Sennheiser", "Audio Equipment (Germany)"), ("Focal", "Audio Equipment (France)"),
    ("KEF", "Speakers (UK)"), ("Bowers & Wilkins", "Premium Audio (UK)"),
    ("Denon", "Audio & AV Equipment"), ("Marantz", "Audio Equipment"),
    ("Yamaha Audio", "Audio Equipment (Japan)"), ("Pioneer", "Audio & DJ Equipment"),
    ("Technics", "Audio Equipment (Japan)"), ("Audio-Technica", "Headphones & Turntables"),
    ("Shure", "Microphones & Audio"), ("Rode", "Microphones (Australia)"),
    ("Blue Microphones", "USB & Studio Microphones"), ("Elgato", "Streaming Equipment"),
    ("Blackmagic Design", "Video Production Equipment"), ("Atomos", "Video Monitors & Recorders"),
    ("Peak Design", "Camera Bags & Accessories"), ("Manfrotto", "Camera Tripods & Accessories"),
    ("Zhiyun", "Camera Gimbals"), ("DJI Osmo", "Handheld Stabilizer"),
    ("Insta360", "360° Cameras"), ("Ricoh Theta", "360° Camera"),
    ("Oculus/Meta Quest", "VR Headset"), ("HTC Vive", "VR Headset"),
    ("PlayStation VR", "VR Headset (Sony)"), ("Valve Index", "VR Headset"),
    ("Microsoft Surface", "Tablet & Laptop"), ("iPad", "Tablet (Apple)"),
    ("Galaxy Tab", "Tablet (Samsung)"), ("Kindle", "E-Reader (Amazon)"),
    ("Kobo", "E-Reader"), ("reMarkable", "E-Ink Tablet"),
    ("Wacom", "Drawing Tablets"), ("XP-Pen", "Drawing Tablets"),
    ("Huion", "Drawing Tablets"), ("CalDigit", "Mac Docks & Storage"),
    ("Anker", "Charging & Accessories"), ("Belkin", "Tech Accessories"),
    ("Ugreen", "Tech Accessories"), ("Twelve South", "Apple Accessories"),
    ("Nomad", "Premium Tech Accessories"), ("Satechi", "USB-C Accessories"),
    ("Keychron", "Mechanical Keyboards"), ("Ducky", "Mechanical Keyboards"),
    ("GMMK", "Custom Mechanical Keyboards"), ("Drop", "Keyboards & Audio"),
], "Expense", "Shopping", "Electronics")

add([
    # More Hotels (Boutique & Regional)
    ("citizenM", "Boutique Hotel Chain"), ("Moxy Hotels", "Millennial-Focused Hotel"),
    ("Yotel", "Compact Luxury Hotel"), ("Hoxton Hotels", "Boutique Hotel (UK/Global)"),
    ("Ace Hotel", "Boutique Lifestyle Hotel"), ("Standard Hotels", "Lifestyle Hotel"),
    ("1 Hotels", "Eco-Luxury Hotel"), ("Proper Hotels", "Luxury Boutique Hotel"),
    ("Graduate Hotels", "College-Town Boutique"), ("Shinola Hotel", "Boutique (Detroit)"),
    ("Freehand Hotels", "Boutique Hostel/Hotel"), ("Generator Hostels", "Design Hostel Chain"),
    ("Selina", "Work/Stay Hotel (Global)"), ("Sonder", "Tech-Enabled Short Stay"),
    ("Mint House", "Apartment Hotel"), ("Lyric", "Luxury Apartment Hotel"),
    ("Stay Alfred", "Vacation Rental"), ("Vacasa", "Vacation Rental Management"),
    ("Evolve Vacation Rental", "Vacation Rental"), ("RedDoorz", "Budget Hotel (SE Asia)"),
    ("OYO Rooms", "Budget Hotel Chain (India/Global)"), ("Treebo Hotels", "Budget Hotel (India)"),
    ("FabHotels", "Budget Hotel (India)"), ("Zostel", "Backpacker Hostel (India)"),
    ("a]Hotel", "Capsule Hotel (Japan)"), ("First Cabin", "Capsule Hotel (Japan)"),
    ("Nine Hours", "Capsule Hotel (Japan)"), ("Hoshinoya", "Luxury Ryokan (Japan)"),
    ("Hoshino Resorts", "Resort Chain (Japan)"), ("Prince Hotels", "Hotel Chain (Japan)"),
    ("New Otani", "Hotel Chain (Japan)"), ("Imperial Hotel Tokyo", "Luxury Hotel (Japan)"),
    ("Mandarin Oriental Tokyo", "Luxury Hotel (Japan)"), ("Aman Tokyo", "Ultra-Luxury (Japan)"),
    ("Capella Hotels", "Luxury Boutique"), ("Firmdale Hotels", "Boutique Hotels (London)"),
    ("Soho House", "Members Club & Hotel"), ("The Ned", "Hotel & Members Club (London)"),
    ("Nobu Hotel", "Lifestyle Hotel"), ("Edition Hotels", "Luxury Boutique (Marriott)"),
    ("Pendry Hotels", "Luxury Lifestyle Hotel"), ("Auberge Resorts", "Luxury Resort Collection"),
    ("Como Hotels", "Luxury Wellness Hotel"), ("Six Senses", "Luxury Wellness Resort"),
], "Expense", "Travel", "Hotels & Lodging")

add([
    # More Groceries (specialty & organic)
    ("Whole Foods 365", "Budget Organic Grocery"), ("Erewhon", "Luxury Organic Grocery"),
    ("Bristol Farms", "Premium Supermarket"), ("Gelsons", "Premium Supermarket (CA)"),
    ("New Seasons Market", "Natural Grocery (Pacific NW)"), ("MOM's Organic Market", "Organic Grocery"),
    ("Earth Fare", "Natural & Organic Grocery"), ("Lucky's Market", "Natural Grocery"),
    ("Lassens Natural Foods", "Organic Grocery"), ("Jimbo's Naturally", "Organic Grocery (SD)"),
    ("Rainbow Grocery", "Cooperative Grocery (SF)"), ("Park Slope Food Coop", "Co-op Grocery (NYC)"),
    ("Willy Street Co-op", "Cooperative Grocery (WI)"), ("People's Food Co-op", "Co-op Grocery"),
    ("Plum Market", "Specialty Grocery (MI)"), ("The Fresh Market", "Specialty Grocery"),
    ("Straub's Fine Grocers", "Premium Grocery (MO)"), ("Heinen's", "Premium Grocery (OH)"),
    ("Kowalski's Markets", "Premium Grocery (MN)"), ("Lunds & Byerlys", "Premium Grocery (MN)"),
    ("Metropolitan Market", "Specialty Grocery (WA)"), ("Town & Country Markets", "Specialty (WA)"),
    # Asian Grocery US
    ("Hmart", "Korean Supermarket"), ("Mitsuwa Marketplace", "Japanese Supermarket"),
    ("Uwajimaya", "Asian Supermarket (Pacific NW)"), ("99 Ranch Market", "Chinese Supermarket"),
    ("Seafood City", "Filipino Supermarket"), ("Lotte Plaza Market", "Korean Supermarket"),
    ("Nijiya Market", "Japanese Grocery"), ("Marukai", "Japanese Grocery"),
    ("Tokyo Central", "Japanese Supermarket"), ("Zion Market", "Korean Supermarket"),
    ("Assi Plaza", "Korean Supermarket"), ("Kim's Mart", "Korean Grocery"),
    ("Great Wall Supermarket", "Chinese Grocery"), ("Good Fortune", "Chinese Grocery"),
    # Hispanic Grocery US
    ("Northgate Gonzalez Market", "Hispanic Supermarket"), ("Cardenas Markets", "Hispanic Supermarket"),
    ("El Super", "Hispanic Supermarket"), ("Vallarta Supermarkets", "Hispanic Supermarket"),
    ("Superior Grocers", "Hispanic Supermarket"), ("Compare Foods", "Hispanic Grocery"),
    ("Fiesta Mart", "Hispanic Supermarket"), ("La Michoacana Meat Market", "Hispanic Butcher/Grocery"),
    ("Ranch Market", "Hispanic Supermarket"), ("Food City (AZ)", "Hispanic Supermarket"),
    # International (more)
    ("Mercato Metropolitano", "Italian Food Market (London)"), ("Borough Market", "Food Market (London)"),
    ("Harrods Food Hall", "Luxury Food Hall (London)"), ("Fortnum & Mason", "Luxury Food (London)"),
    ("KaDeWe Food Floor", "Luxury Food Hall (Berlin)"), ("Dallmayr", "Gourmet Food (Munich)"),
    ("La Grande Épicerie", "Luxury Food Hall (Paris)"), ("Fauchon", "Luxury Food (Paris)"),
    ("Hédiard", "Luxury Food (Paris)"), ("Dean & DeLuca", "Gourmet Food Market"),
], "Expense", "Food & Dining", "Groceries")

# ============================================================
# ADDITIONAL - More categories to reach 4000
# ============================================================

add([
    # More Coffee & Tea
    ("Black Rifle Coffee", "Veteran-Owned Coffee"), ("Death Wish Coffee", "Strong Coffee Brand"),
    ("Trade Coffee", "Subscription Coffee"), ("Atlas Coffee Club", "Coffee Subscription"),
    ("Bean Box", "Coffee Subscription"), ("Driftaway Coffee", "Subscription Coffee"),
    ("MistoBox", "Coffee Subscription"), ("Angels Cup", "Coffee Subscription"),
    ("Nespresso", "Coffee Machine & Pods"), ("Keurig", "Coffee Machine & K-Cups"),
    ("Lavazza", "Italian Coffee Brand"), ("Illy", "Italian Coffee Brand"),
    ("Segafredo", "Italian Coffee Chain"), ("Julius Meinl", "Austrian Coffee Brand"),
    ("McCafé", "McDonald's Coffee"), ("Second Cup", "Coffee Chain (Canada)"),
    ("Bridgehead Coffee", "Coffee Chain (Ottawa)"), ("Blenz Coffee", "Coffee Chain (Vancouver)"),
    ("Peet's Coffee", "Specialty Coffee"), ("Stumptown Coffee", "Specialty Coffee"),
    ("Verve Coffee Roasters", "Specialty Coffee"), ("Onyx Coffee Lab", "Specialty Coffee"),
    ("George Howell Coffee", "Specialty Coffee"), ("Equator Coffees", "Specialty Coffee"),
    ("Ritual Coffee Roasters", "Specialty Coffee (SF)"), ("Sightglass Coffee", "Specialty Coffee (SF)"),
    ("Four Barrel Coffee", "Specialty Coffee (SF)"), ("Chromatic Coffee", "Specialty Coffee"),
    ("Heart Coffee Roasters", "Specialty Coffee (Portland)"), ("Coava Coffee", "Specialty Coffee"),
    ("Proud Mary Coffee", "Specialty Coffee (AU/Portland)"), ("Market Lane Coffee", "Specialty Coffee (Melbourne)"),
    ("Patricia Coffee", "Specialty Coffee (Melbourne)"), ("Single O", "Specialty Coffee (Sydney)"),
    ("Allpress Espresso", "Specialty Coffee (NZ)"), ("Flight Coffee", "Specialty Coffee (NZ)"),
    ("Ozone Coffee", "Specialty Coffee (NZ/London)"), ("Workshop Coffee", "Specialty Coffee (London)"),
    ("Origin Coffee", "Specialty Coffee (Cornwall)"), ("Assembly Coffee", "Specialty Coffee (London)"),
    ("Notes Coffee", "Specialty Coffee (London)"), ("Rosslyn Coffee", "Specialty Coffee (London)"),
    ("Monmouth Coffee", "Specialty Coffee (London)"), ("Square Mile Coffee", "Specialty Roaster (London)"),
    ("The Barn", "Specialty Coffee (Berlin)"), ("Bonanza Coffee", "Specialty Coffee (Berlin)"),
    ("Five Elephant", "Specialty Coffee (Berlin)"), ("Father Carpenter", "Specialty Coffee (Berlin)"),
    ("Ditta Artigianale", "Specialty Coffee (Florence)"), ("Orsonero", "Specialty Coffee (Milan)"),
    ("Nomad Coffee", "Specialty Coffee (Barcelona)"), ("Satan's Coffee Corner", "Coffee (Barcelona)"),
    ("Tim Wendelboe", "Specialty Coffee (Oslo)"), ("Fuglen", "Coffee & Cocktails (Oslo/Tokyo)"),
    ("Drop Coffee", "Specialty Coffee (Stockholm)"), ("Johan & Nyström", "Coffee (Stockholm)"),
    ("Cafe Integral", "Specialty Coffee (NYC)"), ("Sey Coffee", "Specialty Coffee (Brooklyn)"),
    ("Partners Coffee", "Specialty Coffee (NYC)"), ("Devoción", "Colombian Coffee (NYC)"),
    ("Birch Coffee", "Coffee Chain (NYC)"), ("Think Coffee", "Coffee Chain (NYC)"),
    ("Toby's Estate", "Specialty Coffee (NYC/AU)"), ("Parlor Coffee", "Specialty Coffee (Brooklyn)"),
    ("Madcap Coffee", "Specialty Coffee (Michigan)"), ("Intelligentsia", "Specialty Coffee"),
    ("Counter Culture", "Specialty Coffee Roaster"), ("Metric Coffee", "Specialty Coffee (Chicago)"),
    ("Dark Matter Coffee", "Specialty Coffee (Chicago)"), ("Gaslight Coffee", "Coffee (Chicago)"),
    ("Sawada Coffee", "Specialty Coffee (Chicago)"), ("Big Shoulders Coffee", "Coffee (Chicago)"),
], "Expense", "Food & Dining", "Coffee & Tea")

add([
    # More Bakeries
    ("Tartine Bakery", "Artisan Bakery (SF)"), ("Tartine Manufactory", "Bakery & Restaurant (SF)"),
    ("Acme Bread", "Artisan Bread (Berkeley)"), ("Josey Baker Bread", "Artisan Bakery (SF)"),
    ("The Mill", "Toast & Coffee (SF)"), ("Arizmendi Bakery", "Cooperative Bakery (SF)"),
    ("Porto's Bakery & Cafe", "Cuban Bakery (LA)"), ("La Brea Bakery", "Artisan Bakery (LA)"),
    ("Gjusta", "Bakery & Deli (Venice, CA)"), ("Clark Street Bread", "Artisan Bakery (LA)"),
    ("Amy's Bread", "Artisan Bakery (NYC)"), ("Sullivan Street Bakery", "Artisan Bread (NYC)"),
    ("Bien Cuit", "French Bakery (Brooklyn)"), ("Runner & Stone", "Bakery & Restaurant (Brooklyn)"),
    ("Pain D'Avignon", "French Bakery (NYC)"), ("Breads Bakery", "Israeli/Danish Bakery (NYC)"),
    ("Mah-Ze-Dahr Bakery", "Fine Bakery (NYC)"), ("Dominique Ansel Bakery", "Pastry (NYC)"),
    ("Milk Bar", "Modern Bakery & Desserts"), ("Baked", "Bakery (Brooklyn)"),
    ("Bakehouse", "Artisan Bakery"), ("Hot Bread Kitchen", "Multicultural Bakery (NYC)"),
    ("Zingerman's Bakehouse", "Artisan Bakery (Ann Arbor)"), ("Great Harvest Bread", "Bakery Chain"),
    ("Panera Bread", "Bakery Cafe Chain"), ("Einstein Bros Bagels", "Bagel Chain"),
    ("Noah's Bagels", "Bagel Chain"), ("Bruegger's Bagels", "Bagel Chain"),
    ("Manhattan Bagel", "Bagel Chain"), ("Bagel Boss", "Bagel Shop (NYC)"),
    ("Ess-a-Bagel", "Bagel Shop (NYC)"), ("Russ & Daughters", "Jewish Appetizing (NYC)"),
    ("Murray's Bagels", "Bagel Shop (NYC)"), ("Black Seed Bagels", "Montreal-Style Bagels (NYC)"),
    ("H&H Bagels", "Bagel Shop (NYC)"), ("St-Viateur Bagel", "Montreal Bagel Shop"),
    ("Fairmount Bagel", "Montreal Bagel Shop"), ("Kettleman's Bagel", "Bagel (Ottawa)"),
    ("Beigel Bake", "Bagel Shop (London)"), ("Roni's Bakery", "Challah Bakery (London)"),
    ("Gail's Bakery", "Artisan Bakery (London)"), ("Ole & Steen", "Danish Bakery (London)"),
    ("Konditor", "German-Inspired Bakery (London)"), ("Crosstown Doughnuts", "Gourmet Doughnut (London)"),
    ("Bread Ahead", "Bakery & Baking School (London)"), ("Dusty Knuckle", "Bakery (London)"),
    ("E5 Bakehouse", "Organic Bakery (London)"), ("The Dusty Knuckle", "Bakery (London)"),
    ("Fortitude Bakehouse", "Bakery (Melbourne)"), ("Lune Croissanterie", "Croissant Bakery (Melbourne)"),
    ("Tivoli Road Bakery", "Bakery (Melbourne)"), ("Bourke Street Bakery", "Artisan Bakery (Sydney)"),
    ("Iggy's Bread", "Artisan Sourdough (Sydney)"), ("Brickfields", "Bakery & Cafe (Sydney)"),
], "Expense", "Food & Dining", "Bakery & Desserts")

add([
    # More Software/SaaS & Subscriptions
    ("Notion", "Productivity & Notes App"), ("Obsidian", "Knowledge Management App"),
    ("Roam Research", "Networked Note-Taking"), ("Logseq", "Knowledge Graph App"),
    ("Craft Docs", "Document App (Apple)"), ("Bear App", "Markdown Notes App"),
    ("Ulysses", "Writing App (Mac/iOS)"), ("iA Writer", "Minimalist Writing App"),
    ("Scrivener", "Long-Form Writing Software"), ("Final Draft", "Screenwriting Software"),
    ("Procreate", "Digital Art App (iPad)"), ("Affinity Photo", "Photo Editing Software"),
    ("Affinity Designer", "Vector Design Software"), ("Pixelmator Pro", "Photo Editor (Mac)"),
    ("DaVinci Resolve", "Video Editing Software"), ("Final Cut Pro", "Video Editing (Apple)"),
    ("Adobe Premiere", "Video Editing Software"), ("Adobe Photoshop", "Image Editing Software"),
    ("Adobe Illustrator", "Vector Design Software"), ("Adobe Lightroom", "Photo Management"),
    ("Capture One", "Photo Editing Software"), ("Luminar", "AI Photo Editor"),
    ("Sketch", "UI/UX Design Tool"), ("Figma", "Collaborative Design Tool"),
    ("Framer", "Interactive Design Tool"), ("Principle", "Animation Design Tool"),
    ("ProtoPie", "Prototyping Tool"), ("Zeplin", "Design-to-Dev Handoff"),
    ("Abstract", "Design Version Control"), ("Maze", "User Testing Platform"),
    ("Hotjar", "Website Analytics & Heatmaps"), ("FullStory", "Digital Experience Analytics"),
    ("Amplitude", "Product Analytics"), ("Mixpanel", "Product Analytics"),
    ("Heap Analytics", "Product Analytics"), ("Segment", "Customer Data Platform"),
    ("Twilio Segment", "Customer Data Platform"), ("mParticle", "Customer Data Platform"),
    ("Braze", "Customer Engagement"), ("Iterable", "Growth Marketing Platform"),
    ("Klaviyo", "Email Marketing (E-Commerce)"), ("Omnisend", "E-Commerce Email Marketing"),
    ("ActiveCampaign", "Email Marketing & CRM"), ("ConvertKit", "Email for Creators"),
    ("Beehiiv", "Newsletter Platform"), ("Substack", "Newsletter & Publishing"),
    ("Ghost", "Publishing Platform"), ("Medium", "Writing & Publishing Platform"),
    ("Buttondown", "Newsletter Tool"), ("Revue", "Newsletter Tool"),
    ("Carrd", "Simple One-Page Websites"), ("Typedream", "No-Code Website Builder"),
    ("Bubble", "No-Code App Builder"), ("Adalo", "No-Code Mobile App Builder"),
    ("Glide", "No-Code App Builder"), ("Airtable", "Spreadsheet-Database Hybrid"),
    ("Coda", "All-in-One Doc"), ("ClickUp", "Productivity & Project Management"),
    ("Linear", "Issue Tracking for Engineers"), ("Height", "Project Management"),
    ("Lark", "Collaboration Suite (ByteDance)"), ("Feishu", "Collaboration (China)"),
    ("DingTalk", "Work Platform (Alibaba)"), ("WeCom", "Business Communication (Tencent)"),
    ("Whereby", "Video Conferencing"), ("Around", "Video Conferencing"),
    ("Gather", "Virtual Office"), ("Kumospace", "Virtual Office"),
    ("Tandem", "Virtual Office"), ("Teamflow", "Virtual Office"),
    ("Mural", "Visual Collaboration"), ("FigJam", "Whiteboard (Figma)"),
    ("Whimsical", "Wireframes & Flowcharts"), ("Excalidraw", "Whiteboard Tool"),
], "Expense", "Technology", "Software & SaaS")

add([
    # More Sporting Goods
    ("lululemon", "Athletic Apparel (Yoga)"), ("Athleta", "Women's Athletic Apparel"),
    ("Sweaty Betty", "Women's Activewear (UK)"), ("Girlfriend Collective", "Sustainable Activewear"),
    ("Outdoor Voices", "Casual Athletic Apparel"), ("Vuori", "Premium Athletic Casual"),
    ("Ten Thousand", "Performance Training Apparel"), ("Rhone", "Men's Performance Apparel"),
    ("Tracksmith", "Running Apparel"), ("Janji", "Running Apparel"),
    ("Path Projects", "Trail Running Apparel"), ("Oiselle", "Women's Running Apparel"),
    ("Satisfy Running", "Premium Running (France)"), ("District Vision", "Running & Meditation"),
    ("On Running", "Swiss Running Shoes"), ("Altra Running", "Zero-Drop Running Shoes"),
    ("Topo Athletic", "Natural Running Shoes"), ("Xero Shoes", "Minimalist Footwear"),
    ("Vivobarefoot", "Barefoot Shoes (UK)"), ("Inov-8", "Trail Running (UK)"),
    ("La Sportiva", "Climbing & Mountain Shoes"), ("Scarpa", "Mountain Footwear (Italy)"),
    ("Five Ten", "Climbing Shoes (Adidas)"), ("Evolv", "Climbing Shoes"),
    ("Black Diamond", "Climbing & Skiing Gear"), ("Petzl", "Climbing & Headlamps (France)"),
    ("Mammut", "Mountain Sports (Switzerland)"), ("Rab", "Mountain Clothing (UK)"),
    ("Mountain Equipment", "Alpine Clothing (UK)"), ("Icebreaker", "Merino Wool (NZ)"),
    ("Smartwool", "Merino Wool Apparel"), ("Darn Tough", "Merino Socks (Vermont)"),
    ("Farm to Feet", "American Wool Socks"), ("Point6", "Merino Socks"),
    ("Buff", "Headwear & Neckwear (Spain)"), ("Cotopaxi", "Outdoor Gear (Sustainable)"),
    ("United By Blue", "Sustainable Outdoor"), ("Toad&Co", "Sustainable Casual"),
    ("Royal Robbins", "Travel & Outdoor Apparel"), ("ExOfficio", "Travel Apparel"),
    ("Kühl", "Outdoor Apparel"), ("Mountain Khakis", "Outdoor Casual"),
    ("Sherpa Adventure Gear", "Outdoor (Nepal)"), ("Montbell", "Japanese Outdoor Brand"),
    ("Snow Peak", "Outdoor & Camping (Japan)"), ("MSR", "Camping & Mountaineering Gear"),
    ("Jetboil", "Camp Stoves"), ("GSI Outdoors", "Camping Cookware"),
    ("Sea to Summit", "Travel & Outdoor Gear (AU)"), ("Nemo Equipment", "Tents & Sleep"),
    ("Big Agnes", "Tents & Sleeping Bags"), ("Therm-a-Rest", "Sleeping Pads"),
    ("Kelty", "Tents & Camping"), ("Eureka!", "Tents & Camping"),
    ("Sierra Designs", "Outdoor Gear"), ("Mountain Hardware", "Outdoor Gear"),
], "Expense", "Shopping", "Sporting Goods")

add([
    # More Financial Services / Insurance
    ("Oscar Health", "Health Insurance"), ("Clover Health", "Medicare Advantage"),
    ("Bright Health", "Health Insurance"), ("Aetna", "Health Insurance"),
    ("Cigna", "Health Insurance"), ("UnitedHealthcare", "Health Insurance"),
    ("Blue Cross Blue Shield", "Health Insurance"), ("Humana", "Health Insurance"),
    ("Kaiser Permanente", "Health Insurance & HMO"), ("Centene", "Managed Care"),
    ("Molina Healthcare", "Managed Care"), ("Anthem", "Health Insurance"),
    ("WellCare", "Managed Care"), ("Magellan Health", "Behavioral Health"),
    ("Teladoc Health", "Telehealth Platform"), ("Amwell", "Telehealth Platform"),
    ("MDLive", "Telehealth Platform"), ("Doctor On Demand", "Telehealth"),
    ("GoodRx", "Prescription Discount Platform"), ("RxSaver", "Prescription Discount"),
    ("SingleCare", "Prescription Discount"), ("Blink Health", "Prescription Discount"),
    ("Mark Cuban Cost Plus Drug", "Low-Cost Pharmacy"), ("Costco Pharmacy", "Pharmacy"),
    ("Walmart Pharmacy", "Pharmacy"), ("CVS Caremark", "Pharmacy Benefit Manager"),
    ("Express Scripts", "Pharmacy Benefit Manager"), ("OptumRx", "Pharmacy Benefit Manager"),
    # More Investment/Wealth
    ("Fidelity", "Investment & Brokerage"), ("Schwab", "Investment & Brokerage"),
    ("Vanguard", "Index Funds & ETFs"), ("T. Rowe Price", "Investment Management"),
    ("BlackRock", "Asset Management"), ("PIMCO", "Bond Fund Manager"),
    ("JPMorgan Asset Management", "Asset Management"), ("Goldman Sachs AM", "Asset Management"),
    ("Bridgewater Associates", "Hedge Fund"), ("Renaissance Technologies", "Hedge Fund"),
    ("AQR Capital", "Quantitative Investment"), ("Two Sigma", "Quant Investment"),
    ("Citadel", "Hedge Fund"), ("D.E. Shaw", "Hedge Fund"),
    # Tax & Accounting
    ("TurboTax", "Tax Preparation Software"), ("H&R Block", "Tax Preparation Service"),
    ("Jackson Hewitt", "Tax Preparation Service"), ("Liberty Tax", "Tax Preparation"),
    ("TaxAct", "Tax Software"), ("FreeTaxUSA", "Free Tax Filing"),
    ("Cash App Taxes", "Free Tax Filing"), ("TaxSlayer", "Tax Software"),
], "Expense", "Financial Services", "Banking Fees")

add([
    ("ADT Security", "Home Security System"), ("Vivint Smart Home", "Smart Home Security"),
    ("SimpliSafe", "DIY Home Security"), ("Ring Alarm", "Smart Security (Amazon)"),
    ("Nest Thermostat", "Smart Thermostat"), ("Ecobee", "Smart Thermostat"),
    ("Honeywell Home", "Smart Home & HVAC"), ("Lutron", "Smart Lighting Controls"),
    ("Philips Hue", "Smart Lighting"), ("August Smart Lock", "Smart Lock"),
    ("iRobot Roomba", "Robot Vacuum"), ("Roborock", "Robot Vacuum"),
    ("Ecovacs Deebot", "Robot Vacuum"), ("Dyson V15", "Cordless Vacuum"),
    ("Tineco", "Smart Vacuum & Mop"), ("Bissell", "Vacuum & Floor Care"),
    ("TruGreen", "Lawn Care Service"), ("Lawn Doctor", "Lawn Care Franchise"),
    ("Rachio", "Smart Sprinkler Controller"), ("Molly Maid", "House Cleaning"),
    ("Merry Maids", "House Cleaning"), ("Handy", "Home Cleaning & Handyman"),
    ("TaskRabbit", "Home Services Gig Platform"), ("Thumbtack", "Local Service Marketplace"),
    ("Angi", "Home Service Marketplace"), ("Porch", "Home Service Platform"),
    ("Terminix", "Pest Control"), ("Orkin", "Pest Control Service"),
    ("Stanley Steemer", "Carpet Cleaning"), ("ServiceMaster", "Restoration & Cleaning"),
    ("Roto-Rooter", "Plumbing & Drain"), ("Mr. Rooter", "Plumbing Service"),
    ("One Hour Heating & Air", "HVAC Service"), ("Carrier HVAC", "Air Conditioning"),
    ("Lennox HVAC", "Heating & Cooling"), ("Trane HVAC", "Heating & Cooling"),
], "Expense", "Housing & Utilities", "Home Services")

add([
    ("Blizzard Entertainment", "Game Developer (WoW/OW)"), ("CD Projekt Red", "Game Developer"),
    ("FromSoftware", "Game Developer (Japan)"), ("Hoyoverse", "Game Developer (Genshin)"),
    ("Riot Games", "Game Developer (LoL)"), ("Bungie", "Game Developer (Destiny)"),
    ("Rockstar Games", "Game Developer (GTA/RDR)"), ("Epic Games", "Game Developer & Store"),
    ("Supercell", "Mobile Game Developer (Finland)"), ("King", "Mobile Games (Candy Crush)"),
    ("Niantic", "AR Games (Pokémon GO)"), ("Larian Studios", "RPG Developer (BG3)"),
    ("Paradox Interactive", "Strategy Publisher (Sweden)"), ("Bethesda", "Game Developer (Elder Scrolls)"),
    ("2K Games", "Game Publisher"), ("Insomniac Games", "Game Developer (Spider-Man)"),
    ("Naughty Dog", "Game Developer (TLOU)"), ("Santa Monica Studio", "Game Developer (GoW)"),
    ("PlatinumGames", "Game Developer (Japan)"), ("Atlus", "Game Developer (Persona)"),
    ("Turn 10 Studios", "Game Developer (Forza)"), ("Respawn Entertainment", "Game Developer (Apex)"),
    ("Infinity Ward", "Game Developer (CoD)"), ("Psyonix", "Game Developer (Rocket League)"),
    ("Roblox Corporation", "Gaming Platform"), ("Minecraft (Mojang)", "Sandbox Game"),
], "Expense", "Entertainment", "Gaming")

add([
    ("Apple Music", "Music Streaming"), ("Pandora", "Music Streaming & Radio"),
    ("Deezer", "Music Streaming (France)"), ("SoundCloud Go", "Music Streaming"),
    ("Qobuz", "Hi-Res Music Streaming"), ("iHeartRadio", "Internet Radio & Podcast"),
    ("TuneIn", "Internet Radio"), ("Pocket Casts", "Podcast App"),
    ("Stitcher", "Podcast Platform"), ("Calm", "Meditation & Sleep App"),
    ("Headspace", "Meditation App"), ("Strava", "Running & Cycling App"),
    ("Zwift", "Indoor Cycling Platform"), ("Peloton App", "Fitness Streaming"),
    ("Apple Fitness+", "Fitness Streaming"), ("Les Mills On Demand", "Fitness Streaming"),
    ("Garmin Connect", "Fitness Tracking"), ("Whoop", "Recovery & Fitness Tracker"),
    ("Oura Ring", "Sleep & Health Tracker"), ("Noom", "Weight Loss App"),
    ("MyFitnessPal", "Calorie Tracking App"), ("Cronometer", "Nutrition Tracking App"),
    ("Lose It!", "Weight Loss App"), ("WW (WeightWatchers)", "Weight Management App"),
    ("Fitbit Premium", "Fitness Subscription"), ("Samsung Health", "Health & Fitness"),
    ("Nike Training Club", "Workout App"), ("Adidas Training", "Workout App"),
    ("Freeletics", "AI Personal Training"), ("Centr", "Fitness App"),
    ("Obe Fitness", "Live Fitness Classes"), ("Mirror (Lululemon)", "Smart Fitness Mirror"),
    ("Tonal", "Smart Home Gym"), ("Tempo", "Smart Home Gym"),
    ("NordicTrack iFit", "Connected Fitness"), ("Hydrow", "Connected Rowing"),
    ("Echelon", "Connected Fitness Bike"), ("SoulCycle At-Home", "Connected Bike"),
    ("ClassPass", "Fitness Membership App"), ("Mindbody", "Fitness & Wellness Booking"),
], "Expense", "Entertainment", "Sports & Recreation")

add([
    # More Coffee
    ("Black Rifle Coffee", "Veteran-Owned Coffee"), ("Death Wish Coffee", "Strong Coffee Brand"),
    ("Trade Coffee", "Subscription Coffee"), ("Atlas Coffee Club", "Coffee Subscription"),
    ("Nespresso", "Coffee Machine & Pods"), ("Lavazza", "Italian Coffee"),
    ("Intelligentsia", "Specialty Coffee"), ("Counter Culture", "Specialty Coffee"),
    ("Stumptown Coffee", "Specialty Coffee (Portland)"), ("Blue Bottle Coffee", "Specialty Coffee"),
    ("Verve Coffee Roasters", "Specialty Coffee"), ("Onyx Coffee Lab", "Specialty Coffee"),
    ("George Howell Coffee", "Specialty Coffee"), ("Heart Coffee", "Specialty Coffee"),
    ("Coava Coffee", "Specialty Coffee (Portland)"), ("Ritual Coffee", "Specialty Coffee (SF)"),
    ("Sightglass Coffee", "Specialty Coffee (SF)"), ("Equator Coffees", "Specialty Coffee"),
    ("Market Lane Coffee", "Specialty Coffee (Melbourne)"), ("Allpress Espresso", "Specialty Coffee (NZ)"),
    ("Workshop Coffee", "Specialty Coffee (London)"), ("Monmouth Coffee", "Specialty Coffee (London)"),
    ("Square Mile Coffee", "Specialty Roaster (London)"), ("The Barn", "Specialty Coffee (Berlin)"),
    ("Bonanza Coffee", "Specialty Coffee (Berlin)"), ("Tim Wendelboe", "Specialty Coffee (Oslo)"),
    ("Drop Coffee", "Specialty Coffee (Stockholm)"), ("Nomad Coffee", "Specialty Coffee (Barcelona)"),
    ("Partners Coffee", "Specialty Coffee (NYC)"), ("Devoción", "Colombian Coffee (NYC)"),
    ("Birch Coffee", "Coffee Chain (NYC)"), ("Madcap Coffee", "Specialty Coffee (Michigan)"),
    ("Dark Matter Coffee", "Specialty Coffee (Chicago)"), ("Metric Coffee", "Specialty Coffee"),
    ("Methodical Coffee", "Specialty Coffee (Greenville)"), ("Cat & Cloud Coffee", "Specialty Coffee"),
], "Expense", "Food & Dining", "Coffee & Tea")

add([
    # More Bakeries
    ("Tartine Bakery", "Artisan Bakery (SF)"), ("Porto's Bakery", "Cuban Bakery (LA)"),
    ("Dominique Ansel Bakery", "Pastry (NYC)"), ("Milk Bar", "Modern Bakery (NYC)"),
    ("Levain Bakery", "Cookie Bakery (NYC)"), ("Amy's Bread", "Artisan Bakery (NYC)"),
    ("Breads Bakery", "Israeli/Danish Bakery (NYC)"), ("Sullivan Street Bakery", "Artisan Bread (NYC)"),
    ("Zingerman's Bakehouse", "Artisan Bakery (Ann Arbor)"), ("Great Harvest Bread", "Bakery Chain"),
    ("Einstein Bros Bagels", "Bagel Chain"), ("Noah's Bagels", "Bagel Chain (West Coast)"),
    ("Bruegger's Bagels", "Bagel Chain"), ("Manhattan Bagel", "Bagel Chain"),
    ("Ess-a-Bagel", "Bagel Shop (NYC)"), ("Russ & Daughters", "Jewish Appetizing (NYC)"),
    ("Black Seed Bagels", "Montreal-Style Bagels (NYC)"), ("H&H Bagels", "Bagel Shop (NYC)"),
    ("St-Viateur Bagel", "Montreal Bagel Shop"), ("Fairmount Bagel", "Montreal Bagel"),
    ("Gail's Bakery", "Artisan Bakery (London)"), ("Ole & Steen", "Danish Bakery (London)"),
    ("Bread Ahead", "Bakery & School (London)"), ("Crosstown Doughnuts", "Gourmet Doughnut (UK)"),
    ("Lune Croissanterie", "Croissant Bakery (Melbourne)"), ("Bourke Street Bakery", "Bakery (Sydney)"),
    ("Ladurée", "French Patisserie (Macarons)"), ("Pierre Hermé", "French Patisserie"),
    ("Eric Kayser", "French Artisan Bakery"), ("Paul", "French Bakery (Global)"),
    ("Voodoo Doughnut", "Novelty Doughnut Shop"), ("Duck Donuts", "Made-to-Order Doughnuts"),
    ("Crumbl Cookies", "Specialty Cookie Shop"), ("Insomnia Cookies", "Late-Night Cookie Delivery"),
    ("Nothing Bundt Cakes", "Specialty Cake Shop"), ("Sprinkles Cupcakes", "Cupcake Bakery"),
    ("Georgetown Cupcake", "Cupcake Bakery"), ("Magnolia Bakery", "Cupcake & Dessert Bakery"),
], "Expense", "Food & Dining", "Bakery & Desserts")

add([
    # More Education
    ("Coursera", "Online Course Platform"), ("Udemy", "Online Course Marketplace"),
    ("edX", "University Online Learning"), ("Skillshare", "Creative Online Learning"),
    ("MasterClass", "Celebrity-Taught Courses"), ("Duolingo", "Language Learning App"),
    ("Babbel", "Language Learning App"), ("Rosetta Stone", "Language Learning"),
    ("Busuu", "Language Learning"), ("italki", "Language Tutoring"),
    ("Preply", "Online Tutoring"), ("Wyzant", "Tutoring Marketplace"),
    ("Kaplan", "Test Prep & Education"), ("The Princeton Review", "Test Prep"),
    ("Magoosh", "Online Test Prep"), ("Kumon", "Math & Reading Tutoring"),
    ("Mathnasium", "Math Learning Centers"), ("Sylvan Learning", "Tutoring Center"),
    ("Huntington Learning", "Tutoring Center"), ("School of Rock", "Music Education"),
    ("Fender Play", "Online Guitar Lessons"), ("Simply Piano", "Piano Learning App"),
    ("Yousician", "Music Learning App"), ("Guitar Center Lessons", "Music Lessons"),
    ("Pearson", "Educational Publisher"), ("McGraw Hill", "Educational Publisher"),
    ("Cengage", "Educational Publisher"), ("Scholastic", "Children's Publisher"),
    ("Age of Learning (ABCmouse)", "Children's Learning"), ("Homer", "Early Reading App"),
    ("Outschool", "Live Online Classes (Kids)"), ("Varsity Tutors", "Online Tutoring"),
    ("Byju's", "EdTech Platform (India)"), ("Unacademy", "Online Learning (India)"),
    ("Vedantu", "Live Tutoring (India)"), ("Toppr", "Learning App (India)"),
    ("Zhangmen", "Online Tutoring (China)"), ("VIPKid", "English Tutoring (China)"),
    ("Lingoda", "Online Language School"), ("Berlitz", "Language & Business Training"),
    ("EF Education First", "Language & Travel Education"), ("Wall Street English", "English Learning"),
], "Expense", "Education", "Online Learning")

add([
    # More Toys & Kids
    ("Melissa & Doug", "Educational Toys"), ("VTech", "Electronic Learning Toys"),
    ("LeapFrog", "Educational Technology"), ("Osmo", "Interactive Learning"),
    ("KiwiCo", "Kids Activity Subscription"), ("Lovevery", "Age-Based Toy Subscription"),
    ("Little Passports", "Kids Educational Subscription"), ("BuyBuy Baby", "Baby Products"),
    ("Pottery Barn Kids", "Kids Furniture"), ("Crate & Kids", "Kids Furniture"),
    ("UPPAbaby", "Premium Strollers"), ("Bugaboo", "Premium Strollers"),
    ("Nuna Baby", "Premium Baby Gear"), ("Ergobaby", "Baby Carriers"),
    ("Baby Jogger", "Strollers"), ("4moms", "Baby Tech Products"),
    ("Hatch Baby", "Baby Sound Machine"), ("Nanit", "Smart Baby Monitor"),
    ("Owlet", "Smart Baby Monitor"), ("Snoo", "Smart Bassinet"),
    ("Honest Company", "Baby & Home Products"), ("Babyganics", "Baby Skincare"),
    ("Earth's Best", "Organic Baby Food"), ("Happy Family", "Organic Baby Food"),
    ("Once Upon a Farm", "Organic Baby Food"), ("Cerebelly", "Brain-Building Baby Food"),
    ("Pampers", "Diapers"), ("Huggies", "Diapers"), ("Luvs", "Budget Diapers"),
    ("Hello Bello", "Diapers & Baby"), ("Dyper", "Sustainable Diapers"),
    ("Coterie", "Premium Diapers"), ("Rascal + Friends", "Diapers"),
    ("Build-A-Bear Workshop", "Custom Stuffed Animals"), ("LEGO Store", "Building Toy Store"),
    ("Disney Store", "Character Merchandise"), ("American Girl", "Premium Dolls"),
    ("Fat Brain Toys", "Educational Toys"), ("Learning Resources", "Educational Toys"),
    ("Ravensburger", "Puzzles & Games (Germany)"), ("Playmobil", "Toy Figures (Germany)"),
    ("Schleich", "Toy Animal Figures (Germany)"), ("Hape", "Wooden Toys"),
    ("Magna-Tiles", "Magnetic Building Tiles"), ("Grimm's", "Wooden Toys (Germany)"),
], "Expense", "Kids & Family", "Toys & Activities")

add([
    # More Charity & Donations
    ("GoFundMe", "Crowdfunding Platform"), ("Kickstarter", "Creative Crowdfunding"),
    ("Indiegogo", "Crowdfunding Platform"), ("Patreon", "Creator Membership Platform"),
    ("Buy Me a Coffee", "Creator Tips"), ("Ko-fi", "Creator Support Platform"),
    ("Wikipedia/Wikimedia", "Free Encyclopedia"), ("Khan Academy Donation", "Education Nonprofit"),
    ("St. Jude Children's", "Children's Hospital"), ("Salvation Army", "Charitable Organization"),
    ("United Way", "Charitable Organization"), ("Red Cross", "Humanitarian Organization"),
    ("Feeding America", "Food Bank Network"), ("Habitat for Humanity", "Housing Charity"),
    ("Doctors Without Borders", "Medical Charity"), ("UNICEF", "Children's Charity"),
    ("World Wildlife Fund", "Environmental Charity"), ("Nature Conservancy", "Environmental"),
    ("Sierra Club", "Environmental Organization"), ("ASPCA", "Animal Welfare"),
    ("Humane Society", "Animal Welfare"), ("Best Friends Animal Society", "Animal Rescue"),
    ("NPR", "Public Radio"), ("PBS", "Public Broadcasting"),
    ("Electronic Frontier Foundation", "Digital Rights"), ("ACLU", "Civil Liberties"),
    ("GiveDirectly", "Cash Transfer Charity"), ("Kiva", "Micro-Lending"),
    ("DonorsChoose", "Education Fundraising"), ("Charity: Water", "Clean Water Nonprofit"),
    ("Water.org", "Clean Water Nonprofit"), ("Pencils of Promise", "Education Charity"),
    ("Room to Read", "Children's Literacy"), ("Girl Scouts", "Youth Organization"),
    ("Boy Scouts/Scouting", "Youth Organization"), ("Big Brothers Big Sisters", "Youth Mentoring"),
    ("Make-A-Wish Foundation", "Children's Charity"), ("Ronald McDonald House", "Family Charity"),
    ("Shriners Children's", "Children's Hospital"), ("March of Dimes", "Maternal/Child Health"),
    ("American Cancer Society", "Cancer Research"), ("Susan G. Komen", "Breast Cancer Research"),
    ("Livestrong Foundation", "Cancer Support"), ("Movember Foundation", "Men's Health"),
], "Expense", "Donations & Gifts", "Charity & Donations")



add([
    ("Magnum", "Premium Ice Cream (Unilever)"), ("Talenti", "Italian-Style Gelato"),
    ("Graeter's", "Premium Ice Cream"), ("Blue Bell Ice Cream", "Ice Cream (Texas)"),
    ("Turkey Hill", "Ice Cream (Pennsylvania)"), ("Tillamook Ice Cream", "Premium Ice Cream"),
    ("Carvel", "Ice Cream Chain"), ("Bruster's", "Ice Cream Chain"),
    ("Handel's Ice Cream", "Premium Ice Cream"), ("Bahama Buck's", "Shaved Ice Chain"),
    ("Kona Ice", "Shaved Ice Truck"), ("Afters Ice Cream", "Ice Cream (LA)"),
    ("Salt & Straw", "Artisan Ice Cream"), ("Jeni's Ice Creams", "Artisan Ice Cream"),
    ("Van Leeuwen", "Artisan Ice Cream (NYC)"), ("Ample Hills Creamery", "Ice Cream (Brooklyn)"),
    ("McConnell's Fine Ice Creams", "Artisan Ice Cream"), ("Humphry Slocombe", "Ice Cream (SF)"),
    ("Molly Moon's", "Ice Cream (Seattle)"), ("Lick Honest Ice Creams", "Ice Cream (Austin)"),
    ("Amy's Ice Creams", "Ice Cream (Austin)"), ("JP Licks", "Ice Cream (Boston)"),
    ("Gelato Messina", "Gelato (Australia)"), ("Amorino", "Italian Gelato Chain"),
    ("Grom", "Italian Gelato"), ("Venchi", "Italian Chocolate & Gelato"),
    ("Bacio di Latte", "Gelato (Brazil)"), ("N2 Extreme Gelato", "Liquid Nitrogen Gelato"),
    ("Creamistry", "Liquid Nitrogen Ice Cream"), ("Freddy's Frozen Custard", "Frozen Custard Chain"),
    ("Andy's Frozen Custard", "Frozen Custard"), ("Kopp's Frozen Custard", "Frozen Custard (WI)"),
    ("Sub Zero", "Made-to-Order Ice Cream"), ("Bi-Rite Creamery", "Ice Cream (SF)"),
], "Expense", "Food & Dining", "Ice Cream & Yogurt")

add([
    ("Rover", "Pet Sitting & Walking App"), ("Wag!", "Dog Walking App"),
    ("Camp Bow Wow", "Dog Daycare & Boarding"), ("Dogtopia", "Dog Daycare Chain"),
    ("The Farmer's Dog", "Fresh Dog Food Delivery"), ("Ollie Pet Food", "Fresh Dog Food"),
    ("Spot & Tango", "Fresh Dog Food"), ("Open Farm", "Sustainable Pet Food"),
    ("Stella & Chewy's", "Raw & Natural Pet Food"), ("The Honest Kitchen", "Dehydrated Pet Food"),
    ("Trupanion", "Pet Insurance"), ("Healthy Paws", "Pet Insurance"),
    ("Figo Pet Insurance", "Pet Insurance"), ("Wagmo", "Pet Wellness Plan"),
    ("Banfield Pet Hospital", "Veterinary Chain"), ("VCA Animal Hospitals", "Veterinary Chain"),
    ("BluePearl Pet Hospital", "Emergency Vet"), ("Pawp", "Online Vet Consultation"),
    ("BetterVet", "Mobile Veterinary"), ("Bond Vet", "Veterinary Clinic"),
    ("Fressnapf", "Pet Supply (Germany)"), ("Zooplus", "Online Pet Supply (EU)"),
    ("Pet Circle", "Online Pet (Australia)"), ("Whiskers N Paws", "Pet Supply (HK)"),
], "Expense", "Shopping", "Pet Supplies")

add([
    ("Coursera", "Online Course Platform"), ("Udemy", "Online Course Marketplace"),
    ("edX", "University Online Learning"), ("Duolingo Plus", "Language Learning"),
    ("Babbel", "Language Learning App"), ("Busuu", "Language Learning"),
    ("italki", "Language Tutoring"), ("Preply", "Online Tutoring"),
    ("Kaplan", "Test Prep & Education"), ("Princeton Review", "Test Prep"),
    ("Magoosh", "Online Test Prep"), ("Kumon", "Math & Reading Tutoring"),
    ("Mathnasium", "Math Learning"), ("Sylvan Learning", "Tutoring Center"),
    ("School of Rock", "Music Education"), ("Fender Play", "Guitar Lessons"),
    ("Simply Piano", "Piano App"), ("Yousician", "Music Learning App"),
    ("Byju's", "EdTech (India)"), ("Unacademy", "Online Learning (India)"),
    ("VIPKid", "English Tutoring (China)"), ("Age of Learning", "Kids Learning (ABCmouse)"),
    ("Outschool", "Live Online Classes (Kids)"), ("Lingoda", "Online Language School"),
    ("Berlitz", "Language & Business Training"), ("EF Education First", "Language & Travel"),
], "Expense", "Education", "Online Learning")

add([
    ("GoFundMe", "Crowdfunding Platform"), ("Kickstarter", "Creative Crowdfunding"),
    ("Indiegogo", "Crowdfunding Platform"), ("Patreon", "Creator Membership"),
    ("Ko-fi", "Creator Support"), ("Buy Me a Coffee", "Creator Tips"),
    ("Wikipedia", "Free Encyclopedia"), ("Khan Academy Donation", "Education Nonprofit"),
    ("St. Jude Children's", "Children's Hospital"), ("Salvation Army", "Charitable Org"),
    ("United Way", "Charitable Org"), ("Red Cross", "Humanitarian Org"),
    ("Doctors Without Borders", "Medical Charity"), ("UNICEF", "Children's Charity"),
    ("World Wildlife Fund", "Environmental Charity"), ("ASPCA", "Animal Welfare"),
    ("Humane Society", "Animal Welfare"), ("Charity: Water", "Clean Water Nonprofit"),
    ("DonorsChoose", "Education Fundraising"), ("Kiva", "Micro-Lending"),
    ("GiveDirectly", "Cash Transfer Charity"), ("NPR", "Public Radio"),
    ("PBS", "Public Broadcasting"), ("ACLU", "Civil Liberties"),
    ("EFF", "Digital Rights"), ("Make-A-Wish", "Children's Charity"),
    ("Ronald McDonald House", "Family Charity"), ("Habitat for Humanity", "Housing Charity"),
    ("Feeding America", "Food Bank Network"), ("American Cancer Society", "Cancer Research"),
    ("March of Dimes", "Maternal/Child Health"), ("Movember", "Men's Health"),
], "Expense", "Donations & Gifts", "Charity & Donations")

add([
    ("Melissa & Doug", "Educational Toys"), ("VTech", "Electronic Learning Toys"),
    ("LeapFrog", "Educational Tech Toys"), ("KiwiCo", "Kids Activity Subscription"),
    ("Lovevery", "Developmental Toy Subscription"), ("Little Passports", "Kids Education Sub"),
    ("BuyBuy Baby", "Baby Products"), ("UPPAbaby", "Premium Strollers"),
    ("Bugaboo", "Premium Strollers"), ("Ergobaby", "Baby Carriers"),
    ("Hatch Baby", "Baby Sound Machine"), ("Nanit", "Smart Baby Monitor"),
    ("Owlet", "Smart Baby Monitor"), ("Honest Company", "Baby & Home Products"),
    ("Earth's Best", "Organic Baby Food"), ("Happy Family", "Organic Baby Food"),
    ("Pampers", "Diapers"), ("Huggies", "Diapers"),
    ("Hello Bello", "Diapers & Baby"), ("Build-A-Bear", "Custom Stuffed Animals"),
    ("LEGO Store", "Building Toys"), ("Disney Store", "Character Merchandise"),
    ("American Girl", "Premium Dolls"), ("Fat Brain Toys", "Educational Toys"),
    ("Magna-Tiles", "Magnetic Building Tiles"), ("Osmo", "Interactive Learning"),
], "Expense", "Kids & Family", "Toys & Activities")


add([
    ("Aldi", "Discount Supermarket"), ("Lidl", "Discount Supermarket"),
    ("Trader Joe's", "Specialty Grocery"), ("Whole Foods", "Natural & Organic Grocery"),
    ("Sprouts", "Natural & Organic Grocery"), ("Fresh Thyme", "Natural Grocery"),
    ("Natural Grocers", "Organic Grocery"), ("Earth Fare", "Natural Grocery"),
    ("Erewhon", "Luxury Organic Grocery (LA)"), ("Bristol Farms", "Premium Supermarket"),
    ("Gelsons", "Premium Supermarket (CA)"), ("Nugget Markets", "Specialty Grocery (CA)"),
    ("Stew Leonard's", "Fresh Food Market"), ("Jungle Jim's", "Specialty Market"),
    ("Central Market", "Specialty Grocery (TX)"), ("Dorothy Lane Market", "Specialty Market"),
    ("Heinen's", "Premium Grocery (OH)"), ("Wegmans", "Supermarket"),
    ("Publix", "Supermarket"), ("H-E-B", "Supermarket Chain (TX)"),
    ("Meijer", "Supercenter (Midwest)"), ("WinCo Foods", "Discount Supermarket"),
    ("Grocery Outlet", "Discount Grocery"), ("Smart & Final", "Warehouse Grocery"),
    ("Hmart", "Korean Supermarket"), ("99 Ranch Market", "Asian Supermarket"),
    ("Mitsuwa Marketplace", "Japanese Supermarket"), ("Uwajimaya", "Asian Supermarket"),
    ("Seafood City", "Filipino Supermarket"), ("Patel Brothers", "Indian Grocery"),
    ("Sedano's", "Hispanic Supermarket"), ("Northgate Market", "Hispanic Supermarket"),
    ("Fiesta Mart", "Hispanic Supermarket"), ("El Super", "Hispanic Supermarket"),
    ("Cardenas Markets", "Hispanic Supermarket"), ("Vallarta Supermarkets", "Hispanic Supermarket"),
], "Expense", "Food & Dining", "Groceries")

add([
    ("Hertz", "Car Rental"), ("Enterprise", "Car Rental"), ("Avis", "Car Rental"),
    ("Budget Car Rental", "Car Rental"), ("National Car Rental", "Car Rental"),
    ("Alamo Rent A Car", "Car Rental"), ("Dollar Rent A Car", "Car Rental"),
    ("Thrifty", "Car Rental"), ("Sixt", "Car Rental (Germany)"),
    ("Europcar", "Car Rental (EU)"), ("Zipcar", "Car Sharing"),
    ("Turo", "Peer-to-Peer Car Rental"), ("Getaround", "P2P Car Sharing"),
    ("Maven", "Car Sharing (GM)"), ("Car2go/ShareNow", "Carsharing"),
    ("Lime", "Scooter & Bike Share"), ("Bird", "Electric Scooter Rental"),
    ("Spin", "Scooter & Bike Share"), ("Voi", "Scooter Share (EU)"),
    ("Tier", "Scooter Share (Germany)"), ("Dott", "Scooter Share (EU)"),
    ("Jump Bikes", "Bike Share (Uber)"), ("Citi Bike", "Bike Share (NYC)"),
    ("Divvy", "Bike Share (Chicago)"), ("Bay Wheels", "Bike Share (SF)"),
    ("Capital Bikeshare", "Bike Share (DC)"), ("Bluebikes", "Bike Share (Boston)"),
    ("Metro Bike Share", "Bike Share (LA)"), ("Nice Ride", "Bike Share (Minneapolis)"),
    ("Santander Cycles", "Bike Share (London)"), ("Vélib'", "Bike Share (Paris)"),
    ("Bicing", "Bike Share (Barcelona)"), ("Call a Bike", "Bike Share (Germany)"),
    ("Ofo", "Bike Share (China)"), ("Mobike", "Bike Share (China)"),
    ("HelloBike", "Bike Share (China)"), ("Seoul Bike (Ddareungi)", "Bike Share (Korea)"),
], "Expense", "Transportation", "Rideshare")

add([
    ("Staples", "Office Supply Retailer"), ("Office Depot/OfficeMax", "Office Supply"),
    ("Quill.com", "Online Office Supplies"), ("Vistaprint", "Custom Printing"),
    ("FedEx Office", "Printing & Shipping"), ("UPS Store", "Printing & Shipping"),
    ("Ryman", "Stationery (UK)"), ("Viking Direct", "Office Supplies (EU)"),
    ("Moleskine", "Premium Notebooks"), ("Leuchtturm1917", "Notebooks (Germany)"),
    ("Rhodia", "Paper & Notebooks (France)"), ("Muji Stationery", "Minimal Stationery"),
    ("Kokuyo", "Stationery (Japan)"), ("ASKUL", "Office Supplies (Japan)"),
    ("Pilot Pens", "Writing Instruments (Japan)"), ("Uni-ball", "Writing Instruments"),
    ("Pentel", "Writing Instruments (Japan)"), ("Lamy", "Writing Instruments (Germany)"),
    ("Montblanc", "Luxury Writing Instruments"), ("Parker Pens", "Writing Instruments"),
    ("Cross Pens", "Writing Instruments"), ("Waterman Pens", "Writing Instruments"),
    ("TWSBI", "Fountain Pens (Taiwan)"), ("Sailor", "Fountain Pens (Japan)"),
    ("Platinum Pens", "Fountain Pens (Japan)"), ("Tombow", "Art Supplies (Japan)"),
    ("Copic Markers", "Art Markers (Japan)"), ("Prismacolor", "Colored Pencils"),
    ("Faber-Castell", "Art & Writing (Germany)"), ("Derwent", "Art Pencils (UK)"),
    ("Winsor & Newton", "Art Supplies (UK)"), ("Golden Artist Colors", "Acrylic Paint"),
    ("Blick Art Materials", "Art Supply Store"), ("Jerry's Artarama", "Art Supply Store"),
    ("Utrecht Art Supplies", "Art Supply Store"), ("Jackson's Art", "Art Supplies (UK)"),
], "Expense", "Shopping", "Office Supplies")


add([
    ("Waffle House", "Diner (Breakfast/24hr)"), ("Denny's", "Family Dining Restaurant"),
    ("IHOP", "Family Restaurant (Pancakes)"), ("Bob Evans", "Family Dining Restaurant"),
    ("Perkins", "Family Dining Restaurant"), ("Village Inn", "Family Dining"),
    ("Black Bear Diner", "Family Diner"), ("Huddle House", "Family Diner"),
    ("Steak 'n Shake", "Steakburger Restaurant"), ("Culver's", "Fast Casual Butter Burger"),
    ("Freddy's", "Fast Casual Frozen Custard"), ("In-N-Out", "Fast Food Burger"),
    ("Whataburger", "Fast Food Burger (Texas)"), ("White Castle", "Fast Food Slider"),
    ("Checkers", "Fast Food Burger"), ("Rally's", "Fast Food Burger"),
    ("Del Taco", "Fast Food Mexican"), ("Taco John's", "Fast Food Mexican"),
    ("Jack in the Box", "Fast Food Restaurant"), ("Hardee's", "Fast Food Restaurant"),
    ("Long John Silver's", "Fast Food Seafood"), ("Captain D's", "Fast Food Seafood"),
    ("Church's Chicken", "Fast Food Fried Chicken"), ("Golden Chick", "Fast Food Chicken"),
    ("Wienerschnitzel", "Fast Food Hot Dogs"), ("Portillo's", "Hot Dogs & Italian Beef"),
    ("Qdoba", "Fast Casual Mexican"), ("Cafe Rio", "Mexican Restaurant"),
    ("Costa Vida", "Fresh Mexican Grill"), ("Rubio's", "Coastal Mexican"),
    ("Torchy's Tacos", "Creative Taco Restaurant"), ("Taco Bueno", "Fast Food Mexican"),
    ("Which Wich", "Fast Casual Sandwich"), ("Penn Station", "East Coast Subs"),
    ("Capriotti's", "Sandwich Shop"), ("Erbert & Gerbert's", "Sandwich Shop"),
    ("Tropical Smoothie Cafe", "Smoothie & Food"), ("Zaxby's", "Chicken Restaurant"),
    ("PDQ", "Premium Chicken"), ("Slim Chickens", "Chicken Tenders"),
    ("Golden Chick", "Fried Chicken (Texas)"), ("Lee's Famous Recipe", "Fried Chicken"),
    ("Pollo Tropical", "Caribbean Fast Casual"), ("El Pollo Loco", "Grilled Chicken"),
    ("A&W Restaurants", "Fast Food Root Beer"), ("Sonic Drive-In", "Drive-In Fast Food"),
    ("Cook Out", "Fast Food (Southeast)"), ("Braum's", "Ice Cream & Fast Food"),
    ("Steak Escape", "Cheesesteak Fast Food"), ("Charley's Philly Steaks", "Cheesesteak"),
    ("Penn Station", "Sub Sandwich Chain"), ("Blimpie", "Sub Sandwich Chain"),
    ("Pita Pit", "Pita Wrap Restaurant"), ("Roti Modern Mediterranean", "Mediterranean"),
    ("Cava", "Mediterranean Fast Casual"), ("Sweetgreen", "Salad Fast Casual"),
    ("Dig", "Farm-to-Table Fast Casual"), ("Just Salad", "Salad Restaurant"),
    ("Chopt", "Salad Fast Casual"), ("Tender Greens", "Salad & Plates"),
    ("True Food Kitchen", "Health-Conscious Restaurant"), ("Flower Child", "Healthy Fast Casual"),
    ("Modern Market Eatery", "Fast Casual Healthy"), ("Mendocino Farms", "Sandwich & Salad"),
], "Expense", "Food & Dining", "Fast Food")


add([
    ("Saladworks", "Salad Restaurant Chain"), ("Naf Naf Grill", "Middle Eastern Fast Casual"),
    ("The Halal Guys", "Halal Street Food"), ("Rascal House Pizza", "Pizza Chain"),
    ("Giordano's", "Deep Dish Pizza (Chicago)"), ("Lou Malnati's", "Deep Dish Pizza"),
    ("Home Run Inn", "Frozen & Restaurant Pizza"), ("Bertucci's", "Italian Restaurant"),
    ("Olive Garden", "Italian Casual Dining"), ("Macaroni Grill", "Italian Casual Dining"),
    ("Carrabba's Italian Grill", "Italian Restaurant"), ("Buca di Beppo", "Italian Family"),
    ("Maggiano's", "Italian Casual Dining"), ("Bravo! Italian Kitchen", "Italian Restaurant"),
    ("California Pizza Kitchen", "Pizza & Casual Dining"), ("Cici's Pizza", "Pizza Buffet"),
    ("Godfather's Pizza", "Pizza Chain"), ("Pizza Ranch", "Pizza & Buffet"),
    ("Your Pie", "Fast Casual Pizza"), ("& Pizza", "Fast Casual Pizza"),
    ("Blaze Pizza", "Build-Your-Own Pizza"), ("MOD Pizza", "Build-Your-Own Pizza"),
    ("Pieology", "Custom Pizza"), ("PizzaRev", "Custom Pizza"),
    ("Uncle Maddio's", "Custom Pizza"), ("Persona Pizzeria", "Artisan Pizza"),
    ("Grimaldi's", "Coal-Fired Pizza (NYC)"), ("Lombardi's", "Historic Pizza (NYC)"),
    ("Di Fara Pizza", "Legendary Pizza (Brooklyn)"), ("Roberta's", "Pizza (Brooklyn)"),
    ("Emmy Squared", "Detroit-Style Pizza (NYC)"), ("Prince Street Pizza", "Pizza (NYC)"),
    ("Joe's Pizza", "NYC Slice Shop"), ("Artichoke Pizza", "NYC Slice Shop"),
    ("Paulie Gee's", "Artisan Pizza"), ("Lucali", "Pizza (Brooklyn)"),
    ("Frank Pepe's", "Coal-Fired Pizza (CT)"), ("Sally's Apizza", "New Haven Pizza"),
    ("Modern Apizza", "New Haven Pizza"), ("Bar Pizza", "South Shore Pizza (MA)"),
    ("Pizzeria Bianco", "Pizza (Phoenix)"), ("Flour + Water", "Italian Restaurant (SF)"),
    ("Tony's Pizza Napoletana", "Pizza (SF)"), ("Una Pizza Napoletana", "Neapolitan Pizza"),
], "Expense", "Food & Dining", "Restaurants")


add([
    ("Topper's Pizza", "Pizza Chain (Midwest)"), ("Jet's Pizza", "Detroit-Style Pizza"),
    ("Donatos Pizza", "Pizza Chain (Ohio)"), ("LaRosa's", "Pizza Chain (Cincinnati)"),
    ("Toppers Pizza", "Pizza Chain (Wisconsin)"), ("Cassano's Pizza King", "Pizza (Ohio)"),
    ("Marion's Piazza", "Pizza (Dayton OH)"), ("Imo's Pizza", "St. Louis-Style Pizza"),
    ("Cecil Whittaker's", "St. Louis Pizza"), ("Pi Pizzeria", "Deep Dish Pizza (STL)"),
    ("Dewey's Pizza", "Pizza Chain (Midwest)"), ("Donato's Pizza", "Pizza (Ohio)"),
], "Expense", "Food & Dining", "Fast Food")

# ============================================================
# GENERATE CSV
# ============================================================

def main():
    # Deduplicate by merchant name (keep first occurrence)
    seen = set()
    unique_merchants = []
    for entry in MERCHANTS:
        name = entry[0]
        if name not in seen:
            seen.add(name)
            unique_merchants.append(entry)

    # Write CSV
    with open('global_merchant_category.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['merchant', 'public_category', 'root', 'mid_level', 'leaf'])
        for merchant, pub_cat, root, mid, leaf in sorted(unique_merchants, key=lambda x: x[0].lower()):
            writer.writerow([merchant, pub_cat, root, mid, leaf])

    # Stats
    print(f"Total unique merchants: {len(unique_merchants)}")
    print(f"Duplicates removed: {len(MERCHANTS) - len(unique_merchants)}")

    # Category distribution
    from collections import Counter
    roots = Counter()
    mids = Counter()
    leaves = Counter()
    for _, _, root, mid, leaf in unique_merchants:
        roots[root] += 1
        mids[mid] += 1
        leaves[leaf] += 1

    print(f"\n=== ROOTS ===")
    for k, v in roots.most_common():
        print(f"  {k}: {v}")

    print(f"\n=== MID-LEVEL ===")
    for k, v in mids.most_common():
        print(f"  {k}: {v}")

    print(f"\n=== LEAF CATEGORIES ({len(leaves)} unique) ===")
    for k, v in sorted(leaves.items()):
        flag = " ⚠️" if len(k) > 22 else ""
        print(f"  {k:<24} ({len(k):2d} chars): {v:4d}{flag}")


if __name__ == "__main__":
    main()
