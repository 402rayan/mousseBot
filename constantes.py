CONSTANTS = {
    'HOURLY_TICKETS': 5,
    'INVOCATION_COST': 1,
    'MULTI_INVOCATION_COST': 5,
    'MAX_CHARACTERS': 999,
    'BASE_CHANCE_VICTORY': 0.6,
    'HOURLY_XP': [5000,4000,15000,1,300000,2,5000,3200,3300,4200,4100,4001,3000,3500,4500,6000,1000,10000,5250,5100,5300,5555,4200,100000,4000,8000,20000,3000,5000,5555,5432,10000],
    'RARITY': ['F', 'E', 'D', 'C', 'B', 'A', 'S', 'SS', 'X','Z'],
    'ADMINS' : [724383641752436757,617045747862470803], # ID des admins
    'RARITY_PRICE': {
        # Nombre de tickets obtenus en vendant un personnage de la rareté correspondante
        'Z': 40,
        'X': 18,
        'SS': 7,
        'S': 4,
        'A': 2,
        'B': 1,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
    },
    'RARITY_XP': {
        # Nombre d'expérience obtenue en vendant un personnage de la rareté correspondante
        'Z': 1000000,
        'X': 180000,
        'SS': 50000,
        'S': 10000,
        'A': 6000,
        'B': 3500,
        'C': 2400,
        'D': 1300,
        'E': 1000,
        'F': 3500,
    },
    'RARITY_CHANCE': {
        # Chance d'obtenir un personnage de la rareté correspondante
        'Z': 0.001,
        'X': 0.008,
        'SS': 0.02,
        'S': 0.05,
        'A': 0.1,
        'B': 0.2,
        'C': 0.2755,
        'D': 0.1595,
        'E': 0.1,
        'F': 0.08,
    },
    'RARITY_CHANCE_HIGH': {
        # Change d'obtenir un personnage de la rareté correspondante en cas de GROS ticket
        'Z': 0.004,
        'X': 0.07,
        'SS': 0.15,
        'S': 0.30,
        'A': 0.45,
    },
    'RARITY_COLOR': {
        # Couleur des personnages de la rareté correspondante
        'Z': 0xf70dff,
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
        'Z': 1000, 'X' : 100,'SS': 75, 'S' : 60, 'A' : 50, 'B' : 30, 'C' : 20, 'D' : 0, 'E' : 0, 'F' : 0
    },
    'LISTE_MESSAGES_FIN_DE_BATAILLE' :  ["Le combat semble être terminé ...", "Le combat est fini ...", "Nous avons un vainqueur!", "...", "C'est fini!", "On dirait que c'est fini ...", "Le combat est terminé!", "C'est terminé ..."],
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
        "EREN" : 0x3f3131, "SOMA" : 0xf62a43, "NANAMI" : 0xaca97f,
        "NOUS": 0x000000, "BEERUS": 0xba7eca
        
    },
    "NOMS_GIF_INVOCATION": [
        # Nom du gif, texte à afficher, couleur du texte, pfp, isLong
        ["genkidama", "Goku vous prête sa force!", 0x4e6cd9, "goku"],
        ["narutoLight","Naruto vous prête sa force!", 0xff4e03, "naruto"],
        ["shanksPreteForce", "Shanks vous transmet un pouvoir!", 0xffce68, "shanks"],
        ["shenronInvocation", "Votre souhait est exaucé!", 0x90f724, "shenron", True],
        ["gohanTransformation", "Son Gohan vous prête sa force!", 0xaa0011, "gohanSSJ2",True],
        ["unionFaitLaForce","L'union fait la force !", 0x5cb0ef, "toriko"],
        ["bizarreInvocation","Bizarre cette invocation...", 0xe8e3e3,"megumi"],
        ["roiDesPirates","Le roi des pirates ?... Ça sera moi !", 0xd4d8cb,"luffy"],
        ["vegetaRain","...", 0x09185d, "vegeta"],
        ["luffyLaugh","Cette invocation me fait rire!",0xfefef8,"luffy"],
        ["stardustCrusaders","...",0xfec2e6, "jotaro"],
        
    ],
    'DESCRIPTION_COMMANDES' : {
        "`!tutoriel`": "Permet d'avoir un **tutoriel spécifique** de comment jouer.",

        "`!hourly`": "Permet de réclamer **tickets et expériences** chaque heure!",
        "`!tickets`": "Permet de **voir le nombre de tickets** que vous avez.",
        "`!invo` / `!summon`": "Permet d'**invoquer un personnage**.",

        "`!inve` / `!sac` / `!box`": "Permet de **voir votre inventaire**.",
        "`!info {personnage}`": "Permet de **voir les informations d'un personnage**.",
        "`!sell {personnage}` / `!vendre`": "Permet de **vendre un personnage** contre tickets et expérience.",
        "`!team` / `!team @personne`": "Permet de **voir votre team** ou celle de quelqu'un.",
        "`!auto`": "Permet de **voir vos meilleurs teams** potentiels",

        "`!ajouterteam` / `!addteam {position} {personnage}`": "Permet d'**ajouter un personnage à votre team**.",

        "`!pvp @personne`": "Permet de **combattre un autre joueur** en pariant des tickets.",
        "`!infoSynergie {nom}`": "Permet de **voir les détenteurs d'une synergie**.",
        "`!stats` / `!stats @personne`": "Permet de **voir vos statistiques**.",
        
        "`!power` / `!puissance`": "Permet de **voir votre puissance** basé sur l'inventaire.",
        "`!classement`": "Permet de **voir le classement** en fonction de la puissance parmi votre serveur.",
        "`!givetickets @personne {nombre}`": "Permet de **donner des tickets** à un autre joueur.",
        "`!technique {personnage}`": "Permet de **voir les techniques d'un personnage**. **EN CONSTRUCTION**",
        "`!infoTechnique {nom}`": "Permet de **voir une technique en particulière**. **EN CONSTRUCTION**",
    },
    "LISTE_TUTORIEL" : [
        ["Bienvenue sur le tutoriel de **Mousse**", "Le but est simple! Il faut invoquer des personnages!\nCela coûte des tickets!\nAvec ces personnages plusieurs choix s'offrent à nous :\n- Essayer de former la meilleure équipe possible avec des synergies!\n- Affronter ses amis la commande `!pvp`\n- Découvrir l'histoire du jeu avec `!histoire`\n- Compléter la collection de tous les personnages! Visible avec `!statistique`", "https://i.imgur.com/je30fG0.gif"],
        ["Réclamer des tickets","Vous pouvez réclamer des tickets toutes les heures grâce à la commande `!hourly`", "https://i.imgur.com/IwF6GGe.gif"],
        ["Voir ses tickets","Vous pouvez voir vos tickets grâce à la commande `!tickets` , Aller, faites le!", "https://i.imgur.com/uI2K7CT.gif"],
        ["Invoquer des personnages","Vous pouvez invoquer des personnages grâce à la commande `!invocation`", "https://i.imgur.com/rDTgoJF.gif"],
        ["Voir les informations d'un personnage","Vous pouvez voir les informations d'un personnage grâce à la commande `!info #personnage`", "https://i.imgur.com/crIn1Gd.gif"], #https://i.imgur.com/ZSWdXAH.gif
        ["Voir son inventaire","Vous pouvez voir votre inventaire grâce à la commande `!inventaire`", "https://i.imgur.com/TnBrvNu.gif"],
        ["Créer sa team automatiquement","Vous pouvez créer votre team automatiquement grâce à la commande `!auto`", "https://i.imgur.com/O69GxIz.gif"],
        ["Ajouter un personnage à sa team","Vous pouvez ajouter manuellement un personnage à votre team grâce à la commande `!addteam {nombre} #nom`", "https://i.imgur.com/fu1vlTe.gif"],
        ["Jouer au mode Histoire","Vous pouvez jouer au mode histoire grâce à la commande `!histoire`", "https://i.imgur.com/2Nnskt8.gif"],
        ["Vendre un personnage","Vous pouvez vendre un personnage grâce à la commande `!vendre` ou `!sell #personnage`", "https://i.imgur.com/pndwDbg.gif"],
        ["Combattre un autre joueur","Vous pouvez combattre un autre joueur grâce à la commande `!pvp @personne`", "https://i.imgur.com/srxwlXO.gif"],
        ["Voir les détenteurs d'une synergie","Vous pouvez voir les détenteurs d'une synergie grâce à la commande `!infoSynergie`", "https://i.imgur.com/H8B6IZE.gif"],
        ["Voir ses statistiques","Vous pouvez voir vos statistiques grâce à la commande `!stats` ou `!stats @personne`", "https://i.ibb.co/pzztmhD/ezgif-2-0df5ddd9b1.gif"], # https://i.imgur.com/ScdroHQ.gif
        ["Et bien d'autres!","Il y a encore plein de commandes à découvrir! N'hésitez pas à les voir dans `!help`", "https://i.imgur.com/F06wJCG.gif"],
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
    "🎉   🎁   🎉   🎁",
    "🤩   🎊   🎉   🎈",
    "Est-ce que c'est vraiment possible ?",
    "C'est un signe du destin !",
    "Je suis sûr que c'est quelque chose de rare !",
    "Peut-être que..",
    "🤩   🤩   🤩   🤩",
    "🎉   🎉   🎉   🎉",
    "🎊   🎊   🎊   🎊",
    "🎁   🎁   🎁   🎁",
    "🎈   🎈   🎈   🎈",
    "Est-ce que c'est un signe ?",
    "C'est le moment de vérité !",
    "Le suspens est à son comble...",
]


ennemis = {
    "ROB_LUCCI_TRANSFORM" : {
        'nom' : 'Rob Lucci',
        'couleur' : CONSTANTS['COLORS']['DARK_RED'],
        'nomGif' : 'robLucciTransform',
        'nomPfp' : 'robLucciTransform',
        'isNotGif' : False,
        'stats' : {
            'HP' : 15000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "ROB_LUCCI" : {
        'nom' : 'Rob Lucci',
        'couleur' : CONSTANTS['COLORS']['DARK_RED'],
        'nomGif' : 'robLucci',
        'nomPfp' : 'robLucci',
        'isNotGif' : False,
        'stats' : {
            'HP' : 10000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "NANAMI" : {
        'nom' : 'Kento Nanami',
        'couleur' : CONSTANTS['COLORS']['NANAMI'],
        'nomGif' : 'nanami',
        'nomPfp' : 'nanami',
        'isNotGif' : False,
        'stats' : {
            'HP' : 13000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "YORUICHI" : {
        'nom' : 'Yoruichi',
        'couleur' : CONSTANTS['COLORS']['YORUICHI'],
        'nomGif' : 'yoruichi',
        'nomPfp' : 'yoruichi',
        'isNotGif' : False,
        'stats' : {
            'HP' : 12000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "FRANKLIN" : {
        'nom' : 'Franklin',
        'couleur' : CONSTANTS['COLORS']['FRANKLIN'],
        'nomGif' : 'franklinPose',
        'nomPfp' : 'franklin',
        'isNotGif' : True,
        'stats' : {
            'HP' : 2500,
            'ATK' : 1500,
            'DEF' : 800,
        }
    },
    "Rui" : {
        'nom' : 'Rui',
        'couleur' : 0x490c11,
        'nomGif' : 'rui',
        'nomPfp' : 'rui',
        'isNotGif' : False,
        'stats' : {
            'HP' : 2000,
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
            'HP' : 2500,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "Dorry et Broggy" : {
        'nom' : 'Dorry et Broggy',
        'couleur' : CONSTANTS['COLORS']['BROGGY'],
        'nomGif' : 'dorryBroggyFight',
        'isNotGif' : True,
        'nomPfp' : 'broggy',
        'stats' : {
            'HP' : 2000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "UVOGUINE" : {
        'nom' : 'Uvogin',
        'couleur' : CONSTANTS['COLORS']['UVOGUINE'],
        'nomGif' : 'uvoguine',
        'nomPfp' : 'uvoguine',
        'isNotGif' : False,
        'stats' : {
            'HP' : 8000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
    "SAIBAMAN" : {
        'nom' : 'Saibaman',
        'couleur' : CONSTANTS['COLORS']['SAIBAMAN'],
        'nomGif' : 'saibaman',
        'nomPfp' : 'saibaman',
        'isNotGif' : False,
        'stats' : {
            'HP' : 1000,
            'ATK' : 0,
            'DEF' : 0,
        }
    },
}
