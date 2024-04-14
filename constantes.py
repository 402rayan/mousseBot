CONSTANTS = {
    'DAILY_TICKETS': 1,
    'INVOCATION_COST': 0,
    'MAX_CHARACTERS': 20,
    'RARITY_PRICE': {
        'X': 0.1,
        'SS': 50,
        'S': 25,
        'A': 10,
        'B': 5,
        'C': 1,
        'D': 0.5,
        'E': 0.25,
        'F': 0.1,
    },
    'RARITY_CHANCE': {
        'X': 1,
        'SS': 0.02,
        'S': 0.05,
        'A': 0,
        'B': 0.15,
        'C': 0.2,
        'D': 0.15,
        'E': 0.1,
        'F': 0.1,
    },
    'RARITY_COLOR': {
        'X' : 0x800080,
        'SS': 0xFFD700,
        'S' : 0xFFA500,
        'A' : 0xFF0000,
        'B' : 0x00FF00,
        'C' : 0x0000FF,
        'D' : 0x800000,
        'E' : 0x008000,
        'F' : 0x000080,
    },
}

phrases_invocation = [
    "Mais... C'est incroyable !",
    "C'est un miracle !",
    "Je n'en reviens pas !",
    "C'est un rêve !",
    "Wow..",
    "Incroyable !",
    "Qu'est-ce que ça pourrait bien être ?",
    "Je suis impatient de voir ça !",
    "Je suis sûr que c'est quelque chose de bien..",
    "Je sens que c'est quelque chose de rare !",
    "Impressionnant !",
    "Impossible..",
    "Est-ce que c'est vraiment possible ?",
    "C'est un signe du destin !",
    "Je suis sûr que c'est quelque chose de rare !"
]

all_characters_templates = [
            # """ PERSONNAGE DRAGON BALL"""
            # Personnages X
            ("Vegeta Ultra Ego", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Goku Ultra Instinct", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zeno", "X", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages SS
            ("Broly", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Golden Freezer", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Beerus", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Champa", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Vados", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Whis", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Goku Black", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zamasu", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Jiren", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages S
            ("Hit", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kefla", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Toppo", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Android 17", "S", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages A
            ("Cabba", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Cell", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Majin Buu", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kale", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Caulifla", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Trunks (Futur)", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gotenks", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gohan", "A", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages B
            ("Kale", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("C-18", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Frost", "B", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages C
            ("Tien", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Bardock", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zarbon", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dodoria", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ginyu", "C", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages D
            ("Chiaotzu", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Raditz", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nappa", "D", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages E
            ("Yamcha", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pui Pui", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Saibaman", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Oolong", "E", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages F
            ("Mr. Satan", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yajirobe", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pilaf", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Plume", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Chichi", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Bulma", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gyumao", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dr. Brief", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dende", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE NARUTO"""
            # Personnages X
            ("Naruto Six Path", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sasuke Rinnegan", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kaguya", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Madara Rinnegan", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Rikudo", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Indra", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ashura", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Obito Jinchuriki", "X", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages SS
            ("Hashirama", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Toneri", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pain", "SS", "https://imgur.com/MUcsXLQ", 0, 0, 0),
            ("Itachi", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Minato", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Orochimaru", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kabuto", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sasuke", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Naruto", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Guy (8 portes)", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages S
            ("Hidan", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kakuzu", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mei Terumi", "S", "https://i.imgur.com/JTaGhQQ.gif", 0, 0, 0),
            ("Gaara", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tsunade", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kisame", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Darui", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Asuma", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Neji", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kimimaro", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shikamaru", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Rock Lee", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sasori", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Deidara", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Killer Bee", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Jiraiya", "S", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages A
            ("Yamato (ANBU)", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zabuza", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kankuro", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Choji", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sai", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Temari", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Konan", "A", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages B
            ("Shino", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kiba", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ino", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sakura", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Hinata", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Suigetsu", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Jugo", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Haku", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kurenai", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Fugaku", "B", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages C
            ("Iruka", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shizune", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Anko", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Guren", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yugao", "C", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages D
            ("Ebisu", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tenten", "D", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages E
            ("Tonton", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pakkun", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gama", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Konohamaru", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Karin", "E", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages F
            ("Mizuki", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Inari", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gato", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE ONE PIECE"""

            # Personnages X
            ("Kaido", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Luffy Gear 5", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Big Mom", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Barbe Noire", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Barbe Blanche", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shanks", "X", "https://i.imgur.com/IwGDEdb.gif", 0, 0, 0),
            ("Dragon", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gol D. Roger", "X", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages SS
            ("Akainu", "SS", "https://i.imgur.com/OkB0Vk3.gif", 0, 0, 0),
            ("Aokiji", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kizaru", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Fujitora", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Rayleigh", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Katakuri", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ryokugyu", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Garp", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sengoku", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mihawk", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Doflamingo", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Law", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kid", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zoro", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("King", "SS", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages S
            ("Crocodile", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Smoker", "S", "https://i.imgur.com/3vJPaRx.gif", 0, 0, 0),
            ("Kuma", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Oden", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sabo", "S", "https://i.imgur.com/vjcu8Gg.gif", 0, 0, 0),
            ("Marco", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sanji", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yamato", "S", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages A
            ("Brook", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Franky", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Robin", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Jinbe", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Rob Lucci", "A", "https://i.imgur.com/aewCvhP.gif", 0, 0, 0),
            ("Magellan", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ace", "A", "https://i.imgur.com/8AGmDrS.gif", 0, 0, 0),
            ("Karasu", "A", "https://picsum.photos/900/500", 0, 0, 0),
            
            # Personnages B
            ("Chooper", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nami", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ussop", "B", "https://i.imgur.com/oJD4qsv.gif", 0, 0, 0),
            ("Hina", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Buggy", "B", "https://picsum.photos/900/500", 0, 0, 0),
            

            # Personnages C
            ("Vivi", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Arlong", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Don Krieg", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tashigi", "C", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages D
            ("Koby", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Helmeppo", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dorry", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Brogy", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Lindbergh", "D", "https://picsum.photos/900/500", 0, 0, 0),
            
            # Personnages E
            ("Hatchan", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pell", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Wapol", "E", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages F
            ("Gaimon", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kaya", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Laboon", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE BLEACH"""

            # Personnages X
            ("Yhwach", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ichigo Final", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Aizen", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yamamoto", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kenpachi", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ichibe", "X", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages SS
            ("Jugram", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Uryu", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kyoraku", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Byakuya", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Toshiro", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Urahara", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yoruichi", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Unohana", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ulquiorra", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gin", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Stark", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Renji", "SS", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages S
            ("Mayuri", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Senjumaru", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Isshin", "S", "https://picsum.photos/900/500", 0, 0, 0),

            ("Rukia", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shinji", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Soi Fon", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tosen", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Baraggan", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Grimmjow", "S", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages A

            ("Nnoitra", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shuhei", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ryuken", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Orihime", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ginjo", "A", "https://picsum.photos/900/500", 0, 0, 0),
            
            
            # Personnages B

            ("Kira", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ikkaku", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kensei", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Chad", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yumichika", "B", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages C
            ("Ganju", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Marechiyo", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Love", "C", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages D
            ("Tessai", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Hanataro", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yachiru", "D", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages E
            ("Jinta", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ururu", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Keigo", "E", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages F
            ("Kon", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Karin", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yuzu", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tatsuki", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mizuiro", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE MY HERO ACADEMIA"""
            # Personnages X
            ("All Might", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Endeavor", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shigaraki", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Deku (100%)", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("All For One", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Star And Stripe", "X", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages SS
            ("Overhaul", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Hawks", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Beast Jeanist", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dabi", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mirio", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Re Destro", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages S
            ("Twice", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shoto", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Bakugo", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Eraserhead", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Tamaki", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Stain", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Fumikage", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nana Shimura", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mirko", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Lady Nagant", "S", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages A
            ("Tenya", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mt Lady", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nighteye", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sun Eater", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ryuku", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gran Torino", "A", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages B
            ("Ochaco", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Midnight", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Denki", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Crimson Riot", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nezu", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Momo", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gang Orca", "B", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages C
            ("Shindo", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Rock Lock", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Vlad King", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Testutetsu", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Snipe", "C", "https://picsum.photos/900/500", 0, 0, 0),
            
            # Personnages D
            ("Spinner", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shihai", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nomu", "D", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages E
            ("Mineta", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shoji", "E", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages F
            ("Eri", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kenji", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sansa", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE HUNTER X HUNTER"""
            # Personnages X
            ("Meruem", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gon Adulte", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Netero", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ging", "X", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages SS
            ("Kuroro", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Hisoka", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Killua", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zeno", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Silva", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Illumi", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Neferopito", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yupi", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Aruka", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages S
            ("Kurapika", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Morel", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kaito", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Feitan", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Uvogin", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Phinks", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Knuckle", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pouf", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nabunaga", "S", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages A
            ("Machi", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shoot", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Genthru", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Sharnak", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Biscuit", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Razor", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gon", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pariston", "A", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages B
            ("Pakunoda", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Shizuku", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Franklin", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Cheetu", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Korutopi", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Leorio", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kalluto", "B", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages C
            ("Zushi", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Wing", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ponzu", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pokkle", "C", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages D
            ("Kikyo", "D", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages E
            ("Tompa", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Neon", "E", "https://picsum.photos/900/500", 0, 0, 0),
            # Personnages F
            ("Komugi", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mito", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE AVATAR"""
            # Personnages X
            ("Aang (Avatar)", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ozai", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kyoshi (Avatar)", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Roku (Avatar)", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Iroh", "X", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages SS
            ("Katara", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Zuko", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Toph", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Azula", "SS", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages S
            ("Amiral Zhao", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Hama", "S", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages A
            ("Sokka", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Suki", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Ty Lee", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mai", "A", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages B
            ("Jet", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Haru", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("June", "B", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages C
            
            # Personnages D
            ("Demi-Portion", "D", "https://picsum.photos/900/500", 0, 0, 0),
            ("La Flèche", "D", "https://picsum.photos/900/500", 0, 0, 0),
            
            # Personnages E
            ("Le Duc", "E", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages F
            ("Meng", "F", "https://picsum.photos/900/500", 0, 0, 0),
            ("Pesticide", "F", "https://picsum.photos/900/500", 0, 0, 0),

            # """ PERSONNAGE JUJUTSU KAISEN"""
            # Personnages X
            ("Sukuna", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gojo", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yuta", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kenjaku", "X", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mahoraga", "X", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages SS
            ("Toji", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Aoi Todo", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Geto", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Choso", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mahito", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Jogo", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kinji Hakari", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yuki Tsukumo", "SS", "https://picsum.photos/900/500", 0, 0, 0),
            ("Dagon", "SS", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages S
            ("Megumi", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Maki", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nanami", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Higuruma", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Naobito", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Miguel", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mei mei", "S", "https://picsum.photos/900/500", 0, 0, 0),
            ("Naoya", "S", "https://picsum.photos/900/500", 0, 0, 0),
            
            
            #Personnages A
            ("Panda", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Inumaki", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kugisaki", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kamo", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Nobara", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Toge", "A", "https://picsum.photos/900/500", 0, 0, 0),
            ("Mechamaru", "A", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages B
            ("Yuji Itadori", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Kusakabe", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Takuma Ino", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Yaga", "B", "https://picsum.photos/900/500", 0, 0, 0),
            ("Gakuganji", "B", "https://picsum.photos/900/500", 0, 0, 0),
            

            # Personnages C
            ("Junpei", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Miwa", "C", "https://picsum.photos/900/500", 0, 0, 0),
            ("Utahime", "C", "https://picsum.photos/900/500", 0, 0, 0),
            

            # Personnages D
            ("Ijichi", "D", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages E
            ("Juzo", "E", "https://picsum.photos/900/500", 0, 0, 0),
            ("Momo", "E", "https://picsum.photos/900/500", 0, 0, 0),

            # Personnages F
            ("Kechizu", "F", "https://picsum.photos/900/500", 0, 0, 0),
        ]

all_synergies = [
    (1, "Akatsuki", "ATK", 0.15,"L'akkatsuki est une organisation criminelle de ninjas déserteurs.", "https://picsum.photos/900/500", "#FF0000"),
    (2, "Saiyan", "ATK", 0.15, "Les Saiyans sont connus pour leur force et leur capacité à se transformer en Super Saiyan.", "https://picsum.photos/900/500", "#FFA500"),
    (3, "Hollow", "ATK", 0.15, "Les Hollows sont des âmes corrompues qui ont perdu leur coeur et leur raison.", "https://picsum.photos/900/500", "#0000FF"),
    (4, "Mugiwara", "ATK", 0.15, "Les Mugiwara sont l'équipage de Luffy, un pirate qui cherche le One Piece.", "https://picsum.photos/900/500", "#800080"),
    (5, "Uchiha", "ATK", 0.15, "Le clan Uchiha est connu pour ses capacités de combat et son Sharingan.", "https://picsum.photos/900/500", "#FF0000"),
    (6, "Quincy", "ATK", 0.15, "Les Quincy sont des chasseurs de Hollows qui utilisent des arcs pour combattre.", "https://picsum.photos/900/500", "#FFA500"),
    (7, "Amiraux", "ATK", 0.15, "Les Amiraux sont les trois plus puissants marins de la Marine.", "https://picsum.photos/900/500", "#0000FF"),
    (8, "Espada", "ATK", 0.15, "Les Espadas sont les dix plus puissants Hollows sous les ordres d'Aizen.", "https://picsum.photos/900/500", "#800080"),
    (9, "Vongola", "ATK", 0.15, "La famille Vongola est une organisation mafieuse italienne qui utilise des anneaux pour combattre.", "https://picsum.photos/900/500", "#FF0000"),
    (10, "Yonko", "ATK", 0.3, "Les Yonkos sont les quatre plus puissants pirates du Nouveau Monde.", "https://picsum.photos/900/500", "#FFA500"),
    (11, "Akimichi", "ATK", 0.15, "Le clan Akimichi est connu pour sa technique de transformation en géant.", "https://picsum.photos/900/500", "#0000FF"),
    (12, "Vizard", "ATK", 0.15, "Les Vizards sont des Shinigamis qui ont acquis des pouvoirs de Hollows.", "https://picsum.photos/900/500", "#800080"),
    (13, "Varia", "ATK", 0.15, "La Varia est un groupe d'assassins de la famille Vongola.", "https://picsum.photos/900/500", "#FF0000"),
    (14, "Gotei 13", "ATK", 0.15, "Le Gotei 13 est une organisation de Shinigamis qui protège le monde des âmes.", "https://picsum.photos/900/500", "#FFA500"),
    (15, "Kage", "ATK", 0.15, "Les Kages sont les plus puissants ninjas de leur village.", "https://picsum.photos/900/500", "#0000FF"),
    (16, "Shichibukai", "ATK", 0.15, "Les Shichibukai sont des pirates qui ont accepté de servir la Marine.", "https://picsum.photos/900/500", "#800080"),
    (17, "Sannin", "ATK", 0.50, "Les Sannins sont les trois ninjas légendaires de Konoha.", "https://picsum.photos/900/500", "#FF0000"),
    (18, "Révolutionnaires", "ATK", 0.15, "Les Révolutionnaires sont un groupe qui lutte contre le Gouvernement Mondial.", "https://picsum.photos/900/500", "#FFA500"),
    (19, "Volonté du D", "ATK", 0.15, "La Volonté du D est une mystérieuse lignée de pirates qui défient le Gouvernement Mondial.", "https://picsum.photos/900/500", "#0000FF"),
]

all_link_synergies = {
    1 : ["Itachi", "Kisame", "Deidara", "Sasori", "Hidan", "Kakuzu", "Pain", "Konan", "Zetsu", "Tobi"], # Akatsuki
    2 : ["Goku", "Vegeta", "Gohan", "Trunks", "Goten", "Bardock", "Raditz", "Nappa", "Broly", "Cabba"], # Saiyan
    4 : ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"], # Mugiwara
    5 : ["Itachi", "Sasuke", "Madara", "Obito", "Shisui", "Fugaku", "Indra", "Izuna", "Sarada", "Boruto"], # Uchiha
    7 : ["Akainu", "Aokiji", "Kizaru", "Sengoku", "Garp", "Fujitora", "Ryokugyu", "Kong"], # Amiraux
    10 : ["Barbe Blanche", "Kaido", "Big Mom", "Shanks", "Barbe Noire","Luffy","Mihawk","Crocodile"], # Yonko
    14 : ["Yamamoto", "Unohana", "Byakuya", "Kenpachi", "Ukitake", "Shunsui", "Sajin", "Mayuri", "Toshiro", "Rukia"], # Gotei 13
    15 : ["Hashirama", "Tobirama", "Hiruzen", "Minato", "Tsunade", "Kakashi", "Naruto","Mei Terumi", "Onoki", "Gaara"], # Kage
    16 : ["Crocodile", "Doflamingo", "Mihawk", "Kuma", "Boa Hancock", "Jinbe", "Buggy", "Law", "Barbe Noire"], # Shichibukai,
    17 : ["Jiraya","Orochimaru","Tsunade"], # Sannin
    18 : ["Dragon", "Ivankov", "Kuma", "Sabo", "Koala", "Hack", "Inazuma", "Belo Betty", "Lindbergh", "Karasu"], # Révolutionnaires
    19 : ["Luffy", "Garp", "Roger", "Ace", "Dragon", "Sabo", "Law", "Barbe Noire", "Kaido", "Shanks"], # Volonté du D
}