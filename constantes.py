CONSTANTS = {
    'HOURLY_TICKETS': 4,
    'INVOCATION_COST': 1,
    'MAX_CHARACTERS': 999999,
    'BASE_CHANCE_VICTORY': 0.6,
    'RARITY': ['F', 'E', 'D', 'C', 'B', 'A', 'S', 'SS', 'X'],
    'ADMINS' : [724383641752436757,617045747862470803], # ID des admins
    'RARITY_PRICE': {
        # Nombre de tickets obtenus en vendant un personnage de la rareté correspondante
        'X': 50,
        'SS': 25,
        'S': 12.5,
        'A': 5,
        'B': 2.5,
        'C': 0.5,
        'D': 0.25,
        'E': 0.15,
        'F': 0.1,
    },
    'RARITY_CHANCE': {
        # Chance d'obtenir un personnage de la rareté correspondante
        'X': 0.01,
        'SS': 0.02,
        'S': 0.05,
        'A': 0.1,
        'B': 0.2,
        'C': 0.3,
        'D': 0.15,
        'E': 0.1,
        'F': 0.07,
    },
    'RARITY_CHANCE_HIGH': {
        # Change d'obtenir un personnage de la rareté correspondante en cas de GROS ticket
        'X': 0.1,
        'SS': 0.15,
        'S': 0.25,
        'A': 0.3,
        'B': 0.2
    },
    'RARITY_COLOR': {
        # Couleur des personnages de la rareté correspondante
        'X': 0x1e103b, 
        'SS': 0x8C001A,
        'S': 0xD82F00,
        'A': 0xF5B521,
        'B': 0x4C66D6,
        'C': 0x2CBBCB,
        'D': 0x1E9021,
        'E': 0xD3CB34,
        'F': 0x9CA1A7,
    },
    'RARITY_POWER': {
        # Puissance des personnages de la rareté correspondante
        'X' : 100,'SS': 75, 'S' : 60, 'A' : 50, 'B' : 30, 'C' : 20, 'D' : 0, 'E' : 0, 'F' : 0
    },
    'INGREDIENTS': {
        "Pomme": "🍎",
        "Banane": "🍌",
        "Pain": "🍞",
        "Poulet": "🍗",
        "Pizza": "🍕",
        "Poisson": "🐟",
        "Sushi": "🍣",
        "Glace": "🍦",
        "Hamburger": "🍔",
        "Frites": "🍟",
        "Hot Dog": "🌭",
        "Pop Corn": "🍿",
        "Tarte": "🥧",
        "Gâteau": "🍰",
        "Chocolat": "🍫",
        "Bonbon": "🍬",
        "Lait": "🥛",
        "Café": "☕",
        "Jus": "🥤",
        "Vin": "🍷",
        "Bière": "🍺",
        "Eau": "💧",
        "Carotte": "🥕",
        "Tomate": "🍅",
        "Pomme de terre": "🥔",
        "Oignon": "🧅",
        "Ail": "🧄",
        "Concombre": "🥒",
        "Courgette": "🥬",
        "Champignon": "🍄",
        "Brocoli": "🥦",
        "Piment": "🌶️",
        "Citron": "🍋",
        "Orange": "🍊",
        "Poire": "🍐",
        "Ananas": "🍍",
        "Pastèque": "🍉",
        "Melon": "🍈",
        "Fraise": "🍓",
        "Cerise": "🍒",
        "Raisin": "🍇",
        "Noix de coco": "🥥",
        "Noix": "🌰",
        "Miel": "🍯",
        "Sel": "🧂",
        "Pêche": "🍑",
        "Croissant": "🥐",
        "Baguette": "🥖",
        "Fromage": "🧀",
        "Menthe": "🌿",
    },
    'COLORS': {
        'HISTOIRE' : 0x00BFFF,
        'INCONNU' : 0x000000,
        'FORET' : 0x228B22,
        'SHANKS' : 0xcc1215,
        'SAIBAMAN' : 0x00FF00,
        'BRUIT' : 0x261b12,
        'ENRICO_PUCCI' : 0x1c0116,
        'FUMEE' : 0x1c1c1c,
        'MONTAGNE' : 0x8B4513,
        'NARRATEUR' : 0x360801,
        'BROGGY' : 0x8B0000,
        'FIN_NIVEAU' : 0x00bf66,
        'NIGHT' : 0x000000,
        'DARK_RED' : 0x8B0000,
        'FROID' : 0x87CEEB,
        'ZUKO' : 0x8B0000,
        'RUI' : 0xFFFFFF,
        'GROTTE' : 0x8B4513,
        'PURPLE_HAZE' : 0xa424c7,
        'LIGHT' : 0xf4ff91, 'TICKET_DIAMANT' : 0xcd81a1,
        'CIEL' : 0x87CEEB, 'YORUICHI': 0x4d073b,
        'DANGER' : 0xff0000, 'MAHITO' : 0xa8bacd,
        'FLAMME' : 0xff0000, 'FRANKLIN' : 0x5c3307,
        'BRIGADE_FANTOME' : 0x000000, 'UVOGUINE' : 0x5c5d51,
        "C18" : 0xeedbab, "DENKI" : 0xb38d48, "BAGGY" : 0xa10f21,
        "ERWIN" : 0xb89e81, "LEORIO" : 0x3a476b, "GRAY_CAT" : 0x3c3c3d,
        "EREN" : 0x3f3131
        
    },
    "NOMS_GIF_INVOCATION": [
        # Nom du gif, texte à afficher, couleur du texte, pfp, isLong
        # ["genkidama", "Goku vous prête sa force!", 0x4e6cd9, "goku"],
        # ["narutoLight","Naruto vous prête sa force!", 0xff4e03, "naruto"],
        # ["shanksPreteForce", "Shanks vous transmet un pouvoir!", 0xffce68, "shanks"],
        ["shenronInvocation", "Votre souhait est exaucé!", 0x90f724, "shenron", True],
    ]
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
    "Je suis sûr que c'est quelque chose de rare !",
    "Peut-être que..",
    "🤩   🤩   🤩   🤩",
    "🎉   🎉   🎉   🎉",
    "🎊   🎊   🎊   🎊",
    "🎁   🎁   🎁   🎁",
    "🎈   🎈   🎈   🎈",
    "C'est le moment de vérité !",
    "Le suspens est à son comble...",
]


ennemis = {
    "YORUICHI" : {
        'nom' : 'Yoruichi',
        'couleur' : CONSTANTS['COLORS']['YORUICHI'],
        'nomGif' : 'yoruichi',
        'nomPfp' : 'yoruichi',
        'isNotGif' : False,
        'stats' : {
            'HP' : 2000,
            'ATK' : 2500,
            'DEF' : 2200,
        }
    },




    "FRANKLIN" : {
        'nom' : 'Franklin',
        'couleur' : CONSTANTS['COLORS']['FRANKLIN'],
        'nomGif' : 'franklinPose',
        'nomPfp' : 'franklin',
        'isNotGif' : True,
        'stats' : {
            'HP' : 1000,
            'ATK' : 1100,
            'DEF' : 500,
        }
    },
    "Rui" : {
        'nom' : 'Rui',
        'couleur' : 0x490c11,
        'nomGif' : 'rui',
        'nomPfp' : 'rui',
        'isNotGif' : False,
        'stats' : {
            'HP' : 1000,
            'ATK' : 1100,
            'DEF' : 500,
        }
    },
    "Tompa" : {
        'nom' : 'Tompa',
        'couleur' : CONSTANTS['COLORS']['FORET'],
        'nomGif' : 'tompa',
        'nomPfp' : 'tompaPfp',
        'isNotGif' : True,
        'stats' : {
            'HP' : 250,
            'ATK' : 350,
            'DEF' : 500,
        }
    },
    "Haku" : {
        'nom' : 'Haku',
        'couleur' : CONSTANTS['COLORS']['FROID'],
        'nomGif' : 'haku',
        'nomPfp' : 'haku',
        'isNotGif' : False,
        'stats' : {
            'HP' : 500,
            'ATK' : 600,
            'DEF' : 500,
        }
    },
    "Dorry et Broggy" : {
        'nom' : 'Dorry et Broggy',
        'couleur' : CONSTANTS['COLORS']['BROGGY'],
        'nomGif' : 'dorryBroggyFight',
        'isNotGif' : True,
        'nomPfp' : 'broggy',
        'stats' : {
            'HP' : 500,
            'ATK' : 400,
            'DEF' : 500,
        }
    },
    "UVOGUINE" : {
        'nom' : 'Uvogin',
        'couleur' : CONSTANTS['COLORS']['UVOGUINE'],
        'nomGif' : 'uvoguine',
        'nomPfp' : 'uvoguine',
        'isNotGif' : False,
        'stats' : {
            'HP' : 1340,
            'ATK' : 1340,
            'DEF' : 1340,
        }
    },
    "SAIBAMAN" : {
        'nom' : 'Saibaman',
        'couleur' : CONSTANTS['COLORS']['SAIBAMAN'],
        'nomGif' : 'saibaman',
        'nomPfp' : 'saibaman',
        'isNotGif' : False,
        'stats' : {
            'HP' : 150,
            'ATK' : 130,
            'DEF' : 150,
        }
    },
}