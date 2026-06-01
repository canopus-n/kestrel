"""
Generate merchant_category.csv mapping each merchant to a 3-level hierarchy.
Root levels: Expense, Income
"""
import csv

# Merchant -> (root, mid, leaf) mapping
# Leaf categories are kept to ~20 chars
CATEGORIES = {}

# Helper to bulk assign
def assign(merchants, root, mid, leaf):
    for m in merchants:
        CATEGORIES[m] = (root, mid, leaf)

# ============================================================
# FOOD & DINING
# ============================================================

# Groceries
assign([
    "ACME", "ACME Markets", "ALDI", "Albert Heijn", "Albertsons",
    "APNA BAZAR", "BHAVANI FARMERS MARKET", "Big Basket", "Big C",
    "Biedronka", "Billa", "BJ's Wholesale Club", "Bravo", "Carrefour",
    "Chedraui", "Cold Storage", "Coles", "Coop", "Costco", "COSTCO",
    "Coto", "Countdown", "Coop", "EDEKA", "E-Mart", "Exito",
    "Extra", "FairPrice", "Fairprice", "Food 4 Less", "Food Lion",
    "Føtex", "Giant", "Giant Eagle", "Globus", "H-E-B", "Hannaford",
    "Harris Teeter", "Hemköp", "Hy-Vee", "ICA", "IGA", "Indomaret",
    "Ingles Market", "Intermarché", "Jewel-Osco", "Jumbo", "Kaufland",
    "Kroger", "Lawson", "Leclerc", "Lidl", "Loblaws", "Lotte Mart",
    "LOTTE PLAZA", "Lulu Hypermarket", "Magnit", "Maxi", "Meijer",
    "Mercadona", "Metro", "Migros", "Ministop", "Monoprix", "Morrisons",
], "Expense", "Food & Dining", "Groceries")


assign([
    "Netto", "OXXO", "ParknShop", "Pão de Açúcar", "Perekrestok",
    "Pick n Pay", "Price Chopper", "Publix", "Ralphs", "Rema 1000",
    "REWE", "Safeway", "Sainsbury's", "Save A Lot", "Schnucks",
    "Shoppers Drug Mart", "ShopRite", "SHOPRITE", "Shufersal",
    "Sobeys", "Soriana", "SPAR", "Spinneys", "SPROUTS FARMERS MARKET",
    "Sprouts", "Stop & Shop", "STOP & SHOP", "SUBZI MANDI",
    "SAMAHA'S FARM", "SAMAHA`S FARM", "Tesco", "Tesco Lotus",
    "Trader Joe's", "Union Coop", "Vons", "Waitrose", "Wegmans",
    "WEGMANS", "Weis Markets", "Wellcome", "Whole Foods", "WHOLE FOODS",
    "Winn Dixie", "Winn-Dixie", "Woolworths", "A101",
    "PATEL BROTHERS", "STAR BAZAAR", "AT YOUR CONVENIENCE",
    "FamilyMart", "7-Eleven", "Cumberland Farms", "Casey's General Store",
    "Kwik Trip", "Kwik-E-Mart", "Stewart's Shops",
    "Holiday Station Stores", "QUICK CHEK",
], "Expense", "Food & Dining", "Groceries")

# Fast Food
assign([
    "Arby's", "Bojangles", "Burger King", "Carl's Jr.",
    "Chick-fil-A", "Culver's", "Culvers", "Domino's", "DOMINO'S",
    "El Pollo Loco", "Firehouse Subs", "Five Guys", "In-N-Out Burger",
    "Jack in the Box", "Jimmy John's", "KFC", "Krispy Kreme",
    "Little Caesars", "McDonald's", "MCDONALD'S", "Moe's Southwest Grill",
    "Noodles & Company", "Papa John's", "PAPA JOHN'S", "Panda Express",
    "Panda", "Pizza Hut", "Popeyes", "Quiznos", "Raising Cane's",
    "Raising Canes", "SBARRO", "Schlotzsky's", "Shake Shack",
    "Sonic Drive In", "Subway", "Taco Bell", "TACO BELL", "Taco 911",
    "Taco Fiesta", "Wendy's", "WENDY'S", "Whataburger", "Wingstop",
    "Zaxby's", "Burger Bliss", "SMASHVILLE HOT CHICKEN",
    "ROUND PIE PIZZA", "THE PIZZERIA", "SALERNOS PIZZERIA",
    "Jaans Pizza", "Mighty Pizza", "Pizza Paradise",
    "DOORDASH CROWN FRIED CHICKEN", "ROYAL CHICKEN",
    "GERMAN DONER KEBAB", "CHIPOTLE", "Chipotle",
], "Expense", "Food & Dining", "Fast Food")


# Restaurants
assign([
    "AUBONPAIN", "Applebee's", "BAITHAKH RESTAURANT", "Bratwurst Haus",
    "CHARRITOS", "CHEESECAKE FACTORY", "Corner Bakery Cafe",
    "Cracker Barrel", "Einstein Bros Bagels", "FLAME KABOB",
    "GYRO", "Gyros Galore", "HALAL EATZ", "IBBY'S FALAFEL",
    "IHOP", "Jason's Deli", "Jersey Mike's", "GRUBHUB JERSEY MIKES",
    "KABAB PARADISE", "KANDAHAR", "KARAHI HOUSE", "Kebab King Istanbul",
    "LA CONTESSA", "LAHORE RESTAURANT", "MAZA RESTAURANTS",
    "McAlister's Deli", "N THAI", "Olive Garden", "Panera Bread",
    "Pasta Paradise", "Paella Paradise", "Pierogi Palace",
    "Potbelly Sandwich Shop", "Poutine Paradise",
    "RAAVI NAAN KABAB", "RIFFYS KITCHEN", "Schnitzel Haus",
    "Schnitzel Shack", "SHAAN GRILL", "Sizzling Szechuan",
    "Spicy Ramen", "Sushi Sensation", "Sushi Supreme",
    "Tapas Bar", "Tapas Town", "TERMINAL 9 GRILL",
    "Texas Roadhouse", "THE HALAL CRAVE", "TGI Fridays",
    "THE ANCHOR FISH", "TURKUAZ RESTAURANT", "TURNING POINT",
    "GOOD FOOD BY UZMA", "GRUBHUB GOOD FOOD BY UZMA",
    "ZAIKA BBQ", "Falafel Feast", "Currywurst Corner",
    "Fish and Chips", "DOORDASH KANDAHAR", "DOORDASH KHOKHA",
    "DOORDASH RIFFYS KITCHEN", "DOORDASH ROUND PIE PIZZA",
    "GRUBHUB ROUND PIE PIZZA", "GRUBHUB MCDONALDS",
    "DOORDASH MCDONALDS", "Food Truck",
], "Expense", "Food & Dining", "Restaurants")

# Coffee & Tea
assign([
    "Starbucks", "STARBUCKS", "Peet's Coffee", "MDC PEETS",
    "Dunkin' Donuts", "DUNKIN", "DOORDASH DUNKIN", "DAVIDsTEA",
    "Local Coffee Brewery", "Coffee Haven", "REFRESH TEA", "TEN TEA",
], "Expense", "Food & Dining", "Coffee & Tea")


# Bakery & Desserts
assign([
    "ABBATE BAKERY", "BAKED BY MELISSA", "Boulangerie Baguette Magique",
    "Boulangerie Fougasse", "Boulangerie Le Petit Pain",
    "Boulangerie Pain au Chocolat", "Boulangerie Pain aux Cereales",
    "Boulangerie Pain aux Figues", "Boulangerie Pain aux Graines",
    "Boulangerie Pain aux Noix", "Boulangerie Pain aux Olives",
    "Boulangerie Pain aux Raisins", "Boulangerie Pain de Campagne",
    "Boulangerie Pain de Seigle", "Boulangerie Patisserie Artisanale",
    "Cinnabon", "CINNABON-CARVEL", "LA BON BAKE SHOPPES",
    "Patisserie Chocolaterie Delice", "Patisserie Chouquette",
    "Patisserie Eclair", "Patisserie Financier",
    "Patisserie Gateaux Divins", "Patisserie Macaron",
    "Patisserie Madeleine", "Patisserie Mille-Feuille",
    "Patisserie Opera Cake", "Patisserie Palmier",
    "Patisserie Paris-Brest", "Patisserie Religieuse",
    "Patisserie Saint Honore", "Positive Bakery",
    "ROSETTA BAKERY", "Wetzel's Pretzels", "AUNTIE ANNE'S",
    "Auntie Anne's",
], "Expense", "Food & Dining", "Bakery & Desserts")

# Ice Cream & Yogurt
assign([
    "Baskin Robbins", "Cold Stone Creamery", "COLD STONE",
    "Dairy Queen", "Frozen Yogurt", "Gelato Dreams",
    "Gelateria Artigianale", "ICE CREAM MONSTER", "ICECREAM TRUCK",
    "ICY MELON", "JOYCE CREAMERY", "Menchie's", "Orange Leaf",
    "Pinkberry", "Red Mango", "SWEET ICE CREAMERY", "Sweet Frog",
    "TCBY", "Tutti Frutti", "Yogen Früz", "Yogurt City",
    "Yogurt Mountain", "Yogurt World", "Yogurt Zone", "Yogurtland",
    "SUNDAES INTERNATIONAL",
], "Expense", "Food & Dining", "Ice Cream & Yogurt")

# Food Delivery
assign([
    "DoorDash", "DOORDASH CROWN FRIED CHICKEN", "Deliveroo",
    "Foodora", "Foodpanda", "Glovo", "GrubHub", "Grubhub",
    "Instacart", "Jumia Food", "Just Eat", "Postmates",
    "Rappi", "Seamless", "Skip The Dishes", "Swiggy",
    "Takeaways", "Talabat", "UBR POSTMATES", "Uber Eats",
    "UBER EATS", "Wolt", "Zomato", "Caviar",
], "Expense", "Food & Dining", "Food Delivery")


# Snacks & Drinks
assign([
    "JUICE AND DESSERT", "Jamba Juice", "Smoothie King",
    "REAL FRUIT BUBBLE", "KING SWEETS", "SHALIMAR SWEETS",
    "GERTRUDE HAWK CHOCOLATE", "POTATO PALOOZA",
    "FERRERO ROCHER", "Ferrero Rocher",
], "Expense", "Food & Dining", "Snacks & Drinks")

# ============================================================
# TRANSPORTATION
# ============================================================

# Gas & Fuel
assign([
    "BP", "Chevron", "CITGO", "Citgo", "CONOCO", "Conoco",
    "COSTCO GAS", "Exxon Mobil", "EXXON MOBIL", "Marathon",
    "PHILLIPS 66", "Phillips 66", "Pilot Travel", "RaceTrac",
    "QuikTrip", "SHELL OIL", "Shell", "SPEEDWAY", "Speedway",
    "SUNOCO", "Sunoco", "Texaco", "Valero",
    "Love's Travel Stops", "Maverik", "Sheetz", "Wawa", "WAWA",
], "Expense", "Transportation", "Gas & Fuel")

# Rideshare
assign([
    "Bolt", "Cabify", "Careem", "DiDi", "Gett", "Gojek",
    "Grab", "Kakao T", "Lyft", "Mytaxi", "Ola", "Taxify",
    "Uber", "UBER",
], "Expense", "Transportation", "Rideshare")

# Public Transit
assign([
    "NJ TRANSIT", "NEW JERSEY E-ZPASS", "NJ EZPASS",
], "Expense", "Transportation", "Public Transit")

# Tolls & Parking
assign([
    "SPOTHERO",
], "Expense", "Transportation", "Tolls & Parking")

# Car Service & Parts
assign([
    "Advance Auto Parts", "AutoZone", "CIRCLE CHEVROLET",
    "DCH ACADEMY HONDA", "HONDA", "HYUNDAI BLUE LINK",
    "HYUNDAI SERVICE", "NRS Tint Shop", "PEP BOYS",
    "REYDEL VOLKSWAGEN", "Volkswagen", "XPEL",
], "Expense", "Transportation", "Car Service & Parts")


# ============================================================
# SHOPPING
# ============================================================

# General Retail
assign([
    "AMAZON.COM", "Amazon", "AMAZON DIGITAL", "Costco",
    "Dollar General", "DOLLAR GENERAL", "Dollar Tree", "DOLLAR TREE",
    "DOLLARTREE", "DOLLARS N THINGS", "A DOLLAR", "A-Z DOLLAR",
    "M CITY DOLLAR", "FAMILY DOLLAR", "Family Dollar",
    "FIVE BELOW", "MARSHALLS", "Marshalls", "HOMEGOODS",
    "Overstock", "Ross", "T.J. Maxx", "Target", "TARGET",
    "Walmart", "WALMART", "PAYPAL WALMART", "Wayfair",
    "Wish", "eBay", "Ali Express", "AMERICAN DREAM MALL",
    "MINISO", "Etsy", "ETSY",
], "Expense", "Shopping", "General Retail")

# Clothing & Apparel
assign([
    "Abercrombie & Fitch", "Adidas", "Aerie", "American Eagle",
    "Anthropologie", "Balenciaga", "Banana Republic", "Birkenstock",
    "Bulgari", "BURLINGTON STORES", "Canada Goose", "Coach",
    "Crocs", "Dior", "Dolce & Gabbana", "Express", "Fendi",
    "Ferrari Store", "Forever 21", "Fossil", "Gap", "Gucci",
    "H & M", "H&M", "Hollister", "J. Crew", "J.Crew",
    "JCPenney", "Kohl's", "KOHL'S", "L.L.Bean", "Louis Vuitton",
    "Lululemon", "Mango", "New Balance", "Nike", "Nordstrom",
    "Old Navy", "OLD NAVY", "Prada", "PUMA", "Ralph Lauren",
    "Reebok", "Revolution Clothing", "Skechers", "Ted Baker",
    "The North Face", "Tiffany's", "Tissot", "Tommy Hilfiger",
    "Under Armour", "Uniqlo", "Vans", "Yves Saint Laurent",
    "Zara", "ZGMYC Fashion Leopard", "Omega", "Zappos",
    "FILA", "FIT N FEET", "FLYNN & O HARA",
    "KIDS FOOT LOCKER", "Foot Locker", "Cartier",
], "Expense", "Shopping", "Clothing & Apparel")

# Electronics
assign([
    "Acer", "AMD", "Apple", "APPLE", "ASUS", "B&H PHOTO",
    "Beats", "BenQ", "Best Buy", "BESTBUY", "Bose", "Canon",
    "Dell", "DJI", "Ford", "HP", "Intel", "Lenovo", "LG",
    "MACSALES.COM", "Mattel", "Microsoft", "MSI", "Netgear",
    "NVIDIA", "OTHER WORLD COMPUTING", "Qualcomm", "Razer",
    "Samsung", "Sony", "TESLA", "Tesla",
], "Expense", "Shopping", "Electronics")


# Home & Garden
assign([
    "Abagail Furniture", "Ace Hardware", "ANDERSEN WINDOWS",
    "BED BATH & BEYOND", "Bed Bath & Beyond", "HOME DEPOT",
    "Home Depot", "IKEA", "LOWES", "Lowe's", "Pottery Barn",
    "YANKEE CANDLE", "ARCTIC AIR", "GUARDIAN TECHNOLOGIES",
    "CRYSTAL SPRINGS", "DS SERVICES", "PRIMO WATER",
    "HandyTools", "RangeShop",
], "Expense", "Shopping", "Home & Garden")

# Sporting Goods
assign([
    "Academy", "Bass Pro Shops", "Dick's Sporting Goods",
    "DICK'S CLOTHING & SPORT", "Hibbett Sports", "RTIC Outdoors",
    "Salty Crew", "Sports Authority", "Sports Store",
    "TEAM EXPRESS", "LS SKATE PRO INC.",
], "Expense", "Shopping", "Sporting Goods")

# Office Supplies
assign([
    "Office Depot", "Staples", "STAPLES",
], "Expense", "Shopping", "Office Supplies")

# Online Marketplace
assign([
    "Groupon", "StubHub", "Wish", "Overstock",
], "Expense", "Shopping", "Online Marketplace")

# Pet Supplies
assign([
    "Chewy", "Petco", "PetSmart",
], "Expense", "Shopping", "Pet Supplies")

# Books & Media
assign([
    "Audible", "Barnes & Noble", "BARNES & NOBLE",
    "Books-A-Million", "Goodreads", "Scholastic",
    "SCHOLASTIC BOOK FAIRS",
], "Expense", "Shopping", "Books & Media")

# Luxury & Jewelry
assign([
    "Waldorf Astoria",
], "Expense", "Shopping", "Luxury & Jewelry")

# Discount Stores
assign([
    "PARTY CITY", "Party City",
], "Expense", "Shopping", "Discount Stores")


# ============================================================
# ENTERTAINMENT
# ============================================================

# Streaming Video
assign([
    "AMAZON PRIME VIDEO", "AMAZON PRIME", "BritBox", "Cinemax",
    "Criterion Channel", "Crunchyroll", "DISNEY PLUS", "Disney+",
    "Discovery+", "ESPN", "Fubo", "Funimation", "HBO",
    "Hulu", "MUBI", "Netflix", "NETFLIX.COM", "Paramount+",
    "Peacock", "Philo", "Plex", "Prime Video", "Roku",
    "Showtime", "Shudder", "Sling TV", "Starz", "Sundance Now",
    "Tubi", "Vimeo", "Vudu", "YouTube", "GOOGLE YOUTUBE",
], "Expense", "Entertainment", "Streaming Video")

# Streaming Music
assign([
    "Spotify", "Tidal",
], "Expense", "Entertainment", "Streaming Music")

# Gaming
assign([
    "Activision", "Electronic Arts", "GameStop", "Gamestop",
    "Nintendo", "PlayStation", "Xbox Live", "Twitch",
    "Discord",
], "Expense", "Entertainment", "Gaming")

# Movies & Events
assign([
    "AMC", "Broadway", "CINEMARK", "CONDOCERTS",
    "RCMH FOOD & MERCH", "Ticketmaster", "TICKETMASTER",
    "NYC FILM LAB",
], "Expense", "Entertainment", "Movies & Events")

# Amusement & Parks
assign([
    "BEAR MOUNTAIN", "CHILDREN'S MUSEUM", "CRAYOLA EXPERIENCE",
    "ESCAPOLOGY", "HERITAGE AMUSEMENT", "JENKINSON'S AQUARIUM",
    "JENKINSON'S CANDY", "JENKINSON'S PAVILLION",
    "LEGOLAND DISCOVERY", "LIBERTY SCIENCE CENTER",
    "LUMINOCITY", "PLAYLAND", "ROCK N AIR ADVENTURE",
    "Space Needle", "URBAN AIR", "FUN KIDS TRAIN",
    "FANTASY RIDE", "AIR PLAY", "SWING LOOSE",
], "Expense", "Entertainment", "Amusement & Parks")

# Sports & Recreation
assign([
    "Gulfstream Park", "NFL Shop", "MONMOUTH COUNTY PARK",
    "OLD BRIDGE PARK", "SPRING LAKE COMMUNITY",
    "NEW JERSEY TITANS HOCKEY",
], "Expense", "Entertainment", "Sports & Recreation")


# ============================================================
# TRAVEL
# ============================================================

# Airlines
assign([
    "Alaska Airlines", "Allegiant Air", "American Airlines",
    "Delta Air Lines", "ETIHAD AIRWAYS", "Frontier Airlines",
    "Hawaiian Airlines", "JetBlue", "QATAR AIRWAYS", "SAS",
    "Southwest Airlines", "Spirit Airlines", "United Airlines",
], "Expense", "Travel", "Airlines")

# Hotels & Lodging
assign([
    "Airbnb", "Best Western", "COMFORT INNS", "COURTYARD BY MARRIOT",
    "Four Seasons", "Grand Hyatt", "HAMPTON INNS", "Hilton",
    "Hilton Garden Inn", "Hyatt", "Hyatt Regency",
    "Intercontinental", "Mandarin Oriental", "Marriott",
    "Park Hyatt", "Peninsula Hotel", "Ritz-Carlton", "Shangri-La",
    "Sheraton", "Sofitel", "St. Regis", "W Hotel", "Waldorf Astoria",
    "Westin",
], "Expense", "Travel", "Hotels & Lodging")

# Travel Booking
assign([
    "Booking.com", "EXPEDIA", "Expedia",
], "Expense", "Travel", "Travel Booking")

# Car Rental
assign([
    "Hertz",
], "Expense", "Travel", "Car Rental")

# ============================================================
# HEALTH & WELLNESS
# ============================================================

# Medical & Dental
assign([
    "BARNABAS HEALTH", "BAYSHORE OPHTHALMOLOGY",
    "FRANK LIPMAN, M.D.", "FUSION REHABILITATIVE",
    "HOCH ORTHODONTICS", "IMAMIA MEDICS",
    "JERSEY COAST NEPHROLOGY", "KIDZDENT", "MINUTE CLINIC",
    "ORAL SURGERY GROUP", "QUEST DIAGNOSTICS",
    "RMG PEDIATRICS", "SERENITY DENTAL",
    "WOODBRIDGE INTERNAL MEDICINE",
], "Expense", "Health & Wellness", "Medical & Dental")

# Pharmacy
assign([
    "CVS", "Rite Aid", "Walgreens", "WALGREENS", "Boots",
], "Expense", "Health & Wellness", "Pharmacy")

# Fitness & Gym
assign([
    "LA FITNESS", "Peloton", "YMCA", "Yoga Studio",
    "Zumba Power Gym", "TEAM BEACHBODY",
], "Expense", "Health & Wellness", "Fitness & Gym")

# Beauty & Spa
assign([
    "AAINA BEAUTY PARLOR", "Bath & Body Works", "Birchbox",
    "CELINES SPA", "D'BELLA SALON", "HEAD OVER HEELS",
    "HUMA BEAUTY SALON", "MASSAGE ENVY", "MASSAGELUXE",
    "Sephora", "SEPHORA.COM", "Ulta Beauty", "ULTA",
    "ZARA SALON", "J & G SALON",
], "Expense", "Health & Wellness", "Beauty & Spa")

# Health Products
assign([
    "3X4 GENETICS", "3X4GENETICS", "CRI GENETICS",
    "EUVEXIA", "FATTY15", "FOREVER LIVING", "FULLSCRIPT",
    "HOLISTIC HEALTH LABS", "LEVELS", "Omron", "OURA RING INC.",
    "SENSATE",
], "Expense", "Health & Wellness", "Health Products")


# ============================================================
# HOUSING & UTILITIES
# ============================================================

# Utilities
assign([
    "Comcast", "NEW JERSEY NATURAL GAS", "OPTIMUM",
    "VONAGE",
], "Expense", "Housing & Utilities", "Utilities")

# Insurance
assign([
    "GEICO", "RENTERS/CONDO INSURANCE",
], "Expense", "Housing & Utilities", "Insurance")

# Home Services
assign([
    "ALL CITY ELECTRICAL", "DIVINE TOUCH CLEANERS",
    "ECOSHIELD", "GLOBAL PLUMBING", "GLOW EXPRESS CAR WASH",
    "OXFORD CONTRACTING",
], "Expense", "Housing & Utilities", "Home Services")

# Telecom & Internet
assign([
    "ALTICEMOBILE.COM", "AT&T", "T-MOBILE", "VERIZON",
    "VERIZON WIRELESS",
], "Expense", "Housing & Utilities", "Telecom & Internet")

# ============================================================
# EDUCATION
# ============================================================

# Tuition & School
assign([
    "DIOCESE OF TRENTON", "EDMENTUM", "EXL PREP",
    "JOSTENS INC.", "MIDDLESEX COUNTY COLLEGE",
    "PAYPAL JAFARIA SCHOOOL", "ST JOHN VIANNEY HIGH SCHOOL",
    "ST JOHN'S NURSERY SCHOOL", "ST. BENEDICT", "ST.BENEDICT",
    "BNL SCHOOL PICTURES", "CODE NINJAS",
    "RAZ SPARDHA LEARNINGS",
], "Expense", "Education", "Tuition & School")

# Online Learning
assign([
    "BRILLIANT.ORG", "Chegg", "IXL", "KHAN ACADEMY",
    "KHANACADEMY", "LEARNER.COM", "LEETCODE.COM",
    "VARSITYTUTORS",
], "Expense", "Education", "Online Learning")

# ============================================================
# FINANCIAL SERVICES
# ============================================================

# Banking Fees
assign([
    "ALLY", "ATB", "BANK OF AMERICA", "Clearbanks",
    "HDFC BANK LTD.", "FIDELITY",
    "THE DEPOSITORY TRUST & CLEARING CORP.",
], "Expense", "Financial Services", "Banking Fees")

# Lending & Loans
assign([
    "SOFI LENDING", "APPRAISAL FEE SERVICES",
], "Expense", "Financial Services", "Lending & Loans")

# Investment
assign([
    "Acorn", "MOTLEY.FOOL.COM",
], "Expense", "Financial Services", "Investment")


# ============================================================
# TECHNOLOGY
# ============================================================

# Software & SaaS
assign([
    "Adobe", "Atlassian", "Autodesk", "Canva", "Cisco",
    "Datorama", "DocuSign", "Dropbox", "Evernote", "GitHub",
    "GoDaddy", "GOOGLE", "Google", "Grammarly", "GRAMMARLY",
    "Intuit", "JetBrains", "LinkedIn", "OPENAI", "Oracle",
    "ProtonMail", "Salesforce", "Slack", "Snowflake", "Splunk",
    "Squarespace", "VMware", "Workday", "Zscaler", "ZOOM", "Zoom",
    "IBM", "Akamai",
], "Expense", "Technology", "Software & SaaS")

# VPN & Privacy
assign([
    "Avast", "CyberGhost", "CyberGhost VPN", "ExpressVPN",
    "GhostPath", "GhostVPN", "HideMyAss", "HotSpot Shield",
    "IPVanish", "LastPass", "Dashlane", "Mullvad", "NordVPN",
    "Private Internet Access", "PrivateVPN", "ProtonVPN",
    "PureVPN", "SaferVPN", "StrongVPN", "Surfshark",
    "TorGuard", "Trust.Zone", "TunnelBear", "VPN Unlimited",
    "VPNArea", "VPNSecure", "VyprVPN", "Windscribe", "ZenMate",
], "Expense", "Technology", "VPN & Privacy")

# Cloud & Security
assign([
    "Acorn",
], "Expense", "Technology", "Cloud & Security")

# Hardware
assign([
    "ICOM", "Borg Warner",
], "Expense", "Technology", "Hardware")

# ============================================================
# DONATIONS & GIFTS
# ============================================================

# Charity & Donations
assign([
    "ACTBLUE STACEY.ABRAMS", "ACTBLUE VOTE.ORG", "CHANGE.ORG",
    "GIRL SCOUTS", "JUSTGIVING.COM", "RACE REGISTER DONATIONS",
    "THE NATIONAL SOCIETY",
], "Expense", "Donations & Gifts", "Charity & Donations")

# Gifts & Cards
assign([
    "CARDMART", "ZOLA.COM", "Shutterfly",
], "Expense", "Donations & Gifts", "Gifts & Cards")


# ============================================================
# KIDS & FAMILY
# ============================================================

# Toys & Activities
assign([
    "KUUQA Kids Art", "SNAPOLOGY", "THE CHILDREN'S PLACE",
    "THE HOBBY", "TOYS STOP", "Toys R Us",
    "Bob's Hobbies", "Hobby Store",
], "Expense", "Kids & Family", "Toys & Activities")

# Childcare
assign([
    "PRESCHOOL SMILES",
], "Expense", "Kids & Family", "Childcare")

# ============================================================
# PERSONAL SERVICES
# ============================================================

# Photography
assign([
    "DWAYNES PHOTO", "PICTURE PEOPLE", "TEDDYBEARPORTRAITS.COM",
], "Expense", "Personal Services", "Photography")

# Printing & Shipping
assign([
    "937 Printshop", "FEDEX", "USPS", "LULU.COM",
    "WRITTEN OUT LOUD",
], "Expense", "Personal Services", "Printing & Shipping")

# Auto & Vehicle
assign([
    "TOWNSHIP OF OLD BRIDGE", "NJ GOV", "NJ MOTOR VEHICLE",
], "Expense", "Personal Services", "Gov & DMV")

# ============================================================
# SUBSCRIPTION SERVICES
# ============================================================

assign([
    "AMAZON PRIME", "Birchbox", "GUM.CO", "KINDLE",
    "New York Times", "Proactive", "SUPERSUMMARY",
    "WINXDVD.COM", "MISEN",
], "Expense", "Subscriptions", "Media & Lifestyle")

# ============================================================
# FOOD - remaining halal/ethnic
# ============================================================

assign([
    "EMIR HALAL", "MARS HALAL", "SHAHNAWAZ HALAL MEAT.",
    "SHALIMAR HALAL MEAT", "SHILLEH HALAL",
    "ROBAAZ",
], "Expense", "Food & Dining", "Groceries")

# Misc food/candy
assign([
    "JENKINSON'S CANDY", "GOLDIE LOX",
    "MDC WENDYS", "MDM JERRYS",
], "Expense", "Food & Dining", "Fast Food")


# ============================================================
# INCOME
# ============================================================

assign([
    "PAYMENT", "ATM Withdrawal",
], "Income", "Transfers", "Bank Transfer")

assign([
    "NBPA", "Hukn", "Mpon", "ADLB", "CMS", "SM",
    "RCCA", "CTM GROUP INC.", "LMXAC", "RFC MENLO PARK",
    "R Bailey",
], "Income", "Transfers", "Deposit")

# ============================================================
# Remaining misc merchants
# ============================================================

# Crypto
assign([
    "THE CRYPTO MERCHANT",
], "Expense", "Financial Services", "Crypto & Trading")

# Water/beverage delivery
assign([
    "NAYAX VENDING",
], "Expense", "Food & Dining", "Snacks & Drinks")

# Misc retail brands mapped above or catch-all
assign([
    "CLAIRE'S", "Michaels", "MICHAELS", "LOVELY",
], "Expense", "Shopping", "General Retail")

# Art & Creative
assign([
    "ARC STUDIO",
], "Expense", "Entertainment", "Arts & Hobbies")

# Misc services and remaining
assign([
    "NOMURA", "NOMURA CAF\xe9", "NOMURA CAF\ufffd", "WAVE HOSPITALITY",
    "SHOWCASE", "VFS SERVICES", "SUBMITTABLE",
    "LAAM TECHNOLOGIES", "MAZUMDER ENTERTAINMENT",
    "RAVE", "Bingo",
], "Expense", "Entertainment", "Movies & Events")

assign([
    "NORDMARK PURE", "NORDIC PURE",
], "Expense", "Shopping", "Home & Garden")

assign([
    "MEAL MAGIC",
], "Expense", "Food & Dining", "Restaurants")

# More remaining
assign([
    "Jerry's PC Enterprise", "Jerico's Dairy",
], "Expense", "Shopping", "General Retail")

assign([
    "Oh Happy Day",
], "Expense", "Entertainment", "Movies & Events")

# Fix auto-categorized merchants
assign([
    "ASDA", "Auchan", "CONAD", "Circle K", "Sam's Club", "Thorntons", "Tinex",
], "Expense", "Food & Dining", "Groceries")

assign([
    "Asos", "CHAMPION", "Macy's", "Pandora",
], "Expense", "Shopping", "Clothing & Apparel")

assign([
    "Curiosity Stream",
], "Expense", "Entertainment", "Streaming Video")

assign([
    "HERSHEY PARK",
], "Expense", "Entertainment", "Amusement & Parks")

assign([
    "The Cheesecake Factory", "FRIENDLY", "JIN SOY", "SAHARA", "Sub Zero",
], "Expense", "Food & Dining", "Restaurants")

assign([
    "KENDALL HUNT PUBLISHING",
], "Expense", "Education", "Books & Supplies")

assign([
    "Verizon",
], "Expense", "Housing & Utilities", "Telecom & Internet")

assign([
    "Yandex", "MYQ", "Synapse",
], "Expense", "Technology", "Software & SaaS")

assign([
    "FRAN LEBOWITZ", "SUMMIT ONE",
], "Expense", "Entertainment", "Movies & Events")

assign([
    "The Bricks",
], "Expense", "Shopping", "Home & Garden")


# ============================================================
# GENERATE CSV - with fallback categorization for any missed
# ============================================================

import re

def guess_category(merchant):
    """Fallback categorizer for merchants not explicitly mapped."""
    m = merchant.lower()

    # Food patterns
    if any(w in m for w in ['restaurant', 'grill', 'pizza', 'burger', 'taco',
                            'kebab', 'kabab', 'halal', 'diner', 'cafe', 'kitchen',
                            'bbq', 'chicken', 'sushi', 'ramen', 'noodle',
                            'deli', 'sub ', 'wings', 'falafel', 'gyro',
                            'thai', 'mexican', 'chinese', 'indian', 'italian']):
        return ("Expense", "Food & Dining", "Restaurants")
    if any(w in m for w in ['bakery', 'boulangerie', 'patisserie', 'bread',
                            'cake', 'pastry', 'donut', 'bagel', 'pretzel']):
        return ("Expense", "Food & Dining", "Bakery & Desserts")
    if any(w in m for w in ['yogurt', 'ice cream', 'gelato', 'frozen',
                            'creamery', 'sundae']):
        return ("Expense", "Food & Dining", "Ice Cream & Yogurt")
    if any(w in m for w in ['grocery', 'market', 'supermarket', 'mart',
                            'food', 'farm']):
        return ("Expense", "Food & Dining", "Groceries")
    if any(w in m for w in ['coffee', 'tea', 'starbucks', 'dunkin']):
        return ("Expense", "Food & Dining", "Coffee & Tea")
    if any(w in m for w in ['doordash', 'grubhub', 'uber eat', 'postmate',
                            'deliveroo', 'instacart']):
        return ("Expense", "Food & Dining", "Food Delivery")

    # Gas
    if any(w in m for w in ['gas', 'fuel', 'shell', 'exxon', 'chevron',
                            'sunoco', 'bp ', 'valero', 'speedway']):
        return ("Expense", "Transportation", "Gas & Fuel")

    # Rideshare
    if any(w in m for w in ['uber', 'lyft', 'taxi', 'cab', 'ride']):
        return ("Expense", "Transportation", "Rideshare")

    # Streaming
    if any(w in m for w in ['netflix', 'hulu', 'disney', 'hbo', 'spotify',
                            'youtube', 'streaming', 'prime video']):
        return ("Expense", "Entertainment", "Streaming Video")

    # VPN
    if any(w in m for w in ['vpn', 'nordvpn', 'express', 'surfshark',
                            'tunnel', 'ghost']):
        return ("Expense", "Technology", "VPN & Privacy")

    # Hotels
    if any(w in m for w in ['hotel', 'inn', 'resort', 'hilton', 'marriott',
                            'hyatt', 'westin', 'sheraton']):
        return ("Expense", "Travel", "Hotels & Lodging")

    # Airlines
    if any(w in m for w in ['airline', 'airways', 'air ', 'jetblue', 'delta',
                            'united', 'southwest', 'frontier']):
        return ("Expense", "Travel", "Airlines")

    # Medical
    if any(w in m for w in ['medical', 'dental', 'doctor', 'clinic',
                            'hospital', 'health', 'pharma', 'diagnostic']):
        return ("Expense", "Health & Wellness", "Medical & Dental")

    # Default
    return ("Expense", "Shopping", "General Retail")


def main():
    # Read all merchants from the source CSV
    merchants = set()
    with open('combined_transactions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            merchants.add(row['merchant'])

    # Write output
    with open('merchant_category.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['merchant', 'root', 'mid_level', 'leaf'])

        for merchant in sorted(merchants):
            if merchant in CATEGORIES:
                root, mid, leaf = CATEGORIES[merchant]
            else:
                root, mid, leaf = guess_category(merchant)
            writer.writerow([merchant, root, mid, leaf])

    # Stats
    print(f"Total merchants: {len(merchants)}")
    mapped = sum(1 for m in merchants if m in CATEGORIES)
    print(f"Explicitly mapped: {mapped}")
    print(f"Auto-categorized: {len(merchants) - mapped}")

    # Verify leaf lengths
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
        print("All leaf categories <= 22 chars ✓")


if __name__ == "__main__":
    main()
