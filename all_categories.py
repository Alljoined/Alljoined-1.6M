def get_categories():

    word_categories = {
        "Animals": {
            "Mammals_Land": [
                "aardvark",
                "affenpinscher",
                "Afghan_hound",
                "African_hunting_dog",
                "Airedale",
                "alpaca",
                "American_black_bear",
                "Angora",
                "antelope",
                "anteater",
                "armadillo",
                "Australian_terrier",
                "baboon",
                "badger",
                "basset",
                "bat1",
                "bear",
                "beaver",
                "Bernese_mountain_dog",
                "bison",
                "black-and-tan_coonhound",
                "Blenheim_spaniel",
                "bloodhound",
                "bluetick",
                "boar",
                "Border_terrier",
                "borzoi",
                "briard",
                "camel",
                "Cardigan",
                "cat",
                "cheetah",
                "Chihuahua",
                "chinchilla",
                "chipmunk",
                "chow",
                "clumber",
                "collie",  # Added based on Shetland sheepdog context
                "cougar",
                "cow",
                "coyote",
                "dalmatian",
                "Dandie_Dinmont",
                "deer",
                "dog",
                "donkey",
                "elephant",
                "English_foxhound",
                "English_springer",
                "ferret",
                "fox",
                "fox_squirrel",
                "gazelle",
                "German_shepherd",
                "German_short-haired_pointer",
                "giant_panda",
                "gibbon",
                "giraffe",
                "goat",
                "golden_retriever",
                "gopher",
                "gorilla",
                "Great_Dane",
                "Greater_Swiss_Mountain_dog",
                "grey_fox",
                "groenendael",
                "groundhog",
                "guinea_pig",
                "hamster",
                "hare",
                "hedgehog",
                "hippopotamus",
                "horse",
                "howler_monkey",
                "hyena",
                "Ibizan_hound",
                "indri",
                "Irish_setter",
                "Irish_terrier",
                "Irish_water_spaniel",
                "jaguar",
                "Japanese_spaniel",
                "kangaroo",
                "keeshond",
                "Kerry_blue_terrier",
                "kit_fox",
                "koala",
                "kuvasz",
                "Labrador_retriever",
                "lamb",
                "Leonberg",
                "leopard",
                "lion",
                "llama",
                "malamute",
                "marmot",
                "meerkat",
                "Mexican_hairless",
                "mink",
                "miniature_poodle",
                "mole",
                "mongoose",
                "monkey",
                "moose",
                "mouse1",
                "orangutan",
                "otter",
                "panda",
                "panther",
                "papillon",
                "Pekinese",
                "pig",
                "piglet",
                "platypus",
                "polar_bear",
                "Pomeranian",
                "poodle",
                "porcupine",
                "possum",
                "pug",
                "puppy",
                "rabbit",
                "raccoon",
                "ram",
                "rat",
                "redbone",
                "reindeer",
                "rhinoceros",
                "Rhodesian_ridgeback",
                "Samoyed",
                "schipperke",
                "Scotch_terrier",
                "sheep",
                "Shetland_sheepdog",
                "Siberian_husky",
                "siamang",
                "skunk",
                "sloth",
                "sloth_bear",
                "snow_leopard",
                "sorrel",
                "spaniel",  # Added based on Blenheim/Japanese etc.
                "squirrel",
                "squirrel_monkey",
                "standard_schnauzer",
                "Sussex_spaniel",
                "terrier",  # Added based on Border/Kerry etc.
                "tiger",
                "titi",
                "vizsla",
                "Walker_hound",
                "walrus",
                "warthog",
                "weasel",
                "Weimaraner",
                "Welsh_springer_spaniel",
                "whippet",
                "wild_boar",
                "wolf",
                "wood_rabbit",
                "yak",
                "zebra",
            ],
            "Mammals_Marine": [
                "dolphin",
                "manatee",
                "sea_lion",
                "seal",
                "whale",
            ],
            "Birds": [
                "bird",
                "black_grouse",
                "chick",
                "chicken1",
                "cock",
                "cockatoo",
                "crane",
                "crow",
                "duck",
                "duckling",
                "eagle",
                "flamingo",
                "goldfinch",
                "goose",
                "great_grey_owl",
                "hawk",
                "hornbill",
                "hummingbird",
                "jay",
                "macaw",
                "ostrich",
                "owl",
                "parrot",
                "peacock",
                "pelican",
                "penguin",
                "pheasant",
                "pigeon",
                "prairie_chicken",
                "puffin",
                "quail",
                "robin",
                "rooster",
                "ruffed_grouse",
                "ruddy_turnstone",
                "seagull",
                "spoonbill",
                "swan",
                "toucan",
                "turkey",
                "vulture",
                "water_ouzel",
                "white_stork",
            ],
            "Fish": [
                "barracouta",
                "catfish",
                "coho",
                "eel",
                "fish",
                "gar",
                "goldfish",
                "hammerhead",
                "rock_beauty",
                "sardine",
                "shark",
                "sturgeon",
                "swordfish",
                "tench",
                "tiger_shark",
            ],
            "Reptiles_Amphibians": [
                "African_crocodile",
                "alligator",
                "American_chameleon",
                "axolotl",
                "banded_gecko",
                "boa",
                "box_turtle",
                "cobra",
                "common_newt",
                "European_fire_salamander",
                "frog",
                "frilled_lizard",
                "gecko",
                "green_lizard",
                "iguana",
                "Komodo_dragon",
                "leatherback_turtle",
                "lizard",
                "loggerhead",
                "mud_turtle",
                "rattlesnake",
                "sea_snake",
                "snake",
                "tailed_frog",
                "terrapin",
                "toad",
                "tree_frog",
                "turtle",
                "vine_snake",
                "water_snake",
            ],
            "Insects_Arachnids_Invertebrates": [
                "ant",
                "bee",
                "beetle",
                "black_and_gold_garden_spider",
                "brain_coral",
                "bug",
                "butterfly",
                "caterpillar",
                "clam",
                "cockroach",
                "coral",  # Moved animal interpretation here
                "crab",
                "crayfish",
                "damselfly",
                "dragonfly",
                "earwig",
                "flatworm",
                "fly",
                "grasshopper",
                "jellyfish",
                "ladybug",
                "leech",
                "lightning_bug",
                "lobster",
                "lycaenid",
                "maggot",
                "mantis",
                "mosquito",
                "moth",
                "mussel",
                "octopus",
                "oyster",
                "praying_mantis",
                "rhinoceros_beetle",
                "ringlet",
                "scallop",
                "scorpion",
                "sea_anemone",
                "sea_urchin",
                "shrimp",
                "slug",
                "snail",
                "spider",
                "squid",
                "starfish",
                "stingray",
                "sulphur_butterfly",
                "tarantula",
                "tick",
                "tiger_beetle",
                "wasp",
                "worm",
            ],
            "Extinct_Animals": ["triceratops"],
            "Human_Animal_Parts": [
                "abdomen",  # (stomach/torso)
                "ankle",
                "antenna",  # Animal part
                "appendix",  # Internal organ
                "arm",
                "artery",  # Internal
                "back",  # (torso)
                "beard",
                "belly",  # (stomach)
                "bile",  # Internal fluid
                "bladder",  # Internal organ
                "blood",  # Internal fluid
                "bone",
                "brain",  # Internal organ
                "breast",  # (chest)
                "breath",  # Process/Result
                "brow",  # (face part)
                "buttocks",  # (hip)
                "calf1",
                "calf2",  # Body part
                "cartilage",  # (bone)
                "cheek",  # (face part)
                "chest",  # Body part (chest1/2)
                "chin",
                "claw",  # Animal part
                "cocoon",  # Animal structure part
                "diaphragm",  # Internal muscle
                "digit",  # (finger/toe)
                "ear",
                "earlobe",  # (ear)
                "elbow",
                "embryo",  # Stage
                "eye",
                "eyebrow",  # (eye)
                "eyelash",  # (eye)
                "eyelid",  # (eye)
                "face",
                "fang",  # (tooth)
                "feather",  # Bird part
                "femur",  # (bone)
                "fin",  # Fish part
                "finger",
                "fingernail",  # (finger)
                "fingerprint",  # Body feature
                "fist",  # (hand)
                "flesh",  # (skin/muscle)
                "foot",
                "forearm",  # (arm)
                "forehead",  # (face)
                "footprint",  # Body feature
                "fur",  # (hair)
                "gallbladder",  # Internal organ
                "gill",  # Fish part
                "gland",  # Internal
                "groin",  # (hip)
                "gut",  # (stomach)
                "hair",
                "hand",
                "handprint",  # Body feature
                "haunch",  # (hip)
                "head",  # Implied
                "heart",  # Internal organ
                "heel",  # (foot)
                "hip",
                "hoof",  # Animal part
                "horn",  # Animal part
                "humerus",  # (bone)
                "index_finger",  # (finger)
                "intestine",  # Internal organ
                "iris",  # (eye)
                "jaw",  # (chin/mouth)
                "joint",  # (elbow/knee/etc)
                "kidney",  # Internal organ
                "knuckle",  # (finger/hand)
                "lap",  # Body feature when sitting
                "larynx",  # Internal
                "leg",
                "limb",  # (arm/leg)
                "lip",  # (mouth)
                "liver",  # Internal organ
                "loin",  # (hip/torso)
                "lung",  # Internal organ
                "lymph",  # Internal fluid
                "mane",  # (hair) - Animal
                "marrow",  # (bone)
                "membrane",  # Internal
                "mouth",
                "mouthpiece",  # Tool related to mouth? Or part? Ambiguous, place here
                "mucus",  # Body fluid
                "muscle",  # Internal
                "mustache",
                "nail",  # Fingernail/Toenail
                "navel",
                "neck",
                "nerve",  # Internal
                "nipple",  # (chest)
                "nostril",  # (nose)
                "nose",
                "organ",  # General internal part
                "palm",  # (hand)
                "paw",  # (foot) - Animal
                "pelvis",  # (hip/bone)
                "pharynx",  # Internal
                "pinky",  # (finger)
                "pimple",  # (skin feature)
                "prostate",  # Internal organ
                "pupil",  # (eye)
                "retina",  # (eye)
                "rib",  # (bone)
                "rumen",  # Internal organ (animal)
                "rump",  # (hip)
                "saliva",  # Body fluid
                "scale",  # Fish/Reptile part
                "scalp",  # (hair/skin)
                "scapula",  # (bone/shoulder)
                "shin",  # (leg)
                "shoulder",  # Body part
                "skeleton",  # Body structure
                "skin",
                "skull",  # (bone/head)
                "snout",  # (nose) - Animal
                "sole",  # (foot)
                "sperm",  # Body fluid
                "spinal_cord",  # Internal
                "spine",  # (bone/back)
                "spleen",  # Internal organ
                "stomach",
                "sweat",  # Body fluid
                "tail",  # Animal part
                "talon",  # (claw)
                "tear",  # Body fluid
                "teeth",  # (tooth)
                "tendon",  # Internal
                "testicle",  # Internal organ
                "thigh",  # (leg)
                "thorax",  # (chest/torso)
                "throat",  # (neck)
                "thumb",
                "thymus",  # Internal organ
                "thyroid",  # Internal organ
                "toe",
                "toenail",  # (toe)
                "tongue",
                "tonsil",  # Internal
                "torso",
                "trachea",  # Internal
                "trunk",  # Elephant part/Torso
                "tusk",  # (tooth) - Animal
                "umbilical_cord",  # (navel)
                "urine",  # Body fluid
                "uterus",  # Internal organ
                "uvula",  # Internal
                "vagina",  # Internal organ
                "vein",  # Internal
                "vertebra",  # (bone/spine)
                "waist",  # (torso/hip)
                "whisker",  # (mustache/hair) - Animal
                "windpipe",  # (trachea)
                "wing",  # Animal part
                "womb",  # (uterus)
                "wooden_leg",  # Prosthetic part
                "wrist",
            ],
        },
        "Food_Drink_Plants_Fungi": {
            "Prepared_Meals_Dishes": [
                "appetizer",
                "burrito",
                "calamari",
                "calzone",
                "casserole",
                "caviar",
                "cheeseburger",
                "chili",
                "coleslaw",
                "cordon_bleu",
                "cornbread",
                "crepe",
                "curry",
                "dessert",
                "dip",
                "egg_roll",
                "enchilada",
                "fast_food",
                "fondue",
                "french_fries",
                "fritter",  # Implied (e.g. corn fritter)
                "guacamole",
                "hamburger",
                "hash",
                "hotdog",
                "hummus",
                "kebab",
                "lasagna",
                "macaroni",
                "mashed_potato",
                "meatball",
                "meat_loaf",
                "meatloaf",
                "nacho",
                "noodle",
                "omelet",
                "paella",  # Implied common dish
                "parfait",
                "pasta",
                "patty",
                "pizza",
                "potpie",
                "quesadilla",
                "quiche",
                "ravioli",
                "ready_meal",
                "salad",
                "sandwich",
                "sauerkraut",
                "scrambled_egg",
                "seafood",
                "souffle",
                "soup",
                "spaghetti",
                "spareribs",
                "spring_roll",
                "steak",
                "stew",
                "stir_fry",
                "stuffing",
                "sushi",
                "taco",
                "tamale",
                "tiramisu",
                "toast",
                "tortellini",
                "tortilla",
                "tostada",
            ],
            "Baked_Goods_Sweets_Snacks": [
                "bagel",
                "baklava",
                "biscuit",
                "bread",
                "breadstick",
                "brownie",
                "bun",
                "cake",
                "candy",
                "candy_bar",
                "candy_cane",
                "cheesecake",
                "chip",
                "chips",
                "chocolate",
                "cookie",
                "cotton_candy",
                "cracker",
                "creme_brulee",
                "croissant",
                "crumb",
                "cupcake",
                "donut",
                "eclair",
                "flan",
                "fruitcake",
                "fudge",
                "gingerbread_man",
                "granola",
                "gum",
                "gumball",
                "gumdrop",
                "ice_cream",
                "ice-cream_cone",
                "jelly_bean",
                "licorice",
                "lollipop",
                "marmalade",
                "marshmallow",
                "mousse",
                "muffin",
                "pastry",
                "peanut_butter",
                "pie",
                "piecrust",
                "popcorn",
                "popsicle",
                "pretzel",
                "pudding",
                "scone",
                "shortbread",
                "sorbet",
                "sundae",
                "sweet",  # General term
                "taffy",
                "wafer",
                "waffle",
                "wedding_cake",
                "whipped_cream",
                "yogurt",
            ],
            "Fruits_Vegetables_Processed": [
                "applesauce",
                "cornmeal",
                "jam",
                "juice",
                "lemonade",
                "maple_syrup",
                "olive_oil",  # Implied from olive
                "orange_rind",
                "pickle",
                "pesto",
                "pineapple_juice",  # Implied
                "prune",
                "raisin",
                "tomato_sauce",
            ],
            "Meats_Proteins_Other": [
                "bacon",
                "batter",
                "bologna",
                "egg",
                "ham",
                "jerky",  # Implied meat product
                "lamb_chop",
                "meat",
                "pepperoni",
                "salami",
                "sausage",
                "spam",
                "yolk",
            ],
            "Dairy_Fats": [
                "butter",
                "cheese",
                "cream",
                "cream_cheese",
                "margarine",  # Implied
                "milk",
                "milkshake",
            ],
            "Drinks": [
                "beer",
                "champagne",
                "coffee",
                "eggnog",
                "espresso",
                "hot_chocolate",
                "latte",
                "margarita",
                "soda",
                "tea",
                "water",  # Added, common drink
                "wine",
                "wine_cooler",
                "water_fountain",
            ],
            "Ingredients_Condiments_Spices": [
                "caramel",
                "cinnamon",
                "corn_syrup",  # Implied
                "dough",
                "flour",
                "gravy",
                "grits",
                "honey",
                "ketchup",
                "mustard",
                "oatmeal",
                "oil",
                "peppermint",
                "pepper2",  # Assume shaker/ground pepper
                "powder",  # General, often food
                "salt",  # Implied by saltshaker
                "sauce",
                "soy_sauce",
                "sugar_cube",
                "syrup",
                "vinegar",  # Implied common condiment
            ],
            "Trees_Woody_Plants": [
                "acorn",
                "aloe",
                "apple_tree",
                "bamboo",
                "bonsai",
                "bush",
                "cactus",
                "grapevine",
                "hedge",
                "ivy",
                "maple_syrup",  # Product implies tree
                "oak",  # Implied by acorn
                "palm_tree",
                "pine_needle",
                "pine_tree",
                "pinecone",
                "plant",
                "root",
                "stump",
                "thorn",
                "tree",
                "tree_trunk",
                "tumbleweed",
                "vine",
                "wood",  # Moved from Materials
            ],
            "Flowers_Herbs_Grasses": [
                "arugula",
                "basil",
                "chive",
                "cilantro",
                "clover",
                "daisy",
                "dandelion",
                "fern",
                "flower",
                "grass",
                "hay",
                "kale",
                "lavender",
                "leek",
                "lettuce",
                "marijuana",
                "mint",
                "moss",
                "okra",
                "onion",
                "orchid",
                "parsley",
                "peppermint",
                "poinsettia",
                "poppy",
                "rose",
                "saffron",
                "scallion",
                "seaweed",
                "spinach",
                "sprouts",
                "sunflower",
                "thatch",
                "tulip",
                "turf",
                "weed",
                "wheat",
            ],
            "Fruits_Vegetables_Nuts_Seeds": [
                "almond",
                "apple",
                "artichoke",
                "asparagus",
                "avocado",
                "banana",
                "bean",
                "beet",
                "bell_pepper",
                "berry",
                "blackberry",
                "bok_choy",
                "broccoli",
                "brussels_sprouts",
                "butternut_squash",
                "cabbage",
                "cantaloupe",
                "carrot",
                "cashew",
                "cauliflower",
                "celery",
                "cherry",
                "chickpea",
                "coconut",
                "corn",
                "cranberry",
                "cucumber",
                "eggplant",
                "fig",
                "fruit",
                "garlic",
                "ginger",
                "grain",
                "grape",
                "grapefruit",
                "green_beans",
                "head_cabbage",
                "jalapeno",
                "kiwi",
                "lemon",
                "lime",
                "macadamia",
                "mango",
                "melon",
                "mulberry",
                "nut",
                "olive",
                "orange",
                "papaya",
                "pea",
                "peach",
                "peanut",
                "pear",
                "pecan",
                "pepper1",
                "pineapple",
                "pistachio",
                "plum",
                "pomegranate",
                "potato",
                "prune",
                "pumpkin",
                "radish",
                "raspberry",
                "rhubarb",
                "rice",
                "seed",
                "soybean",  # Implied by soy sauce
                "star_fruit",
                "strawberry",
                "sweet_potato",
                "tomato",
                "vegetable",
                "walnut",
                "watermelon",
                "zucchini",
            ],
            "Fungi": [
                "fungus",
                "mushroom",
                "mold1",
                "mold2",  # Assuming mold refers to fungi
            ],
            "Other_Plant_Parts": [
                "bark",
                "branch",
                "cornhusk",
                "cornmeal",  # Processed part
                "leaf",
                "orange_rind",
                "petal",
                "pulp",  # Implied (pulpit?) - Keep here for now
            ],
        },
        "Clothing_Accessories_Tools_Instruments": {
            "Garments_Bodywear": [
                "abaya",
                "apron",
                "bathrobe",
                "bikini",
                "blazer",
                "blouse",
                "boxer_shorts",
                "bra",
                "cape",
                "cardigan",
                "chaps",
                "cloak",
                "coat",
                "corset",
                "costume",
                "coverall",
                "diaper",
                "dress",
                "fishnet_stockings",
                "fur_coat",
                "garter",
                "hoodie",
                "jacket",
                "jeans",
                "jersey",
                "jumpsuit",
                "kilt",
                "kimono",
                "lab_coat",
                "leggings",
                "leotard",
                "lingerie",
                "loincloth",
                "nightshirt",
                "outfit",
                "overalls",
                "pajama",
                "pajamas",
                "panties",
                "pants",
                "pantsuit",
                "pantyhose",
                "pocket",  # Part of garment
                "polo_shirt",
                "raincoat",
                "robe",
                "shirt",
                "shorts",
                "ski_suit",  # Assumed from ski context
                "skirt",
                "snowsuit",
                "sock",
                "spacesuit",
                "stockings",
                "straightjacket",
                "suit",
                "sweater",
                "sweatshirt",
                "sweatsuit",
                "swimsuit",
                "t-shirt",
                "toga",
                "tube_top",
                "turtleneck",
                "tuxedo",
                "undershirt",
                "underwear",
                "uniform",
                "veil",
                "vest",
                "wetsuit",
                "yoke",  # Part of garment
            ],
            "Footwear": [
                "boot",
                "cleat",
                "clog",
                "flipper",  # For swimming
                "flip_flop",
                "iceskate",
                "moccasin",
                "rollerblade",
                "rollerskate",
                "running_shoe",
                "sandal",
                "shoe",
                "ski_boots",
                "slipper",
                "snowshoe",
                "stiletto",
            ],
            "Headwear": [
                "bandanna",
                "bathing_cap",
                "beanie",
                "bonnet",
                "bowler_hat",
                "cap",
                "crown",
                "fedora",  # Implied hat type
                "hat",
                "headband",
                "headdress",
                "headscarf",
                "helmet",
                "hood",  # Often part of garment
                "mask",
                "pickelhaube",
                "sombrero",
                "tiara",
                "top_hat",
                "turban",
                "wig",
            ],
            "Accessories_Jewelry": [
                "anklet",
                "backpack",
                "bag",
                "barrette",
                "belt",
                "belt_buckle",
                "bib",
                "bolo_tie",
                "bowtie",
                "bracelet1",
                "bracelet2",
                "briefcase",
                "brooch",
                "buckle",
                "button1",
                "button2",  # Often on clothes
                "clasp",
                "collar",  # Often part of garment
                "corsage",
                "cufflink",
                "cummerbund",
                "duffel_bag",
                "earring",
                "glasses",
                "glove",
                "goggles",
                "handbag",  # Implied (purse)
                "handkerchief",
                "jewel",
                "jewelry",
                "knee_pad",
                "kneepad",
                "lanyard",
                "locket",
                "luggage",
                "lunchbox",
                "medal",
                "mitten",
                "muff",
                "necklace",
                "necktie",  # (tie)
                "patch",
                "pearl",
                "pin",
                "pocket_watch",
                "purse",
                "ribbon",
                "ring",
                "rosary",
                "ruby",
                "sash",  # Implied accessory
                "scarf",
                "sequin",
                "shawl",
                "shoulder",  # Assume epaulet/pad
                "ski_pole",  # Accessory for skiing
                "stud",  # Earring type
                "suitcase",
                "sunglasses",
                "suspenders",
                "tie",
                "visor",
                "wallet",
                "watch",
                "zipper",  # Part of clothes/bags
            ],
            "Makeup_Personal_Care": [
                "comb",
                "deodorant",
                "eyeliner",
                "face_mask",
                "face_powder",
                "floss",
                "hair_spray",
                "hairbrush",
                "hairnet",
                "hairpin",
                "lip_balm",
                "lip_gloss",
                "lipstick",
                "makeup",
                "mascara",
                "nail_clippers",
                "nail_file",
                "nail_polish",
                "perfume",
                "razor",
                "razor_blade",
                "shaving_cream",
                "soap",
                "swab",
                "tattoo",
                "thimble",  # For sewing, personal care task
                "toothbrush",
                "toothpaste",
                "tweezers",
            ],
            "Hand_Tools_Manual_Equipment": [
                "awl",  # Implied tool
                "axe",
                "backscratcher",
                "bellows",  # Implied tool
                "bolt",  # Fastener, requires tool
                "brace",  # Tool
                "brush",
                "chainsaw",
                "chisel",
                "clipper1",
                "clipper2",
                "crowbar",
                "dagger",
                "drill",
                "duster",
                "file1",
                "file2",
                "fire_extinguisher",
                "firewood",  # Needs axe/saw
                "gear",
                "grappling_hook",  # Implied (hook1/2)
                "gun",  # Hand tool (weapon)
                "hammer",
                "handbrake",
                "hatchet",
                "hoe",
                "hook1",
                "hook2",
                "icepick",
                "jack",
                "jackhammer",
                "key",
                "knife",
                "knitting_needle",
                "lever",  # Implied
                "lockpick",  # Implied tool
                "machete",
                "magnet",
                "mallet",
                "match",
                "nail",
                "nutcracker",
                "oar",
                "paddle",
                "pickax",
                "pitchfork",
                "pliers",
                "plunger",
                "pocketknife",
                "prybar",  # (crowbar)
                "pulley",
                "pump",
                "punch1",
                "punch2",
                "rake",
                "ratchet",
                "safety_pin",
                "sandpaper",
                "saw",
                "sawhorse",
                "scalpel",
                "scissors",
                "scoop",
                "scraper",
                "screw",
                "screwdriver",
                "shears",
                "shovel",
                "shiv",
                "sickle",
                "sledgehammer",
                "slingshot",
                "soldering_iron",
                "spade",  # (shovel)
                "spear",
                "spike",  # (nail)
                "staple",
                "staple_gun",
                "stick",
                "sword",
                "syringe",
                "tack",
                "thumbtack",
                "tongs",
                "tool",
                "toolbox",
                "torch",
                "trowel",
                "vise",
                "wand",
                "wedge",
                "whip",
                "wire_cutters",
                "wrench",
            ],
            "Kitchen_Tools_Utensils": [
                "bottle_opener",
                "bowl",
                "can_opener",
                "chopsticks",
                "cleaver",
                "colander",  # (strainer)
                "cookie_cutter",
                "corkscrew",
                "cup",
                "cutting_board",
                "dish",
                "eggbeater",
                "fork",
                "funnel",
                "grater",
                "griddle",  # (hotplate?)
                "grinder",
                "hotplate",
                "juicer1",
                "juicer2",
                "kettle",
                "ladle",
                "measuring_cup",
                "meat_grinder",
                "mug",
                "nutcracker",
                "pan",
                "peeler",
                "pepper_mill",
                "pitcher",
                "plate",
                "pot",
                "potholder",
                "rolling_pin",
                "saltshaker",
                "saucer",
                "sifter",
                "skewer",
                "slicer",
                "spatula",
                "spoon",
                "strainer",
                "swizzle_stick",
                "teacup",
                "teapot",
                "thermometer",  # Cooking/Medical
                "timer",
                "whisk",
                "wok",
                "wooden_spoon",  # Implied
            ],
            "Musical_Instruments": [
                "accordion",
                "bagpipe",
                "banjo",
                "bassoon",
                "bell",
                "bongo",
                "bow3",  # Music bow
                "bugle",  # Implied (horn)
                "cello",
                "chime",
                "clarinet",
                "cornet",
                "cymbal",
                "didgeridoo",  # Implied
                "drum",
                "drumstick",
                "flute",
                "french_horn",
                "gong",
                "guitar",
                "harmonica",
                "harp",
                "horn",
                "kazoo",
                "keyboard",  # Musical
                "mandolin",
                "maraca",  # (rattle?)
                "metronome",
                "oboe",
                "organ",
                "panpipe",
                "piano",
                "piccolo",  # (flute)
                "recorder",
                "saxophone",
                "tambourine",
                "triangle",
                "trombone",
                "trumpet",
                "tuba",
                "tuning_fork",
                "ukulele",
                "violin",
                "whistle",
                "xylophone",
            ],
            "Weapons_Military_Gear": [
                "ammunition",  # (bullet)
                "armor",
                "arrow",
                "baton1",
                "baton2",
                "baton3",
                "baton4",
                "bazooka",
                "bayonet",  # Implied weapon
                "bomb",
                "boomerang",
                "bow1",  # Weapon bow
                "brass_knuckles",
                "bullet",
                "bulletproof_vest",
                "cannon",
                "cannonball",
                "catapult",
                "club",  # (baton?)
                "crossbow",
                "dagger",
                "dart",  # Weapon/Sport
                "detonator",
                "dynamite",
                "flamethrower",
                "gas_mask",
                "grenade",
                "guillotine",
                "gun",
                "handcuff",
                "holster",
                "javelin",
                "lance",  # (spear)
                "landmine",
                "mace",  # Implied weapon
                "machine_gun",
                "missile",
                "noose",
                "projectile",
                "revolver",
                "rifle",
                "shield",
                "spear",
                "sword",
                "tank1",  # Military vehicle/weapon
                "target",
                "torpedo",
                "trident",
                "trigger",
                "weapon",  # General term
            ],
            "Scientific_Medical_Instruments": [
                "beaker",
                "breathalyzer",
                "centrifuge",
                "compass",
                "crutch",
                "defibrillator",
                "dropper",  # (eyedropper)
                "electrode",  # Implied EEG context
                "eyedropper",
                "first-aid_kit",
                "flask",
                "forceps",  # (tweezers?)
                "gauge",
                "geiger_counter",  # Implied
                "gurney",
                "inhaler",
                "lens",  # Optical instrument part
                "magnifier",
                "magnifying_glass",
                "microscope",
                "mortar",  # And pestle
                "needle",  # Medical/Sewing
                "oscilloscope",
                "peg",  # Scientific apparatus?
                "periscope",
                "petri_dish",
                "pipette",  # (eyedropper?)
                "polygraph",
                "prism",
                "probe",  # Implied instrument
                "radio_telescope",
                "retort",  # (flask?)
                "ruler",
                "scale",
                "scalpel",
                "seismograph",
                "slide_rule",
                "sonar",  # Device
                "sonogram",
                "stethoscope",
                "stopwatch",
                "stretcher",
                "syringe",
                "telescope",
                "test_tube",
                "thermometer",
                "tuning_fork",  # Also musical?
                "vial",
            ],
            "Sports_Games_Equipment": [
                "abacus",
                "backgammon",
                "balance_beam",
                "ball",
                "baseball",
                "baseball_bat",
                "baseball_glove",
                "basketball",
                "basketball_hoop",
                "bat2",  # Sports bat
                "beachball",
                "beanbag",
                "billiard_ball",  # (croquet_ball?)
                "board_game",
                "bobsled",
                "bowling_ball",
                "boxing_gloves",
                "checkerboard",  # (chessboard?)
                "checkers",
                "chess_piece",
                "chessboard",
                "cleat",  # Sport shoe part
                "club",  # Golf club
                "croquet_ball",
                "dart",  # Sport/Weapon
                "dartboard",
                "dice",
                "diving_board",
                "domino",
                "dumbbell",
                "frisbee",
                "game",
                "goal",  # (goalpost)
                "goalpost",
                "golf_club",
                "hockey_puck",  # (puck)
                "hockey_stick",
                "home_plate",
                "hopscotch",
                "hula_hoop",
                "jigsaw_puzzle",
                "joystick",  # Game controller
                "jump_rope",
                "kayak",  # Sport vehicle
                "kite",
                "marble",
                "net",  # Sports net
                "paddle",  # Sport
                "parachute",  # Sport/Safety
                "pinball",
                "ping-pong_ball",
                "ping-pong_table",
                "pogo_stick",
                "poker",  # Game
                "pool_table",
                "puck",
                "racket",
                "rattle",  # Toy/Instrument
                "rollerblade",
                "rollerskate",
                "roulette_wheel",
                "scooter",  # Sport/Vehicle
                "scoreboard",
                "scrabble",
                "scuba",  # Gear
                "shuffleboard",
                "skateboard",
                "ski",
                "ski_pole",
                "sled",
                "slide",  # Playground
                "snorkel",
                "snowball",
                "snowboard",
                "soccer_ball",
                "springboard",
                "squirt_gun",  # Toy
                "surfboard",  # Sport
                "swing",
                "swing_set",
                "table_tennis",  # (ping-pong)
                "target",  # Sport/Weapon
                "tee",  # Golf
                "tennis_ball",
                "ticktacktoe",
                "toboggan",  # (sled)
                "toy",
                "trampoline",
                "treadmill",
                "trophy",
                "volleyball",
                "yo-yo",
            ],
            "Drawing_Writing_Art_Supplies": [
                "ballpoint",
                "bookmark",
                "calligraphy_pen",  # Implied (pen)
                "canvas",
                "chalk",
                "charcoal",  # Art medium
                "clipboard",
                "crayon",
                "easel",
                "eraser",
                "felt-tip_pen",  # (marker)
                "fountain_pen",
                "highlighter",
                "ink",
                "marker",
                "notebook",
                "notepad",
                "paintbrush",
                "palette",
                "paper",  # Moved from materials
                "paperclip",  # Office/Art
                "pen",
                "pencil",
                "pencil_sharpener",
                "penholder",
                "penlight",  # Utility light
                "photograph",  # Art/Record
                "protractor",  # Implied tool
                "quill",
                "rubber_eraser",
                "ruler",  # Also scientific
                "stencil",  # Implied tool
                "stylus",  # (pen)
                "whiteboard",
            ],
            "Cleaning_Supplies": [
                "bleach",  # Implied cleaner
                "broom",
                "brush",  # Cleaning brush
                "bucket",  # Used for cleaning
                "detergent",  # (dishwashing_liquid)
                "dishrag",
                "dishwashing_liquid",
                "duster",
                "dustpan",
                "feather_duster",  # (duster)
                "mop",
                "plunger",  # Cleaning tool
                "polisher",
                "rag",
                "scraper",  # Cleaning tool
                "scrub_brush",  # (brush)
                "soap",
                "soap_dispenser",
                "sponge",
                "squeegee",
                "vacuum",  # Electronic appliance, but cleaning focus
                "washboard",
                "washcloth",
            ],
        },
        "Things": {
            "Organic_Materials_Non_Plant_Animal": [
                "beeswax",  # (wax) - Animal product
                "bone",  # Material sense
                "bristle",  # Animal hair material
                "canvas",  # Fabric material (plant derived)
                "cardboard",  # Processed plant material
                "cashmere",  # Animal fiber
                "chitin",  # Animal material
                "cloth",  # (fabric)
                "cork",  # Plant material
                "cotton",  # Plant fiber
                "down",  # (feather) - Animal material
                "dung",  # Animal waste material
                "fabric",  # General woven material
                "felt",  # Fabric material
                "fiber",  # General threadlike material
                "flannel",  # Fabric material
                "fleece",  # (wool)
                "guano",  # Animal waste material
                "gut",  # Animal material (string)
                "hemp",  # Plant fiber
                "hide",  # (leather)
                "horn",  # Material sense
                "ivory",  # Animal material
                "jute",  # Plant fiber
                "kapok",  # Plant fiber
                "keratin",  # (horn/hair/nail)
                "lace",  # Fabric material
                "leather",  # Animal material
                "linen",  # Fabric material (plant derived)
                "lumber",  # Processed wood
                "manure",  # (dung)
                "mother-of-pearl",  # (shell) - Animal material
                "mulch",  # Organic material cover
                "muslin",  # Fabric material
                "nylon",  # Synthetic material (place here?)
                "paper",  # Processed plant material
                "papyrus",  # Plant material paper
                "parchment",  # Animal material paper
                "peat",  # Organic soil material
                "pelt",  # (hide)
                "plastic",  # Synthetic material (place here?)
                "plastic_film",  # Product
                "plywood",  # Processed wood
                "polyester",  # Synthetic material (place here?)
                "pulp",  # Processed plant material
                "raffia",  # Plant fiber
                "rayon",  # Semi-synthetic material
                "resin",  # Plant secretion material
                "rope",  # Made from fibers
                "rubber",  # Natural/Synthetic material
                "satin",  # Fabric material
                "sawdust",  # Wood particles
                "serum",  # Body fluid material
                "shell1",
                "shell2",
                "shell3",  # Material sense (seashell)
                "shellac",  # Animal resin material
                "silk",  # Animal fiber
                "sisal",  # Plant fiber
                "skin",  # Material sense
                "straw1",
                "straw2",  # Plant material
                "string",  # Made from fibers
                "sugar",  # Processed plant material
                "tape",  # Often plastic/paper based
                "tarpaulin",  # (tarp) - Fabric material
                "tarp",  # Fabric material
                "textile",  # (fabric)
                "thread",  # Made from fibers
                "twine",  # (string)
                "vellum",  # (parchment)
                "velvet",  # Fabric material
                "veneer",  # Wood material layer
                "vinyl",  # Synthetic material
                "wax",
                "wax_paper",  # Product
                "web",  # Spider web material
                "wicker",  # Plant material weave
                "wire",  # Metal material thread
                "wool",  # Animal fiber
                "yarn",  # Made from fibers
            ],
            "Furniture": [
                "altar",
                "armoire",  # (cabinet?)
                "backdrop",
                "bassinet",
                "bathmat",
                "bathtub",
                "bed",
                "bedpost",
                "bench",
                "bookcase",
                "bookshelf",
                "buffet",
                "bunkbed",
                "cabinet",
                "chair",
                "chaise_longue",  # (couch)
                "chest",
                "chest1",
                "chest2",  # Furniture chest
                "china_cabinet",  # (cabinet)
                "closet",
                "coffee_table",
                "coffin",
                "cot",
                "couch",
                "counter",
                "crib",
                "cupboard",  # (cabinet)
                "cushion",
                "desk",
                "display_case",  # (cabinet)
                "divan",  # (couch)
                "dresser",
                "easel",  # Art/Furniture
                "end_table",  # (table)
                "filing_cabinet",
                "folding_chair",
                "footbath",
                "footrest",
                "furniture",  # General
                "hammock",
                "hassock",  # (ottoman)
                "headboard",  # (bedpost)
                "highchair",
                "lectern",
                "loveseat",
                "mantle",
                "mattress",
                "medicine_chest",
                "mirror",  # Wall furniture
                "nightstand",
                "ottoman",
                "pew",  # (bench)
                "piano",  # Furniture/Instrument
                "playpen",
                "podium",  # (lectern)
                "pulpit",
                "rack1",
                "rack2",  # Storage furniture
                "recliner",
                "rocking_chair",
                "sarcophagus",
                "screen",  # Room divider
                "secretary",  # (desk)
                "settee",  # (couch)
                "shelf",
                "shower",  # Fixture
                "sideboard",  # (buffet)
                "sink",
                "sofa_bed",
                "stool",
                "step_stool",
                "studio_couch",
                "table",
                "throne",
                "toilet",
                "trough",  # Feeding furniture
                "trunk",  # Storage furniture
                "tv_stand",  # Implied furniture
                "wardrobe",  # (closet)
                "workbench",
            ],
            "Appliances_Non_Electronic": [
                "barbecue",  # (grill)
                "blender",  # Can be manual? Place here for now
                "burner",
                "can_opener",  # Manual appliance
                "clock",  # Often non-electronic (grandfather clock etc)
                "coffee_grinder",  # (grinder) - Often manual
                "coffee_pot",  # Non-electric versions exist
                "coffeepot",
                "cooker",
                "dishwasher",  # Typically electronic, but function is household appliance
                "dryer",  # Clothes dryer - Typically electronic, but function is household appliance
                "dutch_oven",  # Cookware/Appliance
                "fan",  # Manual fans exist
                "food_processor",  # Often electronic, place here for function
                "freezer",  # Typically electronic
                "furnace",
                "grill",  # Non-electric exist
                "heater",  # Non-electric exist
                "hotplate",  # Can be non-electric
                "ice_chest",  # (cooler)
                "icemaker",  # Typically part of electronic freezer
                "iron",  # Appliance
                "ironing_board",  # Accessory to appliance
                "juicer1",
                "juicer2",  # Can be manual
                "lawnmower",  # Can be manual
                "meat_grinder",  # Can be manual
                "mixer",  # Can be manual
                "oven",
                "projector",  # Typically electronic, place here for function? No, move to electronics
                "radiator",  # Household heating
                "refrigerator",  # Typically electronic
                "sewing_machine",  # Can be manual
                "shredder",  # Can be manual
                "soda_fountain",
                "stove1",
                "stove2",  # Heating/Cooking
                "toaster",  # Typically electronic, but simple appliance
                "toaster_oven",  # Typically electronic
                "vacuum",  # Typically electronic, but cleaning appliance
                "waffle_iron",
                "washing_machine",  # Typically electronic
                "water_cooler",
                "water_filter",
                "water_heater",
                "woodstove",  # (stove2)
            ],
            "Containers_Storage": [
                "album",
                "amphora",  # (jar)
                "aquarium",
                "ashcan",  # (trashcan)
                "bag",
                "barrel",
                "basket",
                "bin",
                "birdcage",
                "bottle",
                "box",
                "breadbox",
                "bucket",
                "bulletin_board",  # Storage/Display
                "can",
                "canister",
                "carafe",  # (pitcher)
                "carton",
                "case",  # (box, briefcase)
                "cask",  # (barrel)
                "chest",  # Container sense
                "coffer",  # (chest)
                "coffin",  # Storage for dead
                "coin",  # Storage of value
                "cooler",
                "coop",  # Animal container
                "corkboard",
                "crate",
                "decanter",  # (bottle)
                "doghouse",
                "envelope",  # Paper container
                "file",  # Folder sense (file1/2)
                "filing_cabinet",  # Storage furniture
                "fishbowl",
                "flask",
                "folder",
                "garbage_can",  # (trashcan)
                "gas_pump",  # Dispenser/Container
                "glass",  # Container sense
                "goblet",
                "hamper",  # (laundry_basket)
                "hatbox",
                "holder",  # General
                "honeypot",
                "hot-water_bottle",
                "ice_bucket",  # (bucket)
                "inkwell",
                "jar",
                "jug",
                "keg",
                "locker",
                "mailbox",
                "mailbag",  # (bag)
                "matchbox",
                "milk_can",
                "money",  # Storage of value
                "mug",  # Container
                "napkin_ring",  # Holder
                "oilcan",
                "package",  # (box)
                "pail",  # (bucket)
                "pallet",  # Storage/Transport base
                "penholder",
                "piggy_bank",
                "pillbox",
                "pitcher",  # Container
                "plastic_bag",
                "portfolio",  # (briefcase)
                "pot",  # Cooking/Plant container
                "purse",  # Container accessory
                "quiver",  # Arrow container
                "rack1",
                "rack2",  # Storage
                "rain_barrel",
                "safe",  # Security container
                "saltshaker",  # Container
                "sandbox",  # Container
                "sarcophagus",  # Container
                "satchel",  # (bag)
                "shaker",  # Container
                "shelf",  # Storage
                "shopping_basket",
                "shopping_cart",
                "soap_dispenser",  # Container
                "spool",  # Container for thread/wire
                "steamer",  # Cooking container
                "suitcase",  # Container
                "tank2",  # Storage tank
                "teapot",  # Container
                "terrarium",
                "thermos",
                "toolbox",  # Container
                "trashcan",
                "tray",
                "trough",  # Container
                "trunk",  # Container sense
                "tupperware",
                "urn",
                "vase",
                "wallet",  # Container
                "wastebasket",  # (trashcan)
            ],
            "Decor_Linens_Bedding": [
                "afghan",  # (blanket)
                "altarpiece",  # (painting?)
                "banner",
                "bath_towel",
                "bedspread",  # (blanket)
                "blanket",
                "blinder",  # Horse decor/tool
                "bolo_tie",  # Decor accessory
                "bonsai",  # Decor plant
                "bouquet",
                "bow",  # Decorative knot
                "candle",
                "jack-o'-lantern",
                "candlestick",  # Decor holder
                "candelabra",  # Decor holder
                "carpet",  # (rug)
                "centerpiece",
                "chandelier",
                "chime",  # Wind chime? Decor
                "christmas_card",  # Decor/Stationery
                "christmas_tree",  # Decor
                "coaster",
                "cornucopia",  # Decor
                "curtain",
                "cushion",
                "decal",  # (sticker)
                "doily",
                "doll",
                "dollhouse",  # Toy/Decor
                "dreamcatcher",  # Decor
                "embroidery",  # Decor
                "figurine",
                "flag",  # Decor/Symbol
                "flowerpot",  # (pot) - Decor use
                "fresco",  # (painting)
                "garland",  # (wreath)
                "gargoyle",  # Decor statue
                "gravestone",  # Decor/Memorial
                "hanging",  # (tapestry)
                "hearth",  # (fireplace)
                "incense",  # Decor/Sensory
                "inlay",  # Decor
                "lace",  # Decor fabric
                "lampshade",
                "lantern",  # Decor light
                "macrame",  # Decor
                "mannequin",  # Decor/Tool
                "mantelpiece",  # (mantle)
                "mat",
                "menorah",  # (candelabra)
                "mobile",  # Decor
                "mosaic",  # Decor
                "mural",  # (painting)
                "napkin",
                "needlepoint",  # Decor
                "ornament",  # Decor
                "painting",
                "pennant",  # Decor flag
                "photograph",  # Decor/Record
                "picture",  # (painting, photograph)
                "pillow",
                "pincushion",  # Decor/Tool
                "placard",  # (poster)
                "place_mat",
                "plaque",  # Decor
                "poster",
                "potpourri",  # Decor
                "print",  # Decor art
                "quilt",  # Bedding/Decor
                "red_carpet",  # Decor
                "rug",
                "sampler",  # (embroidery)
                "sconce",  # Decor light fixture
                "sculpture",  # (statue)
                "sheet",  # Bedding
                "shower_curtain",  # Decor/Functional
                "sleeping_bag",  # Bedding
                "slipcover",  # Furniture cover
                "stained_glass",  # Decor
                "statue",
                "sticker",  # Decor
                "streamer",  # Decor
                "tablecloth",
                "tapestry",
                "teddy_bear",  # Toy/Decor
                "terracotta",  # Material/Decor
                "tinsel",  # Decor
                "totem_pole",  # Decor/Structure
                "towel",
                "towel_rack",  # Holder furniture
                "trophy",  # Decor/Award
                "valance",  # (curtain)
                "wallpaper",  # Decor
                "wall_hanging",  # (tapestry)
                "wind_chimes",  # Decor/Instrument
                "window_blind",  # (blinder?) - Window covering
                "window_shade",  # Window covering
                "wrapping_paper",  # Decor paper
                "wreath",  # Decor
            ],
            "Tableware_Dishware": [
                "bowl",  # Eating
                "candlestick",  # Table setting
                "carafe",  # Serving container
                "centerpiece",  # Table decor
                "chalice",  # Drinking cup
                "charger",  # Plate type
                "chinaware",  # General
                "coaster",  # Table protection
                "coffee_mug",  # Cup
                "creamer",  # Serving container
                "cup",  # Drinking
                "cutlery",  # (fork, knife, spoon)
                "decanter",  # Serving container
                "dish",  # Plate/Bowl
                "fork",  # Utensil
                "glass",  # Drinking container
                "goblet",  # Drinking cup
                "gravy_boat",  # Serving container
                "jug",  # Serving container
                "knife",  # Eating utensil
                "ladle",  # Serving utensil
                "mug",  # Drinking cup
                "napkin",  # Table linen
                "napkin_ring",  # Table accessory
                "pitcher",  # Serving container
                "place_mat",  # Table setting
                "plate",
                "platter",  # Serving dish
                "saltshaker",  # Table condiment holder
                "sauceboat",  # (gravy_boat)
                "saucer",  # Dish part
                "serving_dish",  # (platter)
                "silverware",  # (cutlery)
                "spoon",  # Utensil
                "stein",  # (mug)
                "sugar_bowl",  # Serving container
                "tablecloth",  # Table linen
                "tankard",  # (mug)
                "teacup",  # Cup
                "teapot",  # Serving container
                "tray",  # Serving/Holding
                "tureen",  # Serving bowl
                "tumbler",  # (glass)
                "wineglass",  # Drinking container
            ],
            "Bathroom_Items": [
                "bidet",  # (toilet)
                "comb",  # Personal care, often bathroom
                "diaper",  # Often changed in bathroom context
                "faucet",  # Fixture
                "hairdryer",  # Often used in bathroom
                "hamper",  # Laundry basket, often bathroom
                "loofah",  # (sponge) - Bathing item
                "medicine_chest",  # Furniture, often bathroom
                "mirror",  # Often bathroom furniture
                "plunger",  # Tool, often bathroom
                "potty",  # (toilet) - Child's version
                "q-tip",  # (swab) - Personal care
                "razor",  # Personal care
                "scale",  # Often bathroom item
                "shampoo",  # Implied personal care
                "shower",  # Fixture
                "shower_cap",  # Clothing/Bathroom item
                "shower_curtain",  # Bathroom decor/functional
                "showerhead",  # Fixture part
                "sink",  # Fixture
                "soap",  # Personal care/Cleaning
                "soap_dish",  # Holder
                "soap_dispenser",  # Holder
                "sponge",  # Bathing/Cleaning
                "swab",  # Personal care
                "toilet",  # Fixture
                "toilet_brush",  # Cleaning tool
                "toilet_paper",  # Consumable
                "toilet_seat",  # Fixture part
                "toothbrush",  # Personal care
                "toothpaste",  # Personal care
                "towel",  # Bathroom linen
                "towel_rack",  # Holder furniture
                "tub",  # (bathtub)
                "urinal",  # Fixture
                "vanity",  # (desk/counter) - Bathroom furniture
                "washbasin",  # (sink)
                "washcloth",  # Bathroom linen
            ],
            "Office_Supplies_Stationery": [
                "ballpoint",  # Pen
                "binder",  # Holder
                "blotter",  # Desk accessory
                "bookmark",  # Reading accessory
                "calculator",  # Tool, often office
                "calendar",  # Implied stationery
                "carbon_paper",  # Stationery
                "card",  # Greeting card, etc.
                "checkbook",  # Financial stationery
                "clipboard",  # Holder
                "compass",  # Drawing tool
                "computer",  # Office machine (moved to Electronics)
                "copier",  # Office machine (moved to Electronics)
                "correction_fluid",  # Stationery
                "desk_lamp",  # (lamp) - Office context
                "diary",  # (notebook)
                "dictionary",  # (book)
                "envelope",  # Stationery
                "eraser",  # Stationery
                "fax_machine",  # Office machine (moved to Electronics)
                "file",  # Folder sense
                "file_cabinet",  # (filing_cabinet)
                "folder",  # Holder
                "fountain_pen",  # Pen
                "glue",  # Adhesive
                "graph_paper",  # (paper)
                "highlighter",  # Marker
                "hole_punch",  # Tool
                "index_card",  # (card)
                "ink",  # Consumable
                "label",  # (tag)
                "ledger",  # (notebook)
                "letter",  # (paper)
                "letter_opener",  # Tool
                "manila_folder",  # (folder)
                "marker",  # Pen type
                "modem",  # Office electronics (moved to Electronics)
                "mousepad",  # Computer accessory (moved to Electronics)
                "newspaper",  # Publication
                "notebook",  # Stationery
                "notepad",  # Stationery
                "organizer",  # Holder
                "paper",  # Stationery
                "paper_clip",  # (paperclip)
                "paper_shredder",  # (shredder)
                "paper_weight",  # (paperweight)
                "paperclip",  # Fastener
                "paperweight",  # Desk accessory
                "pen",  # Writing tool
                "pencil",  # Writing tool
                "pencil_case",  # Container
                "pencil_sharpener",  # Tool
                "planner",  # (notebook)
                "post-it_note",  # (sticker)
                "printer",  # Office machine (moved to Electronics)
                "projector",  # Office machine (moved to Electronics)
                "protractor",  # Tool
                "rolodex",  # Holder
                "rubber_band",  # Fastener
                "rubber_stamp",  # (stamp1/2)
                "ruler",  # Tool
                "scanner",  # Office machine (moved to Electronics)
                "scissors",  # Tool
                "scotch_tape",  # (tape)
                "seal",  # Stamp/Fastener
                "sharpener",  # (pencil_sharpener)
                "spreadsheet",  # Abstract (web_site?)
                "staple",  # Fastener
                "stapler",  # Tool
                "stationery",  # General term
                "sticker",  # Adhesive label
                "stylus",  # Pen type (moved to Electronics)
                "tab",  # Folder part
                "tag",  # Label
                "tape",  # Adhesive
                "tape_dispenser",  # Holder
                "thumbtack",  # Fastener
                "typewriter",  # Office machine
                "white_out",  # (correction_fluid)
            ],
            "Computing_Devices_Peripherals": [
                "calculator",
                "computer",
                "computer_screen",
                "copier",  # Office machine
                "diskette",
                "fax_machine",  # Office machine
                "flash_drive",  # (memory_stick)
                "floppy_disk",  # (diskette)
                "game_console",  # (videogame device)
                "hard_disk",
                "joystick",  # Input device
                "keyboard",  # Input device
                "laptop",
                "memory_stick",
                "modem",
                "monitor",  # (computer_screen)
                "motherboard",
                "mouse2",  # Input device
                "mousepad",  # Accessory
                "printer",  # Output device
                "router",  # Networking device
                "scanner",  # Input device
                "server",  # (computer)
                "sim_card",  # Component
                "slot",  # Interface part
                "space_bar",  # Keyboard part
                "stylus",  # Input device
                "tablet",
                "touchpad",  # Input device
                "trackball",  # (mouse2)
                "usb_drive",  # (memory_stick)
            ],
            "Audio_Video_Photography": [
                "amplifier",
                "antenna",  # Reception device
                "boombox",  # (radio/stereo)
                "camcorder",
                "camera1",
                "camera2",
                "camera_lens",  # Part
                "cassette",  # Media
                "cassette_player",  # Playback device
                "cd",  # Media (implied by cd_player)
                "cd_player",  # Playback device
                "digital_clock",  # Time display
                "digital_watch",  # Time display
                "dvd",  # Media (implied)
                "dvd_player",  # Playback device
                "earbuds",  # (headphones)
                "earphone",  # (headphones)
                "entertainment_center",  # Furniture holding electronics
                "equalizer",  # Audio device
                "film",  # Media
                "flash",  # Photography accessory (flashbulb)
                "flashbulb",  # Photography accessory
                "gramophone",  # Playback device
                "headphone",  # (headphones)
                "headphones",  # Output device
                "headset",  # Input/Output device
                "hi-fi",  # (stereo)
                "jukebox",  # Playback device
                "loudspeaker",  # Output device
                "megaphone",  # Amplification device
                "microphone",  # Input device
                "mp3_player",  # Playback device
                "negative",  # (film)
                "photograph",  # Output/Record
                "projector",  # Output device
                "radio",  # Reception/Playback device
                "radio_telescope",  # Scientific electronic device
                "record",  # Media
                "record_player",  # Playback device
                "remote_control",  # Input device
                "satellite",  # Communication device
                "satellite_dish",  # Reception device
                "screen1",
                "screen2",  # Display surface
                "slide",  # Photography media
                "speaker",  # Output device
                "stereo",  # Playback system
                "tape_player",  # Playback device
                "tape_recorder",  # Recording/Playback device
                "television",
                "tripod",  # Photography accessory
                "turntable",  # Playback device
                "vcr",  # (videocassette player)
                "videocamera",  # (camcorder)
                "videocassette",  # Media
                "videogame",  # Software/System
                "viewfinder",  # Camera part
                "walkie-talkie",  # (radio) - Communication device
                "webcam",  # Input device
            ],
            "Communication_Devices": [
                "beeper",  # (pager)
                "cellphone",
                "intercom",  # Device
                "pager",  # Device
                "payphone",  # Public phone
                "phone",  # Device
                "receiver",  # Phone part
                "repeater",  # Signal booster
                "smartphone",  # (cellphone)
                "telegraph",  # Device
                "telephone",  # (phone)
                "telephone_pole",  # Structure supporting comm lines
                "transmitter",  # Device
            ],
            "Electronic_Appliances": [
                "air_conditioner",  # Household appliance
                "blender",  # Kitchen appliance
                "coffee_grinder",  # Kitchen appliance
                "coffeemaker",  # Kitchen appliance
                "curling_iron",  # Personal care appliance
                "dishwasher",  # Kitchen appliance
                "dryer",  # Clothes appliance
                "electric_blanket",  # (blanket) - Appliance
                "electric_guitar",  # Instrument/Electronic
                "electric_heater",  # (heater) - Appliance
                "electric_kettle",  # (kettle) - Appliance
                "electric_razor",  # (razor) - Appliance
                "electric_toothbrush",  # (toothbrush) - Appliance
                "espresso_maker",  # Kitchen appliance
                "fan",  # Household appliance
                "food_processor",  # Kitchen appliance
                "freezer",  # Kitchen appliance
                "hairdryer",  # Personal care appliance
                "heater",  # Household appliance
                "humidifier",  # Household appliance
                "icemaker",  # Kitchen appliance part
                "kettle",  # Kitchen appliance
                "lamp",  # Household appliance
                "lightbulb",  # Component/Appliance part
                "microwave",  # Kitchen appliance
                "refrigerator",  # Kitchen appliance
                "sewing_machine",  # Household appliance
                "shaver",  # (razor) - Appliance
                "shredder",  # Office appliance
                "smoke_alarm",  # Safety device
                "toaster",  # Kitchen appliance
                "toaster_oven",  # Kitchen appliance
                "vacuum",  # Cleaning appliance
                "vibrator",  # Personal device
                "waffle_iron",  # Kitchen appliance
                "washing_machine",  # Household appliance
                "water_heater",  # Household appliance
            ],
            "Other_Electronics_Components": [
                "adapter",  # Component
                "alternator",  # Component
                "ammeter",  # Measuring device
                "anode",  # Component
                "battery",  # Power source
                "capacitor",  # Component
                "cathode",  # Component
                "charger",  # Power device
                "chip",  # Microchip component
                "circuit",  # Component assembly
                "circuit_board",  # (motherboard)
                "coil",  # Component
                "condenser",  # Component (capacitor)
                "conductor",  # Material property/Component
                "connector",  # Component
                "converter",  # Device
                "diode",  # Component
                "dynamo",  # (generator)
                "electrode",  # Component
                "electromagnet",  # (magnet) - Electronic component
                "filament",  # (lightbulb part)
                "fuse",  # Safety component
                "galvanometer",  # Measuring device
                "generator",  # Power source
                "grid",  # Component pattern
                "gyroscope",  # Electronic sensor version exists
                "inductor",  # (coil)
                "insulator",  # Material property/Component
                "inverter",  # Device
                "laser",  # Device (laser_pointer)
                "laser_pointer",  # Device
                "led",  # (lightbulb) - Component
                "light_meter",  # Measuring device
                "magnetron",  # (microwave part)
                "microchip",  # (chip)
                "motor",  # Component
                "multimeter",  # Measuring device
                "ohmmeter",  # Measuring device
                "oscilloscope",  # Measuring device
                "photocell",  # Component
                "pylon",  # Structure supporting power lines
                "rectifier",  # Component
                "relay",  # Component
                "resistor",  # Component
                "rheostat",  # Component
                "semiconductor",  # Material/Component
                "sensor",  # Component
                "solar_panel",  # Power source
                "solenoid",  # Component
                "spark_plug",  # Component
                "switch",  # Component
                "synthesizer",  # Instrument/Electronic device
                "terminal",  # Component part
                "thermistor",  # Component
                "thermostat",  # Control device
                "thyristor",  # Component
                "transformer",  # Component
                "transistor",  # Component
                "tube",  # Vacuum tube component
                "turbine",  # Generator component
                "valve",  # Component (electronic valve)
                "voltmeter",  # Measuring device
                "wire",  # Component/Material
            ],
            "Abstract_Concepts_Symbols_Misc": [
                "ace",  # Playing card/Symbol
                "advertisement",  # Abstract concept/Media
                "air",  # Abstract element
                "alphabet",  # Abstract system
                "anchor",  # Symbol/Tool
                "angle",  # Abstract geometry
                "anniversary",  # Abstract event
                "arc",  # Abstract geometry
                "area",  # Abstract space
                "asterisk",  # Symbol
                "autograph",  # (signature)
                "award",  # (trophy/medal) - Abstract concept
                "axis",  # Abstract line
                "background",  # Abstract part of scene
                "badge",  # Symbol/Accessory
                "barcode",  # Symbol/Data
                "block",  # Shape/Toy
                "blueprint",  # Abstract plan
                "blur",  # Abstract visual effect
                "brand",  # Abstract concept
                "bubble",  # Shape/Object
                "bubble_wrap",  # Material/Packaging
                "button",  # Abstract UI element? (button1/2 ambiguity)
                "byte",  # Abstract unit
                "cache",  # Abstract storage
                "calorie",  # Abstract unit
                "camouflage",  # Abstract pattern
                "cartoon",  # Abstract representation
                "category",  # Abstract grouping
                "character",  # Symbol/Abstract entity
                "chart",  # Abstract representation
                "checkers",  # Game - Abstract pattern?
                "cipher",  # Abstract code
                "circle",  # Abstract shape
                "clue",  # Abstract information
                "code",  # Abstract system
                "color",  # Abstract property
                "column",  # Abstract layout element
                "combination",  # Abstract sequence (combination_lock)
                "combination_lock",  # Object
                "comic_book",  # Media/Object
                "comma",  # Symbol
                "comment",  # Abstract communication
                "commercial",  # (advertisement)
                "confetti",  # Small objects/Abstract scatter
                "content",  # Abstract information
                "context",  # Abstract setting
                "contour",  # Abstract line
                "contrast",  # Abstract property
                "copy",  # Abstract concept/Result
                "corner",  # Abstract location
                "count",  # Abstract number
                "coupon",  # Abstract voucher/Paper object
                "crest",  # Symbol/Body part/Wave top
                "cross",  # Symbol/Object
                "crucifix",  # Symbol/Object
                "cube",  # Abstract shape (ice_cube)
                "cue",  # Abstract signal
                "curve",  # Abstract line
                "cylinder",  # Abstract shape
                "data",  # Abstract information
                "date",  # Abstract time point
                "decimal",  # Abstract number type
                "degree",  # Abstract unit
                "depth",  # Abstract dimension
                "design",  # Abstract concept/Pattern
                "detail",  # Abstract part
                "diagram",  # Abstract representation
                "digit",  # Abstract number symbol/Body part
                "dimension",  # Abstract measurement
                "direction",  # Abstract concept
                "discount",  # Abstract concept
                "distance",  # Abstract measurement
                "dot",  # Abstract shape/Mark
                "double",  # Abstract quantity
                "draft",  # Abstract version
                "dreidel",  # Toy/Symbol
                "edge",  # Abstract boundary
                "effect",  # Abstract result
                "element",  # Abstract part
                "ellipse",  # Abstract shape
                "emblem",  # (badge/crest) - Symbol
                "energy",  # Abstract concept
                "error",  # Abstract concept
                "estimate",  # Abstract calculation
                "event",  # Abstract occurrence
                "example",  # Abstract instance
                "exception",  # Abstract case
                "excerpt",  # Abstract part
                "exclamation_mark",  # Symbol
                "exit",  # Abstract concept/Sign
                "experiment",  # Abstract process
                "exponent",  # Abstract math concept
                "expression",  # Abstract representation/Face
                "factor",  # Abstract concept
                "fade",  # Abstract effect
                "failure",  # Abstract outcome
                "false",  # Abstract value
                "family",  # Abstract group
                "fantasy",  # Abstract genre
                "fashion",  # Abstract concept
                "figure",  # Abstract shape/Number/Statue
                "file",  # Abstract data container (file1/2 ambiguity)
                "filter",  # Abstract process/Object
                "fire",  # Phenomenon/Abstract concept
                "fireworks",  # Event/Object
                "flag",  # Symbol/Object
                "flash",  # Abstract light event
                "float",  # Abstract action/Object
                "flow",  # Abstract movement
                "focus",  # Abstract point/Action
                "font",  # Abstract style
                "force",  # Abstract concept
                "form",  # Abstract shape/Document
                "format",  # Abstract layout
                "formula",  # Abstract representation
                "fraction",  # Abstract number type
                "frame",  # Abstract boundary/Object
                "frequency",  # Abstract concept
                "function",  # Abstract concept
                "future",  # Abstract time
                "game",  # Abstract activity/Object
                "gap",  # Abstract space
                "gender",  # Abstract concept
                "geometry",  # Abstract subject
                "ghost",  # Abstract entity
                "glare",  # Abstract light effect
                "glitch",  # Abstract error
                "goal",  # Abstract concept/Object
                "grade",  # Abstract level/Mark
                "gradient",  # Abstract transition
                "graffiti",  # Marking/Art
                "graph",  # Abstract representation
                "grid",  # Abstract pattern
                "group",  # Abstract collection
                "guess",  # Abstract thought
                "guide",  # Abstract information/Person
                "halo",  # Abstract light effect
                "harmony",  # Abstract concept
                "heat",  # Abstract energy
                "height",  # Abstract dimension
                "helix",  # Abstract shape
                "help",  # Abstract concept
                "hexagon",  # Abstract shape
                "hierarchy",  # Abstract structure
                "highlight",  # Abstract emphasis
                "hint",  # (clue)
                "history",  # Abstract subject/Past
                "hole",  # Abstract opening/Object
                "hologram",  # Abstract representation
                "horizon",  # Abstract line
                "hue",  # (color)
                "humor",  # Abstract concept
                "hypothesis",  # Abstract idea
                "icon",  # Symbol
                "idea",  # Abstract concept
                "illusion",  # Abstract perception
                "image",  # Abstract representation/Object
                "impact",  # Abstract effect
                "index",  # Abstract list/Marker
                "infinity",  # Abstract concept
                "information",  # Abstract concept
                "initial",  # Abstract letter/First part
                "input",  # Abstract concept
                "instruction",  # Abstract information
                "integer",  # Abstract number type
                "interface",  # Abstract boundary/Connection
                "interval",  # Abstract space/Time
                "introduction",  # Abstract part
                "inventory",  # Abstract list
                "invitation",  # Abstract communication/Object
                "issue",  # Abstract topic/Version
                "item",  # Abstract object
                "iteration",  # Abstract repetition
                "jackpot",  # Abstract prize
                "joke",  # (humor)
                "journal",  # (notebook) - Abstract record
                "journey",  # Abstract travel
                "judgment",  # Abstract decision
                "junction",  # Abstract connection point
                "justice",  # Abstract concept
                "key",  # Abstract solution/Tool/Symbol
                "keyword",  # Abstract term
                "kind",  # (type)
                "knowledge",  # Abstract concept
                "label",  # Abstract identifier/Object
                "language",  # Abstract system
                "layer",  # Abstract level
                "layout",  # Abstract arrangement
                "leader",  # Abstract role
                "learning",  # Abstract process
                "legend",  # Abstract story/Map key
                "length",  # Abstract dimension
                "lesson",  # Abstract unit of learning
                "letter",  # Abstract symbol/Communication object
                "level",  # Abstract position
                "liability",  # Abstract concept
                "liberty",  # Abstract concept
                "license",  # Abstract permission/Object
                "life",  # Abstract concept
                "light",  # Abstract energy/Phenomenon
                "limit",  # Abstract boundary
                "line",  # Abstract mark/Queue
                "link",  # Abstract connection
                "list",  # Abstract sequence
                "literature",  # Abstract subject/Works
                "load",  # Abstract quantity/Action
                "location",  # Abstract place
                "logic",  # Abstract system
                "logo",  # Symbol
                "loop",  # Abstract repetition/Shape
                "loss",  # Abstract concept
                "lottery",  # Abstract game/Event
                "luck",  # Abstract concept
                "magic",  # Abstract concept
                "magnitude",  # Abstract size
                "mail",  # Abstract system/Object
                "majority",  # Abstract quantity
                "map",  # Abstract representation/Object
                "margin",  # Abstract boundary space
                "mark",  # Abstract sign/Grade
                "market",  # Abstract system/Place
                "mass",  # Abstract property
                "master",  # Abstract role/Original
                "match",  # Abstract correspondence/Object
                "mathematics",  # Abstract subject
                "matrix",  # Abstract grid
                "maximum",  # Abstract limit
                "meaning",  # Abstract concept
                "measure",  # Abstract quantity/Action
                "median",  # Abstract value
                "medium",  # Abstract means/Size
                "melody",  # Abstract music concept
                "member",  # Abstract part of group
                "memory",  # Abstract faculty/Storage
                "mention",  # Abstract reference
                "menu",  # Abstract list
                "message",  # Abstract communication
                "metadata",  # Abstract data about data
                "method",  # Abstract process
                "metric",  # Abstract measurement system
                "middle",  # Abstract position
                "might",  # Abstract possibility/Strength
                "mileage",  # Abstract measurement
                "minimum",  # Abstract limit
                "minority",  # Abstract quantity
                "minute",  # Abstract time unit
                "miracle",  # Abstract event
                "mistake",  # (error)
                "mix",  # Abstract combination
                "mode",  # Abstract state/Value
                "model",  # Abstract representation/Example
                "modification",  # Abstract change
                "moment",  # Abstract time point
                "mood",  # Abstract state
                "motion",  # Abstract movement
                "motive",  # Abstract reason
                "movement",  # Abstract action
                "movie",  # Abstract media/Event
                "music",  # Abstract art form
                "mystery",  # Abstract concept
                "myth",  # (legend)
                "name",  # Abstract identifier
                "narrative",  # (story)
                "nation",  # Abstract group/Place
                "nature",  # Abstract concept/World
                "negative",  # Abstract value/Photography object
                "network",  # Abstract system
                "news",  # Abstract information
                "nexus",  # Abstract connection point
                "nickname",  # (name)
                "node",  # Abstract point in network
                "noise",  # Abstract sound/Interference
                "norm",  # Abstract standard
                "note",  # Abstract information/Music symbol
                "notice",  # Abstract information
                "notion",  # (idea)
                "noun",  # Abstract language part
                "novel",  # Abstract work/Newness
                "number",  # Abstract concept/Symbol
                "object",  # Abstract thing
                "objective",  # (goal)
                "obligation",  # Abstract concept
                "observation",  # Abstract action/Data
                "occasion",  # (event)
                "occupation",  # Abstract role/Activity
                "occurrence",  # (event)
                "octagon",  # Abstract shape
                "offer",  # Abstract proposal
                "offset",  # Abstract difference
                "omen",  # Abstract sign
                "omission",  # Abstract lack
                "operation",  # Abstract process
                "opinion",  # Abstract thought
                "opportunity",  # Abstract chance
                "opposite",  # Abstract relation
                "option",  # Abstract choice
                "oracle",  # Abstract source of wisdom
                "order",  # Abstract sequence/Command/State
                "organization",  # Abstract group/Structure
                "origin",  # Abstract starting point
                "origami",  # Art form/Object
                "ornament",  # Decoration/Abstract feature
                "oscillation",  # Abstract movement
                "outcome",  # Abstract result
                "outline",  # Abstract boundary/Summary
                "output",  # Abstract result/Signal
                "overlap",  # Abstract intersection
                "overview",  # Abstract summary
                "ownership",  # Abstract concept
                "pace",  # Abstract speed
                "package",  # Abstract unit/Object
                "page",  # Abstract unit/Object part
                "pair",  # Abstract group of two
                "palindrome",  # Abstract sequence
                "panel",  # Abstract group/Object part
                "paradigm",  # Abstract model
                "paradox",  # Abstract concept
                "paragraph",  # Abstract text unit
                "parallel",  # Abstract relation
                "parameter",  # Abstract variable
                "parenthesis",  # Symbol
                "parity",  # Abstract property
                "part",  # Abstract portion
                "particle",  # Abstract small piece
                "partition",  # Abstract division/Object
                "partner",  # Abstract role
                "passage",  # Abstract text section/Way through
                "password",  # Abstract secret code
                "past",  # Abstract time
                "patch",  # Abstract fix/Object piece
                "path",  # Abstract route
                "pattern",  # Abstract repetition/Design
                "pause",  # Abstract stop
                "peace",  # Abstract state
                "peak",  # Abstract maximum/Mountain top
                "penalty",  # Abstract consequence
                "pentagon",  # Abstract shape
                "percent",  # Abstract unit
                "perception",  # Abstract process
                "performance",  # Abstract action/Event
                "perimeter",  # Abstract boundary length
                "period",  # Abstract time duration/Symbol
                "permission",  # Abstract concept
                "permutation",  # Abstract arrangement
                "perpendicular",  # Abstract relation
                "person",  # Abstract entity (man/woman/girl/boy)
                "perspective",  # Abstract viewpoint
                "phase",  # Abstract stage
                "phenomenon",  # Abstract occurrence
                "philosophy",  # Abstract subject
                "phone_number",  # (number) - Abstract identifier
                "phrase",  # Abstract language unit
                "physics",  # Abstract subject
                "picture",  # Abstract representation/Object
                "piece",  # Abstract part
                "pilot",  # Abstract role/First version
                "pinwheel",  # Toy/Abstract rotation shape
                "place",  # Abstract location
                "plan",  # Abstract design/Intention
                "plane",  # Abstract surface/Vehicle
                "plasma",  # Abstract state of matter
                "platform",  # Abstract base/Stage object
                "play",  # Abstract activity/Drama
                "plot",  # Abstract story line/Area of land
                "plus_sign",  # Symbol
                "poem",  # Abstract work
                "point",  # Abstract location/Unit/Action
                "policy",  # Abstract rule set
                "poll",  # Abstract survey
                "polygon",  # Abstract shape
                "pom-pom",  # Object/Abstract shape
                "pool",  # Abstract collection/Object
                "population",  # Abstract group count
                "portion",  # (part)
                "portrait",  # Abstract representation/Object
                "position",  # Abstract location/Role
                "positive",  # Abstract value/Attitude
                "possibility",  # Abstract chance
                "posture",  # Abstract body position
                "potential",  # Abstract capability
                "power",  # Abstract concept/Energy unit
                "practice",  # Abstract activity
                "precedent",  # Abstract example
                "precision",  # Abstract property
                "prediction",  # Abstract forecast
                "preference",  # Abstract choice
                "prefix",  # Abstract language part
                "premise",  # Abstract starting idea
                "premium",  # Abstract value/Object type
                "presence",  # Abstract state of being
                "present",  # Abstract time/Gift object
                "pressure",  # Abstract force
                "prestige",  # Abstract concept
                "presumption",  # Abstract assumption
                "preview",  # Abstract view before
                "price",  # Abstract value
                "pride",  # Abstract emotion
                "primary",  # Abstract first/Main
                "prime",  # Abstract number type/Best state
                "primitive",  # Abstract basic type/Object
                "principal",  # Abstract main part/Role
                "principle",  # Abstract rule/Concept
                "print",  # Abstract copy/Action/Object
                "priority",  # Abstract order
                "prism",  # Abstract shape/Optical object
                "privacy",  # Abstract state
                "privilege",  # Abstract right
                "prize",  # (award/trophy) - Abstract concept/Object
                "probability",  # Abstract chance
                "problem",  # Abstract situation
                "procedure",  # Abstract process
                "process",  # Abstract action sequence
                "prodigy",  # Abstract person type
                "product",  # Abstract result/Object
                "profile",  # Abstract outline/Description
                "profit",  # Abstract gain
                "program",  # Abstract plan/Software
                "progress",  # Abstract advancement
                "prohibition",  # Abstract rule
                "project",  # Abstract task/Object output
                "projection",  # Abstract display/Forecast
                "proof",  # Abstract evidence
                "property",  # Abstract characteristic/Ownership/Place
                "proportion",  # Abstract relation
                "proposal",  # Abstract suggestion
                "prose",  # Abstract writing style
                "prospect",  # Abstract possibility/View
                "protection",  # Abstract concept/Object
                "protocol",  # Abstract procedure
                "prototype",  # Abstract first model
                "proverb",  # Abstract saying
                "provision",  # Abstract supply/Clause
                "proximity",  # Abstract closeness
                "proxy",  # Abstract substitute
                "psychology",  # Abstract subject
                "publication",  # Abstract work/Action
                "pulse",  # Abstract beat/Signal
                "punctuation",  # Abstract marks
                "pupil",  # Abstract student/Eye part
                "purchase",  # Abstract action/Object
                "purity",  # Abstract state
                "purpose",  # Abstract reason
                "puzzle",  # Abstract problem/Object
                "quadrant",  # Abstract section
                "qualification",  # Abstract property
                "quality",  # Abstract property
                "quantity",  # Abstract amount
                "quartet",  # Abstract group of four
                "query",  # Abstract question
                "question",  # Abstract inquiry
                "queue",  # (line)
                "quickness",  # (speed)
                "quiet",  # Abstract state
                "quintessence",  # Abstract core idea
                "quota",  # Abstract limit
                "quotation",  # Abstract citation/Price
                "quotient",  # Abstract math result
                "race",  # Abstract competition/Group/Event
                "radian",  # Abstract angle unit
                "radiation",  # Abstract energy emission
                "radius",  # Abstract measurement
                "randomness",  # Abstract property
                "range",  # Abstract extent
                "rank",  # Abstract position
                "rate",  # Abstract speed/Value
                "ratio",  # Abstract relation
                "reaction",  # Abstract response
                "reading",  # Abstract action/Material
                "reality",  # Abstract state
                "reason",  # Abstract cause/Faculty
                "rebellion",  # Abstract action
                "receipt",  # Abstract proof of purchase/Object
                "recipe",  # Abstract instructions
                "recognition",  # Abstract process
                "recommendation",  # Abstract suggestion
                "record",  # Abstract information/Object
                "rectangle",  # Abstract shape
                "recursion",  # Abstract process
                "reduction",  # Abstract decrease
                "redundancy",  # Abstract excess
                "reference",  # Abstract connection/Source
                "reflection",  # Abstract image/Thought/Action
                "reform",  # Abstract change
                "refrain",  # Abstract music part/Action
                "refund",  # Abstract repayment
                "refusal",  # Abstract denial
                "regard",  # Abstract consideration/View
                "region",  # Abstract area
                "register",  # Abstract list/Device
                "regression",  # Abstract movement back
                "regulation",  # Abstract rule
                "rehearsal",  # (practice)
                "rejection",  # (refusal)
                "relation",  # Abstract connection
                "relationship",  # (relation)
                "relative",  # Abstract relation/Person
                "relaxation",  # Abstract state
                "release",  # Abstract action/Version
                "reliability",  # Abstract property
                "relief",  # Abstract feeling/Sculpture type
                "religion",  # Abstract system
                "remainder",  # Abstract part left
                "remark",  # (comment)
                "remedy",  # Abstract solution
                "reminder",  # Abstract prompt
                "rent",  # Abstract payment/Tear
                "repair",  # Abstract action
                "repeat",  # Abstract action
                "repetition",  # Abstract occurrence
                "replacement",  # Abstract substitute
                "reply",  # Abstract response
                "report",  # Abstract information/Document
                "representation",  # Abstract depiction
                "request",  # Abstract inquiry
                "requirement",  # Abstract need
                "rescue",  # Abstract action
                "research",  # Abstract activity
                "resemblance",  # Abstract similarity
                "reservation",  # Abstract booking/Doubt
                "reset",  # Abstract action
                "residence",  # Abstract place/Act
                "residue",  # (remainder)
                "resistance",  # Abstract opposition
                "resolution",  # Abstract decision/Clarity
                "resource",  # Abstract supply
                "respect",  # Abstract feeling/Aspect
                "response",  # Abstract answer
                "responsibility",  # Abstract duty
                "rest",  # Abstract pause/Remainder
                "restriction",  # Abstract limit
                "result",  # Abstract outcome
                "resume",  # Abstract summary/Action
                "retention",  # Abstract keeping
                "retirement",  # Abstract state/Action
                "retreat",  # Abstract movement back/Place
                "return",  # Abstract movement back/Profit
                "reunion",  # Abstract event
                "revelation",  # Abstract disclosure
                "revenge",  # Abstract action
                "revenue",  # Abstract income
                "reverse",  # Abstract opposite/Action
                "review",  # Abstract assessment/Action
                "revision",  # Abstract change/Version
                "revival",  # Abstract return to life/Event
                "revolution",  # Abstract turn/Uprising
                "reward",  # (prize)
                "rhetoric",  # Abstract language use
                "rhombus",  # Abstract shape
                "rhyme",  # Abstract sound correspondence
                "rhythm",  # Abstract pattern
                "riddle",  # Abstract puzzle/Question
                "right",  # Abstract direction/Correctness/Entitlement
                "rigor",  # Abstract strictness
                "risk",  # Abstract chance of loss
                "rite",  # (ritual)
                "ritual",  # Abstract ceremony
                "rivalry",  # Abstract competition
                "role",  # Abstract function/Part
                "romance",  # Abstract relationship/Genre
                "rotation",  # Abstract movement
                "round",  # Abstract shape/Period/Action
                "route",  # (path)
                "routine",  # Abstract pattern/Procedure
                "row",  # Abstract line
                "royalty",  # Abstract status/Payment
                "rule",  # Abstract regulation/Tool
                "rumor",  # Abstract information
                "run",  # Abstract action/Sequence
                "rupture",  # Abstract break
                "rush",  # Abstract hurried action
                "sabotage",  # Abstract action
                "sacrifice",  # Abstract action/Offering
                "sadness",  # Abstract emotion
                "safety",  # Abstract state
                "salary",  # Abstract payment
                "sale",  # Abstract event/Action
                "salute",  # Abstract gesture
                "salvation",  # Abstract rescue/State
                "sample",  # Abstract part/Example
                "sanction",  # Abstract permission/Penalty
                "sanctuary",  # Abstract place/State
                "satisfaction",  # Abstract feeling
                "saturation",  # Abstract state
                "scale",  # Abstract series/Ratio/Device/Body part
                "scan",  # Abstract action/Image
                "scandal",  # Abstract event
                "scar",  # Abstract mark/Body feature
                "scarcity",  # Abstract lack
                "scenario",  # Abstract situation
                "scene",  # Abstract setting/Part of play
                "scent",  # Abstract smell
                "schedule",  # Abstract plan/List
                "schema",  # (diagram/plan)
                "scheme",  # (plan/plot)
                "scholarship",  # Abstract funding/Learning
                "science",  # Abstract subject/Method
                "scope",  # Abstract extent/Device
                "score",  # Abstract number/Music sheet
                "scorn",  # Abstract feeling
                "scratch",  # Abstract mark/Action
                "screenplay",  # Abstract script
                "script",  # Abstract writing/Code
                "scrutiny",  # Abstract examination
                "sculpture",  # Abstract art form/Object
                "seal",  # Abstract closure/Symbol/Animal/Stamp
                "search",  # Abstract action
                "season",  # Abstract time period/Flavoring
                "seclusion",  # Abstract state
                "second",  # Abstract time unit/Position
                "secret",  # Abstract hidden information
                "section",  # Abstract part
                "sector",  # Abstract area/Part
                "security",  # Abstract safety/Group
                "sedition",  # Abstract action
                "segment",  # Abstract part
                "selection",  # Abstract choice/Group
                "self",  # Abstract entity
                "semantics",  # Abstract meaning study
                "semblance",  # Abstract appearance
                "semicircle",  # Abstract shape
                "seminar",  # Abstract event
                "sensation",  # Abstract feeling/Event
                "sense",  # Abstract faculty/Meaning
                "sentence",  # Abstract language unit/Punishment
                "sentiment",  # Abstract feeling
                "separation",  # Abstract state/Action
                "sequence",  # Abstract order
                "sequin",  # Object/Decoration element
                "series",  # Abstract sequence
                "sermon",  # Abstract speech
                "service",  # Abstract action/System
                "session",  # Abstract period
                "set",  # Abstract group/Action
                "setting",  # Abstract context/Place/Configuration
                "setup",  # Abstract arrangement
                "severity",  # Abstract degree
                "sex",  # (gender)
                "shade",  # Abstract color variation/Object
                "shadow",  # Abstract dark shape
                "shape",  # Abstract form
                "share",  # Abstract part/Action
                "sharpness",  # Abstract property
                "shell",  # Abstract outer layer/Object (shell1/2/3 ambiguity)
                "shelter",  # Abstract protection/Place
                "shift",  # Abstract change/Work period
                "shock",  # Abstract event/Feeling
                "shortage",  # (scarcity)
                "shortcut",  # Abstract path
                "show",  # Abstract event/Display
                "side",  # Abstract surface/Position/Group
                "siege",  # Abstract event
                "sight",  # Abstract sense/View
                "sign",  # Abstract mark/Symbol/Action
                "signal",  # Abstract sign/Wave
                "signature",  # Abstract name written/Mark
                "significance",  # Abstract importance
                "silence",  # Abstract lack of sound
                "silhouette",  # Abstract outline shape
                "similarity",  # Abstract property
                "simile",  # Abstract comparison
                "simplicity",  # Abstract property
                "simulation",  # Abstract imitation
                "simultaneity",  # Abstract occurrence together
                "sin",  # Abstract transgression
                "sincerity",  # Abstract quality
                "single",  # Abstract one/Status
                "singular",  # Abstract one/Grammar
                "situation",  # Abstract circumstances
                "size",  # Abstract dimension
                "sketch",  # Abstract drawing/Plan
                "skill",  # Abstract ability
                "skip",  # Abstract action
                "skyline",  # Abstract outline
                "slander",  # Abstract false statement
                "slant",  # Abstract angle/Bias
                "slice",  # Abstract part/Action
                "slope",  # Abstract incline
                "slot",  # Abstract opening/Position
                "slowness",  # Abstract property
                "slump",  # Abstract decline
                "smell",  # Abstract sense/Odor
                "smile",  # Abstract expression/Action
                "smoke",  # Abstract substance/Action
                "smoothness",  # Abstract property
                "smudge",  # Abstract mark
                "snap",  # Abstract action/Sound
                "snare",  # Abstract trap/Drum part
                "sobriety",  # Abstract state
                "society",  # Abstract group
                "softness",  # Abstract property
                "software",  # Abstract program
                "soil",  # Abstract ground/Dirt material
                "solace",  # Abstract comfort
                "solemnity",  # Abstract seriousness
                "solidity",  # Abstract property
                "soliloquy",  # Abstract speech
                "solitude",  # Abstract state
                "solution",  # Abstract answer/Mixture
                "solvency",  # Abstract financial state
                "some",  # Abstract quantity
                "sonata",  # Abstract music form
                "song",  # Abstract music piece
                "sophistication",  # Abstract quality
                "sorcery",  # (magic)
                "sorrow",  # (sadness)
                "sort",  # Abstract type/Action
                "soul",  # Abstract essence
                "sound",  # Abstract wave/Perception
                "source",  # Abstract origin
                "souvenir",  # Abstract object reminder
                "sovereignty",  # Abstract authority
                "space",  # Abstract area/Outer space
                "span",  # Abstract extent/Duration
                "spark",  # Abstract light particle/Beginning
                "sparkle",  # Abstract light effect
                "specialty",  # Abstract area of expertise
                "species",  # Abstract biological category
                "specific",  # Abstract particular item
                "specification",  # Abstract detailed description
                "specimen",  # (sample)
                "speck",  # Abstract small mark
                "spectacle",  # Abstract event/Eyewear
                "spectator",  # Abstract viewer role
                "spectrum",  # Abstract range
                "speculation",  # Abstract thought/Risk
                "speech",  # Abstract communication/Act
                "speed",  # Abstract rate of motion
                "spell",  # Abstract word sequence/Magic effect
                "sphere",  # Abstract shape
                "spin",  # Abstract rotation/Bias
                "spirit",  # Abstract essence/Mood/Alcohol
                "spite",  # Abstract feeling
                "splash",  # Abstract liquid impact/Mark
                "splendor",  # Abstract magnificence
                "splinter",  # Abstract small piece/Object
                "split",  # Abstract division/Action
                "spoilage",  # Abstract decay
                "spontaneity",  # Abstract quality
                "sport",  # Abstract activity
                "spot",  # Abstract location/Mark
                "spotlight",  # Abstract light beam/Attention
                "spread",  # Abstract extent/Action/Food item
                "spring",  # Abstract season/Device/Source
                "spurt",  # Abstract sudden burst
                "spy",  # Abstract role/Action
                "squad",  # Abstract group
                "square",  # Abstract shape/Area
                "squat",  # Abstract action/Position
                "squeeze",  # Abstract action
                "stability",  # Abstract property
                "stack",  # Abstract pile/Arrangement
                "stadium",  # Place/Abstract venue concept
                "stage",  # Abstract phase/Platform object
                "stain",  # Abstract mark/Colorant
                "stamina",  # Abstract endurance
                "stance",  # Abstract position/Viewpoint
                "standard",  # Abstract level/Type/Flag
                "stanza",  # Abstract poem part
                "staple",  # Abstract main part/Object fastener
                "star",  # Abstract celestial body/Shape/Symbol/Person
                "start",  # Abstract beginning
                "state",  # Abstract condition/Area/Government
                "statement",  # Abstract declaration
                "station",  # Abstract place/Position
                "statistic",  # Abstract number data
                "status",  # Abstract condition/Rank
                "statute",  # Abstract law
                "stay",  # Abstract duration/Action
                "steadiness",  # (stability)
                "steam",  # Abstract vapor/Power
                "stereotype",  # Abstract fixed idea
                "sterility",  # Abstract property/State
                "stigma",  # Abstract mark of disgrace
                "stillness",  # (quiet)
                "stimulus",  # Abstract trigger
                "stipulation",  # Abstract condition
                "stock",  # Abstract supply/Shares/Broth/Gun part
                "stoicism",  # Abstract attitude
                "stop",  # Abstract end/Action/Place/Object
                "storage",  # Abstract action/Place
                "storm",  # Abstract weather event/Uproar
                "story",  # Abstract narrative
                "strain",  # Abstract effort/Type/Injury/Filter action
                "strait",  # Abstract difficulty/Waterway
                "strand",  # Abstract thread/Beach area/Leave behind
                "stranger",  # Abstract person type
                "strategy",  # Abstract plan
                "stratum",  # (layer)
                "streak",  # Abstract line/Period
                "stream",  # Abstract flow/Water body
                "strength",  # Abstract property
                "stress",  # Abstract pressure/Emphasis
                "stretch",  # Abstract extension/Action
                "strictness",  # (rigor)
                "stride",  # Abstract step/Progress
                "strife",  # Abstract conflict
                "strike",  # Abstract action/Event
                "strip",  # Abstract narrow piece/Action
                "stripe",  # Abstract line pattern
                "stroke",  # Abstract action/Mark/Medical event
                "structure",  # Abstract arrangement/Building
                "struggle",  # Abstract effort/Conflict
                "stubbornness",  # Abstract quality
                "student",  # Abstract role
                "study",  # Abstract activity/Room
                "stuff",  # Abstract material/Things
                "stumble",  # Abstract action
                "stupidity",  # Abstract quality
                "stupor",  # Abstract state
                "style",  # Abstract manner/Fashion
                "subject",  # Abstract topic/Person under rule/Grammar part
                "sublime",  # Abstract quality
                "submission",  # Abstract yielding/Document
                "subordinate",  # Abstract rank/Person
                "subpoena",  # Abstract legal document
                "subscription",  # Abstract agreement/Payment
                "subsection",  # (section)
                "subsequence",  # Abstract following part
                "subsidence",  # Abstract sinking
                "subsidy",  # Abstract payment
                "substance",  # Abstract material/Core part
                "substitute",  # Abstract replacement
                "substratum",  # (layer) - Underlying layer
                "subtlety",  # Abstract quality
                "subtraction",  # Abstract math operation
                "suburb",  # Abstract area type
                "subversion",  # Abstract undermining action
                "success",  # Abstract outcome
                "succession",  # Abstract sequence following
                "succor",  # (help)
                "suddenness",  # Abstract quality
                "suffering",  # Abstract state
                "sufficiency",  # Abstract adequacy
                "suffix",  # Abstract language part
                "suggestion",  # Abstract idea/Trace
                "suicide",  # Abstract action
                "suitability",  # Abstract quality
                "sum",  # Abstract total
                "summary",  # Abstract brief account
                "summer",  # Abstract season
                "summit",  # Abstract meeting/Peak
                "summons",  # Abstract call/Document
                "sunbeam",  # Ray of light/Abstract concept
                "superfluity",  # (redundancy)
                "superiority",  # Abstract quality
                "superlative",  # Abstract highest degree
                "superstition",  # Abstract belief
                "supervision",  # Abstract oversight
                "supplement",  # Abstract addition
                "supply",  # Abstract stock/Action
                "support",  # Abstract help/Structure
                "supposition",  # (assumption)
                "suppression",  # Abstract action of stopping
                "supremacy",  # Abstract highest authority
                "surcharge",  # Abstract extra charge
                "surface",  # Abstract outer layer/Area
                "surge",  # Abstract sudden increase/Wave
                "surgery",  # Abstract medical procedure
                "surname",  # (name)
                "surpass",  # Abstract action of exceeding
                "surprise",  # Abstract feeling/Event
                "surrender",  # Abstract action of giving up
                "surrogate",  # (substitute)
                "surroundings",  # Abstract environment
                "surveillance",  # Abstract watching
                "survey",  # Abstract examination/Questionnaire
                "survival",  # Abstract state of continuing
                "suspect",  # Abstract person/Idea
                "suspense",  # Abstract feeling
                "suspicion",  # Abstract feeling/Idea
                "sustenance",  # Abstract food/Support
                "sway",  # Abstract influence/Movement
                "swearword",  # Abstract type of word
                "sweep",  # Abstract action/Range
                "sweetness",  # Abstract taste/Quality
                "swiftness",  # (speed)
                "swirl",  # Abstract rotating movement/Shape
                "syllable",  # Abstract language unit
                "symbol",  # Abstract representation
                "symmetry",  # Abstract property
                "sympathy",  # Abstract feeling
                "symphony",  # Abstract music piece/Harmony
                "symposium",  # Abstract meeting
                "symptom",  # Abstract sign of condition
                "synchronicity",  # Abstract simultaneous occurrence
                "syndicate",  # Abstract group
                "syndrome",  # Abstract set of symptoms
                "synergy",  # Abstract combined effect
                "synonym",  # Abstract word with same meaning
                "synopsis",  # (summary)
                "synthesis",  # Abstract combination
                "system",  # Abstract organized set
                "taboo",  # Abstract prohibition
                "tack",  # Abstract course/Object fastener
                "tactic",  # Abstract method
                "tag",  # Abstract label/Game/Action
                "talent",  # Abstract ability
                "talisman",  # Abstract object with power
                "talk",  # Abstract communication/Speech
                "tangent",  # Abstract line/Digression
                "tangle",  # Abstract messy state/Knot
                "task",  # Abstract piece of work
                "taste",  # Abstract sense/Preference/Style
                "tax",  # Abstract payment
                "teaching",  # Abstract activity
                "team",  # Abstract group
                "tear",  # Abstract drop of liquid/Rip
                "technique",  # Abstract method
                "technology",  # Abstract application of knowledge
                "temper",  # Abstract mood/Hardness
                "temperament",  # Abstract nature
                "temperature",  # Abstract measurement
                "template",  # Abstract pattern/Guide
                "tempo",  # Abstract speed (music)
                "temptation",  # Abstract lure
                "tenacity",  # Abstract quality
                "tendency",  # Abstract inclination
                "tender",  # Abstract offer/State/Person
                "tenet",  # Abstract principle
                "tenor",  # Abstract general meaning/Voice part
                "tension",  # Abstract state of stretching/Stress
                "term",  # Abstract word/Period/Condition
                "termination",  # Abstract end
                "terminology",  # Abstract set of terms
                "terminus",  # Abstract end point
                "terrain",  # Abstract land features
                "terror",  # Abstract feeling
                "test",  # Abstract examination/Trial
                "testament",  # Abstract will/Evidence
                "testimonial",  # Abstract recommendation/Statement
                "testimony",  # Abstract evidence/Statement
                "text",  # Abstract written words
                "texture",  # Abstract surface quality
                "theft",  # Abstract act
                "theme",  # Abstract topic/Melody
                "theology",  # Abstract study
                "theorem",  # Abstract statement proved
                "theory",  # Abstract idea/System
                "therapy",  # Abstract treatment
                "thesis",  # Abstract statement/Dissertation
                "thickness",  # Abstract dimension
                "thirst",  # Abstract feeling/Desire
                "thought",  # Abstract idea/Process
                "thrall",  # Abstract state of bondage
                "threat",  # Abstract danger/Warning
                "threshold",  # Abstract level/Doorway part
                "thrill",  # Abstract feeling/Event
                "throb",  # Abstract beat/Pain
                "thrust",  # Abstract push/Force/Meaning
                "ticket",  # Abstract voucher/Object
                "tidiness",  # Abstract state
                "tilt",  # Abstract slant/Action
                "time",  # Abstract dimension/Occurrence
                "timeliness",  # Abstract quality
                "tint",  # (shade)
                "tip",  # Abstract end point/Hint/Money/Action
                "title",  # Abstract name/Rank/Right
                "token",  # Abstract symbol/Object representation
                "tolerance",  # Abstract acceptance/Range
                "tone",  # Abstract sound quality/Attitude/Color shade
                "topic",  # Abstract subject
                "topography",  # Abstract land features study/Arrangement
                "topology",  # Abstract mathematical study
                "torch",  # Abstract light source/Symbol
                "torment",  # Abstract suffering
                "torsion",  # Abstract twisting force
                "total",  # Abstract sum/Complete
                "touch",  # Abstract sense/Action/Contact
                "toughness",  # Abstract quality
                "tour",  # Abstract journey/Performance series
                "tournament",  # Abstract competition
                "trace",  # Abstract mark/Small amount/Action
                "track",  # Abstract path/Mark/Recording/Sport event
                "traction",  # Abstract grip/Pulling force
                "trade",  # Abstract exchange/Occupation
                "trademark",  # Abstract symbol/Brand identifier
                "tradition",  # Abstract custom/Belief
                "traffic",  # Abstract movement/Trade
                "tragedy",  # Abstract event/Play genre
                "trail",  # Abstract path/Mark left behind
                "trait",  # Abstract characteristic
                "traitor",  # Abstract person type
                "trajectory",  # Abstract path
                "transaction",  # Abstract exchange/Event
                "transcendence",  # Abstract state beyond limits
                "transcript",  # Abstract written record
                "transfer",  # Abstract movement/Action
                "transformation",  # Abstract change
                "transgression",  # (sin)
                "transition",  # Abstract change/Movement
                "translation",  # Abstract conversion/Version
                "transmission",  # Abstract sending/Vehicle part
                "transparency",  # Abstract quality/Object
                "transport",  # Abstract action/System
                "transposition",  # Abstract change of position
                "trap",  # Abstract situation/Device
                "trauma",  # Abstract injury/Experience
                "travel",  # Abstract movement/Action
                "traverse",  # Abstract action of crossing
                "travesty",  # Abstract distorted representation
                "treachery",  # Abstract betrayal
                "tread",  # Abstract step sound/Pattern/Action
                "treason",  # Abstract crime
                "treasure",  # Abstract valuables/Concept
                "treatment",  # Abstract handling/Medical care
                "treaty",  # Abstract agreement
                "treble",  # Abstract high pitch/Triple amount
                "trend",  # Abstract direction/Fashion
                "trepidation",  # Abstract fear
                "trespass",  # Abstract intrusion/Action
                "trial",  # Abstract test/Legal process/Attempt
                "triangle",  # Abstract shape/Instrument
                "tribe",  # Abstract group
                "tribulation",  # Abstract suffering
                "tribunal",  # Abstract court
                "tribute",  # Abstract payment/Acknowledgement
                "trick",  # Abstract deception/Skillful act
                "trickle",  # Abstract slow flow
                "trigger",  # Abstract cause/Device part
                "trilogy",  # Abstract group of three works
                "trim",  # Abstract edge/Action/Condition
                "trinity",  # Abstract group of three
                "trio",  # Abstract group of three
                "trip",  # Abstract journey/Stumble/Drug experience
                "triumph",  # Abstract victory/Joy
                "triviality",  # Abstract unimportance
                "troop",  # Abstract group
                "trope",  # Abstract figure of speech/Theme
                "trouble",  # Abstract difficulty/Effort
                "truce",  # Abstract agreement to stop fighting
                "true",  # Abstract value/Correctness
                "trust",  # Abstract belief/Arrangement
                "truth",  # Abstract reality/Correctness
                "tryst",  # Abstract meeting
            ],
        },
        "Buildings_Vehicles_Outdoor": {
            "Buildings": [
                "abbey",  # (monastery)
                "airport",  # Implied building complex
                "apartment_building",  # Implied
                "arcade",  # Building type
                "auditorium",  # Building part
                "bakery",  # (shop)
                "bank",  # Building
                "barn",
                "barracks",  # Building type
                "basilica",  # (church)
                "boathouse",
                "bookshop",
                "bowling_alley",  # Implied building
                "bungalow",  # (house)
                "cabin",  # Building type
                "capitol",  # Building
                "casino",  # Building
                "castle",  # Building
                "cathedral",  # (church)
                "chapel",  # (church)
                "church",
                "cinema",  # Building
                "city_hall",  # (capitol)
                "clinic",  # (hospital)
                "clubhouse",  # Building
                "college",  # (school)
                "condominium",  # (apartment_building)
                "conservatory",  # (greenhouse)
                "courthouse",  # Building
                "dormitory",  # Building
                "duplex",  # (house)
                "factory",  # Building
                "fire_station",  # Building
                "fortress",  # (castle)
                "foundry",  # (factory)
                "garage",  # Building part or standalone
                "gas_station",  # Building complex
                "gazebo",  # Structure, often building-like
                "greenhouse",  # Building
                "gymnasium",  # Building
                "hangar",  # Building
                "hospital",  # Building
                "hostel",  # (hotel)
                "hotel",  # Building
                "house",  # Building
                "hut",  # Building
                "igloo",  # Structure/Building
                "inn",  # (hotel)
                "jail",  # (prison)
                "kennel",  # Structure/Building
                "kindergarten",  # (school)
                "laboratory",  # Building part
                "library",  # Building
                "lighthouse",  # Building/Structure
                "lodge",  # (house/hotel)
                "loft",  # Building part
                "lumbermill",  # Building complex
                "mansion",  # (house/palace)
                "mausoleum",  # Building
                "mill",  # Building
                "mine",  # Structure complex
                "mobile_home",  # Structure/Vehicle
                "monastery",  # Building
                "motel",  # (hotel)
                "mosque",  # Building
                "museum",  # Building
                "observatory",  # Building
                "office_building",  # Implied
                "orphanage",  # Building
                "palace",  # Building
                "parsonage",  # (house)
                "planetarium",  # Building
                "police_station",  # Building
                "post_office",  # Building
                "power_plant",  # Building complex
                "prison",  # Building
                "pub",  # (shop)
                "quonset_hut",  # (hut)
                "restaurant",  # Building/Shop
                "saloon",  # (shop)
                "sawmill",  # (lumbermill)
                "school",  # Building
                "shack",  # (hut)
                "shed",  # Building
                "shelter",  # Structure/Building
                "shop",  # Building
                "shopping_mall",  # Building complex
                "skyscraper",  # Building
                "stable",  # (barn)
                "stadium",  # Structure/Building
                "store",  # (shop)
                "studio",  # Building part
                "supermarket",  # (shop)
                "synagogue",  # Building
                "tavern",  # (shop)
                "temple",  # Building
                "tent",  # Structure
                "theater",  # Building
                "tobacco_shop",  # Shop
                "tollbooth",  # Structure
                "tomb",  # Structure
                "tower",  # Building/Structure
                "townhouse",  # (house)
                "university",  # (school)
                "vault",  # Building part
                "villa",  # (house)
                "warehouse",  # Building
                "windmill",  # Building/Structure
                "winery",  # Building complex
                "workshop",  # (studio)
                "yurt",  # Structure/Building
            ],
            "Outdoor_Structures_Features": [
                "amusement_park",  # Complex
                "arch",
                "arena",  # (stadium)
                "aqueduct",  # Structure
                "awning",
                "bandstand",  # Structure
                "barricade",  # Structure
                "beacon",  # Structure
                "bell_cote",  # Structure part
                "boardwalk",  # Structure
                "breakwater",  # Structure
                "bridge",  # Structure
                "bunker",  # Structure
                "buoy",  # Marker structure
                "canal",  # Structure
                "carousel",  # Structure/Ride
                "causeway",  # Structure
                "cemetery",  # Complex
                "column",  # Structure part
                "cornice",  # Structure part
                "court",  # Tennis court etc.
                "crane",  # Structure/Machine
                "curb",  # Structure feature
                "dam",  # Structure
                "deck",  # Structure
                "derrick",  # (drilling_platform)
                "dike",  # (dam)
                "dock",  # Structure
                "dome",  # Structure part
                "drilling_platform",  # Structure
                "driveway",  # Structure feature
                "fairground",  # Complex
                "fence",
                "fencepost",  # Structure part
                "ferris_wheel",  # Structure/Ride
                "fire_escape",  # Structure part
                "fire_hydrant",  # Structure fixture
                "fire_pit",  # Structure
                "flagpole",  # Structure
                "footbridge",  # (bridge)
                "fort",  # (castle)
                "fountain",  # Structure/Decor
                "freeway",  # (road)
                "gallows",  # Structure
                "garden",  # Complex feature
                "gate",
                "goalpost",  # Structure
                "grandstand",  # Structure
                "graveyard",  # (cemetery)
                "grill",  # Outdoor cooking structure
                "guardrail",  # Structure
                "gully",  # Natural feature, but used like structure
                "gutter",  # Structure part
                "harbor",  # Complex feature
                "highway",  # (road)
                "horizontal_bar",  # Structure/Equipment
                "hot_tub",  # Structure/Household
                "hydrant",  # Structure fixture
                "jetty",  # (dock)
                "junkyard",  # Complex feature
                "kiosk",  # Structure
                "lamppost",  # Structure fixture
                "landing",  # Structure feature
                "lane",  # (road)
                "latrine",  # (toilet) - Outdoor context
                "lawn",  # Feature
                "levee",  # (dam)
                "lock",  # Canal structure
                "manhole",  # Structure access
                "market",  # Complex feature (outdoor)
                "maypole",  # Structure/Decor
                "maze",  # Structure
                "memorial",  # Structure/Decor
                "minaret",  # (tower)
                "monument",  # Structure/Decor
                "mooring",  # (dock)
                "mound",  # Natural/Artificial structure
                "obelisk",  # Structure/Decor
                "oilrig",  # (drilling_platform)
                "pagoda",  # Building/Structure
                "parapet",  # Structure part
                "parking_garage",  # Building/Structure
                "parking_lot",  # Complex feature
                "parking_meter",  # Structure fixture
                "patio",  # Structure feature
                "pavilion",  # (gazebo)
                "pedestal",  # Structure base
                "pergola",  # Structure
                "phone_booth",  # Structure
                "photo_booth",  # Structure
                "picket_fence",  # Structure
                "pier",  # Structure
                "pillar",  # (column)
                "pipeline",  # Structure
                "pit",  # Excavation feature
                "playground",  # Complex feature
                "plaza",  # Complex feature
                "pool",  # (swimming_pool)
                "porch",  # Structure part
                "pothole",  # Road feature/damage
                "power_line",  # Structure
                "promenade",  # (boardwalk/road)
                "pyramid",  # Structure
                "quay",  # (dock)
                "railing",  # Structure part
                "ramp",  # Structure feature
                "reservoir",  # Structure/Feature
                "rest_stop",  # Complex feature
                "road",  # Structure feature
                "road_sign",  # Structure fixture
                "runway",  # Airport structure
                "scaffold",
                "scaffolding",  # Temporary structure
                "seesaw",  # Playground structure
                "sewage",  # System/Feature
                "sign",  # (road_sign)
                "signpost",  # (flagpole)
                "silo",  # Structure
                "skatepark",  # Complex feature
                "slide",  # Playground structure
                "sluice",  # (lock)
                "solar_dish",  # Structure/Device
                "spire",  # Structure part
                "sprinkler",  # System fixture
                "square",  # (plaza)
                "stage",  # Structure
                "stair",
                "staircase",  # (stair)
                "steeple",  # (spire)
                "stone_wall",  # Structure
                "street",  # (road)
                "streetlight",  # Structure fixture
                "stupa",  # Structure/Building
                "subway_station",  # Building/Structure complex
                "swimming_pool",  # Structure/Household
                "telephone_pole",  # Structure
                "terrace",  # Structure feature
                "tollbooth",  # Structure
                "track",  # Rail/Race track
                "trail",  # Path feature
                "trellis",  # Structure
                "trestle",  # (bridge)
                "tunnel",  # Structure
                "turnstile",  # Structure fixture
                "underpass",  # Structure
                "viaduct",  # Structure
                "walkway",  # (path)
                "wall",  # Structure
                "water_tower",  # Structure
                "waterfall",  # Natural feature, sometimes artificial structure
                "waterwheel",  # Structure/Device
                "well",  # Structure
                "wharf",  # (dock)
                "worm_fence",  # Structure
                "yard",  # Feature
            ],
            "Building_Parts_Architectural_Elements": [
                "alcove",  # Part
                "archway",  # (arch)
                "attic",  # Part
                "balcony",  # Part
                "bannister",  # Part
                "baseboard",  # Part
                "basement",  # Part
                "bathroom",  # Room part
                "bay_window",  # (window)
                "beam",  # Part
                "bedroom",  # Room part
                "belfry",  # (bell_cote)
                "blind",  # Window covering part
                "buttress",  # Part
                "ceiling",  # Part
                "cellar",  # (basement)
                "chimney",  # Part
                "colonnade",  # Feature made of parts
                "cornice",  # Part
                "corridor",  # Part
                "courtyard",  # Feature part
                "cupola",  # Part
                "door",  # Part
                "doorframe",  # (door)
                "doorhandle",  # Part
                "doorknob",  # Part
                "doorknocker",  # Part
                "doorstep",  # (door)
                "doorstop",  # Household item/Part
                "doorway",  # (door)
                "dormer",  # (window)
                "drain",  # Part fixture
                "drainpipe",  # (gutter)
                "eave",  # Part
                "elevator",  # Part/System
                "entrance",  # (doorway)
                "escalator",  # Part/System
                "facade",  # Part
                "fireplace",  # Part/Fixture
                "floor",  # Part
                "flue",  # (chimney)
                "foundation",  # Part
                "foyer",  # Part
                "frame",  # Window/Door part
                "gable",  # Part
                "gallery",  # Part
                "garage_door",  # (door)
                "gatepost",  # (fencepost)
                "girder",  # (beam)
                "grate",  # Part fixture
                "grille",  # Architectural grille
                "gutter",  # Part
                "hall",  # (corridor)
                "hallway",  # (corridor)
                "handrail",  # (bannister)
                "hearth",  # Part
                "hinge",  # Part fixture
                "joist",  # (beam)
                "keyhole",  # Part fixture
                "kitchen",  # Room part
                "knob",  # Part fixture
                "landing",  # Part
                "latch",  # Part fixture
                "lattice",  # Part feature
                "lintel",  # Part
                "lobby",  # (foyer)
                "loft",  # Part
                "louver",  # Part
                "mantelpiece",  # Part feature
                "molding",  # Part feature
                "mullion",  # (window part)
                "newel",  # (bannister part)
                "niche",  # (alcove)
                "outlet",  # Part fixture
                "overhang",  # (eave)
                "panel",  # Part
                "pantry",  # Room part
                "parapet",  # Part
                "partition",  # (wall)
                "patio",  # Part feature
                "pediment",  # Part
                "pillar",  # Part
                "pilothouse",  # Part (boat/ship)
                "plaster",  # Material/Part
                "platform",  # Part feature
                "plumbing",  # System part
                "porch",  # Part
                "portal",  # (doorway)
                "porthole",  # Part fixture
                "post",  # Part
                "rafter",  # (beam)
                "riser",  # Stair part
                "roof",  # Part
                "room",  # General part
                "sash",  # Window part
                "screen",  # Window/Door screen
                "threshold",  # Door part
                "shingle",  # Roof part
                "shutter",  # Window part
                "siding",  # Wall part
                "sill",  # (windowsill)
                "skylight",  # (window)
                "slot",  # Opening part
                "spout",  # Part fixture
                "stairwell",  # (staircase)
                "steeple",  # Part
                "stud",  # Wall part
                "subfloor",  # (floor)
                "sump_pump",  # (pump) - Part fixture
                "terrace",  # Part feature
                "tile",  # Material/Part
                "tile_roof",  # Part
                "transom",  # Window part
                "trapdoor",  # Part
                "tread",  # Stair part
                "trim",  # (molding)
                "truss",  # Part
                "turret",  # Part
                "vault",  # Part feature
                "vent",  # Part fixture
                "vestibule",  # (foyer)
                "wainscoting",  # Wall part
                "wall",  # Part
                "window",  # Part
                "window_box",  # Part fixture
                "window_frame",  # (frame)
                "window_pane",  # (window)
                "window_screen",  # Part fixture
                "windowsill",  # Part
            ],
            "Geological_Landforms": [
                "arch",  # Natural arch
                "badlands",  # Landform
                "beach",  # (seashore)
                "bluff",  # (cliff)
                "boulder",
                "butte",  # Landform
                "canyon",  # Landform
                "cape",  # Landform
                "cave",  # Landform
                "cliff",
                "coast",  # (seashore)
                "continent",  # Landform
                "cove",  # Landform feature
                "crag",  # (cliff)
                "crater",  # Landform feature
                "crest",  # Hill/Wave top
                "crevasse",  # Landform feature
                "delta",  # Landform
                "desert",  # Landform
                "dune",  # Landform
                "earth",  # (dirt)
                "escarpment",  # (cliff)
                "fjord",  # Landform
                "forest",  # Biome feature
                "geyser",  # Landform feature
                "glacier",  # Landform feature
                "glen",  # (valley)
                "gorge",  # (canyon)
                "grotto",  # (cave)
                "gully",  # Landform feature
                "headland",  # (promontory)
                "hill",  # Landform
                "iceberg",  # Floating landform
                "island",  # Landform
                "isthmus",  # Landform
                "jungle",  # Biome feature
                "knoll",  # (hill)
                "lagoon",  # Landform feature
                "lake",  # Water body feature
                "land",  # General landform
                "lava",
                "marsh",  # Landform feature
                "meadow",  # Landform feature
                "mesa",  # Landform
                "moor",  # Landform feature
                "moraine",  # Landform feature
                "mountain",  # Landform
                "mud",  # Material/Feature
                "oasis",  # Landform feature
                "ocean",  # Water body feature
                "peak",  # (mountain top)
                "peninsula",  # Landform
                "plain",  # Landform
                "plateau",  # Landform
                "pond",  # Water body feature
                "prairie",  # Landform feature
                "precipice",  # (cliff)
                "promontory",  # Landform
                "quicksand",  # (sand) - Hazard feature
                "rapids",  # Water feature
                "ravine",  # (canyon)
                "reef",  # (coral) - Geological feature
                "ridge",  # Landform feature
                "rift",  # Landform feature
                "river",  # Water body feature
                "rock",  # Material/Feature
                "sandbar",  # Landform feature
                "savanna",  # Biome feature
                "sea",  # (ocean)
                "seashore",  # Landform feature
                "shore",  # (seashore)
                "slope",  # Landform feature
                "spring",  # Water feature
                "stalactite",  # Cave feature
                "stalagmite",  # Cave feature
                "steppe",  # Landform feature
                "strait",  # Water body feature
                "stream",  # Water body feature
                "summit",  # (peak)
                "swamp",  # (marsh)
                "taiga",  # Biome feature
                "tar_pit",  # Feature
                "tundra",  # Biome feature
                "valley",  # Landform
                "volcano",  # Landform
                "wadi",  # Landform feature
                "waterfall",  # Feature
                "watershed",  # Feature area
            ],
            "Weather_Atmospheric": [
                "air",  # Implied element
                "atmosphere",  # Implied layer
                "aurora",  # Phenomenon
                "blizzard",  # (snow) - Storm
                "cloud",
                "cyclone",  # Storm
                "dew",  # Phenomenon
                "drizzle",  # (rain)
                "drought",  # Condition
                "fog",  # Phenomenon
                "frost",  # (ice)
                "gale",  # (wind)
                "hail",
                "haze",  # Phenomenon
                "humidity",  # Condition
                "hurricane",  # (cyclone)
                "ice",
                "icicle",  # Ice formation
                "lightning",  # Phenomenon
                "mist",  # (fog)
                "monsoon",  # (rain/wind)
                "moonbeam",  # (light)
                "puddle",  # Rain result
                "rain",  # Phenomenon
                "rainbow",  # Phenomenon
                "sky",  # Implied atmospheric region
                "sleet",  # (hail/rain)
                "smog",  # Atmospheric condition
                "snow",
                "snowball",  # Snow formation
                "snowdrift",  # Snow formation
                "snowflake",  # Snow formation
                "steam",  # Water vapor
                "storm",  # General weather
                "sun",  # Celestial body/Weather influence
                "sunbeam",  # (light)
                "sunlight",  # (light)
                "sunrise",  # Phenomenon
                "sunset",  # Phenomenon
                "temperature",  # Condition
                "thaw",  # Process
                "thunder",  # Phenomenon
                "thunderstorm",  # (storm)
                "tornado",  # (cyclone)
                "typhoon",  # (cyclone)
                "vapor",  # (steam)
                "wind",  # Phenomenon
            ],
            "Minerals_Gems_Metals": [
                "aggregate",  # (gravel/sand)
                "alloy",  # (metal)
                "aluminum",  # (metal) - implied by foil
                "aluminum_foil",  # Product of metal
                "amber",  # Fossil resin/Gem
                "amethyst",  # (gem/crystal)
                "asbestos",  # Mineral
                "asphalt",  # Material derived from mineral
                "basalt",  # (rock)
                "bauxite",  # Mineral ore
                "brass",  # Metal alloy
                "bronze",  # Metal alloy
                "carbon",  # Element (charcoal/coal/diamond)
                "cement",  # Binder from minerals
                "chalk",  # Mineral rock
                "charcoal",  # Material from carbon
                "clay",  # Mineral soil
                "coal",  # Mineral rock
                "cobalt",  # Metal
                "concrete",  # Material from minerals
                "copper",  # Metal
                "corundum",  # Mineral (ruby/sapphire)
                "crystal1",
                "crystal2",  # Mineral formation
                "diamond",  # Mineral/Gem
                "dirt",  # Soil material
                "dust",  # Fine particles
                "emerald",  # Gem
                "feldspar",  # Mineral
                "flint",  # Rock
                "fossil",  # Mineralized remain
                "galena",  # Mineral ore
                "garnet",  # Gem
                "gem",  # General mineral stone
                "glass",  # Material from sand
                "gold",  # Metal
                "granite",  # Rock
                "graphite",  # Mineral (carbon)
                "gravel",  # Rock fragments
                "gypsum",  # Mineral
                "hematite",  # Mineral ore
                "iron",  # Metal
                "jade",  # Gem
                "jasper",  # Gem
                "lead",  # Metal
                "limestone",  # Rock
                "loam",  # (dirt)
                "magnetite",  # Mineral ore
                "malachite",  # Mineral/Gem
                "manganese",  # Metal
                "marble",  # Rock
                "mercury",  # Metal
                "metal",  # General category
                "mica",  # Mineral
                "mineral",  # General category
                "nickel",  # Metal
                "nitrate",  # Mineral salt
                "obsidian",  # (glass) - Volcanic rock
                "onyx",  # Gem
                "opal",  # Gem
                "ore",  # Mineral source
                "pebble",  # (stone)
                "peridot",  # Gem
                "pewter",  # Metal alloy
                "phosphate",  # Mineral salt
                "pitch",  # (tar) - Derived from mineral/organic
                "plaster",  # Material from gypsum
                "platinum",  # Metal
                "potash",  # Mineral salt
                "pumice",  # Rock
                "pyrite",  # Mineral
                "quartz",  # Mineral
                "rock_salt",  # (salt) - Mineral
                "ruby",  # Gem
                "rust",  # Metal oxide
                "salt",  # Mineral
                "sand",
                "sandstone",  # Rock
                "sapphire",  # Gem
                "sediment",  # Mineral particles
                "shale",  # Rock
                "silica",  # (sand/quartz)
                "silicon",  # Element from mineral
                "silver",  # Metal
                "slate",  # Rock
                "slag",  # Industrial byproduct
                "soapstone",  # Rock
                "solder",  # Metal alloy
                "steel",  # Metal alloy
                "stone",  # General rock
                "sulfur",  # Element/Mineral
                "talc",  # Mineral
                "tar",  # Mineral/Organic derived
                "tin",  # Metal
                "topaz",  # Gem
                "tourmaline",  # Gem
                "tungsten",  # Metal
                "turquoise",  # Gem
                "uranium",  # Metal
                "zinc",  # Metal
                "zircon",  # Gem
            ],
            "Water_Bodies_Features": [
                "aquifer",  # Underground water
                "bay",  # Water body
                "brook",  # (stream)
                "channel",  # Water body feature
                "creek",  # (stream)
                "current",  # Water movement
                "estuary",  # Water body feature
                "flood",  # Water event
                "geyser",  # Water feature
                "gulf",  # Water body
                "hot_spring",  # (spring)
                "inlet",  # Water body feature
                "lagoon",  # Water body feature
                "lake",  # Water body
                "marsh",  # Water/Land feature
                "ocean",  # Water body
                "pond",  # Water body
                "pool",  # Small water body
                "puddle",  # Small water body
                "rapids",  # Water feature
                "reservoir",  # Artificial water body
                "river",  # Water body
                "sea",  # Water body
                "seep",  # Water feature
                "sound",  # Water body
                "spring",  # Water source feature
                "strait",  # Water body feature
                "stream",  # Water body
                "surf",  # (wave)
                "swamp",  # Water/Land feature
                "tide",  # Water movement
                "tsunami",  # Water wave event
                "water",  # The substance
                "waterfall",  # Water feature
                "wave",  # Water feature
                "well",  # Water source structure
                "whirlpool",  # Water feature
            ],
            "Land_Vehicles": [
                "ambulance",
                "automobile",  # (car)
                "baby_buggy",
                "bicycle-built-for-two",
                "bike",
                "bulldozer",
                "buggy",
                "bus",
                "camper",
                "car",
                "carriage",
                "cart",
                "cement_mixer",
                "chariot",
                "convertible",  # Car type
                "dirt_bike",
                "dolly",  # Transport tool
                "dump_truck",  # (truck)
                "fire_engine",  # (firetruck)
                "firetruck",
                "forklift",
                "garbage_truck",
                "go-kart",
                "golf_cart",
                "golfcart",
                "handcar",  # Implied vehicle
                "hearse",
                "humvee",
                "jeep",
                "limousine",
                "minibus",
                "minivan",
                "moped",  # (motor_scooter)
                "motor_scooter",
                "motorcycle",
                "mountain_bike",
                "moving_van",
                "pickup",  # Truck type
                "police_car",
                "racer",
                "rickshaw",
                "road_sweeper",
                "roller_coaster",
                "school_bus",
                "scooter",
                "sedan",  # Car type
                "sidecar",
                "skateboard",
                "sled",
                "snowmobile",
                "snowplow",
                "sports_car",
                "station_wagon",
                "steamroller",
                "stroller",
                "subway",
                "suv",  # Car type
                "tanker_truck",  # (truck)
                "taxi",
                "tow_truck",
                "tractor",
                "trailer",
                "train",
                "train_car",
                "tricycle",
                "trolley",
                "trolleybus",
                "truck",
                "unicycle",
                "van",
                "wagon",
                "wheelbarrow",
                "wheelchair",
            ],
            "Air_Vehicles": [
                "aircraft_carrier",  # Also water
                "airboat",  # Air/Water
                "airplane",
                "airship",  # (blimp)
                "biplane",  # (airplane)
                "blimp",
                "bomber",  # (warplane)
                "fighter_jet",  # (warplane)
                "glider",  # Implied aircraft
                "helicopter",
                "hot-air_balloon",
                "jet",
                "parachute",  # Transportation/Safety
                "rocket",
                "seaplane",  # Air/Water
                "space_shuttle",
                "warplane",
            ],
            "Water_Vehicles": [
                "barge",  # Implied boat
                "battleship",  # (ship)
                "boat",
                "canoe",
                "catamaran",  # (boat)
                "container_ship",  # (ship)
                "cruise_ship",
                "destroyer",  # (ship)
                "dinghy",  # (boat)
                "ferry",
                "freighter",  # (ship)
                "gondola",
                "hovercraft",  # Water/Land
                "hydrofoil",  # (boat)
                "jetski",
                "kayak",
                "lifeboat",  # (boat)
                "liner",  # (cruise_ship)
                "motorboat",  # (speedboat)
                "paddlewheel",  # Part, implies boat
                "raft",
                "sailboat",
                "schooner",  # (sailboat)
                "ship",
                "speedboat",
                "submarine",
                "tanker",  # (ship)
                "trawler",  # (boat)
                "tugboat",
                "yacht",
            ],
            "Vehicle_Parts": [
                "airbag",
                "axle",  # Implied part
                "bumper",
                "car_door",
                "car_seat",
                "dashboard",
                "engine",
                "exhaust_pipe",
                "fender",  # Implied part
                "flywheel",  # (engine part)
                "gearshift",
                "grille",  # Vehicle grille
                "handbrake",
                "headlamp",
                "headlight",
                "hood",  # Car hood
                "hubcap",
                "license_plate",
                "mirror",  # rearview_mirror
                "muffler",  # (exhaust_pipe)
                "odometer",
                "propeller",
                "radiator",  # Vehicle radiator
                "rearview_mirror",
                "rim",
                "roof_rack",
                "rudder",
                "sail",
                "seatbelt",
                "skid",  # Landing gear part
                "spark_plug",
                "speedometer",
                "steering_wheel",
                "sunroof",
                "suspension",  # Implied part
                "tail_fin",  # (wing?)
                "taillight",
                "tire",  # (wheel)
                "transmission",  # Implied part
                "trunk",  # Car trunk
                "wheel",
                "windshield",
                "windshield_wiper",
                "wing",  # Vehicle wing
            ],
            "Other_Transport": [
                "conveyor_belt",  # Implied transport
                "crane",  # Transport tool
                "dumbwaiter",  # Building transport
                "escalator",  # Implied transport
                "lift",  # (ski_lift)
                "pipeline",  # Transport structure
                "ski_lift",
                "stretcher",  # Medical transport
                "towline",  # Implied transport
            ],
        },
    }

    # The list of words you provided
    missing_words = [
        "African_chameleon",
        "African_grey",
        "American_Staffordshire_terrier",
        "American_alligator",
        "American_coot",
        "American_egret",
        "American_lobster",
        "Appenzeller",
        "Arabian_camel",
        "Arctic_fox",
        "Band_Aid",
        "Bedlington_terrier",
        "Border_collie",
        "Boston_bull",
        "Bouvier_des_Flandres",
        "Brabancon_griffon",
        "Brittany_spaniel",
        "CD_player",
        "Chesapeake_Bay_retriever",
        "Christmas_stocking",
        "Crock_Pot",
        "Doberman",
        "Dutch_oven",
        "English_setter",
        "EntleBucher",
        "Eskimo_dog",
        "European_gallinule",
        "French_bulldog",
        "French_horn",
        "Gila_monster",
        "Gordon_setter",
        "Great_Pyrenees",
        "Irish_wolfhound",
        "Italian_greyhound",
        "Lakeland_terrier",
        "Lhasa",
        "Loafer",
        "Madagascar_cat",
        "Maltese_dog",
        "Model_T",
        "Newfoundland",
        "Norwegian_elkhound",
        "Norwich_terrier",
        "Old_English_sheepdog",
        "Pembroke",
        "Petri_dish",
        "Polaroid_camera",
        "Rottweiler",
        "Saint_Bernard",
        "Saluki",
        "Scottish_deerhound",
        "Sealyham_terrier",
        "Shih-Tzu",
        "Staffordshire_bullterrier",
        "Tibetan_mastiff",
        "Tibetan_terrier",
        "West_Highland_white_terrier",
        "Windsor_tie",
        "Yorkshire_terrier",
        "academic_gown",
        "acorn_squash",
        "acoustic_guitar",
        "admiral",
        "agama",
        "agaric",
        "albatross",
        "alligator_lizard",
        "alp",
        "amphibian",
        "analog_clock",
        "anemone_fish",
        "apiary",
        "assault_rifle",
        "ballplayer",
        "barbell",
        "barber_chair",
        "barbershop",
        "barn_spider",
        "barometer",
        "barrow",
        "basenji",
        "beach_wagon",
        "beagle",
        "bearskin",
        "bee_eater",
        "beer_glass",
        "bighorn",
        "binoculars",
        "birdhouse",
        "bittern",
        "black-footed_ferret",
        "black_stork",
        "black_swan",
        "black_widow",
        "boa_constrictor",
        "bolete",
        "book_jacket",
        "bow_tie",
        "boxer",
        "brambling",
        "breastplate",
        "brown_bear",
        "bulbul",
        "bull_mastiff",
        "bullet_train",
        "bullfrog",
        "bustard",
        "butcher_shop",
        "cab",
        "cabbage_butterfly",
        "cairn",
        "caldron",
        "candle",
        "capuchin",
        "car_mirror",
        "car_wheel",
        "carbonara",
        "cardoon",
        "carpenter's_kit",
        "cash_machine",
        "cellular_telephone",
        "centipede",
        "chain_mail",
        "chain_saw",
        "chainlink_fence",
        "chambered_nautilus",
        "chickadee",
        "chiffonier",
        "chimpanzee",
        "chiton",
        "chocolate_sauce",
        "cicada",
        "cliff_dwelling",
        "cocker_spaniel",
        "cocktail_shaker",
        "colobus",
        "combination_lock",
        "common_iguana",
        "computer_keyboard",
        "conch",
        "confectionery",
        "consomme",
        "coral_fungus",
        "coral_reef",
        "coucal",
        "cowboy_boot",
        "cowboy_hat",
        "cradle",
        "crash_helmet",
        "cricket",
        "crossword_puzzle",
        "cuirass",
        "curly-coated_retriever",
        "desktop_computer",
        "dhole",
        "dial_telephone",
        "diamondback",
        "dingo",
        "disk_brake",
        "doormat",
        "dowitcher",
        "drake",
        "dugong",
        "dung_beetle",
        "earthstar",
        "echidna",
        "eft",
        "electric_fan",
        "electric_locomotive",
        "electric_ray",
        "feather_boa",
        "fire_screen",
        "flat-coated_retriever",
        "football_helmet",
        "four-poster",
        "freight_car",
        "frying_pan",
        "garden_spider",
        "garter_snake",
        "gasmask",
        "giant_schnauzer",
        "golf_ball",
        "gown",
        "grand_piano",
        "great_white_shark",
        "green_mamba",
        "green_snake",
        "grey_whale",
        "grocery_store",
        "groom",
        "ground_beetle",
        "guenon",
        "gyromitra",
        "hair_slide",
        "half_track",
        "hand-held_computer",
        "hand_blower",
        "hard_disc",
        "harvester",
        "harvestman",
        "hen",
        "hen-of-the-woods",
        "hermit_crab",
        "hog",
        "hognose_snake",
        "home_theater",
        "honeycomb",
        "hook",
        "hoopskirt",
        "horned_viper",
        "hot_pot",
        "hourglass",
        "house_finch",
        "iPod",
        "ibex",
        "ice_bear",
        "indigo_bunting",
        "isopod",
        "jacamar",
        "jack-o'-lantern",
        "jean",
        "junco",
        "kelpie",
        "killer_whale",
        "king_penguin",
        "king_snake",
        "knot",
        "komondor",
        "lacewing",
        "lakeside",
        "langur",
        "leaf_beetle",
        "leafhopper",
        "lens_cap",
        "lesser_panda",
        "lighter",
        "limpkin",
        "lionfish",
        "little_blue_heron",
        "long-horned_beetle",
        "lorikeet",
        "lotion",
        "loupe",
        "macaque",
        "magnetic_compass",
        "magpie",
        "malinois",
        "marimba",
        "marmoset",
        "matchstick",
        "megalith",
        "military_uniform",
        "miniature_pinscher",
        "miniature_schnauzer",
        "mixing_bowl",
        "monarch",
        "mortarboard",
        "mosquito_net",
        "mountain_tent",
        "mouse",
        "mousetrap",
        "muzzle",
        "nematode",
        "night_snake",
        "ocarina",
        "oil_filter",
        "otterhound",
        "overskirt",
        "ox",
        "oxygen_mask",
        "oystercatcher",
        "packet",
        "padlock",
        "paper_towel",
        "parallel_bars",
        "partridge",
        "passenger_car",
        "patas",
        "pay-phone",
        "pencil_box",
        "photocopier",
        "pick",
        "pirate",
        "plate_rack",
        "pole",
        "polecat",
        "police_van",
        "poncho",
        "potter's_wheel",
        "proboscis_monkey",
        "ptarmigan",
        "puffer",
        "punching_bag",
        "recreational_vehicle",
        "red-backed_sandpiper",
        "red-breasted_merganser",
        "red_fox",
        "red_wolf",
        "redshank",
        "reel",
        "reflex_camera",
        "ringneck_snake",
        "rock_python",
        "rotisserie",
        "rugby_ball",
        "sarong",
        "sax",
        "scabbard",
        "scuba_diver",
        "sea_cucumber",
        "sea_slug",
        "seat_belt",
        "shoe_shop",
        "shoji",
        "sidewinder",
        "silky_terrier",
        "ski_mask",
        "sliding_door",
        "soft-coated_wheaten_terrier",
        "soup_bowl",
        "space_heater",
        "spaghetti_squash",
        "spider_monkey",
        "spider_web",
        "spindle",
        "spiny_lobster",
        "spotted_salamander",
        "standard_poodle",
        "steam_locomotive",
        "steel_arch_bridge",
        "steel_drum",
        "stinkhorn",
        "stole",
        "stove",
        "street_sign",
        "streetcar",
        "sulphur-crested_cockatoo",
        "sundial",
        "sunglass",
        "sunscreen",
        "suspension_bridge",
        "table_lamp",
        "tank",
        "teddy",
        "theater_curtain",
        "three-toed_sloth",
        "thresher",
        "thunder_snake",
        "timber_wolf",
        "toilet_tissue",
        "toy_poodle",
        "toy_terrier",
        "toyshop",
        "traffic_light",
        "trailer_truck",
        "trilobite",
        "triumphal_arch",
        "tusker",
        "typewriter_keyboard",
        "umbrella",
        "upright",
        "vending_machine",
        "vestment",
        "walking_stick",
        "wall_clock",
        "wallaby",
        "washer",
        "water_buffalo",
        "web_site",
        "weevil",
        "whiptail",
        "white_wolf",
        "wire-haired_fox_terrier",
        "wolf_spider",
        "wombat",
        "wreck",
    ]

    # Dictionary for the second list of words
    missing_repr_eeg2 = {
        "Animals": {
            "Mammals_Land": [
                "bull",
                "chihuahua",
                "guinea",
                "kitten",
                "polar",
                "pony",
                "racehorse",
            ],  # boxer=dog, polar=bear
            "Mammals_Marine": [],
            "Birds": ["cardinal", "chicken"],
            "Reptiles_Amphibians": ["tadpole"],
            "Insects_Arachnids_Invertebrates": [
                "barnacle",
                "beehive",
                "praying",
            ],  # praying=mantis
            "Fish": [
                "blowfish",
                "mullet",
                "seahorse",
            ],  # Added Fish subcategory previously missed
            "Human": ["baby", "boy", "girl", "man", "woman", "boxer"],
        },
        "Food_Drink_Plants_Fungi": {
            "Prepared_Meals_Dishes": [
                "breakfast",
                "cereal",
                "cordon",
                "dumpling",
                "fast",
                "french",
                "mashed",
                "pancake",
                "ready",
                "scrambled",
                "stir",
            ],  # cordon=bleu, fast=food, french=fries, mashed=potato, ready=meal, scrambled=egg, stir=fry
            "Baked_Goods_Sweets_Snacks": [
                "birthday",
                "creme",
                "easter",
                "gingerbread",
                "hot",
                "ice-cream",
                "jelly",
                "pita",
                "roll",
                "snack",
                "wedding",
            ],  # birthday=cake, creme=brulee, easter=egg, gingerbread=man, hot=dog, ice-cream=cone, jelly=beans, roll=spring roll, wedding=cake
            "Fruits_Vegetables_Processed": [
                "blueberry",
                "bok",
                "brussels",
                "gourd",
                "green",
                "squash",
            ],  # bok=choy, brussels=sprouts, green=beans
            "Nuts_Proteins_OtherFood": [
                "chicken2",
                "dogfood",
                "pet",
            ],  # chicken2=meat, pet=food
            "Dairy_Fats": ["whipped"],  # whipped=cream
            "Drinks": ["cocktail", "drink", "smoothie"],
            "Ingredients_Condiments_Spices": [
                "clove",
                "crouton",
                "maple",
                "pepper",
                "soy",
                "teabag",
            ],  # maple=syrup, pepper=mill/shaker, soy=sauce
            "Trees_Woody_Plants": [],
            "Flowers_Herbs_Grasses": [],
            "Fungi": [],
            "Other_Plant_Parts": [
                "honeycomb",
                "mistletoe",
                "pine",
                "stem",
                "twig",
            ],  # pine=cone/needle
        },
        "Clothing_Accessories_Tools_Instruments": {
            "Garments_Bodywear": [
                "boxer",
                "fishnet",
                "knee",
                "lab",
                "polo",
            ],  # boxer=shorts, fishnet=stockings, knee=pad, lab=coat, polo=shirt
            "Footwear": [
                "flip",
                "insole",
                "shoehorn",
                "shoelace",
            ],  # flip=flop
            "Headwear": [
                "bowler",
                "football",
                "top",
            ],  # bowler=hat, football=helmet, top=hat
            "Accessories_Jewelry": [
                "bead",
                "blindfold",
                "bolo",
                "bow2",
                "braid",
                "duffel",
                "harness",
                "strap",
                "umbrella",
                "velcro",
            ],  # bolo=tie, bow2=bowtie, duffel=bag
            "Makeup_Personal_Care": [
                "hairspray",
                "shaving",
                "tooth",
            ],  # shaving=cream, tooth=toothbrush/paste
            "Hand_Tools_Manual_Equipment": [
                "anvil",
                "barbed",
                "blower",
                "blowtorch",
                "cane",
                "clothespin",
                "crank",
                "curling",
                "extinguisher",
                "flashlight",
                "flatiron",
                "flypaper",
                "flyswatter",
                "gavel",
                "hookah",
                "horseshoe",
                "hose",
                "knitting",
                "ladder",
                "leash",
                "lighter",
                "loom",
                "mousetrap",
                "padlock",
                "pipe1",
                "sewing",
                "soldering",
                "stake",
                "watering",
            ],  # barbed=wire, knitting=needle, pipe1=smoking pipe, sewing=kit
            "Kitchen_Tools_Utensils": [
                "cutting",
                "food",
                "measuring",
                "rolling",
                "swizzle",
                "toothpick",
            ],  # cutting=board, food=processor, measuring=cup, rolling=pin
            "Weapons_Military_Gear": [
                "blowgun",
                "bulletproof",
                "gas",
                "machine",
                "sheath",
                "sling",
            ],  # bulletproof=vest, gas=mask, machine=gun, sling=slingshot (or medical?) -> weapon default
            "Scientific_Medical_Instruments": [
                "gyro",
                "incubator",
                "magnifying",
                "pedometer",
                "petri",
            ],  # gyro=gyroscope, magnifying=glass, petri=dish
            "Sports_Games_Equipment": [
                "balance",
                "barbell",
                "board",
                "bowling",
                "boxing",
                "bungee",
                "chess",
                "diving",
                "exerciser",
                "fishhook",
                "fishing",
                "hobbyhorse",
                "hockey",
                "home",
                "hula",
                "jigsaw",
                "jump",
                "kaleidoscope",
                "lego",
                "lifesaver",
                "noisemaker",
                "ping-pong",
                "playing",
                "pogo",
                "punching",
                "puppet",
                "reel",
                "rocking",
                "roulette",
                "rugby",
                "saddle",
                "soccer",
                "spur",
                "squirt",
                "stilt",
                "stirrup",
                "tackle",
                "tennis",
                "whoopee",
            ],  # balance=beam, bowling=ball, boxing=gloves, chess=board/piece, diving=board, fishing=pole, home=plate, hula=hoop, jigsaw=puzzle, jump=rope, ping-pong=table/ball, playing=card, punching=bag, reel=fishing reel, rocking=horse, roulette=wheel, soccer=ball, squirt=gun, tackle=fishing tackle, tennis=ball
            "Musical_Instruments": ["tuning"],  # tuning=fork
            "Drawing_Writing_Art_Supplies": [
                "paint"
            ],  # paint=paint? material? -> Art supply seems specific use
            "Cleaning_Supplies": ["dishwashing"],  # dishwashing=liquid
        },
        "Things": {
            "Organic_Materials_Non_Plant_Animal": [
                "compost",
                "crystal",
                "eggshell",
                "foam",
                "gel",
                "log",
                "silicone",
                "slime",
            ],
            "Furniture": [
                "bulletin",
                "drawer",
                "filing",
                "headrest",
                "ironing",
                "sofa",
                "step",
                "walker1",
            ],  # bulletin=board, filing=cabinet, ironing=board, sofa=bed, step=stool, walker1=baby walker?
            "Appliances_Non_Electronic": [],
            "Containers_Storage": [
                "cage",
                "clothes",
                "container",
                "dogfood",
                "dumpster",
                "hot-water",
                "laundry",
                "piggy",
                "sandbag",
                "shopping",
            ],  # clothes=hamper/basket, hot-water=bottle, laundry=basket, piggy=bank, shopping=cart/basket
            "Decor_Linens_Bedding": [
                "ashtray",
                "doormat",
                "globe",
                "hanger",
                "teddy",
            ],  # teddy=bear
            "Tableware_Dishware": [],
            "Bathroom_Items": [],
            "Office_Supplies_Stationery": [
                "ballot",
                "book",
                "chalkboard",
                "comic",
                "credit",
                "stamp1",
                "stamp2",
                "wrap",
                "wrapping",
            ],  # ballot=box, book=comic book?, comic=book, credit=card, stamp1/2=stamp, wrap/wrapping=paper
            "Computing_Devices_Peripherals": [
                "hard",
                "remote",
                "sim",
            ],  # hard=disk, remote=control, sim=card
            "Audio_Video_Photography": [
                "camera",
                "photo",
                "polaroid",
            ],  # photo=booth, polaroid=camera
            "Communication_Devices": [
                "cash",
                "cuckoo",
                "hourglass",
                "radar",
                "siren",
                "sundial",
            ],  # cash=machine/register, cuckoo=clock
            "Electrical_Appliances": [
                "doorbell",
                "electric",
                "plug",
                "robot",
                "solar",
                "vending",
                "washing",
                "cash_machine",
                "cash_register",
                "electric_chair",
                "fire_alarm",
                "light_switch",
                "metal_detector",
                "revolving_door",
                "train_set",
                "vending_machine",
                "water_fountain",
            ],  # electric=chair?, solar=panel, washing=machine
            "Electronic_Components": [],
            "Abstract_Concepts_Symbols_Misc": [
                "cigar",
                "cigarette",
                "firecracker",
                "gift",
                "knot",
                "sparkler",
                "brick",
                "candle",
                "chicken_wire",
                "combination_lock",
                "credit_card",
                "crystal_ball",
                "cuckoo_clock",
                "duct",
                "ice_cube",
                "ice_pack",
                "rain_gauge",
                "weather_vane",
                "whoopee_cushion",
                "gift_wrap",
            ],  # gift=wrap?
            "Medical_Supplies": [
                "bandage",
                "bedpan",
                "contact",
                "denture",
                "earplug",
                "first-aid",
                "gauze",
                "hearing",
                "pacifier",
                "pill",
                "retainer",
                "sling",
                "walker2",
                "wooden",
            ],  # contact=lens, first-aid=kit, hearing=aid, pill=pillbox?, sling=arm sling, walker2=mobility walker, wooden=leg
            "Parts_Components_Mechanical": [
                "bracket",
                "brake",
                "cable",
                "chain",
                "cord",
                "dial",
                "exhaust",
                "eyepiece",
                "gasket",
                "handle",
                "handlebar",
                "lid",
                "pedal",
                "pendulum",
                "rearview",
                "steering",
                "wick",
            ],  # rearview=mirror, steering=wheel
            "Cleaning_Supplies": [],  # Added
        },
        "Buildings_Vehicles_Outdoor": {
            "Buildings": ["teepee"],
            "Outdoor_Structures_Features": [
                "beehive",
                "birdbath",
                "birdhouse",
                "ferris",
                "nest",
                "parking",
                "pole",
                "sandcastle",
                "scarecrow",
                "snowman",
                "swimming",
                "totem",
                "weather",
                "windsock",
            ],  # parking=meter, pole=totem pole?, swimming=pool, weather=vane
            "Building_Parts_Architecture_Elements": [
                "chute",
                "mast",
                "pipe2",
                "revolving",
                "stained",
            ],  # pipe2=drain pipe?, revolving=door, stained=glass
            "Geological_Landforms": [],
            "Weather_Atmospheric": [],
            "Water_Bodies_Features": [],
            "Land_Vehicles": [
                "garbage",
                "golf",
                "police",
                "quad",
                "roadsweeper",
                "roller",
                "sweeper",
                "wreck",
            ],  # aircraft=carrier? let's assume generic aircraft -> Air, garbage=truck, golf=cart, police=car, roller=coaster/steamroller?, sweeper=roadsweeper, wreck=car wreck
            "Air_Vehicles": [
                "aircraft",
                "hot-air-baloon",
            ],  # hot-air=balloon, adding 'aircraft' here
            "Water_Vehicles": ["cruise"],  # cruise=ship
            "Other_Transport": [],
        },
    }

    # # Correcting aircraft placement based on interpretation
    # missing_repr_eeg2["Buildings_Vehicles_Outdoor"]["Land_Vehicles"].remove('aircraft')
    # missing_repr_eeg2["Buildings_Vehicles_Outdoor"]["Air_Vehicles"].append('aircraft')

    # # Correcting roller placement based on interpretation (coaster context)
    # missing_repr_eeg2["Buildings_Vehicles_Outdoor"]["Land_Vehicles"].remove('roller')
    # missing_repr_eeg2["Buildings_Vehicles_Outdoor"]["Outdoor_Structures_Features"].append('roller') # roller=coaster

    # print("Dictionary with the second list of categorized words created.")
    # You can now use this `missing_repr_eeg2` with the `merge_categories` function
    # defined previously, perhaps merging it with the result of the first merge.
    # Example: final_dict_v3 = merge_categories(final_merged_categories, missing_repr_eeg2)

    missing_things_eeg2 = {
        "Animals": {
            "Mammals_Land": [
                "bull",
                "chihuahua",
                "kitten",
                "mullet",
                "pony",
                "quad",
                "racehorse",
            ],
            "Mammals_Marine": ["blowfish", "seahorse"],
            "Birds": ["cardinal", "chicken2", "nest"],
            "Reptiles_Amphibians": ["tadpole"],
            "Insects_Arachnids_Invertebrates": [
                "barnacle",
                "beehive",
                "flypaper",
                "flyswatter",
                "honeycomb",
                "mosquito_net",
                "spider_web",
            ],
            "Human_Animal_Parts": ["baby", "knee", "man", "tooth", "woman"],
        },
        "Food_Drink_Plants_Fungi": {
            "Prepared_Meals_Dishes": [
                "banana_split",
                "breakfast",
                "dumpling",
                "pancake",
            ],
            "Baked_Goods_Sweets_Snacks": [
                "birthday_cake",
                "pita",
                "roll",
                "snack",
            ],
            "Fruits_Vegetables_Processed": [
                "blueberry",
                "crouton",
                "gourd",
                "smoothie",
                "squash",
                "string_cheese",
            ],
            "Dairy_Fats": [],
            "Drinks": ["cocktail", "drink", "smoothie"],
            "Ingredients_Condiments_Spices": [
                "cake_mix",
                "clove",
                "coffee_bean",
                "crouton",
            ],
            "Trees_Woody_Plants": ["log", "mistletoe", "stem", "twig"],
            "Flowers_Herbs_Grasses": [],
            "Fruits_Vegetables_Nuts_Seeds": ["blueberry", "gourd", "squash"],
            "Fungi": [],
            "Other_Plant_Parts": ["banana_peel", "teabag"],
        },
        "Clothing_Accessories_Tools_Instruments": {
            "Garments_Bodywear": [
                "clothes",
                "eye_patch",
                "football_helmet",
                "life_jacket",
            ],
            "Footwear": ["insole", "shoe_polish", "shoehorn", "shoelace"],
            "Headwear": ["blindfold"],
            "Accessories_Jewelry": ["bead"],
            "Makeup_Personal_Care": ["hairspray", "silicone"],
            "Hand_Tools_Manual_Equipment": [
                "anvil",
                "barbell",
                "blower",
                "blowgun",
                "blowtorch",
                "cane",
                "crank",
                "crowbar",
                "duct_tape",
                "extinguisher",
                "fishing_pole",
                "flashlight",
                "flatiron",
                "flyswatter",
                "gavel",
                "gyro",
                "handle",
                "handlebar",
                "hoe",
                "hose",
                "jack",
                "ladder",
                "loom",
                "mallet",
                "oar",
                "paddle",
                "paint",
                "pedal",
                "pick",
                "pipe1",
                "pipe2",
                "plaster_cast",
                "plug",
                "pole",
                "pump",
                "reel",
                "saw",
                "screwdriver",
                "sewing_kit",
                "sheath",
                "shovel",
                "sickle",
                "sling",
                "spur",
                "stake",
                "stirrup",
                "tape_measure",
                "tongs",
                "toothpick",
                "umbrella",
                "watering_can",
                "wick",
            ],
            "Kitchen_Tools_Utensils": [
                "coffee_filter",
                "cookie_sheet",
                "ladle",
                "paper_plate",
                "paper_towel",
                "rolling_pin",
                "sieve",
                "skewer",
                "spatula",
            ],
            "Musical_Instruments": ["music_box"],
            "Weapons_Military_Gear": [
                "barbed_wire",
                "blowgun",
                "blowtorch",
                "firecracker",
                "grenade",
                "gun",
                "knife",
                "missile",
                "rifle",
                "shield",
                "spear",
                "sword",
            ],
            "Scientific_Medical_Instruments": [
                "bedpan",
                "contact_lens",
                "denture",
                "hearing_aid",
                "incubator",
                "kaleidoscope",
                "pacifier",
                "pill",
                "plaster_cast",
                "retainer",
                "stethoscope",
                "thermometer",
            ],
            "Sports_Game_Equipment": [
                "ball",
                "barbell",
                "dartboard",
                "football",
                "football_helmet",
                "goal",
                "hula_hoop",
                "kite",
                "paddle",
                "ping_pong_ball",
                "playing_card",
                "punching_bag",
                "quad",
                "racket",
                "roller_skate",
                "skateboard",
                "ski",
                "sled",
                "slot_machine",
                "soccer_ball",
                "stilts",
                "surfboard",
                "swing",
                "tackle",
                "trampoline",
            ],
            "Drawing_Writing_Art_Supplies": [
                "chalkboard",
                "crayon",
                "easel",
                "glue",
                "ink",
                "marker",
                "paint",
                "paper",
                "pencil",
                "rubber_eraser",
                "ruler",
                "stamp1",
                "stamp2",
            ],
            "Cleaning_Supplies": [
                "broom",
                "dustpan",
                "mop",
                "soap",
                "sponge",
                "sweeper",
            ],
        },
        "Things": {
            "Organic_Materials_Non_Plant_Animal": [
                "banana_peel",
                "eggshell",
                "foam",
                "gel",
                "honeycomb",
                "slime",
                "spider_web",
            ],
            "Furniture": [
                "bed",
                "bench",
                "bookcase",
                "cabinet",
                "chair",
                "coat_rack",
                "crib",
                "desk",
                "drawer",
                "hammock",
                "headrest",
                "shelf",
                "stool",
                "table",
            ],
            "Appliances_Non_Electronic": [
                "air_pump",
                "can_opener",
                "coffee_filter",
                "corkscrew",
                "grater",
                "juicer",
                "knife",
                "ladle",
                "meat_grinder",
                "peeler",
                "rolling_pin",
                "sieve",
                "skewer",
                "spatula",
                "umbrella",
                "waffle_iron",
                "watering_can",
            ],
            "Containers_Storage": [
                "ashtray",
                "ballot_box",
                "basket",
                "bottle",
                "bowl",
                "bucket",
                "cage",
                "can",
                "container",
                "cup",
                "desk_organizer",
                "drawer",
                "dumpster",
                "jar",
                "laundry_basket",
                "lid",
                "lunchbox",
                "mug",
                "paper_bag",
                "sack",
                "suitcase",
                "trash_can",
                "tray",
                "vase",
                "water_bottle",
                "wine_bottle",
            ],
            "Textiles_Linens_Bedding": [
                "air_mattress",
                "bandage",
                "blanket",
                "curtain",
                "doormat",
                "gauze",
                "pillow",
                "sheet",
                "sleeping_bag",
                "towel",
            ],
            "Bathroom_Items": [
                "bedpan",
                "comb",
                "contact_lens",
                "denture",
                "earplug",
                "floss",
                "hairbrush",
                "loofah",
                "mirror",
                "razor",
                "shampoo",
                "soap",
                "sponge",
                "toothbrush",
                "toothpaste",
                "towel",
            ],
            "Office_Supplies_Stationery": [
                "binder",
                "calendar",
                "card",
                "chalkboard",
                "clipboard",
                "computer_keyboard",
                "computer_mouse",
                "crayon",
                "desk_organizer",
                "diary",
                "easel",
                "envelope",
                "glue",
                "hole_punch",
                "ink",
                "label",
                "marker",
                "notebook",
                "paper",
                "paper_clip",
                "pen",
                "pencil",
                "rubber_eraser",
                "ruler",
                "stamp1",
                "stamp2",
                "stapler",
                "tape",
            ],
            "Clothing_Personal_Accessories": [
                "belt",
                "blindfold",
                "bra",
                "button",
                "cufflink",
                "diaper",
                "dress",
                "earmuff",
                "eye_patch",
                "glove",
                "handbag",
                "hat",
                "hood",
                "jacket",
                "jeans",
                "jewelry",
                "necklace",
                "overall",
                "pants",
                "purse",
                "scarf",
                "shirt",
                "shoe",
                "skirt",
                "sock",
                "suit",
                "sunglasses",
                "sweater",
                "tie",
                "umbrella",
                "wallet",
                "watch",
                "wig",
            ],
            "Audio_Video_Photography": [
                "camera",
                "film",
                "microphone",
                "projector",
                "radio",
                "record_player",
                "speaker",
                "television",
                "video_camera",
            ],
            "Communication_Devices": [
                "cellular_telephone",
                "pager",
                "telephone",
                "walkie_talkie",
            ],
            "Electrical_Appliances": [
                "blender",
                "computer",
                "dishwasher",
                "dryer",
                "fan",
                "freezer",
                "hair_dryer",
                "iron",
                "microwave_oven",
                "oven",
                "refrigerator",
                "sewing_machine",
                "stove",
                "toaster",
                "vacuum_cleaner",
                "washing_machine",
            ],
            "Electronic_Components": [
                "battery",
                "cable",
                "circuit_board",
                "computer_chip",
                "diode",
                "fuse",
                "light_bulb",
                "magnet",
                "microchip",
                "monitor",
                "printer",
                "resistor",
                "sensor",
                "solar_panel",
                "transistor",
                "wire",
            ],
            "Abstract_Concepts_Symbols_Misc": [
                "air",
                "anger",
                "art",
                "beauty",
                "belief",
                "braid",
                "brake",
                "cable",
                "chain",
                "chaos",
                "circle",
                "comfort",
                "communication",
                "compassion",
                "concept",
                "confidence",
                "connection",
                "conscience",
                "contentment",
                "courage",
                "creativity",
                "crowd",
                "culture",
                "curiosity",
                "danger",
                "darkness",
                "data",
                "day",
                "death",
                "debt",
                "decision",
                "defeat",
                "defense",
                "delight",
                "democracy",
                "desire",
                "destiny",
                "determination",
                "development",
                "difference",
                "difficulty",
                "dignity",
                "direction",
                "disaster",
                "discipline",
                "discovery",
                "discussion",
                "disease",
                "distance",
                "diversity",
                "division",
                "doubt",
                "dream",
                "duty",
                "dynamism",
                "earth",
                "ease",
                "ecology",
                "education",
                "effort",
                "electricity",
                "emotion",
                "energy",
                "enjoyment",
                "enthusiasm",
                "environment",
                "equality",
                "error",
                "escape",
                "essence",
                "eternity",
                "ethics",
                "evaluation",
                "event",
                "evidence",
                "evil",
                "evolution",
                "examination",
                "example",
                "excitement",
                "existence",
                "experience",
                "experiment",
                "expert",
                "explanation",
                "exploration",
                "expression",
                "eye",
                "fact",
                "failure",
                "faith",
                "fame",
                "family",
                "fear",
                "feeling",
                "fiction",
                "field",
                "fight",
                "figure",
                "film",
                "fire",
                "firmness",
                "flag",
                "flight",
                "flow",
                "focus",
                "force",
                "form",
                "fortune",
                "foundation",
                "freedom",
                "friendship",
                "frustration",
                "fuel",
                "fun",
                "future",
                "galaxy",
                "game",
                "garden",
                "gas",
                "gate",
                "gathering",
                "gaze",
                "gender",
                "generation",
                "genius",
                "gesture",
                "gift",
                "glass",
                "glory",
                "goal",
                "gold",
                "goodness",
                "government",
                "grace",
                "grade",
                "grain",
                "grandeur",
                "grant",
                "graph",
                "grass",
                "gravity",
                "greatness",
                "grief",
                "group",
                "growth",
                "guidance",
                "guilt",
                "habit",
                "happiness",
                "harmony",
                "hate",
                "health",
                "heat",
                "heaven",
                "height",
                "heritage",
                "heroism",
                "hesitation",
                "history",
                "holiday",
                "hope",
                "horizon",
                "horror",
                "hospitality",
                "hot",
                "house",
                "housing",
                "humanity",
                "humility",
                "humor",
                "hunger",
                "hurry",
                "hurt",
                "hypothesis",
                "ice",
                "idea",
                "ideal",
                "identity",
                "ideology",
                "ignorance",
                "image",
                "imagination",
                "impact",
                "importance",
                "impression",
                "improvement",
                "impulse",
                "incentive",
                "incident",
                "inclusion",
                "income",
                "increase",
                "independence",
                "index",
                "individual",
                "industry",
                "inequality",
                "inference",
                "influence",
                "information",
                "initiative",
                "injury",
                "innocence",
                "innovation",
                "input",
                "insight",
                "inspiration",
                "instance",
                "instinct",
                "institution",
                "instruction",
                "instrument",
                "insult",
                "insurance",
                "integration",
                "integrity",
                "intellect",
                "intelligence",
                "intensity",
                "intention",
                "interaction",
                "interest",
                "interference",
                "interior",
                "interpretation",
                "interview",
                "introduction",
                "intuition",
                "investment",
                "invitation",
                "irony",
                "isolation",
                "issue",
                "item",
                "journey",
                "joy",
                "judgment",
                "justice",
                "kindness",
                "knowledge",
                "labor",
                "language",
                "laughter",
                "law",
                "layer",
                "leadership",
                "learning",
                "legacy",
                "legislation",
                "leisure",
                "lesson",
                "letter",
                "level",
                "liberty",
                "library",
                "license",
                "life",
                "light",
                "limit",
                "line",
                "link",
                "liquid",
                "list",
                "literature",
                "loan",
                "location",
                "logic",
                "loneliness",
                "loss",
                "love",
                "loyalty",
                "luck",
                "luxury",
                "machine",
                "madness",
                "magic",
                "magnitude",
                "majority",
                "management",
                "manner",
                "map",
                "margin",
                "mark",
                "market",
                "marriage",
                "mass",
                "mastery",
                "material",
                "mathematics",
                "matter",
                "maturity",
                "meaning",
                "measure",
                "mechanism",
                "media",
                "medicine",
                "meditation",
                "memory",
                "menace",
                "metal",
                "method",
                "mind",
                "mineral",
                "minority",
                "minute",
                "miracle",
                "misery",
                "mistake",
                "model",
                "moment",
                "momentum",
                "money",
                "month",
                "mood",
                "morality",
                "motion",
                "motivation",
                "mountain",
                "movement",
                "movie",
                "mud",
                "muscle",
                "mystery",
                "myth",
                "name",
                "nation",
                "nature",
                "need",
                "negotiation",
                "nerve",
                "network",
                "news",
                "night",
                "noise",
                "norm",
                "note",
                "novel",
                "number",
                "object",
                "objective",
                "observation",
                "obstacle",
                "occasion",
                "ocean",
                "odor",
                "offer",
                "oil",
                "opinion",
                "opportunity",
                "opposition",
                "optimism",
                "order",
                "organization",
                "origin",
                "other",
                "outcome",
                "output",
                "pain",
                "painting",
                "pair",
                "paradox",
                "parallel",
                "parameter",
                "parent",
                "park",
                "part",
                "particle",
                "partner",
                "party",
                "passage",
                "passion",
                "past",
                "path",
                "patience",
                "pattern",
                "peace",
                "peak",
                "penalty",
                "perception",
                "performance",
                "period",
                "permission",
                "person",
                "perspective",
                "phase",
                "philosophy",
                "photo",
                "phrase",
                "physics",
                "picture",
                "piece",
                "place",
                "plan",
                "plant",
                "plastic",
                "plate",
                "play",
                "pleasure",
                "plot",
                "poem",
                "point",
                "poison",
                "policy",
                "politics",
                "pollution",
                "pond",
                "population",
                "position",
                "possibility",
                "power",
                "practice",
                "praise",
                "prayer",
                "precedent",
                "precision",
                "prediction",
                "preference",
                "prejudice",
                "preparation",
                "presence",
                "present",
                "pressure",
                "prestige",
                "price",
                "pride",
                "principle",
                "priority",
                "prison",
                "privacy",
                "prize",
                "problem",
                "procedure",
                "process",
                "product",
                "profession",
                "profit",
                "program",
                "progress",
                "project",
                "promise",
                "promotion",
                "proof",
                "property",
                "proposal",
                "protection",
                "protest",
                "province",
                "provision",
                "psychology",
                "public",
                "publication",
                "punishment",
                "purpose",
                "puzzle",
                "quality",
                "quantity",
                "question",
                "quiet",
                "quit",
                "race",
                "radiation",
                "rain",
                "range",
                "rank",
                "rate",
                "reaction",
                "reality",
                "reason",
                "rebellion",
                "recall",
                "receipt",
                "recognition",
                "recommendation",
                "record",
                "recovery",
                "reduction",
                "reference",
                "reflection",
                "reform",
                "refuge",
                "regret",
                "regulation",
                "relation",
                "relationship",
                "release",
                "relief",
                "religion",
                "relish",
                "remark",
                "remedy",
                "renewal",
                "rent",
                "repair",
                "report",
                "representation",
                "reputation",
                "request",
                "rescue",
                "research",
                "reserve",
                "residence",
                "resistance",
                "resolution",
                "resource",
                "respect",
                "response",
                "responsibility",
                "rest",
                "restaurant",
                "restraint",
                "result",
                "retreat",
                "return",
                "revelation",
                "revenge",
                "revenue",
                "review",
                "revolution",
                "reward",
                "rhythm",
                "rice",
                "richness",
                "ride",
                "right",
                "ring",
                "risk",
                "ritual",
                "river",
                "road",
                "rock",
                "role",
                "romance",
                "room",
                "root",
                "rope",
                "roughness",
                "round",
                "routine",
                "rule",
                "rumor",
                "running",
                "sadness",
                "safety",
                "salad",
                "salt",
                "sand",
                "satisfaction",
                "sauce",
                "saving",
                "scale",
                "scene",
                "scent",
                "schedule",
                "scheme",
                "school",
                "science",
                "scope",
                "score",
                "scratch",
                "screen",
                "script",
                "sea",
                "search",
                "season",
                "seat",
                "second",
                "secret",
                "section",
                "sector",
                "security",
                "seed",
                "selection",
                "self",
                "sense",
                "sentence",
                "separation",
                "series",
                "service",
                "session",
                "setting",
                "shape",
                "share",
                "sharpness",
                "shelter",
                "shock",
                "shoe",
                "shop",
                "shore",
                "shortage",
                "shot",
                "show",
                "side",
                "sight",
                "sign",
                "silence",
                "silk",
                "silver",
                "similarity",
                "simplicity",
                "sin",
                "singer",
                "single",
                "sink",
                "site",
                "situation",
                "size",
                "skill",
                "skin",
                "sky",
                "sleep",
                "slice",
                "slope",
                "smell",
                "smile",
                "smoke",
                "smoothness",
                "snake",
                "snow",
                "soap",
                "society",
                "soil",
                "solution",
                "song",
                "sorrow",
                "soul",
                "sound",
                "soup",
                "source",
                "space",
                "spark",
                "speaker",
                "speed",
                "spell",
                "sphere",
                "spirit",
                "sport",
                "spot",
                "spring",
                "square",
                "stability",
                "staff",
                "stage",
                "stain",
                "stair",
                "stake",
                "stamp",
                "stand",
                "standard",
                "star",
                "start",
                "state",
                "statement",
                "station",
                "statistic",
                "status",
                "stay",
                "steak",
                "steel",
                "step",
                "stick",
                "stillness",
                "stock",
                "stone",
                "stop",
                "story",
                "strain",
                "stranger",
                "strategy",
                "stream",
            ],
        },
    }

    # Create the dictionary structure to hold the categorized new words
    # Based on the image structure, adding subcategories where needed
    missing_imagenet_ext = {
        "Animals": {
            "Mammals_Land": [
                "American_Staffordshire_terrier",
                "Arabian_camel",
                "Brittany_spaniel",
                "Chesapeake_Bay_retriever",
                "Appenzeller",
                "English_setter",
                "Arctic_fox",
                "basenji",
                "beagle",
                "Bedlington_terrier",
                "Border_collie",
                "Boston_bull",
                "Bouvier_des_Flandres",
                "echidna",
                "three-toed_sloth",
                "boxer",
                "Brabancon_griffon",
                "brown_bear",
                "bull_mastiff",
                "cairn",
                "capuchin",
                "chimpanzee",
                "cocker_spaniel",
                "colobus",
                "curly-coated_retriever",
                "dhole",
                "dingo",
                "Doberman",
                "EntleBucher",
                "Eskimo_dog",
                "flat-coated_retriever",
                "French_bulldog",
                "giant_schnauzer",
                "Gordon_setter",
                "Great_Pyrenees",
                "guenon",
                "hog",
                "ibex",
                "ice_bear",
                "Irish_wolfhound",
                "Italian_greyhound",
                "kelpie",
                "komondor",
                "Lakeland_terrier",
                "langur",
                "lesser_panda",
                "Lhasa",
                "macaque",
                "Madagascar_cat",
                "malinois",
                "Maltese_dog",
                "marmoset",
                "miniature_pinscher",
                "miniature_schnauzer",
                "mouse",
                "Newfoundland",
                "Norwegian_elkhound",
                "Norwich_terrier",
                "Old_English_sheepdog",
                "otterhound",
                "ox",
                "patas",
                "Pembroke",
                "polecat",
                "proboscis_monkey",
                "red_fox",
                "red_wolf",
                "Rottweiler",
                "Saint_Bernard",
                "Saluki",
                "Scottish_deerhound",
                "Sealyham_terrier",
                "Shih-Tzu",
                "silky_terrier",
                "soft-coated_wheaten_terrier",
                "spider_monkey",
                "Staffordshire_bullterrier",
                "standard_poodle",
                "Tibetan_mastiff",
                "Tibetan_terrier",
                "timber_wolf",
                "toy_poodle",
                "toy_terrier",
                "tusker",
                "wallaby",
                "water_buffalo",
                "West_Highland_white_terrier",
                "white_wolf",
                "wire-haired_fox_terrier",
                "wombat",
                "Yorkshire_terrier",
                "bighorn",
                (  # Added bighorn here assuming sheep/goat relative
                    "black-footed_ferret"
                ),
            ],
            "Mammals_Marine": [
                "dugong",
                "grey_whale",
                "killer_whale",
                "electric_ray",
                "great_white_shark",
            ],
            "Birds": [
                "African_grey",
                "American_coot",
                "American_egret",
                "albatross",
                "bee_eater",
                "bittern",
                "black_stork",
                "black_swan",
                "brambling",
                "bulbul",
                "bustard",
                "chickadee",
                "coucal",
                "dowitcher",
                "drake",
                "European_gallinule",
                "hen",
                "house_finch",
                "indigo_bunting",
                "jacamar",
                "junco",
                "king_penguin",
                "limpkin",
                "little_blue_heron",
                "lorikeet",
                "magpie",
                "oystercatcher",
                "partridge",
                "ptarmigan",
                "red-backed_sandpiper",
                "red-breasted_merganser",
                "redshank",
                (  # Cockatoo likely fits here better than land mammals
                    "sulphur-crested_cockatoo"
                ),
            ],
            "Reptiles_Amphibians": [
                "African_chameleon",
                "American_alligator",
                "Gila_monster",
                "agama",
                "alligator_lizard",
                "amphibian",
                "boa_constrictor",
                "bullfrog",
                "common_iguana",
                "diamondback",
                "eft",
                "garter_snake",
                "green_mamba",
                "green_snake",
                "hognose_snake",
                "horned_viper",
                "king_snake",
                "night_snake",
                "ringneck_snake",
                "rock_python",
                "sidewinder",
                "spotted_salamander",
                "thunder_snake",
                "whiptail",
            ],
            "Insects_Arachnids_Invertebrates": [
                "American_lobster",
                "barn_spider",
                "black_widow",
                "cabbage_butterfly",
                "centipede",
                "chambered_nautilus",
                "chiton",
                "cicada",
                "conch",
                "cricket",
                "dung_beetle",
                "garden_spider",
                "ground_beetle",
                "harvestman",
                "hermit_crab",
                "isopod",
                "lacewing",
                "leaf_beetle",
                "leafhopper",
                "long-horned_beetle",
                "monarch",
                "nematode",
                "puffer",
                "sea_cucumber",
                "sea_slug",
                "spiny_lobster",
                "trilobite",
                "weevil",
                "wolf_spider",
                "anemone_fish",
                (  # Fish added here as 'invertebrate' isn't quite right, but fits under non-mammal/bird/reptile marine
                    "lionfish"
                ),
            ],
            "Human": [  # Added this subcategory
                "admiral",
                "ballplayer",
                "groom",
                "pirate",
                "scuba_diver",
            ],
        },
        "Food_Drink_Plants_Fungi": {
            "Prepared_Meals_Dishes": [
                "carbonara",
                "consomme",
                "hot_pot",  # Hot pot is arguably a dish/meal style
            ],
            "Baked_Goods_Sweets_Snacks": [
                "confectionery"  # General term for sweets
            ],
            "Fruits_Vegetables_Processed": [
                "acorn_squash",
                "cardoon",
                "spaghetti_squash",
            ],
            "Nuts_Proteins_OtherFood": [],
            "Dairy_Fats": [],
            "Drinks": ["beer_glass"],  # The vessel implies the drink context
            "Ingredients_Condiments_Spices": ["chocolate_sauce"],
            "Trees_Woody_Plants": [],  # Many animals listed, but not plants themselves
            "Flowers_Herbs_Grasses": [],
            "Fungi": [
                "agaric",
                "bolete",
                "coral_fungus",
                "earthstar",
                "gyromitra",
                "hen-of-the-woods",
                "stinkhorn",
            ],
            "Other_Plant_Parts": [
                "honeycomb"  # Natural structure, often associated with food (honey)
            ],
        },
        "Clothing_Accessories_Tools_Instruments": {
            "Garments_Bodywear": [
                "academic_gown",
                "bearskin",
                "breastplate",
                "chain_mail",
                "cuirass",
                "feather_boa",
                "gown",
                "hoopskirt",
                "jean",
                "military_uniform",
                "overskirt",
                "poncho",
                "sarong",
                "stole",
                "vestment",
            ],
            "Footwear": ["Loafer", "cowboy_boot"],  # Added subcategory
            "Headwear": [  # Added subcategory
                "cowboy_hat",
                "crash_helmet",
                "football_helmet",
                "mortarboard",
                "ski_mask",
            ],
            "Accessories_Jewelry": [
                "Windsor_tie",
                "bow_tie",
                "hair_slide",
                "sunglass",  # Note: sunglass vs sunglasses
            ],
            "Makeup_Personal_Care": ["lotion", "sunscreen"],
            "Hand_Tools_Manual_Equipment": [
                "barbell",
                "binoculars",
                "chain_saw",
                "carpenter's_kit",
                "hand_blower",
                "hook",
                "lighter",
                "loupe",
                "magnetic_compass",
                "matchstick",
                "mousetrap",
                "muzzle",
                "padlock",
                "pick",
                "reel",
                "scabbard",
                "spindle",
                "walking_stick",  # Assuming walking aid/tool
            ],
            "Kitchen_Tools_Utensils": [  # Added subcategory
                "Crock_Pot",
                "Dutch_oven",
                "cocktail_shaker",
                "frying_pan",
                "mixing_bowl",
                "rotisserie",
                "soup_bowl",
            ],
            "Weapons_Military_Gear": [
                "assault_rifle",
                "gasmask",  # gasmask could also be safety gear
            ],
            "Scientific_Medical_Instruments": ["Petri_dish", "barometer"],
            "Sports_Games_Equipment": [
                "golf_ball",
                "punching_bag",
                "rugby_ball",
            ],
            "Musical_Instruments": [  # Added subcategory
                "French_horn",
                "acoustic_guitar",
                "grand_piano",
                "marimba",
                "ocarina",
                "sax",
                "steel_drum",
            ],
            "Drawing_Writing_Art_Supplies": [
                "pencil_box",
                (  # puzzle could be misc, but often paper based
                    "crossword_puzzle"
                ),
            ],
            "Cleaning_Supplies": [],  # 'washer' placed under appliances
        },
        "Things": {
            "Organic_Materials_Non_Plant_Animal": [
                # 'honeycomb' moved to plant parts as it's built structure often with plant products
            ],
            "Furniture": [
                "barber_chair",
                "chiffonier",
                "cradle",
                "four-poster",
                "plate_rack",
            ],
            "Appliances_Non_Electronic": [
                "stove"  # Assuming non-electric variant for this category
                # Crock_Pot, Dutch_oven moved to Kitchen Tools
            ],
            "Containers_Storage": [
                "caldron",
                "packet",  # Packet is vague, assuming small container
            ],
            "Decor_Linens_Bedding": [
                "Christmas_stocking",
                "doormat",
                "mosquito_net",
                "teddy",  # Teddy bear often decor/toy
            ],
            "Tableware_Dishware": [
                # Moved beer_glass, soup_bowl
            ],
            "Bathroom_Items": ["paper_towel", "toilet_tissue"],
            "Office_Supplies_Stationery": [
                "book_jacket"  # Could also be Decor?
            ],
            "Computing_Devices_Peripherals": [
                "CD_player",  # Can be argued Audio/Video, but fundamentally computing storage tech
                "cellular_telephone",
                "computer_keyboard",
                "desktop_computer",
                "dial_telephone",
                "hand-held_computer",
                "hard_disc",
                "iPod",
                "typewriter_keyboard",
            ],
            "Audio_Video_Photography": [
                "Polaroid_camera",
                "home_theater",
                "reflex_camera",
                # Moved CD_player
            ],
            "Communication_Devices": [
                "analog_clock",
                "pay-phone",
                # Moved cellular/dial telephones
            ],
            "Electrical_Appliances": [  # Appliances needing electricity
                "electric_fan",
                "photocopier",
                "space_heater",
                "table_lamp",
                "upright",  # Assuming upright vacuum
                "vending_machine",
                "washer",
                "wall_clock",  # Assuming electric/battery wall clock
                # 'stove' if electric? Ambiguous word. Let's put base 'stove' in non-elec for now.
            ],
            "Electronic_Components": [],  # disk_brake, oil_filter are mechanical parts
            "Abstract_Concepts_Symbols_Misc": [
                "knot",
                "web_site",  # web_site is abstract/digital location
            ],
            "Medical_Supplies": [  # Added subcategory
                "Band_Aid",
                "oxygen_mask",
            ],
            "Parts_Components_Mechanical": [  # Added subcategory
                "car_mirror",
                "car_wheel",
                "disk_brake",
                "lens_cap",
                "oil_filter",
                "seat_belt",
            ],
        },
        "Buildings_Vehicles_Outdoor": {
            "Buildings": [
                "barbershop",
                "butcher_shop",
                "cliff_dwelling",
                "grocery_store",
                "shoe_shop",
                "toyshop",
            ],
            "Outdoor_Structures_Features": [
                "apiary",
                "birdhouse",
                "cairn",
                "chainlink_fence",
                "lakeside",
                "megalith",
                "mountain_tent",
                "parallel_bars",
                "pole",
                "potter's_wheel",
                "steel_arch_bridge",
                "street_sign",
                "suspension_bridge",
                "traffic_light",
                "triumphal_arch",
            ],
            "Building_Parts_Architecture_Elements": [
                "fire_screen",
                "shoji",
                "sliding_door",
                "theater_curtain",
            ],
            "Geological_Landforms": [
                "alp",
                "coral_reef",  # Lakeside could arguably be here too
            ],
            "Weather_Atmospheric": [],
            "Water_Bodies_Features": [],
            "Land_Vehicles": [
                "Model_T",
                "beach_wagon",
                "barrow",
                "bullet_train",
                "cab",
                "electric_locomotive",
                "freight_car",
                "half_track",
                "harvester",
                "passenger_car",
                "police_van",
                "recreational_vehicle",
                "steam_locomotive",
                "streetcar",
                "tank",
                "thresher",
                "trailer_truck",
                "wreck",  # Assuming vehicle wreck
            ],
            "Air_Vehicles": [],
            "Water_Vehicles": [],
            "Other_Transport": [],  # Cleared this, moved items to Land_Vehicles mostly
        },
    }

    # --- How to Use ---

    # 1. Assume you have your *original* category dictionary loaded
    #    Let's create a placeholder example based on the structure
    #    Replace this with loading your actual original dictionary
    # original_categories = {
    #     "Animals": {
    #         "Mammals_Land": ['dog', 'cat'],
    #         "Birds": ['robin'],
    #         # ... other original categories and words ...
    #          "Human":[]
    #     },
    #     "Food_Drink_Plants_Fungi": {
    #         "Fruits_Vegetables_Processed": ['apple', 'banana'],
    #         # ...
    #         "Fungi": ['mushroom']
    #     },
    #     "Clothing_Accessories_Tools_Instruments": {
    #          "Hand_Tools_Manual_Equipment": ['hammer'],
    #          #...
    #          "Kitchen_Tools_Utensils": [] # Ensure subcats exist if merging into them
    #     },
    #     "Things":{
    #         "Computing_Devices_Peripherals": ['keyboard', 'mouse'],
    #         "Medical_Supplies": [],
    #         "Parts_Components_Mechanical": [],
    #         #...
    #          "Bathroom_Items": ['soap']
    #     },
    #      "Buildings_Vehicles_Outdoor": {
    #           "Land_Vehicles": ['car'],
    #           "Buildings": ['house'],
    #           #...
    #           "Outdoor_Structures_Features": ['fence']
    #      }
    #     # Make sure this original_categories has ALL the necessary keys/subkeys
    #     # down to the list level that exist in missing_imagenet_ext, even if lists are empty.
    #     # The merge function assumes compatible structures.
    # }

    # 2. Merge the original dictionary with the newly categorized words
    print("\nMerging dictionaries...")
    final_merged_categories = merge_categories(
        word_categories, missing_imagenet_ext
    )
    final_merged_categories = merge_categories(
        final_merged_categories, missing_things_eeg2
    )
    final_merged_categories = merge_categories(
        final_merged_categories, missing_repr_eeg2
    )
    print("Merging complete.")

    return final_merged_categories


print("Dictionary with newly categorized words created.")
# You can inspect `missing_imagenet_ext` here if needed.

import copy  # Needed for deepcopy


def merge_categories(dict1, dict2):
    """
    Recursively merges two dictionaries with a compatible nested structure,
    combining lists found at the leaf nodes. Modifies dict1 in place (via merged_dict).

    Args:
        dict1: The first dictionary (will be used as the base).
        dict2: The second dictionary (to merge into the first).

    Returns:
        dict: A new dictionary containing the merged content.
            Returns a deep copy of dict1 if dict2 is not a dictionary.
            Returns a deep copy of dict2 if dict1 is not a dictionary.
    Raises:
        TypeError: If incompatible types are found at the same key
                (e.g., dict vs list).
    """
    # print("\nMerging dictionaries...")
    # Handle cases where one input isn't a dictionary
    if not isinstance(dict1, dict):
        print(
            f"Warning: dict1 is not a dictionary ({type(dict1)}). Returning"
            " copy of dict2."
        )
        return copy.deepcopy(dict2) if isinstance(dict2, dict) else {}
    if not isinstance(dict2, dict):
        print(
            f"Warning: dict2 is not a dictionary ({type(dict2)}). Returning"
            " copy of dict1."
        )
        return copy.deepcopy(dict1)  # dict1 is confirmed dict here

    # Start with a deep copy of dict1 to avoid modifying the original directly
    merged_dict = copy.deepcopy(dict1)

    # Iterate through keys of dict2 to merge them into merged_dict
    for key, value_d2 in dict2.items():
        if key not in merged_dict:
            # Key from dict2 is new, add it
            merged_dict[key] = copy.deepcopy(value_d2)
        else:
            # Key exists in both dictionaries
            value_d1 = merged_dict[key]

            if isinstance(value_d1, dict) and isinstance(value_d2, dict):
                # Both values are dicts -> recursive call
                merged_dict[key] = merge_categories(value_d1, value_d2)
            elif isinstance(value_d1, list) and isinstance(value_d2, list):
                # Both values are lists -> combine and remove duplicates
                # Convert to sets for efficient union, then back to list
                combined_set = set(value_d1) | set(value_d2)
                merged_dict[key] = sorted(
                    list(combined_set)
                )  # Keep sorted for consistency
            elif type(value_d1) == type(value_d2):
                # Types match but aren't dict or list (e.g. string, int), overwrite (or choose specific logic)
                # Let's keep the value from dict1 (already in merged_dict) - or overwrite with d2? Let's overwrite as that's common merge behavior.
                merged_dict[key] = copy.deepcopy(value_d2)
            else:
                # Types are incompatible (e.g., dict vs list) at the same key
                raise TypeError(
                    f"Incompatible types for key '{key}': {type(value_d1)} and"
                    f" {type(value_d2)}"
                )

    return merged_dict


# 3. (Optional) Inspect the final merged dictionary
# import json
# print("\n--- Final Merged Dictionary (sample) ---")
# print(json.dumps(final_merged_categories.get("Animals", {}).get("Mammals_Land", []), indent=2))
# print(json.dumps(final_merged_categories.get("Things", {}).get("Computing_Devices_Peripherals", []), indent=2))
# print(json.dumps(final_merged_categories, indent=2)) # Print the whole thing if needed
