image_temporaire = "https://picsum.photos/900/500"
all_characters_templates = {
            "Dragon Ball" : [ # ✅
            ("Son Goku", "X", "https://i.imgur.com/1dpz2hV.gif", 905, 1050, 900),
            ("Zeno", "X", "https://i.imgur.com/W579wtw.gif", 800, 1300, 800),
            ("Grand Pretre", "X", "https://i.imgur.com/XFKPYIb.gif", 1000, 1200, 1000),
            ("Whis", "X", 'https://i.imgur.com/UHCV2D1.gif', 1050, 1040, 1000),
            ("Vados", "X", 'https://i.imgur.com/6WuAjqS.gif',1010, 1050, 1000),
            ("Beerus", "X", 'https://i.imgur.com/9ZLOxBK.gif', 920, 1150, 910),
            ("Gohan", "X", 'https://i.imgur.com/SJPfZLY.gif', 950, 960, 970),

            # Personnages SS
            ("Belmod", "SS", "https://i.imgur.com/Yeq7JQY.gif", 800, 900, 800),
            ("Piccolo", "SS", "https://i.imgur.com/srHRyMX.gif", 800, 850, 800),
            ("Champa", "SS", 'https://i.imgur.com/F7Q78tL.gif', 800, 1000, 800),
            ("Vegeto", "SS", "https://i.imgur.com/DBewj1R.gif", 770, 810, 770),
            ("Gogeta", "SS", "https://i.imgur.com/5sTq4Q6.gif", 750, 800, 760),
            ("Broly", "SS", "https://i.imgur.com/gstppUE.gif", 750, 780, 730), 
            ("Jiren", "SS", 'https://i.imgur.com/K7M25Xe.gif', 740, 750, 745),
            ("Zamasu", "SS", 'https://i.imgur.com/Cz6XOfz.gif', 730, 750, 735),
            ("Vegeta", "SS", "https://i.imgur.com/CkK8SBp.gif", 700, 750, 680),
            ("Toppo", "SS", 'https://i.imgur.com/PIp2SBH.gif', 710, 730, 720),
            
            # Personnages S
            ("Kefla", "S", 'https://i.imgur.com/VjmzJvV.gif', 560, 550, 560),
            ("Black Goku", "S", 'https://i.imgur.com/20z0F8R.gif', 550, 620, 560),
            ("Hit", "S", 'https://i.imgur.com/vPZDJKq.gif', 520, 610, 540),
            ("C-17", "S", 'https://i.imgur.com/UsE616g.gif', 545, 545, 545),
            ("Kale", "S", 'https://i.imgur.com/6K1YluE.gif', 515, 530, 540),

            # Personnages A
            ("Golden Freezer", "A", 'https://i.imgur.com/dqV5UcM.gif', 430, 425, 450),
            ("Trunks", "A", 'https://i.imgur.com/4j08x7s.gif', 445, 490, 460),
            ("Caulifla", "A", 'https://i.imgur.com/38lAUJ6.gif', 420, 430, 415),
            ("Kid Buu", "A", 'https://i.imgur.com/Aycebhm.gif', 410, 440, 420),

            # Personnages B
            ("Gotenks", "B", 'https://i.imgur.com/IkgUQSo.jpeg', 320, 310, 300),
            ("Cabba", "B", 'https://i.imgur.com/eOEdwJB.jpeg', 315, 340, 305),
            ("Cell", "B", 'https://i.imgur.com/wzqjr1t.gif', 340, 350, 400),
            ("Majin Buu", "B", 'https://i.imgur.com/dRswoNA.gif', 400, 300, 400),
            ("C-18", "B", 'https://i.imgur.com/mFr10hN.jpeg', 333, 333, 333),
            ("Frost", "B", 'https://i.imgur.com/RrX5env.jpeg', 325, 315, 350),
            ("Krillin", "B", 'https://i.imgur.com/9RsmzSP.jpeg', 310, 305, 290),
            ("Ten Shin Han", "B", 'https://i.imgur.com/74avz2G.jpeg', 305, 300, 290),
            ("Tortue Geniale", "B", 'https://i.imgur.com/DCbiqFg.jpeg', 320, 320, 295),
            ("Shenron", "B", "https://i.imgur.com/DiVySQ9.gif", 333, 333, 333),

            # Personnages C
            ("Dabra", "C", 'https://i.imgur.com/bzYsWfm.jpeg', 260, 265, 255),
            ("Bardock", "C", 'https://i.imgur.com/MSTYpQg.jpeg', 260, 280, 250),
            ("Roi Vegeta", "C", "https://i.imgur.com/mtsE4Cy.jpeg", 255, 270, 245),
            ("Uub", "C", "https://i.imgur.com/fZvqk1U.jpeg", 250, 250, 235),
            ("Kaio Shin", "C", "https://i.imgur.com/NNcDlai.jpeg", 230, 240, 270),
            ("Goten", "C", 'https://i.imgur.com/LaP4Y5P.jpeg', 240, 255, 270),
            # Personnages D
            ("Cell JR", "D", "https://i.imgur.com/phScIgK.png", 200, 195, 190),
            ("Ginyu", "D", 'https://i.imgur.com/dlJPBnS.png', 180, 180, 180),
            ("Nappa", "D", 'https://i.imgur.com/BlMwN5j.png', 175,180, 160),
            ("Yamcha", "D", 'https://i.imgur.com/aiWaIkE.jpeg', 165, 155, 120),
            ("Raditz", "D", 'https://i.imgur.com/tpHt9cZ.jpeg', 155, 140, 135),
            
            # Personnages E

            ("Chaozu", "E", 'https://i.imgur.com/ptM5r0p.jpeg', 135, 125, 115),
            ("Tao Pai Pai", "E", 'https://i.imgur.com/x1oDMNg.jpeg', 120, 120, 120),
            ("Jaco", "E", "https://i.imgur.com/HM25j5z.jpeg", 110, 120, 90),
            ("Saibaman", "E", 'https://i.imgur.com/pDn0yZZ.jpeg', 100, 100, 100),
            ("Babidi", "E", 'https://i.imgur.com/4u5Iy99.jpeg', 110, 130, 80),
            ("Videl", "E", "https://i.imgur.com/cVYDJ9A.png", 100, 100, 90),
            ("Yajirobe", "E", "https://i.imgur.com/7yk8rDr.png", 90, 100, 85),
           # Personnages F
            ("Oolong", "F", 'https://i.imgur.com/K00wC2U.png', 20, 10, 20),
            ("Mr. Satan", "F", 'https://i.imgur.com/1GwcT5j.jpeg', 30, 40, 30),
            ("Pilaf", "F", 'https://i.imgur.com/4M83VcL.png', 10, 10, 10),
            #("Plume", "F", 'https://static.wikia.nocookie.net/dragonball/images/c/c0/Pu_erh_vs_Oolong.png/revision/latest?cb=20150803173741&path-prefix=fr', 0, 0, 0),
            ("Karin", "F", 'https://i.imgur.com/ig9vUqp.png', 10, 5, 5),
            ("Chichi", "F", 'https://i.imgur.com/bES47n2.png', 20, 10, 10),
            ("Bulma", "F", 'https://i.imgur.com/IlZlAEM.png', 20, 10, 10),
            #("Dende", "E", 'https://static.wikia.nocookie.net/dragonball/images/4/45/Dende.png/revision/latest?cb=20150705191047&path-prefix=fr', 0, 0, 0),
            #("Gyumao", "F", 'https://static.wikia.nocookie.net/dragonball/images/c/c2/300px-Ox-KingPresentsEp05-1-.png/revision/latest?cb=20150707150216&path-prefix=fr', 0, 0, 0),
            #("Dr. Brief", "F", 'https://static.wikia.nocookie.net/dragonball/images/8/87/Vlcap-2015-05-23-12h32m25s768.png/revision/latest?cb=20150523110821&path-prefix=fr', 0, 0, 0),
            ],
            "Naruto" : [
            # Personnages X
            ("Naruto", "X", "https://i.imgur.com/n8cS6mP.gif", 0, 0, 0),
            ("Sasuke", "X", "https://i.imgur.com/PYEEX2h.gif", 0, 0, 0), 
            ("Kaguya", "X", "https://i.imgur.com/P3M8HQH.gif", 0, 0, 0),
            ("Madara", "X", "https://i.imgur.com/c0NF2KN.gif", 0, 0, 0),
            ("Rikudo", "X", "https://i.imgur.com/bn7KwyD.gif", 0, 0, 0),
            ("Obito", "X", "https://i.imgur.com/A6roLXk.gif", 0, 0, 0),
            # Personnages SS
            ("Indra", "SS", "https://i.imgur.com/dlXLwgN.gif", 0, 0, 0),
            ("Ashura", "SS", "https://i.imgur.com/aRMeDPa.gif", 0, 0, 0),
            ("Hashirama", "SS", 'https://media1.tenor.com/m/sd97xiiyvtkAAAAC/hashirama-jutsu-naruto.gif', 0, 0, 0),
            ("Tobirama", "SS", 'https://media1.tenor.com/m/4CQxkScISFkAAAAC/tobirama-senju-tobirama.gif', 0, 0, 0),
            ("Toneri", "SS", 'https://media1.tenor.com/m/3iys2Q_ijIsAAAAC/chakra-tenseigan-tenseigan.gif', 0, 0, 0),
            ("Pain", "SS", "https://s12.gifyu.com/images/SZkqx.gif", 0, 0, 0),
            ("Itachi", "SS", 'https://media1.tenor.com/m/9T4QZFujmdcAAAAd/itachi-itachi-uchiha.gif', 0, 0, 0),
            ("Minato", "SS", 'https://image.myanimelist.net/ui/BQM6jEZ-UJLgGUuvrNkYUCG8p-X1WhZLiR4h-oxkqQeLoNhlaOE5k1-WWjqlPZDj72Af1W1e42Hk51ndFh6GBw', 0, 0, 0), # TOREVIEW
            ("Kabuto", "SS", 'https://media1.tenor.com/m/-nxrWjUdXRYAAAAC/anime-kabuto-yakushi.gif', 0, 0, 0),
            ("Guy (8 portes)", "SS", 'https://media1.tenor.com/m/xa87Jinyrc0AAAAC/naruto-shippuden-might-guy.gif', 0, 0, 0),
            ("Momoshiki", "SS", 'https://media1.tenor.com/m/74cmic57CwoAAAAC/momoshiki.gif', 0, 0, 0),
            # Personnages S
            ("Shisui", "S", 'https://media1.tenor.com/m/_To3NtVgZv0AAAAC/shisui-uchiha-shisui.gif', 0, 0, 0),
            ("Hidan", "S", 'https://i.imgur.com/Nz7dGAU.png', 0, 0, 0),
            ("Kakuzu", "S", 'https://i.imgur.com/BKf04A1.gif', 0, 0, 0),
            ("Hiruzen", "S", 'https://media1.tenor.com/m/j6hgBpYSrL4AAAAC/hiruzen-sarutobi.gif', 0, 0, 0),
            ("Orochimaru", "S", 'https://media1.tenor.com/m/5lzbp1JeaGoAAAAd/anime-naruto-shippuden.gif', 0, 0, 0),
            ("Mei Terumi", "S", "https://i.imgur.com/JTaGhQQ.gif", 0, 0, 0),
            ("Onoki", "S", "https://pa1.aminoapps.com/8436/0050341a556d26a1e018daa2d679190837ffd8a2r1-500-281_hq.gif", 0, 0, 0),
            ("Gaara", "S", 'https://i.imgur.com/39HCNme.png', 0, 0, 0),
            ("Tsunade", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808357678472232960/Tsunade.gif', 0, 0, 0),
            ("Kakashi", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808401405283008593/KAKASHI.gif', 0, 0, 0),
            ("Kisame", "S", 'https://i.imgur.com/50KuDl3.gif', 0, 0, 0),
            ("Darui", "S", 'https://i.imgur.com/4agHAoM.gif', 0, 0, 0),
            ("Asuma", "S", 'https://i.imgur.com/lGIqLP3.gif', 0, 0, 0),
            ("Kimimaro", "S", 'https://i.imgur.com/OEKnkD4.png', 0, 0, 0),
            ("Shikamaru", "S", 'https://i.imgur.com/KySPqGV.gif', 0, 0, 0),
            ("Rock Lee", "S", 'https://i.imgur.com/1V4WwG9.png', 0, 0, 0),
            ("Sasori", "S", 'https://i.imgur.com/RlpI6Rd.gif', 0, 0, 0),
            ("Deidara", "S", 'https://i.imgur.com/k83MFjs.gif', 0, 0, 0),
            ("Killer Bee", "S", "https://64.media.tumblr.com/0857bfcd4a3b9401ea2a12eaf84b0837/tumblr_n1b28tG2DJ1sigvrqo3_500.gif", 0, 0, 0),
            ("Jiraya", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808356331022319616/JIRAYA.gif', 0, 0, 0),
            ("Izuna", "S", 'https://i.imgur.com/OxGlzHg.png', 0, 0, 0),
            ("Konan", "S", 'https://i.imgur.com/3mOmZ0v.gif', 0, 0, 0),
            ("Tobi", "S", 'https://64.media.tumblr.com/a6ac04d437e10a8c383c601e9f8421a6/tumblr_n5vm5cCKrX1qk9powo1_500.gif', 0, 0, 0),

            # Personnages A 
            ("Yamato (ANBU)", "A", "https://i.pinimg.com/originals/9d/49/b6/9d49b6f4cbb2548a130d259a6c302ede.gif", 0, 0, 0), #TO REVIEW
            ("Sai", "A", 'https://i.imgur.com/03ICbLj.gif', 0, 0, 0),
            ("Temari", "A", 'https://cdn.discordapp.com/attachments/805054171661336590/817119251750977566/TEMARI.gif', 0, 0, 0),
            
            # Personnages B
            ("Neji", "B", "https://i.imgur.com/acFMgGN.png", 0, 0, 0),
            ("Kankuro", "B", 'https://i.imgur.com/6h0fZTJ.png', 0, 0, 0),
            ("Choji", "B", 'https://media1.tenor.com/m/FAqetz7SiCEAAAAd/choji.gif', 0, 0, 0), #TO REVIEW
            ("Shino", "B", 'https://i.imgur.com/mVxNOAM.png', 0, 0, 0),
            ("Kiba", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808361778567970876/KIBA.gif', 0, 0, 0),
            ("Ino", "B", 'https://media1.tenor.com/m/tdptC0lOIB4AAAAC/ino-yamanaka-ino.gif', 0, 0, 0),
            ("Sakura", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808354355744342026/SAKUA.gif', 0, 0, 0),
            ("Hinata", "B", 'https://i.imgur.com/VsFYMA1.gif', 0, 0, 0),
            ("Suigetsu", "B", 'https://i.imgur.com/E6d3rSt.gif', 0, 0, 0),
            ("Jugo", "B", 'https://i.imgur.com/lfSps90.png', 0, 0, 0),
            ("Haku", "B", 'https://i.imgur.com/vqQD56N.png', 0, 0, 0),
            ("Kurenai", "B", 'https://i.imgur.com/1E2Ux2a.png', 0, 0, 0),
            ("Fugaku", "B", "https://hero.fandom.com/wiki/Fugaku_Uchiha", 0, 0, 0), #TO REVIEW
            ("Zabuza", "B", "https://i.imgur.com/ntmenx6.png", 0, 0, 0), #TO REVIEW

            # Personnages C
            ("Iruka", "C", 'https://i.imgur.com/p0YmijL.png', 0, 0, 0),
            ("Zetsu", "C", "https://cdn.shopify.com/s/files/1/0046/2779/1960/files/black_zetsu.jpg?v=1583191483", 0, 0, 0),
            ("Shizune", "C", "https://i.imgur.com/53rdzBL.png", 0, 0, 0),
            ("Anko", "C", "https://static.wikia.nocookie.net/narutoinuyashapokemnyharrypotter/images/0/08/Anko_Mitarashi.jpg/revision/latest?cb=20130327192458&path-prefix=es", 0, 0, 0),
            ("Guren", "C", "https://static.wikia.nocookie.net/naruto/images/9/90/Guren.png/revision/latest?cb=20171125162907&path-prefix=fr", 0, 0, 0),
            ("Yugao", "C", "https://static.wikia.nocookie.net/naruto/images/9/9a/Y%C3%BBgao_Uzuki.png/revision/latest?cb=20170810173430&path-prefix=fr", 0, 0, 0),
            ("Sarada", "C", "https://i0.wp.com/www.univers-otaku.com/wp-content/uploads/2020/12/sarada-uchiha.jpg?resize=740%2C370&ssl=1", 0, 0, 0),
            ("Tenten", "C", "https://i.imgur.com/s6MEz46.png", 0, 0, 0),
            ("Karin (naruto)", "C", "https://static.wikia.nocookie.net/naruto/images/5/50/Karin.png/revision/latest?cb=20201231015434&path-prefix=fr", 0, 0, 0),
            # Personnages D
            ("Ebisu", "D", 'https://i.imgur.com/qWpczNK.png', 0, 0, 0),

            # Personnages E
            ("Konohamaru", "E", 'https://i.imgur.com/aZoURBF.png', 0, 0, 0),
            ("Mizuki", "E", "https://static.wikia.nocookie.net/naruto/images/9/9c/Mizuki.png/revision/latest?cb=20210529210947&path-prefix=fr", 0, 0, 0),


            # Personnages F
            ("Tonton", "F", "https://static.wikia.nocookie.net/xianb/images/f/fa/60t.png/revision/latest/scale-to-width-down/579?cb=20141101233045", 0, 0, 0),
            ("Pakkun", "F", "https://lh4.googleusercontent.com/vh79H5M8vWfVyuSiNnhk27N59eFH-ukdQUT028m5kmqGsPHp5pO74qpVbTpkhdX80w3utduzz1PaUVEj8ZMAblZXV9n-R4_Z7wdhX1PHxHJDEY7DQbDWOaIVeztagZRM_9WTEYqdRHpawafgywENVw", 0, 0, 0),

            ("Inari", "F", "https://static.wikia.nocookie.net/naruto/images/a/af/Inari_Parte_I_Anime.png/revision/latest?cb=20130829123658&path-prefix=es", 0, 0, 0),
            ("Gato", "F", "https://static.wikia.nocookie.net/villains/images/2/2e/Gat%C5%8D_%28Naruto%29.jpg/revision/latest?cb=20120817183043", 0, 0, 0),
],
            "One Piece" : [
            # Personnages X
            ("Kaido", "X", "https://i.imgur.com/BMDbkl8.gif", 0, 0, 0),
            ("Luffy", "X", "https://i.imgur.com/EmzijMq.gif", 0, 0, 0), # TOREVIEW
            ("Big Mom", "X", "https://i.imgur.com/tPjCbUc.gif", 0, 0, 0),
            ("Barbe Noire", "X", "https://i.pinimg.com/originals/08/74/d1/0874d121307b3cc5c123cbea31146127.gif", 0, 0, 0),
            ("Barbe Blanche", "X", "https://i.imgur.com/BdnDfQj.gif", 0, 0, 0),
            ("Shanks", "X", "https://i.imgur.com/faZclqg.gif", 0, 0, 0),
            ("Dragon", "X", "https://i.imgur.com/Zy9hmOz.gif", 0, 0, 0),
            ("Gol D. Roger", "X", "https://i.imgur.com/jhHkjfz.gif", 0, 0, 0),

            # Personnages SS
            ("Akainu", "SS", "https://i.imgur.com/OkB0Vk3.gif", 0, 0, 0),
            ("Aokiji", "SS", 'https://i.imgur.com/LCqY9UI.gif', 0, 0, 0),
            ("Kizaru", "SS", 'https://i.imgur.com/nTGQsXq.png', 0, 0, 0),
            ("Fujitora", "SS", 'https://i.imgur.com/27FScKO.jpg', 0, 0, 0),#TO REVIEW
            ("Rayleigh", "SS", 'https://i.imgur.com/HzaJdFI.gif', 0, 0, 0),
            ("Katakuri", "SS", 'https://i.imgur.com/5z0sR8N.gif', 0, 0, 0),
            ("Ryokugyu", "SS", 'https://i.imgur.com/27FScKO.jpg', 0, 0, 0),
            ("Garp", "SS", 'https://i.imgur.com/ZLd4sdw.gif', 0, 0, 0),
            ("Mihawk", "SS", 'https://i.imgur.com/UICGMYV.gif', 0, 0, 0),
            ("Doflamingo", "SS", 'https://i.imgur.com/HHCqR9J.jpg', 0, 0, 0),
            ("Law", "SS", 'https://i.imgur.com/xJpnwDU.png', 0, 0, 0),
            ("Kid", "SS", 'https://i.imgur.com/5WxLV4L.gif', 0, 0, 0),
            ("Zoro", "SS", 'https://i.imgur.com/fPok6pt.gif', 0, 0, 0),
            ("King", "SS", 'https://i.imgur.com/wq5sEZ7.png', 0, 0, 0),
            
            # Personnages S
            ("Sengoku", "S", "https://64.media.tumblr.com/45078c9fbf7f057b3ad92567b26a0eac/73dc2871fbc4e55a-b4/s540x810/4782ec194db6bba07dd4eb688b2bdc66793f5b54.gif", 0, 0, 0),
            ("Crocodile", "S", 'https://i.imgur.com/H1BwUuK.gif', 0, 0, 0),
            ("Ener", "S", 'https://i.imgur.com/s9LuY59.png', 0, 0, 0),
            ("Shiryu", "S", "https://i.ytimg.com/vi/buw6sNFUQI8/maxresdefault.jpg", 0, 0, 0),
            ("Smoker", "S", "https://i.imgur.com/3vJPaRx.gif", 0, 0, 0),
            ("Kuma", "S", "https://i.pinimg.com/originals/ea/ab/8f/eaab8f1c6b949ac0ba4287b128fe0546.gif", 0, 0, 0),
            ("Oden", "S", 'https://i.imgur.com/mACnc1L.jpg', 0, 0, 0),
            ("Sabo", "S", "https://i.imgur.com/vjcu8Gg.gif", 0, 0, 0),
            ("Boa Hancock", "S", 'https://i.imgur.com/ZWtbLYH.gif', 0, 0, 0),
            ("Marco", "S", 'https://i.imgur.com/LOo1j5P.gif', 0, 0, 0),
            ("Sanji", "S", 'https://i.imgur.com/hkob0Vu.jpg', 0, 0, 0),
            ("Yamato", "S", "https://giffiles.alphacoders.com/216/216308.gif", 0, 0, 0),
            ("Ace", "S", "https://i.imgur.com/8AGmDrS.gif", 0, 0, 0),

            # Personnages A
            ("Kong", "A", "https://i.ytimg.com/vi/iRnFypQECiA/maxresdefault.jpg", 0, 0, 0),
            ("Ivankov", "A", "https://preview.redd.it/was-ivankov-a-marine-before-a-revolutionary-1080-spoilers-v0-hu512bhdd1ua1.jpg?width=480&format=pjpg&auto=webp&s=fc2c8c335222de2eabcc10dc898eb8c758b20d20", 0, 0, 0),
            ("Brook", "A", "https://pa1.aminoapps.com/6441/769e80cfc5fa4264e22470c35758624b0f1844f0_hq.gif", 0, 0, 0),
            ("Robin", "A", 'https://i.imgur.com/tiC5mlA.gif', 0, 0, 0),
            ("Jinbe", "A", 'https://i.imgur.com/5ktjcxG.png', 0, 0, 0),
            ("Rob Lucci", "A", "https://i.imgur.com/aewCvhP.gif", 0, 0, 0),
            ("Magellan", "A", 'https://i.imgur.com/nvHpUU8.png', 0, 0, 0),
            ("Karasu", "A", "https://64.media.tumblr.com/442ea21ce795aef5dd5c530483bb8f34/tumblr_ppxot6VR2p1v6xsm2o3_540.gif", 0, 0, 0),
            ("Yassop", "A","https://64.media.tumblr.com/baec79e8188657006b2e80c7405461ec/tumblr_mx8i0nXwyc1rr37qoo1_500.gif", 0, 0, 0),
            
            # Personnages B
            ("Chooper", "B", 'https://i.imgur.com/eSoVui2.png', 0, 0, 0),
            ("Nami", "B", 'https://i.imgur.com/VAbsCsh.gif', 0, 0, 0),
            ("Ussop", "B", "https://i.imgur.com/oJD4qsv.gif", 0, 0, 0),
            ("Hina", "B", 'https://i.imgur.com/2tbPDP4.png', 0, 0, 0),
            ("Buggy", "B", "https://i.imgur.com/9aeBJHQ.jpeg", 0, 0, 0),
            ("Koala", "B", "https://wegotthiscovered.com/wp-content/uploads/2023/04/koala-one-piece.jpg", 0, 0, 0),
            ("Inazuma", "B", 'https://i.imgur.com/PyUiXXv.png', 0, 0, 0),
            ("Belo Betty", "B", "https://areajugones.sport.es/wp-content/uploads/2020/01/belo-betty-one-piece.jpg", 0, 0, 0),
            ("Franky", "B", 'https://i.imgur.com/U08oSKn.gif', 0, 0, 0),
                    ("Koby", "B", 'https://i.imgur.com/OtsQuBI.png', 0, 0, 0),
            

            # Personnages C
            ("Vivi", "C", "https://www.mangaluxe.com/dossiers/one-piece/img/nefertari-vivi.jpg", 0, 0, 0),
            ("Arlong", "C", 'https://i.imgur.com/MXsMw7m.jpg', 0, 0, 0),
            ("Don Krieg", "C", "https://cdn.oneesports.gg/cdn-data/2024/02/Anime_DonKrieg_OnePiece-1.jpg", 0, 0, 0),
            ("Tashigi", "C", "https://www.opgt.it/wp-content/uploads/2018/07/tashigi-1024x578.jpg", 0, 0, 0),
            ("Cobra", "C", "https://www.mangamag.fr/wp-content/uploads/2023/05/nefertari-cobra-one-piece-1084-assassinat.png", 0, 0, 0),
            ("Hack", "C", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/10/Hack-One-Piece.jpg", 0, 0, 0),
            ("Chopper", "C", "https://i.imgur.com/Xbq06Y8.jpeg", 0, 0, 0),

            # Personnages D
            ("Dorry", "D", "https://m.media-amazon.com/images/M/MV5BZDE2OTA2MTMtN2VkZS00NDZkLThmNDctMTYzNDc5NzgxMDEyXkEyXkFqcGdeQXVyNzgxMzc3OTc@._V1_.jpg", 0, 0, 0),
            ("Brogy", "D", "https://www.roadtolaughtale.fr/wp-content/uploads/2024/01/broggy.jpg", 0, 0, 0),
            ("Lindbergh", "D", "https://static.wikia.nocookie.net/onepiece/images/3/31/Cool_Shooter.png/revision/latest?cb=20190414113534", 0, 0, 0),
            
            # Personnages E
            ("Helmeppo", "E", "https://img24.tokyvideo.com/videos/319/319429/previews/previews_0009.jpg", 0, 0, 0),
            ("Hatchan", "E", "https://lh5.googleusercontent.com/E3R0RFsbrh_SRGWZWQtDSYsYJ7O-aWkJ712dsKRX8b7O6nrEo9-94iFS8UShWmB0OIbaG4ce_C94fQiTrYSiybFqRzVrLAp1N86kHOvzDdoSBbHcfqPTyvNVZhklda5HJl9ybAAIpEJ2nAG8oV5sXXM", 0, 0, 0),
            ("Pell", "E", 'https://i.imgur.com/fzBiN7h.png', 0, 0, 0),
            ("Kuro", "E", "https://cdn-www.konbini.com/files/2023/04/one_piece_eiichiro_oda_premierefois14.jpg", 0,0,0),
            ("Wapol", "E", "https://lh6.googleusercontent.com/VoyVXJY9nyRm35lSZLupPJsQkeHhqjGiWGyvglXg_IzfsrB4yYxJwZoc19Cjbt85aoFBTiDIfXav3q9aCKxC_f2Am_vcWRLqUxI1OMmx6_IysLZ7bzoBnCv4NuOHPdmYu8z-J7eM6JFjX7o4-OURPjs", 0, 0, 0),

            # Personnages F
            ("Merry","F","https://static.wikia.nocookie.net/onepiece/images/c/c1/Merry_spara.png/revision/latest?cb=20220124140512&path-prefix=it",0,0,0),
            ("Gaimon", "F", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/06/gaimon-cropped.jpg", 0, 0, 0),
            ("Kaya", "F", "https://static.wikia.nocookie.net/onepiece/images/7/7c/Kaya_betrachtet_Usopps_Steckbrief.jpg/revision/latest?cb=20110906183227&path-prefix=de", 0, 0, 0),
            ("Laboon", "F", "https://static.wikia.nocookie.net/onepiece/images/8/89/Little_Laboon.png/revision/latest?cb=20121126013140", 0, 0, 0),
            ("Portgas D. Rouge", "F", "https://pm1.aminoapps.com/6197/4c59a4fc722f8d2401d5947667df68b10ba03d0e_hq.jpg", 0, 0, 0),
            ],
            "Bleach" : [ # ✅
            # Personnages X
            ("Yhwach", "X", "https://i.imgur.com/OLYulIP.gif", 950, 1200, 1000), 
            ("Ichigo Kurosaki", "X", "https://i.imgur.com/5LJbZtC.gif", 1000, 1200, 1000),
            ("Aizen", "X", 'https://i.imgur.com/8xq9dtV.gif', 950, 1100, 970),
            ("Yamamoto", "X", 'https://i.imgur.com/EGYHcBd.gif', 900, 1300, 900),
            ("Kenpachi", "X", "https://i.imgur.com/DCS6I2N.gif", 1000, 1100, 1000),
            ("Ichibe", "X", "https://i.imgur.com/dg916bt.gif", 1100, 950, 1000),

            # Personnages SS
            ("Jugram", "SS", "https://i.imgur.com/kXmvoS6.gif", 705, 750, 695),
            ("Uryu", "SS", "https://i.imgur.com/AC2f6Ey.gif", 695, 800, 705),
            ("Kyoraku", "SS", "https://i.imgur.com/7DGfP2z.gif", 745, 850, 705),
            ("Byakuya Kuchiki", "SS", "https://i.imgur.com/VZrc8mU.gif", 695, 800, 725),
            ("Toshiro Hitsugaya", "SS", "https://i.imgur.com/R9S0Qa4.gif", 705, 720, 695),
            ("Urahara", "SS", "https://i.gifer.com/53FX.gif", 725, 800, 715),
            ("Yoruichi", "SS", "https://i.gifer.com/3flV.gif", 705, 770, 715),
            ("Unohana", "SS", "https://i.imgur.com/b1x9GUC.gif", 695, 850, 755),
            ("Ulquiorra", "SS", "https://i.imgur.com/OaYNXCg.gif", 690, 800, 710),
            ("Gin", "SS", "https://i.imgur.com/kveTtpS.gif", 705, 750, 715),
            ("Stark", "SS", "https://i.imgur.com/SNpSgRB.gif", 700, 780, 720),
            ("Renji", "SS", "https://i.imgur.com/RptZEBF.gif", 725, 705, 720),
            ("Senjumaru", "SS", "https://i.imgur.com/EKWGM3I.gif", 715, 800, 725),

            # Personnages S
            ("Mayuri", "S", "https://i.imgur.com/n8BNWm7.gif", 550, 600, 550),
            ("Sajin", "S", "https://i.imgur.com/6cf4JEH.gif", 600, 500, 550),
            ("Isshin", "S", "https://i.imgur.com/GTYbLGY.gif", 550, 550, 550),
            ("Rukia Kuchiki", "S", "https://i.imgur.com/IDjAqqP.gif", 550, 620, 550),
            ("Shinji", "S", 'https://i.imgur.com/9vxW0IN.gif', 550, 650, 550), 
            ("Soi Fon", "S", 'https://i.imgur.com/EVH34qM.gif', 550, 580, 550),
            ("Tosen", "S", 'https://i.imgur.com/4GA76X1.gif', 550, 550, 550),
            ("Baraggan", "S", 'https://i.imgur.com/k89CHqN.gif', 550, 570, 550),
            ("Grimmjow", "S", 'https://i.imgur.com/nj464jc.gif', 580, 600, 550),

            # Personnages A

            ("Ukitake", "A", 'https://i.imgur.com/PqGvVzv.gif', 395, 420, 405), 
            ("Nnoitra", "A", 'https://i.imgur.com/z5SAM9h.gif', 440, 450, 460),
            ("Shuhei", "A", 'https://i.imgur.com/rkQNMQX.gif', 415, 435, 420),
            ("Ryuken", "A", 'https://i.imgur.com/turdL6j.gif', 410, 450, 430),
            ("Orihime", "A", 'https://i.imgur.com/xGhy8ky.gif', 430, 420, 460),
            ("Ginjo", "A", 'https://i.imgur.com/xLPLs5Q.gif', 410, 420, 430),
            
            
            # Personnages B

            ("Kira", "B", 'https://i.imgur.com/H5EQmb0.png', 330, 340, 320),
            ("Ikkaku", "B", 'https://i.imgur.com/wWd1Z4z.png', 345, 360, 335),
            ("Kensei", "B", 'https://i.imgur.com/fHD5IZV.png', 335, 345, 330),
            ("Chad", "B", "https://i.imgur.com/o4eSlWY.jpeg", 340, 360, 330),
            ("Yumichika", "B", "https://i.imgur.com/mC8r7ka.jpeg", 320, 330, 340),

            # Personnages C
            ("Ganju", "C", 'https://i.imgur.com/4HYU47B.png', 245, 255, 240),
            ("Marechiyo", "C", 'https://i.imgur.com/QdU2qIp.png', 250, 260, 270),
            ("Love", "C", 'https://i.imgur.com/LJzVWIY.png', 265, 250, 275),

            # Personnages D
            ("Tessai", "D", 'https://i.imgur.com/VwYCDSH.png', 175, 190, 180),
            ("Hanataro", "D", 'https://i.imgur.com/MPaOL4G.png', 185, 170, 180),
            ("Yachiru", "D", 'https://i.imgur.com/6mO9KFd.jpeg', 180, 190, 175),

            # Personnages E
            ("Jinta", "E", 'https://i.imgur.com/pAuQhV7.png', 115, 120, 125),
            ("Ururu", "E", 'https://i.imgur.com/DoiSB83.png', 120, 130, 110),
            ("Keigo", "E", 'https://i.imgur.com/D8dqhs2.png', 125, 120, 115),

            # Personnages F
            ("Kon", "F", 'https://i.imgur.com/t1az2SQ.png', 45, 50, 55),
            ("Karin Kurosaki", "F", 'https://i.imgur.com/Spca2oo.png', 50, 55, 45),
            ("Yuzu", "F", 'https://i.imgur.com/plnofeu.png', 55, 45, 50),
            ("Tatsuki", "F", 'https://i.imgur.com/mSvWp2O.png', 50, 55, 50),
            ("Mizuiro", "F", 'https://i.imgur.com/b4sfzoT.png', 45, 55, 50),
            
            ],
            "My Hero Academia" : [
            # Personnages X
            ("All Might", "X", "https://i.imgur.com/CUUh7Cd.gif", 0, 0, 0),
            ("Shigaraki", "X", "https://i.imgur.com/4G7TwKg.gif", 0, 0, 0),
            ("All For One", "X", "https://i.imgur.com/rR1sQPU.gif", 0, 0, 0),
            ("Star And Stripe", "X", "https://i.imgur.com/awX9W1z.gif", 0, 0, 0),
            # Personnages SS
            ("Izuku Midoriya", "SS", "https://i.imgur.com/sfcQ2nE.gif", 0, 0, 0),
            ("Endeavor", "SS", "https://i.imgur.com/Y2olaBF.gif", 0, 0, 0),
            ("Overhaul", "SS", "https://i.imgur.com/dcPHh3I.gif", 0, 0, 0),
            ("Beast Jeanist", "SS", "https://i.imgur.com/YomRbmO.gif", 0, 0, 0),
            ("Nana Shimura", "SS", "https://i.imgur.com/ct2j0jN.gif", 0, 0, 0),
            ("Dabi", "SS", "https://i.imgur.com/BjDR5Yi.gif", 0, 0, 0),
            ("Mirio", "SS", "https://i.imgur.com/gOMDPVp.gif", 0, 0, 0),
            ("Re Destro", "SS", "https://i.imgur.com/HQp99hz.gif", 0, 0, 0),
            # Personnages S
            ("Hawks", "S", "https://i.imgur.com/X15PwP6.gif", 0, 0, 0),
            ("Twice", "S", "https://i.imgur.com/aTXRvNJ.gif", 0, 0, 0),
            ("Shoto Todoroki", "S", "https://i.imgur.com/SYm3EIh.gif", 0, 0, 0),
            ("Katsuki Bakugo", "S", "https://i.imgur.com/NK0LePb.gif", 0, 0, 0),
            ("Eraserhead", "S", "https://i.imgur.com/kPsHrCm.gif", 0, 0, 0),
            ("Tamaki", "S", "https://i.imgur.com/PrRON0k.gif", 0, 0, 0),
            ("Stain", "S", "https://i.imgur.com/bLlQH1S.gif", 0, 0, 0),
            ("Fumikage", "S", "https://i.imgur.com/75sU4v8.gif", 0, 0, 0),
            ("Mirko", "S", "https://i.imgur.com/uaH6Nth.gif", 0, 0, 0),
            ("Lady Nagant", "S", "https://i.imgur.com/XTarup4.gif", 0, 0, 0),
            # Personnages A
            ("Tenya", "A", "https://i.imgur.com/XAE3t5c.gif", 0, 0, 0),
            ("Mt Lady", "A", "https://i.imgur.com/BGdhXVd.gif", 0, 0, 0),
            ("Nighteye", "A", "https://i.imgur.com/fgO8qfb.gif", 0, 0, 0),
            ("Ryuku", "A", "https://i.imgur.com/jUEf20r.gif", 0, 0, 0),
            ("Gran Torino", "A", "https://i.imgur.com/pHGoXST.gif", 0, 0, 0),
            # Personnages B
            ("Ochaco", "B", 'https://i.imgur.com/GqBcqOI.jpeg', 0, 0, 0),
            ("Midnight", "B", 'https://i.imgur.com/L4S7dNo.jpeg', 0, 0, 0),
            ("Denki", "B", 'https://i.imgur.com/aq2fHI5.png', 0, 0, 0),
            ("Crimson Riot", "B", 'https://i.imgur.com/8VssE2J.jpeg', 0, 0, 0), #TOREVIEW ya rien dautre cm image 
            ("Nezu", "B", 'https://i.imgur.com/PipbKlv.png', 0, 0, 0),
            ("Momo Yaoyorozu", "B", 'https://i.imgur.com/3knQkZJ.jpeg', 0, 0, 0),
            ("Gang Orca", "B", 'https://i.imgur.com/op6GToE.jpeg', 0, 0, 0),
            ("Shinso Hitoshi", "B", 'https://i.imgur.com/Vw0skrm.jpeg', 0, 0, 0), #TOREVIEW Ajout de perico
            ("Nejire Hado", "B", 'https://i.imgur.com/JRE6K7R.jpeg', 0, 0, 0), #TOREVIEW Ajout de perico
            # Personnages C
            ("Shindo", "C", 'https://i.imgur.com/I7uLCYw.jpeg', 0, 0, 0),
            ("Rock Lock", "C", 'https://i.imgur.com/s3iBS2y.jpeg', 0, 0, 0),
            ("Vlad King", "C", 'https://i.imgur.com/v4AGxIS.jpeg', 0, 0, 0),
            ("Testutetsu", "C", "https://i.imgur.com/06KllgA.jpeg", 0, 0, 0), #TOREVIEW A retirer car no image
            ("Snipe", "C", 'https://i.imgur.com/urx0HwQ.jpeg', 0, 0, 0),
            
            # Personnages D
            ("Spinner", "D", 'https://i.imgur.com/MeW1vaE.jpeg', 0, 0, 0),
            ("Shihai", "D", 'https://i.imgur.com/SIaA75c.jpeg', 0, 0, 0),
            ("Nomu", "D", 'https://i.imgur.com/Vn6WFcc.jpeg', 0, 0, 0),
            ("Kyoka Jiro", "D", 'https://i.imgur.com/R8DEMdM.jpeg', 0, 0, 0), #TOREVIEW Ajout de perico

            # Personnages E
            ("Mineta", "E", 'https://i.imgur.com/gORmmMX.jpeg', 0, 0, 0), #BALANCETONPORC
            ("Shoji", "E", 'https://i.imgur.com/lCTpZJE.jpeg', 0, 0, 0),
            # Personnages F
            ("Eri", "F", 'https://i.imgur.com/thiVSIU.jpeg', 0, 0, 0),
            ("Kenji", "F", 'https://i.imgur.com/BGeI2LC.jpeg', 0, 0, 0), #ou https://www.geekgirlauthority.com/wp-content/uploads/2017/08/mhas2e18-deku.jpg
            ("Sansa", "F", 'https://i.imgur.com/bKASPVp.jpeg', 0, 0, 0),
            ],
            "Hunter x Hunter" : [ # ✅
            # Personnages X
            ("Meruem", "X", "https://i.imgur.com/knC0hFT.gif", 1000, 1000, 1000),
            ("Gon Freecss", "X", "https://i.imgur.com/BiklKkz.gif", 950, 1050, 950),
            ("Kuroro", "X", 'https://i.imgur.com/3TjMAKv.gif', 950, 960, 950),
            ("Isaac Netero", "X", 'https://i.imgur.com/vtkowxL.gif', 920, 980, 950),
            ("Ging", "X", "https://i.imgur.com/VOtkd0O.gif", 900, 930, 960),
            ("Aruka Zoldyck", "X", "https://i.imgur.com/DHIbvOx.gif", 1000, 1000, 1000),

            # Personnages SS
            ("Zeno Zoldyck", "SS", "https://i.imgur.com/inIqhEg.gif", 730, 780, 740),
            ("Illumi Zoldyck", "SS", 'https://i.imgur.com/tFOQgXs.gif', 710, 720, 725),
            ("Silva Zoldyck", "SS", "https://i.imgur.com/K8TUsWM.gif", 720, 760, 730),
            ("Hisoka", "SS", 'https://i.imgur.com/l69c0NZ.gif', 720, 730, 725),
            ("Neferopito", "SS", "https://i.imgur.com/5PkF2QA.gif", 800, 780, 790), # SS+
            ("Pufu", "SS", "https://i.imgur.com/CfoSEeD.gif", 780, 700, 800),
            ("Razor", "SS", 'https://i.imgur.com/LZ1bwdl.gif', 700, 730, 700), #TOREVIEW 
            ("Yupi", "SS", "https://i.imgur.com/tWZDibP.gif", 790, 800, 810),

            # Personnages S
            ("Kaito", "S", "https://i.imgur.com/RehnXP7.gif", 530, 580, 535),
            ("Feitan", "S", "https://i.imgur.com/X3AVK76.gif", 525, 600, 515),
            ("Kurapika", "S", 'https://i.imgur.com/ltImMBx.gif', 580, 580, 575),
            ("Kirua Zoldyck", "S", 'https://i.imgur.com/2sLrUqa.gif', 520, 610, 520),
            ("Uvogin", "S", 'https://i.imgur.com/iqzrrW8.gif', 540, 590, 560),
            ("Nabunaga", "S", 'https://i.imgur.com/1UMIlo3.gif', 520, 580, 520),
            ("Machi", "S", "https://i.imgur.com/HCAKZfB.gif", 520, 575, 520),
            ("Phinks", "S", "https://i.imgur.com/k5BLUMw.gif", 530, 575, 525),
            ("Bonolenov Ndongo", "S", "https://i.imgur.com/WNj1k2B.gif", 520, 565, 530), #TOREVIEW 
            ("Biscuit Kruger", "S", 'https://i.imgur.com/3WUyIRV.gif', 560, 570, 555),
            
            # Personnages A
            ("Botobai Gigante", "A", "https://i.imgur.com/mjz1Chv.png", 430, 450, 440),
            ("Morel", "A", 'https://i.imgur.com/FnQu94R.gif', 430, 400, 420),
            ("Knuckle", "A", 'https://i.imgur.com/sMDxcKR.gif', 420, 415, 410), 
            ("Karuto Zoldyck", "A", "https://i.imgur.com/vCDM9hC.gif", 415, 420, 410),
            ("Hanzo (hxh)", "A", "https://i.imgur.com/HuuzzwW.gif", 410, 400, 410),  
            ("Sharnak", "A", 'https://i.imgur.com/EwSJxbs.gif', 420, 430, 400),
            ("Franklin", "A", "https://i.imgur.com/xoln4Ly.gif", 410, 420, 400),
            ("Shizuku", "A", "https://i.imgur.com/IbkxhGl.gif", 410, 415, 405),
            ("Genthru", "A", 'https://i.imgur.com/WtnOU7k.gif', 400, 440, 420),
            ("Cheetu", "A", "https://i.imgur.com/ZqFKcDD.gif", 420, 430, 410),
            ("Zazan", "A", "https://i.imgur.com/LpXVPsM.gif", 430, 420, 430),  
            ("Novu", "A", "https://i.imgur.com/UIgaydF.gif", 400, 400, 410),  
            ("Shoot", "A", 'https://i.imgur.com/tU2Fwq6.gif', 410, 430, 430),
            ("Pariston Hill", "A", 'https://i.imgur.com/71ouSTW.gif', 420, 440, 420),
            ("Pamu Shiberia", "A", 'https://i.imgur.com/AJTBunT.gif', 430, 440, 420),

            # Personnages B
            ("Leorio", "B", 'https://i.imgur.com/NBFxlLS.gif', 320, 350, 325),
            ("Satotsu", "B", 'https://i.imgur.com/QQS66Kw.jpeg', 300, 320, 310),
            ("Gotoh", "B", 'https://i.imgur.com/hYXIzdH.png', 330, 350, 330),
            ("Mike", "B", 'https://i.imgur.com/Opybqgn.jpeg', 330, 340, 335),
            ("Wing", "B", 'https://i.imgur.com/h8Btyhj.png', 320, 310, 315),
            ("Kastro", "B", 'https://i.imgur.com/mjgiM60.png', 315, 320, 320),
            ("Pakunoda", "B", "https://i.imgur.com/IxWVTzo.gif", 330, 340, 320),
            ("Korutopi", "B", "https://i.imgur.com/uqHvQrZ.jpeg", 325, 335, 315),
            ("Koruto", "B", "https://i.imgur.com/QwL2k3G.png", 340, 330, 340),
            ("Meleoron", "B", "https://i.imgur.com/tcEdwmU.jpeg", 325, 335, 330),
            ("Ikalgo", "B", "https://i.imgur.com/P3Jc5JY.png", 300, 350, 315),
            ("Welfin", "B", "https://i.imgur.com/JfNtetM.jpeg", 345, 350, 340),
            ("Tsezugera", "B", "https://i.imgur.com/3WvsTfn.png", 320, 350, 320),
            
            # Personnages C
            ("Pokkle", "C", "https://i.imgur.com/7A9UCci.png", 240, 275, 235),
            ("Buhara", "C", "https://i.imgur.com/EDIxD4t.png", 300, 220, 260),
            ("Menchi", "C", "https://i.imgur.com/OYoD8tt.jpeg", 270, 260, 255),
            ("Kanaria", "C", "https://i.imgur.com/tSSM35N.jpeg", 270, 260, 255),
            ("Zushi", "C", "https://i.imgur.com/zFDjx8z.png", 265, 275, 255),
            ("Guido", "C", "https://i.imgur.com/6EeZcNz.png", 245, 250, 240),
            ("Riluberto", "C", "https://i.imgur.com/NDJrQVS.png", 245, 250, 240),
            ("Sadaso", "C", "https://i.imgur.com/e2ppqVH.jpeg", 250, 260, 240),
            ("Sukuwara", "C", "https://i.imgur.com/iK18Eos.jpeg", 245, 250, 235),
            ("Senritsu", "C", "https://i.imgur.com/1PhNNbj.jpeg", 250, 230, 240),

            # Personnages D
            ("Kiriko", "D", "https://i.imgur.com/kc1BLPf.jpeg", 150, 140, 170),
            ("Ponzu", "D", 'https://i.imgur.com/f4vOKAP.png', 150, 190, 140),
            ("Kikyo Zoldyck", "D", "https://i.imgur.com/AoZVrw6.png", 160, 180, 170),
            ("Vezze", "D", "https://i.imgur.com/bfKaKiD.jpeg", 150, 180, 160),

            # Personnages E
            ("Tompa", "E", "https://i.imgur.com/ms2R2ki.png", 115, 105, 110),
            ("Todo", "E", "https://i.imgur.com/DAVdi3M.jpeg", 125, 100, 105),
            ("Majtani", "E", "https://i.imgur.com/DmJoWX5.jpeg", 95, 120, 115),
            ("Leluto", "E", "https://i.imgur.com/wgyMHWc.png", 110, 110, 110),
            ("Jones", "E", "https://i.imgur.com/MShzS9R.png", 120, 105, 105),
            ("Zebulo", "E", "https://i.imgur.com/nuTPuxR.png", 105, 110, 115),
            ("Ciquento", "E", "https://i.imgur.com/rfiLrO7.png", 100, 115, 115),
            ("Miruki Zoldyck", "E", "https://i.imgur.com/IcwaCHD.jpeg", 110, 110, 110),
            ("Neon", "E", 'https://i.imgur.com/Rz5HGeZ.png', 95, 115, 120),
            ("Pegui", "E", 'https://i.imgur.com/u2tYaqs.jpeg', 100, 110, 120),
            ("Bodoro", "E", 'https://i.imgur.com/VSWUPF5.jpeg', 115, 110, 105),


            
            # Personnages F
            ("Mito Freecss", "F", 'https://i.imgur.com/Yy7iG5d.png', 45, 50, 45),
            ("Capitaine", "F", 'https://i.imgur.com/Q3iev4b.png', 50, 45, 45),
            ("Beans", "F", 'https://i.imgur.com/ZH36bXI.jpeg', 40, 50, 50),
            ("Kara", "F", 'https://i.imgur.com/zPxLCH0.jpeg', 45, 55, 40),
            ("Cocco", "F", 'https://i.imgur.com/aMpudLr.jpeg', 50, 40, 50),
            ("Komugi", "F", 'https://i.imgur.com/4VchruE.png', 55, 45, 40),
            ("Kon (hxh)", "F", 'https://i.imgur.com/rMn0Ukz.png', 40, 45, 55),
            ],
            "Avatar" : [ # ✅
            # Personnages X
            ("Aang", "X", "https://i.imgur.com/TqtpU5Q.gif", 930, 920, 925),
            # Personnages SS
            ("Lord Ozai", "SS", "https://i.imgur.com/3K6X9Ro.gif", 710, 760, 705),
            ("Iroh", "SS", "https://i.imgur.com/KSigNP8.gif", 690,740,695),
            ("Azula", "SS", "https://i.imgur.com/GT1KSqZ.gif", 660, 720, 685),
            ("Zuko", "SS", "https://i.imgur.com/VLqP4QM.gif", 670, 710, 700),
            # Personnages A
            ("Mai", "A", "https://i.imgur.com/opVoND8.gif", 400, 440, 410),
            ("Toph", "A", "https://i.imgur.com/Bjbn4ew.gif", 390, 430, 420),
            ("Katara", "A", "https://i.imgur.com/4hOIpNj.gif", 400, 420, 425),

            # Personnages 
            ("Ty Lee", "B", "https://i.imgur.com/XFnYb26.jpeg", 390, 450, 400),

            # Personnages C
            ("Sokka", "C", "https://i.imgur.com/VMVIHVh.png", 260, 270, 240),
            
            # Personnages D
            ("Suki", "D", "https://i.imgur.com/Tfhd7Ez.jpeg", 160, 180, 165),
            ("Appa", "D", "https://i.imgur.com/sdASYR2.jpeg", 155, 160, 200),
            # Personnages E
            ("Yue", "E", "https://i.imgur.com/vRv3CZJ.jpeg", 110, 80, 90),
            ],
            "Jujutsu Kaisen" : [  # ✅
            # Personnages X
            ("Sukuna", "X", "https://i.imgur.com/sALgfhD.gif", 1000, 1100, 1050),
            ("Gojo", "X", "https://i.imgur.com/ZRlOmKu.gif", 999, 1050, 999),
            ("Kenjaku", "X", "https://i.imgur.com/40tFQKc.gif", 910, 920, 925),

            # Personnages SS
            ("Yuta", "SS", "https://i.imgur.com/zG66ujn.gif", 750, 790, 785),
            ("Mahoraga", "SS", "https://i.imgur.com/X3JpLMk", 850, 850, 850),
            ("Toji", "SS", 'https://i.imgur.com/W479ima.png', 720, 780, 760),
            ("Aoi Todo", "SS", 'https://i.imgur.com/SpLV3Qv.png', 700, 730, 720),
            ("Geto", "SS", 'https://i.imgur.com/ZetAyjs.gif', 700, 750, 670),
            ("Choso", "SS", 'https://i.imgur.com/tPHJtTO.gif', 730, 740, 760),
            ("Mahito", "SS", 'https://i.imgur.com/a2gCQIC.gif', 650, 730, 700),
            ("Jogo", "SS", 'https://i.imgur.com/iyNljeL.gif', 700, 750, 700),
            ("Kinji Hakari", "SS", 'https://i.imgur.com/OSTYTVF.png', 777, 777, 777),
            ("Yuki Tsukumo", "SS", 'https://i.imgur.com/WlIBwGu.png', 700, 800, 700),
            ("Hanami","SS","https://i.imgur.com/eO8Ezjm.gif", 700, 730, 700),
            ("Dagon", "SS", 'https://i.imgur.com/Arh6UMF.gif', 700, 760, 700),

            # Personnages S
            ("Megumi", "S", "https://i.imgur.com/ZrNNA55.gif", 550, 610, 515),
            ("Maki", "S", 'https://i.imgur.com/zGKPJI9.png', 590, 505, 685),
            ("Nanami", "S", 'https://i.imgur.com/phtWBmN.png', 580, 610, 570),
            ("Higuruma", "S", 'https://i.imgur.com/VnEkm6V.jpeg', 550, 585, 525),
            ("Naobito", "S", 'https://i.imgur.com/FTRAhNn.png', 505, 595, 545),
            ("Miguel", "S", 'https://i.imgur.com/a8zQRsZ.png', 575, 540, 575), 
            ("Mei mei", "S", 'https://i.imgur.com/KoWiulR.png', 525, 565, 535),
            ("Naoya", "S", 'https://i.imgur.com/LiKy4we.png', 510, 590, 540),
            ("Yuji Itadori", "S", "https://i.imgur.com/75H1WqO.gif", 600, 570, 600),
            
            #Personnages A
            ("Inumaki", "A", 'https://i.imgur.com/D7071yc.gif', 400, 420, 400), 
            ("Kamo", "A", 'https://i.imgur.com/8N9AYpE.png', 400, 450, 420),
            ("Mechamaru", "A", 'https://i.imgur.com/bjBDlk6.gif', 430, 400, 440),

            # Personnages B
            ("Panda", "B", 'https://i.imgur.com/32zGh1W.jpeg', 340, 320, 330),
            ("Nobara", "B", "https://i.imgur.com/ToHbnHv.jpeg", 320, 350, 320),
            ("Kusakabe", "B", 'https://i.imgur.com/6rujX3t.png', 320, 335, 330),
            ("Takuma Ino", "B", 'https://i.imgur.com/W3diIlg.png', 310, 360, 320),
            ("Yaga", "B", 'https://i.imgur.com/R8Rq12y.png', 330, 310, 330),
            ("Gakuganji", "B", 'https://i.imgur.com/uAnAEms.png', 310, 340, 320),
            

            # Personnages C
            ("Junpei", "C", 'https://i.imgur.com/7sVsWn3.png', 240, 260, 220),
            ("Momo", "C", "https://i.imgur.com/q0viuTx.png", 240, 260, 230),
            ("Utahime", "C", 'https://i.imgur.com/IPp6E9q.png', 240, 280, 260),
            ("Juzo", "C", "https://i.imgur.com/lkcQCxs.png", 250, 270, 260),
            ("Haruta Shigemo", "C", "https://i.imgur.com/IY5zel0.jpeg", 240, 255, 220),
            

            # Personnages D
            ("Miwa", "D", "https://i.imgur.com/M0twNwm.png", 180, 200, 165),

            # Personnages E
            ("Ijichi", "E", "https://i.imgur.com/6EKKkX3.jpeg", 110, 120, 125),
            ("Kechizu", "E", "https://i.imgur.com/fwEMmNC.png", 110, 130, 110),


            # Personnages F
            ("Riko Amanai", "F", "https://i.imgur.com/WkfCzwy.jpeg", 50, 50, 50),
            ("Tsumiki Fushiguro", "F", "https://i.imgur.com/wNU5qjd.png", 50, 50, 50),

            
            ],
            "Jojo's Bizarre Adventure" : [
            # Personnages X
            ("Giorno Giovanna", "X", 'https://imgur.com/iJ9oUE1', 900, 1200, 950),
            ("Enrico Pucci", "X", 'https://imgur.com/hWurlzP', 950, 1200, 900),
            ("Funny Valentine", "X", "https://i.imgur.com/4ugvBxu.jpeg", 950, 1050, 950),
            ("Johnny", "X", "https://imgur.com/839IXuS", 950, 1100, 900),
            # Personnages SS
            ("Gyro", "SS", "https://imgur.com/sPFgVJQ", 700, 750, 700),
            ("Kars", "SS", 'https://i.imgur.com/4xhIuVK.gif', 850, 850, 850),
            ("Diavolo", "SS", 'https://i.imgur.com/90RxqGR.gif', 750, 850, 700),
            ("Jotaro Kujo", "SS", 'https://i.imgur.com/XzBAKKf.gif', 750, 800, 750),
            ("Diego Brando", "SS", "https://i.imgur.com/Ncp5cvE.jpeg", 740, 800, 730), #TOREVIEW
            ("Dio Brando", "SS", 'https://i.imgur.com/xngzKOg.gif', 800, 850, 750),
            ("Kira Yoshikage", "SS", 'https://i.imgur.com/ZQPBO3Q.gif', 700, 800, 700),
            # Personnages S
            ("Josuke", "S", 'https://i.imgur.com/AcnhlnJ.gif', 550, 580, 550), #TOREVIEW
            ("Fugo", "S", 'https://i.imgur.com/gBcvGNj.gif', 550, 600, 550), #TOREVIEW
            ("Vanilla Ice", "S", "https://i.imgur.com/VoH5XBm.gif", 550, 570, 550),#TOREVIEW
            ("Jolyne", "S", 'https://i.imgur.com/T2yg742.gif', 500, 550, 550),
            ("Weather Report", "S", "https://i.imgur.com/zHlZilS.gif", 550, 550, 550),
            # Personnages A
            ("Anasui", "A", "https://i.imgur.com/cQtCTf7", 400, 450, 440),
            ("Bucciarati", "A", 'https://i.imgur.com/zaBAVFx.gif', 450, 470, 430),
            ("Risotto", "A", 'https://i.imgur.com/hQxmpqR.gif', 440, 480, 400),
            ("Rohan", "A", 'https://i.imgur.com/UJgfmGg.gif', 410, 440, 430),
            ("Kakyoin", "A", 'https://i.imgur.com/ZsxN3PG.gif', 440, 420, 400),
            ("Polnareff", "A", 'https://i.imgur.com/eZjHHa9.gif', 430, 450, 410),
            ("Okuyasu", "A", 'https://i.imgur.com/BiveNFJ.gif', 430, 450, 410),
            ("Ghiaccio", "A", 'https://i.imgur.com/LNoxXyi.gif', 440, 420, 400),
            ("Prosciutto", "A", 'https://i.imgur.com/CsSR05A.gif', 410, 420, 430),
            ("Mohamed Abdul", "A", "https://i.imgur.com/2fIG9TF", 430, 420, 410),
            ("Illuso", "A", "https://i.imgur.com/4oeiAEJ.gif", 400, 420, 440),
            ("Cioccolata", "A", 'https://i.imgur.com/XAu2MDR.gif', 420, 400, 420),
            # Personnages B
            ("Koichi", "B", 'https://i.imgur.com/HZ9vn1d.png', 350, 360, 310),
            ("Emporio", "B", 'https://i.imgur.com/KBZCTy6.png', 320, 340, 310),
            ("Akira", "B", 'https://i.imgur.com/xn6pX9Z.png', 290, 370, 330),
            ("Narancia", "B", 'https://i.imgur.com/ndZcfok.png', 310, 350, 310),
            ("Yukako", "B", 'https://i.imgur.com/JZKQ2KS.png', 340, 330, 310),
            ("Miyamoto", "B", 'https://i.imgur.com/lZLlEhu.png', 310, 330, 320),
            ("Wamuu", "B", 'https://i.imgur.com/2Jc0FTu.png', 330, 320, 350),
            ("Esidisi", "B", 'https://i.imgur.com/mdsI4Ir.png', 360, 320, 320),
            ("Pesci", "B", 'https://i.imgur.com/RiqetYG.png', 320, 320, 310),
            ("Melone", "B", 'https://i.imgur.com/EMitGnp.png', 310, 320, 330),
            ("Squalo", "B", 'https://i.imgur.com/1DP3U16.png', 310, 340, 330),
            ("Joseph", "B", 'https://i.imgur.com/YiGGszt.png', 330, 340, 310),
            ("Mista", "B", 'https://i.imgur.com/ab9sgfg.png', 340, 360, 320),
            # Personnages C
            ("Caesar", "C", 'https://i.imgur.com/3nzbH8Y.png', 250, 270, 260),
            ("Lisa Lisa", "C", 'https://i.imgur.com/YAcAs5c.jpeg', 260, 260, 250),
            ("Shigechi", "C", 'https://i.imgur.com/6JKniYe.png', 240, 230, 220),
            ("Mikitaka", "C", 'https://i.imgur.com/mMs5O78.png', 270, 240, 230),
            ("Iggy", "C", 'https://i.imgur.com/HTb59id.png', 250, 260, 220),
            ("Formaggio", "C", 'https://i.imgur.com/WCQtqwq.png', 260, 270, 220),
            ("Stroheim", "C", 'https://i.imgur.com/OvyOZy3.png', 280, 230, 240),
            ("Foo Fighters", "C", 'https://i.imgur.com/ZlCOCPn.png', 270, 240, 250),
            ("Trish", "C", 'https://i.imgur.com/I4nMHqt.png', 250, 270, 260),
            ("Hermes", "C", 'https://i.imgur.com/TbkuZDj.jpeg', 290, 250, 240),
            # Personnages D
            ("Abbacchio", "D", 'https://i.imgur.com/5FahNJl.png', 200, 180, 170),
            ("Daniel Darby", "D", 'https://i.imgur.com/w1Qu1p2.jpeg', 160, 170, 180),
            ("Jonathan", "D", 'https://i.imgur.com/dqGKC1P.png', 220, 200, 160),
            # Personnages E
            ("Straizo", "E", 'https://i.imgur.com/D4muQp5.png', 100, 130, 110),
            ("Will Zeppeli", "E", 'https://i.imgur.com/SVm9I2K.png', 120, 130, 110),
            ("Boingo", "E", 'https://i.imgur.com/I1GDLQ9.jpeg', 100, 120, 130),
            ("Oingo", "E", 'https://i.imgur.com/4t8W7rq.jpeg', 140, 130, 120),
            # Personnages F
            ("Tonio", "F", 'https://i.imgur.com/PIXbcZb.png', 70, 60, 50),
            ("Luca", "F", 'https://i.imgur.com/3HamVjM.png', 40, 60, 50),
            ("Anne", "F", 'https://i.imgur.com/AkQ1PV2.jpeg', 70, 40, 50),
            ("Speedwagon", "F", 'https://i.imgur.com/Q4pR4ws.png', 50, 60, 70),
            ("Poco", "F", 'https://i.imgur.com/qeYo0He.png', 50, 60, 30),
            ("Mario Zucchero", "F", 'https://i.imgur.com/dBDj9C5.png', 70, 50, 30),
            ("Dario Brando", "F", "https://imgur.com/LjMHPwB", 60, 40, 20),
            ("Tama", "F", 'https://i.imgur.com/1cQyIW5.jpeg', 70, 30, 50),
            ],
            "One Punch Man" : [

            # Personnages X
            ("Saitama", "X", "https://steamuserimages-a.akamaihd.net/ugc/945077695993694686/15A47D5D02A75DB7700CBBC61706AB3CFD8FEEE2/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", 0, 0, 0),
            ("Garou", "X", "https://i.pinimg.com/originals/a2/21/f2/a221f289576e45a0ed2fc3a5f6cb311e.gif", 0, 0, 0),
            ("Boros", "X", "https://steamuserimages-a.akamaihd.net/ugc/930424898985552170/32677D50B018A16166629EC271C52DD6C0644ABE/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", 0, 0, 0),
            


            # Personnages SS

            ("Watchdog Man", "SS", "https://wallpapercave.com/wp/wp8404550.jpg", 0, 0, 0), #TOREVIEW
            ("Tatsumaki", "SS", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0a290752-d7eb-45e3-aa31-8e71b544cde0/ddx9bq9-b00980a3-8482-4791-bf64-f558046bb68f.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBhMjkwNzUyLWQ3ZWItNDVlMy1hYTMxLThlNzFiNTQ0Y2RlMFwvZGR4OWJxOS1iMDA5ODBhMy04NDgyLTQ3OTEtYmY2NC1mNTU4MDQ2YmI2OGYuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.tQyMqurmzcRYBak3ZNXQli2kTvbsZen9MPklCMs4dsw", 0, 0, 0),
            #("Blast", "SS", image_temporaire, 0, 0, 0),
            ("King", "SS", "https://64.media.tumblr.com/bfa88447c156e886f4499efd2e85a436/tumblr_o7une2LCul1t11lc1o3_r2_500.gif", 0, 0, 0),

            # Personnages S

            ("Metal Knight", "S", "https://64.media.tumblr.com/5366a39ff74f49fa99b3b75ddcdbbe5e/tumblr_nxv9s1PRxS1s4tq6xo1_500.gif", 0, 0, 0),
            ("Flashy Flash", "S", "https://i.pinimg.com/originals/65/d9/aa/65d9aaac5b9be737a85f1e3321a31751.gif", 0, 0, 0),
            ("Bang", "S", "https://www.serieously.com/app/uploads/2021/10/sylver.gif", 0, 0, 0),
            ("Atomic Samurai", "S", "https://64.media.tumblr.com/cec8d995e77353273ab04fae8dc843bf/tumblr_o0nbzf0oCI1uxe4abo3_500.gif", 0, 0, 0),
            ("Genos", "S", "https://animesher.com/orig/1/174/1743/17437/animesher.com_genos-gif-one-punch-man-1743758.gif", 0, 0, 0),

            # Personnages A
            ("Zombieman", "A", "https://64.media.tumblr.com/220b8ea9980e47660ccad29010900975/1c5ae4e6d2c27fda-14/s540x810/c999ca2299c96b4d60267133cd29a2de376586a9.gif", 0, 0, 0),
            ("Metal Bat", "A", "https://img.wattpad.com/50bbff7a70c378858c50f33d312d7e9163bc23b2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f41385a745f354872705631354c773d3d2d33352e313566633933666232666339383461663232323833353634353235382e676966", 0, 0, 0),
            ("Sonic", "A", "https://static.wikia.nocookie.net/one-punch-man/images/8/82/Ninja_one_punch_men.gif/revision/latest?cb=20201024101334&path-prefix=pl", 0, 0, 0),
            # Personnages B
            ("Fubuki", "B", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/02/OK6W-koKDTOqqqLDbIoPArZF0g0L4GyCjAjQGnT5hNk-Cropped.png", 0, 0, 0),
            ("Child Emperor", "B", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/03/Dng4IF-W0AAEkCf.jpg", 0, 0, 0),
            ("Tanktop Master", "B", "https://static.wikia.nocookie.net/onepunchman/images/a/a8/Anime_-_Ej%C3%A9rcito_Tank_Tropper.png/revision/latest?cb=20190702134750&path-prefix=es", 0, 0, 0),
            ("Puri Puri Prisoner", "B", "https://i.redd.it/1zy1fprswuk41.jpg", 0, 0, 0),


            # Personnages C
            ("Stinger", "C", "https://i0.wp.com/i.pinimg.com/originals/31/79/a9/3179a9a797c0e033691dd2eda5b5a5b7.jpg", 0, 0, 0),
            ("Sneck", "C", "https://static.wikia.nocookie.net/onepunchman/images/6/67/SneckProfile.png/revision/latest?cb=20161112181329", 0, 0, 0),

            # Personnages D
            ("Cyborgorilla", "D", "https://i.ytimg.com/vi/HJAt5DujlIw/maxresdefault.jpg", 0, 0, 0),

            # Personnages E
            ("Grimasse", "E", "https://static.wikia.nocookie.net/onepunchman/images/a/a4/Saitama_flippe_devant_Grimasse.png/revision/latest?cb=20190501171126&path-prefix=fr", 0, 0, 0),
            ("Crablante", "E", "https://static.wikia.nocookie.net/villains/images/a/a5/Crabrante.jpg/revision/latest?cb=20151214015216", 0, 0, 0),

            # Personnages F
            ("Mumen Rider", "F", "https://i.redd.it/diszh9zoizoa1.jpg", 0, 0, 0),
            ],
            "Demon Slayer" : [
            # Personnages X
            ("Tanjiro", "X", image_temporaire, 0, 0, 0),
            ("Muzan", "X", image_temporaire, 0, 0, 0),
            ("Yoriichi", "X", image_temporaire, 0, 0, 0),
            ("Kokushibo", "X", image_temporaire, 0, 0, 0),

            # Personnages SS

            ("Gyomei", "SS", image_temporaire, 0, 0, 0),
            ("Doma", "SS", image_temporaire, 0, 0, 0),
            ("Akaza", "SS", image_temporaire, 0, 0, 0),

            # Personnages S

            ("Sanemi", "S", image_temporaire, 0, 0, 0),
            ("Muichiro", "S", image_temporaire, 0, 0, 0),
            ("Obanai", "S", image_temporaire, 0, 0, 0),
            ("Giyu", "S", image_temporaire, 0, 0, 0),

            # Personnages A
            ("Rengoku", "A", "https://i.imgur.com/6HL02sP.gif", 0, 0, 0),
            ("Uzui Tengen", "A", image_temporaire, 0, 0, 0),
            ("Mitsuri", "A", image_temporaire, 0, 0, 0),
            ("Nezuko", "A", image_temporaire, 0, 0, 0),
            ("Kanao", "A", image_temporaire, 0, 0, 0),
            ("Tamayo", "A", image_temporaire, 0, 0, 0),
            ("Shinobu Kocho", "A", image_temporaire, 0, 0, 0),

            # Personnages B
            ("Zenitsu", "B", "https://boutique-manga.fr/wp-content/uploads/2021/06/Zenitsu-sensei-711x400.jpg", 0, 0, 0),
            ("Inosuke", "B", image_temporaire, 0, 0, 0),
            ("Kaigaku", "B", image_temporaire, 0, 0, 0),

            ("Genya", "B", image_temporaire, 0, 0, 0),
            ("Daki", "B", image_temporaire, 0, 0, 0),
            ("Enmu", "B", image_temporaire, 0, 0, 0),

            # Personnages C
            ("Rui", "C", image_temporaire, 0, 0, 0),
            ("Mukago", "C", image_temporaire, 0, 0, 0),
            ("Fille Araignee", "C", image_temporaire, 0, 0, 0),
            ("Mere Araignee", "C", image_temporaire, 0, 0, 0),
            ("Susamaru", "C", image_temporaire, 0, 0, 0),
            ("Jigoro", "C", image_temporaire, 0, 0, 0),


            # Personnages D
            ("Tanjuro", "D", image_temporaire, 0, 0, 0),

            # Personnages E
            ("Shinzu", "E", image_temporaire, 0, 0, 0),
            ("Murata", "E", image_temporaire, 0, 0, 0),
            ("Kyogai", "E", image_temporaire, 0, 0, 0),
            ("Kanamue", "E", image_temporaire, 0, 0, 0),
            ("Kagaya Ubuyashiki", "E", image_temporaire, 0, 0, 0),


            # Personnages F
            ("Kiriya Ubuyashiki", "F", image_temporaire, 0, 0, 0),
            ("Nichika Ubuyashiki", "F", image_temporaire, 0, 0, 0),
            ("Chachamaru", "F", image_temporaire, 0, 0, 0),
            ("Aoi Kanzaki", "F", image_temporaire, 0, 0, 0),
            ("Sumi", "F", image_temporaire, 0, 0, 0),
            ("Kiyo", "F", image_temporaire, 0, 0, 0),
            ("Naho", "F", 'https://i.imgur.com/LyTz20q.gif', 0, 0, 0),
            ("Goto", "F", 'https://pm1.aminoapps.com/8315/5f0fa658f4f7bd2bf29453cf963fd9b3453c9240r1-1280-719v2_hq.jpg', 0, 0, 0),
            ("Kaburamaru", "F", 'https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/c/c1/Kaburamaru.png/revision/latest?cb=20190831165508', 0, 0, 0),
            ],
            "Full Metal Alchemist" : [ # ✅
            # Personnages X
            ("Pere", "X", "https://i.imgur.com/X617w07.gif", 963, 963, 963),
            # Personnages SS
            ("Hohenheim", "SS", "https://i.imgur.com/bMNh7n0.gif", 720, 730, 735),
            ("King Bradley", "SS", "https://i.imgur.com/Di7mjqq.gif", 750, 770, 750),
            # Personnages S
            ("Edward", "S", "https://i.imgur.com/Lmbb9ZT.gif", 540, 555, 530),
            ("Izumi Curtis", "S", "https://i.imgur.com/WBcqtWl.gif", 535, 540, 530),
            ("Alphonse", "S", 'https://i.imgur.com/q6IW5xU.gif', 560, 570, 600),
            ("Roy Mustang", "S", 'https://i.imgur.com/Oyk2Pp4.gif', 550, 700, 540), # high S
            ("Scar", "S", 'https://i.imgur.com/9dw5ri9.gif', 580, 600, 790), # high S
            ("Kimbley", "S", 'https://i.imgur.com/r9nB7SF.gif', 530, 555, 535),
            ("Selim", "S", 'https://i.imgur.com/XYj2ZtU.gif', 545, 560, 540),
            # Personnages A
            ("Ling Yao", "A", 'https://i.imgur.com/cEoziXY.gif', 420, 430, 410),
            ("Envy", "A", 'https://i.imgur.com/rRFT3ec.gif', 440, 430, 420),
            ("Sloth", "A", 'https://i.imgur.com/sltbpFK.gif', 450, 430, 410),
            ("Gluttony", "A", "https://i.imgur.com/16YlN6x.gif", 430, 420, 440),
            ("Lust", "A", 'https://i.imgur.com/lriujEU.gif', 420, 410, 440),
            ("Olivia Mira Armstrong", "A", 'https://i.imgur.com/Jwzc22O.gif', 440, 450, 420),
            ("Alex Louis Armstrong", "A", 'https://i.imgur.com/Hx8D4HJ.gif', 450, 430, 430),
            # Personnages B
            ("Mei Chang", "B", 'https://i.imgur.com/tfeqXJu.jpeg', 330, 325, 335),
            ("Riza Hawkeye", "B", 'https://i.imgur.com/vTsQ4ZZ.jpeg', 335, 330, 325),
            ("Lan Fan", "B", 'https://i.imgur.com/ukRcnJx.jpeg', 340, 325, 325),
            ("Fu", "B", 'https://i.imgur.com/yQdAnYc.jpeg', 325, 340, 325),
            ("Buccaneer", "B", 'https://i.imgur.com/v6ykfW1.png', 335, 335, 320),
            ("Sig Curtis", "B", 'https://i.imgur.com/gMvZCxb.png', 325, 325, 340),

            # Personnages C
            ("Heinkel", "C", 'https://i.imgur.com/IFSivAT.jpeg', 255, 260, 265),
            ("Marcoh", "C", 'https://i.imgur.com/6hbihPy.png', 260, 255, 265),
            ("Darius", "C", 'https://i.imgur.com/OugYS2B.jpeg', 265, 260, 255),
            ("Frere de Scar", "C", 'https://i.imgur.com/xwYWbhD.jpeg', 265, 265, 250),

            # Personnages D
            ("Maes Hughes", "D", 'https://i.imgur.com/uvT3bWb.jpeg', 180, 170, 165),
            ("Maria Ross", "D", 'https://i.imgur.com/8zUxWkq.jpeg', 175, 180, 185),
            ("Miles", "D", 'https://i.imgur.com/097qkPG.jpeg', 180, 185, 175),
            ("Falman", "D", 'https://i.imgur.com/zNRwZQT.jpeg', 185, 175, 180),
            ("Barry the Chopper", "D", 'https://i.imgur.com/O7u2J3P.jpeg', 180, 180, 180),

            # Personnages E
            ("Paninya", "E", 'https://i.imgur.com/uS1Dxp3.jpeg', 115, 120, 125),
            ("Havoc", "E", 'https://i.imgur.com/rM9I8Ot.jpeg', 120, 125, 115),
            ("Heymans", "E", 'https://i.imgur.com/jJdB2II.png', 125, 115, 120),
            ("Fuery", "E", "https://i.imgur.com/6dCkq7z.jpeg", 120, 120, 120),

            # Personnages F
            ("Yoki", "F", 'https://i.imgur.com/pPbOaqJ.jpeg', 35, 50, 35),
            ("Nina Tucker", "F", 'https://i.imgur.com/gOeHUXg.jpeg', 50, 45, 35),
            ("Trisha", "F", 'https://i.imgur.com/QVYbkRB.jpeg', 35, 50, 35),
            ("Xiao Mei", "F", 'https://i.imgur.com/FAQHPlD.gif', 30, 55, 35),
            ("Winry", "F", 'https://i.imgur.com/mbX301B.jpeg', 35, 55, 30),
            ],
            "Attack On Titan" : [ # ✅
            # """ PERSONNAGES SNK """
            # Personnages X
            ("Eren Yeager", "X", "https://i.imgur.com/izA5HAI.gif", 960, 950, 945),
            # Personnages SS
            ("Armin", "SS", "https://i.imgur.com/CFmYNyt.gif", 750, 655, 750),
            ("Bertholdt Hoover", "SS", "https://i.imgur.com/kyjgDwH.gif", 750, 650, 750),
            ("Levi Ackerman", "SS", "https://i.imgur.com/YdrDGay.gif", 600, 750, 600),
            ("Reiner Braun", "SS", "https://i.imgur.com/cEEtTgd.gif", 700, 730, 750),
            # Personnages S
            ("Annie Leonhart", "S", "https://i.imgur.com/mmktpLk.gif", 500, 600, 500),
            ("Sieg Yeager", "S", "https://i.imgur.com/cKjSldG.gif", 540, 540, 550),
            ("Mikasa Ackerman", "S", "https://i.imgur.com/GKcCmA0.gif", 490, 600, 450),
            ("Pieck Finger", "S", "https://i.imgur.com/1oeKEPN.gif", 510, 520, 510),
            # Personnages A
            ("Xaver", "A", "https://i.imgur.com/qr62Ecp.jpeg", 500, 330, 500),
            ("Grisha Yeager", "A", "https://i.imgur.com/D5avB4O.gif", 410, 430, 415),
            ("Ymir", "A", "https://i.imgur.com/VtGdbyl.gif", 380, 440, 370),
            ("Falco", "A", "https://i.imgur.com/KYUnpQb.gif", 420, 390, 430),
            ("Kenny Ackerman", "A", "https://i.imgur.com/QQwRAlM.gif", 380, 500, 385),
            ("Porco Galliard", "A", "https://i.imgur.com/b78cQir.gif", 410, 430, 420),
            ("Erwin", "A", "https://i.imgur.com/0WfIayb.gif", 330, 360, 390),
            # Personnages B
            ("Mike Zacharias", "B", "https://i.imgur.com/CdhigbE.png", 300, 400, 300),
            ("Frieda Reiss", "B", "https://i.imgur.com/CScADUO.png", 290, 340, 300),
            ("Jean Kirstein", "B", "https://i.imgur.com/7erh7rA.png", 310, 320, 280),
            ("Hange Zoe", "B", "https://i.imgur.com/IiSqnok.png", 300, 320, 310),
            ("Rhodes Reiss", "B", "https://i.imgur.com/fzsHl7c.png", 500, 200, 400),
            # Personnages C
            ("Hannes", "C", "https://i.imgur.com/XtZvC0L.jpeg", 280, 330, 290),
            ("Historia", "C", "https://i.imgur.com/u6tCLmq.jpeg",230, 245, 230),
            ("Floch", "C", "https://i.imgur.com/K79IX3o.jpeg", 240, 250, 220 ),
            ("Pixis", "C", "https://i.imgur.com/Vx416zK.png", 220, 210, 210),
            ("Sacha", "C", "https://i.imgur.com/XHs9rWi.png", 230, 260, 230),
            ("Kony", "C", "https://i.imgur.com/7MNFSc1.jpeg", 220, 240, 230),
            # Personnages D
            ("Gabi Braun", "D", "https://i.imgur.com/iBw8k6t.png", 160, 180, 140),
            ("Udo", "D", "https://i.imgur.com/p1NWLXE.png", 140, 160, 120),
            ("Zofia", "D", "https://i.imgur.com/99zdhK5.png", 145, 165, 125),
            # Personnages E
            ("Theo Magath", "E", "https://i.imgur.com/0cq6zdB.png", 100, 110, 100),
            ("Yelena", "E", "https://i.imgur.com/9LfUJq0.png", 90, 120, 90),
            # Personnages F
            ("Willy", "F", "https://i.imgur.com/M8eXW0o.jpeg", 40, 50, 40),
            ("Onyankopon", "F", "https://i.imgur.com/wylRQBl.jpeg", 50, 50, 50),
            ("Nicolo", "F", "https://i.imgur.com/cXQk7KZ.jpeg", 40, 45, 45)
            ],
            "Seven Deadly Sins" : [
            # """ PERSONNAGES NNT """
            # Personnages X
            ("Meliodas", "X", image_temporaire, 0, 0, 0),

            # Personnages SS
            ("Ban", "SS", image_temporaire, 0, 0, 0),
            ("Estarossa", "SS", image_temporaire, 0, 0, 0),
            ("Escanor", "SS", image_temporaire, 0, 0, 0),
            ("Zeldris", "SS", image_temporaire, 0, 0, 0),

            # Personnages S
            ("Arthur", "S", image_temporaire, 0, 0, 0),
            ("Gowther", "S", image_temporaire, 0, 0, 0),
            ("Merlin", "S", image_temporaire, 0, 0, 0),

            # Personnages A
            ("Derrierie", "A", image_temporaire, 0, 0, 0),
            ],
            "Chainsaw Man" : [ # ✅
                ("Denji", "X", "https://i.imgur.com/YnDFcsy.gif", 940, 960, 945),
                ("Makima", "X", "https://i.imgur.com/UCcRxPY.gif", 910, 950, 920),

                ("Kishibe", "SS", "https://i.imgur.com/woFsMsu.gif", 720, 730, 715),
                
                ("Aki Hanakawa", "S", "https://i.imgur.com/bnGI6vv.gif", 510, 570, 540),
                ("Himeno", "S", "https://i.imgur.com/qyBRHdk.gif", 520, 540, 530),
                ("Angel", "S", "https://i.imgur.com/rtJFtA9.gif", 530, 560, 555),
                ("Samurai Sword", "S", "https://i.imgur.com/8Bj3B08.gif", 565, 580, 575),
                ("Akane Sawatari", "S", "https://i.imgur.com/mbr0WZ8.gif", 540, 565, 545),
                
                ("Power", "A", "https://i.imgur.com/WzSAOuy.gif", 410, 430, 425),


                ("Kobeni Higashiyama", "B", "https://i.imgur.com/yB3UtcT.jpeg", 330, 320, 315),
                ("Beam", "B", "https://i.imgur.com/LmkjMXS.png", 340, 320, 315),
                ("Galgali", "B", "https://i.imgur.com/hzsrj4W.png", 330, 340, 310),

                ("Michiko Tendo", "C", "https://i.imgur.com/vsE0OlY.png", 240, 250, 255),
                ("Yutaro Kurose", "C", "https://i.imgur.com/Ks0x4qp.png", 255, 250, 240),




                ("Hirokazu Arai", "F", "https://i.imgur.com/74g6mPD.png", 40, 55, 50),
            ]
}

all_synergies = [
    (1, "Akatsuki", "ATK", 0.15,"L'akkatsuki est une organisation criminelle de ninjas deserteurs.", 'https://static.wikia.nocookie.net/naruto/images/6/61/Membres_Akatsuki.png/revision/latest/scale-to-width-down/1200?cb=20130511192621&path-prefix=fr', "#FF0000"),
    (2, "Saiyan", "ATK", 0.15, "Les Saiyans sont connus pour leur force et leur capacite à se transformer en Super Saiyan.", image_temporaire, "#FFA500"),
    (3, "Hollow", "ATK", 0.15, "Les Hollows sont des âmes corrompues qui ont perdu leur coeur et leur raison.", image_temporaire, "#0000FF"),
    (4, "Mugiwara", "ATK", 0.15, "Les Mugiwara sont l'equipage de Luffy, un pirate qui cherche le One Piece.", 'https://steamuserimages-a.akamaihd.net/ugc/481145984302804192/29529359BC636378F426946B2D859F7EB46561BB/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false', "#800080"),
    (5, "Uchiha", "ATK", 0.15, "Le clan Uchiha est connu pour ses capacites de combat et son Sharingan.", 'https://cherry.img.pmdstatic.net/fit/https.3A.2F.2Fimg.2Egaming.2Egentside.2Ecom.2Fs3.2Ffrgsg.2F1280.2Fmanga.2Fdefault_2022-12-21_5b4dbf77-0203-48b1-bfff-103263f3bc90.2Epng/1200x675/quality/80/clan-uchiwa.jpg', "#FF0000"),
    (6, "Quincy", "ATK", 0.15, "Les Quincy sont des chasseurs de Hollows qui utilisent des arcs pour combattre.", 'https://static1.srcdn.com/wordpress/wp-content/uploads/2022/10/Bleach-Quincy-featured.jpg', "#FFA500"), #TOREVIEW 
    (7, "Amiraux", "ATK", 0.15, "Les Amiraux sont les trois plus puissants marins de la Marine.", 'https://steamuserimages-a.akamaihd.net/ugc/914674978440099035/39C53679BC6727A9D6074B90BCD0C9BC72D1DEDD/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false', "#0000FF"), #TOREVIEW
    (8, "Espada", "ATK", 0.15, "Les Espadas sont les dix plus puissants Hollows sous les ordres d'Aizen.", 'https://i.redd.it/d2umjaymimsa1.jpg', "#800080"),
    (9, "Vongola", "ATK", 0.15, "La famille Vongola est une organisation mafieuse italienne qui utilise des anneaux pour combattre.", 'https://images2.wikia.nocookie.net/__cb20100422034551/reborn/images/e/e8/Tsuna_And_The_Guardians.PNG', "#FF0000"),
    (10, "Yonko", "ATK", 0.3, "Les Yonkos sont les quatre plus puissants pirates du Nouveau Monde.", 'https://www.univers-otaku.com/wp-content/uploads/2021/03/one-piece-Yonko.jpg', "#FFA500"),
    (11, "Akimichi", "ATK", 0.15, "Le clan Akimichi est connu pour sa technique de transformation en geant.", 'https://staticg.sportskeeda.com/editor/2022/06/d5daf-16559000633224.png', "#0000FF"), #TOREVIEW 
    (12, "Vizard", "ATK", 0.15, "Les Vizards sont des Shinigamis qui ont acquis des pouvoirs de Hollows.", 'https://i.pinimg.com/originals/b9/54/72/b95472a06de8ce83188fa0c2723c05cc.gif', "#800080"),
    (13, "Varia", "ATK", 0.15, "La Varia est un groupe d'assassins de la famille Vongola.", 'https://static.wikia.nocookie.net/reborn/images/5/5c/Past_Varia.PNG/revision/latest?cb=20111107024622', "#FF0000"),
    (14, "Gotei 13", "ATK", 0.15, "Le Gotei 13 est une organisation de Shinigamis qui protege le monde des âmes.", 'https://i.redd.it/myfksl030a991.gif', "#FFA500"),
    (15, "Kage", "ATK", 0.15, "Les Kages sont les plus puissants ninjas de leur village.", image_temporaire, "#0000FF"),
    (16, "Shichibukai", "ATK", 0.15, "Les Shichibukai sont des pirates qui ont accepte de servir la Marine.", 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/04/Featured-Image-Shichibukai-Cropped.jpg', "#800080"),
    (17, "Sannin", "ATK", 0.50, "Les Sannins sont les trois ninjas legendaires de Konoha.", 'https://64.media.tumblr.com/0d74a734f45f35a984288446fee484a4/tumblr_omf0oel6qW1rqe0rbo3_540.gifv', "#FF0000"),
    (18, "Revolutionnaires", "ATK", 0.15, "Les Revolutionnaires sont un groupe qui lutte contre le Gouvernement Mondial.", image_temporaire, "#FFA500"),
    (19, "Volonte du D", "ATK", 0.15, "La Volonte du D est une mysterieuse lignee de pirates qui defient le Gouvernement Mondial.", image_temporaire, "#0000FF"),
    (20, "Animal", "ATK", 0.15, "Les Animaux sont des creatures qui possedent des pouvoirs speciaux.", image_temporaire, "#800080"),
    (21, "Taka", "ATK", 0.15, "La Taka est un groupe de ninjas qui a ete forme par Sasuke Uchiha.", 'https://i.pinimg.com/originals/d0/14/1c/d0141c035bd6a5a3956e5b8161bda71c.gif', "#FF0000"),
    (22, "Rinnegan", "ATK", 0.15, "Le Rinnegan est le dōjutsu le plus puissant de l'univers Naruto.", 'https://editors.dexerto.fr/wp-content/uploads/sites/2/2023/05/23/naruto-rinnegan.jpg', "#FFA500"),
    (23, "Konoha", "ATK", 0.15, "Konoha est le village cache de la Feuille, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (24, "Suna", "ATK", 0.15, "Suna est le village cache du Sable, l'un des cinq grands villages ninjas.", image_temporaire, "#800080"),
    (25, "Kiri", "ATK", 0.15, "Kiri est le village cache de la Brume, l'un des cinq grands villages ninjas.", image_temporaire, "#FF0000"),
    (26, "Kumo", "ATK", 0.15, "Kumo est le village cache des Nuages, l'un des cinq grands villages ninjas.", image_temporaire, "#FFA500"),
    (27, "Iwa", "ATK", 0.15, "Iwa est le village cache de la Roche, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (28, "Receptacle", "ATK", 0.15, "Les Receptacles sont des personnes qui ont un Monstre scelle en eux.", image_temporaire, "#800080"),
    (29, "Maitre du Feu", "ATK", 0.15, "Les Maitres du Feu sont des personnages qui maitrisent le feu.", image_temporaire, "#FFA500"),
    (30, "Maitre de l'Eau", "ATK", 0.15, "Les Maitres de l'Eau sont des personnages qui maitrisent l'eau.", image_temporaire, "#0000FF"),
    (31, "Maitre de la Terre", "ATK", 0.15, "Les Maitres de la Terre sont des personnages qui maitrisent la terre.", image_temporaire, "#800080"),
    (32, "Maitre de l'Air", "ATK", 0.15, "Les Maitres de l'Air sont des personnages qui maitrisent l'air.", image_temporaire, "#FF0000"),
    (33, "Maitre de la Foudre", "ATK", 0.15, "Les Maitres de la Foudre sont des personnages qui maitrisent l'eclair.", image_temporaire, "#FFA500"),
    (34, "Maitre de la Glace", "ATK", 0.15, "Les Maitres de la Glace sont des personnages qui maitrisent la glace.", image_temporaire, "#0000FF"),
    (35, "Maitre de leclair ", "ATK", 0.15, "Les Maitres de la Foudre sont des personnages qui maitrisent la foudre.", image_temporaire, "#800080"),
    (36, "Maitre de la Lave", "ATK", 0.15, "Les Maitres de la Lave sont des personnages qui maitrisent la lave.", image_temporaire, "#FF0000"),
    (37, "Maitre du Bois", "ATK", 0.15, "Les Maitres du Bois sont des personnages qui maitrisent le bois.", image_temporaire, "#FFA500"),
    (38, "Maitre du Vent", "ATK", 0.15, "Les Maitres du Vent sont des personnages qui maitrisent le vent.", image_temporaire, "#0000FF"),
    (39, "Maitre du Sable", "ATK", 0.15, "Les Maitres du Sable sont des personnages qui maitrisent le sable.", image_temporaire, "#800080"),
    (40, "epeiste", "ATK", 0.15, "Les epeistes sont des combattants qui utilisent une epee pour se battre.", image_temporaire, "#FF0000"),
    (41, "Telekinesiste", "ATK", 0.15, "Les Telekinesistes sont des personnes qui peuvent deplacer des objets par la pensee ou ont des pouvoirs psychiques.", image_temporaire, "#FFA500"),
    (42, "Equipage de Barbe Noire", "ATK", 0.15, "L'equipage de Barbe Noire est un groupe de pirates dirige par Barbe Noire.", image_temporaire, "#0000FF"),
    (43, "Equipage de Barbe Blanche", "ATK", 0.15, "L'equipage de Barbe Blanche est un groupe de pirates dirige par Barbe Blanche.", image_temporaire, "#800080"),
    (44, "Uzumaki", "ATK", 0.15, "Le clan Uzumaki est connu pour sa longevite et ses capacites de guerison.", 'https://static1.srcdn.com/wordpress/wp-content/uploads/2022/03/Uzumaki-Clan.jpg', "#FF0000"),
    (45, "Hyuga", "ATK", 0.15, "Le clan Hyuga est connu pour son Byakugan et ses techniques de combat douces.", image_temporaire, "#FFA500"),
    (46, "Senju", "ATK", 0.15, "Le clan Senju est connu pour son Mokuton et sa capacite à maitriser les Bijuus.", image_temporaire, "#0000FF"),
    (47, "Otsutsuki", "ATK", 0.15, "Le clan Otsutsuki est une famille de ninjas extraterrestres qui cherchent à absorber des planetes pour obtenir du chakra.", image_temporaire, "#800080"),
    (48, "Insecte", "ATK", 0.15, "Les Insectes sont des creatures qui possedent des pouvoirs speciaux.", image_temporaire, "#FF0000"),
    (49, "Garde Royale", "ATK", 0.15, "La Garde Royale est un groupe qui s'assure de la securite du roi.", image_temporaire, "#FFA500"),
    (50, "Zeppeli", "ATK", 0.15, "Les Zeppelis sont une famille de maitres de l'Onde qui combattent les vampires.", image_temporaire, "#0000FF"),
    (52, "Homme du pillar", "ATK", 0.15, "Les Pillars sont des guerriers qui servent les vampires et protegent la pierre rouge de l'Aja.", image_temporaire, "#FF0000"),
    (53, "Maitre du Temps", "ATK", 0.15, "Les Maitres du Temps sont des personnages qui peuvent contrôler le temps.", image_temporaire, "#FFA500"),
    (54, "Maitre de l'Explosion", "ATK", 0.15, "Les Maitres de l'Explosion sont des personnages qui peuvent creer des explosions.", image_temporaire, "#0000FF"),
    (55, "Squadra Esecuzioni", "ATK", 0.15, "La Squadra Esecuzioni est un groupe de tueurs à gages qui travaillent pour la Passione.", image_temporaire, "#0000FF"),
    (56, "Hamon", "ATK", 0.15, "Le Hamon est une technique de combat qui utilise l'energie du soleil pour attaquer les vampires.", image_temporaire, "#800080"),
    (57, "Passione", "ATK", 0.15, "La Passione est une organisation criminelle italienne qui contrôle le trafic de drogue.", image_temporaire, "#FF0000"),
    (58, "Team Bucciarati", "ATK", 0.15, "La Team Bucciarati est un groupe de gangsters qui travaillent pour la Passione.", image_temporaire, "#FFA500"),
    (59, "JoBros", "ATK", 0.15, "Les JoBros sont les amis et allies des Joestars qui les aident dans leur combat contre le mal.", image_temporaire, "#0000FF"),
    (60, "ile de Sirop", "ATK", 0.15, "L'ile de Sirop est une ile paradisiaque où les habitants vivent en paix et en harmonie.", image_temporaire, "#800080"),
    (61, "equipage de Shanks", "ATK", 0.15, "L'equipage de Shanks est un groupe de pirates dirige par Shanks le Roux.", image_temporaire, "#0000FF"),
    (62, "equipage de Kaido", "ATK", 0.15, "L'equipage de Kaido est un groupe de pirates dirige par Kaido le Cent betes.", image_temporaire, "#800080"),
    (63, "equipage de Big Mom", "ATK", 0.15, "L'equipage de Big Mom est un groupe de pirates dirige par Big Mom.", image_temporaire, "#FF0000"),
    (64, "Draconique", "ATK", 0.15, "Les Dragons sont des creatures mythiques qui possedent des pouvoirs magiques.", image_temporaire, "#FFA500"),
    (65, "Speedster", "ATK", 0.15, "Les Speedsters sont des personnages qui peuvent se deplacer à une vitesse supersonique.", image_temporaire, "#0000FF"),
    (66, "Aveugle", "ATK", 0.4 , "Les Aveugles sont des personnages qui ont perdu la vue mais qui ont developpe d'autres sens pour compenser.", image_temporaire, "#800080"),
    (67, "Dojo de Bang", "ATK", 0.15, "Le Dojo de Bang est un lieu d'entrainement où les disciples apprennent les techniques de combat de Bang.", image_temporaire, "#FF0000"),
    (68, "Cyborg", "ATK", 0.15, "Les Cyborgs sont des etres humains qui ont ete ameliores avec des technologies cybernetiques.", image_temporaire, "#FFA500"),
    (69, "JoJo", "ATK", 0.15, "Les JoJos sont les membres de la famille Joestar qui luttent contre les forces du mal.", image_temporaire, "#0000FF"),
    (70, "Fleaux", "ATK", 0.15, "Les Fleaux sont des creatures malefiques qui apportent la destruction et la mort partout où ils passent.", image_temporaire, "#800080"),
    (71, "ecole de Tokyo", "ATK", 0.15, "L'ecole de Tokyo est un etablissement scolaire où les eleves apprennent à maitriser leurs pouvoirs surnaturels.", image_temporaire, "#FF0000"),
    (72, "ecole de Kyoto", "ATK", 0.15, "L'ecole de Kyoto est un etablissement scolaire rival de l'ecole de Tokyo.", image_temporaire, "#FFA500"),
    (73, "Zenin", "ATK", 0.15, "Le clan Zenin est une famille de sorciers qui possede des pouvoirs magiques.", image_temporaire, "#0000FF"),
    (74, "Kamo", "ATK", 0.15, "Le clan Kamo est une famille de sorciers qui possede des pouvoirs magiques.", image_temporaire, "#800080"),
    (75, "Fushiguro", "ATK", 0.15, "La lignee Fushiguro est une lignee d'originaire humaine.", image_temporaire, "#FF0000"),
    (76, "Ubuyashiki", "ATK", 0.15, "La famille Ubuyashiki est une famille de demons qui dirige le clan des pourfendeurs de demons.", image_temporaire, "#FFA500"),
    (77, "Hashira", "ATK", 0.15, "Les Hashiras sont les piliers de l'organisation des pourfendeurs de demons.", image_temporaire, "#0000FF"),
    (78, "Pourfendeur de demons", "ATK", 0.15, "Les Pourfendeurs de demons sont une organisation secrete qui lutte contre les demons.", image_temporaire, "#800080"),
    (79, "Domaine des Papillons", "ATK", 0.15, "Le Domaine des Papillons est un lieu mysterieux où les demons se rassemblent pour se nourrir.", image_temporaire, "#FF0000"),
    (80, "Demons", "ATK", 0.15, "Les Demons sont des creatures malefiques qui se nourrissent de la chair humaine.", image_temporaire, "#FFA500"),
    (81, "Kamado", "ATK", 0.15, "La famille Kamado est une famille de pourfendeurs de demons qui a ete decimee par les demons.", image_temporaire, "#0000FF"),
    (82, "Souffle du Soleil", "ATK", 0.15, "Le Souffle du Soleil est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#800080"),
    (83, "Souffle de la Foudre", "ATK", 0.15, "Le Souffle de la Foudre est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#FF0000"),
    (84, "Souffle de l'Eau", "ATK", 0.15, "Le Souffle de l'Eau est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#FFA500"),
    (85, "Souffle de la Fleur", "ATK", 0.15, "Le Souffle de la Fleur est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#0000FF"),
    (86, "Lune", "ATK", 0.15, "Les Lunes sont des demons puissants qui servent Muzan.", image_temporaire, "#800080"),
    (87, "Brando", "ATK", 0.15, "Les Brando sont une famille de vampires qui cherchent à dominer le monde.", image_temporaire, "#FF0000"),
    (88, "Maitre de la Gravite", "ATK", 0.15, "Les Maitres de la Gravite sont des personnages qui peuvent contrôler la gravite.", image_temporaire, "#FFA500"),
    (89, "Armstrong", "ATK", 0.15, "La famille Armstrog est une famille illustre et noble qui a servi Amestris pendant des generations.", image_temporaire, "#0000FF"),
    (90, "Homonculus", "ATK", 0.15, "Les Homonculus sont des etres artificiels crees par le Pere pour servir ses desseins.", image_temporaire, "#800080"),
    (91, "Alchimiste d'Etat", "ATK", 0.15, "Les Alchimistes d'Etat sont des alchimistes qui servent le gouvernement d'Amestris.", image_temporaire, "#FF0000"),
    (92, "Xing", "ATK", 0.15, "Le pays de Xing est un pays voisin d'Amestris qui pratique l'alchimie de l'est.", image_temporaire, "#FFA500"),
    (93, "Elric", "ATK", 0.15, "La famille Elric est une famille d'alchilmistes (sauf la mere).", image_temporaire, "#0000FF"),
    (94, "Automail", "ATK", 0.15, "L'Automail est une prothese mecanique qui remplace un membre perdu.", image_temporaire, "#800080"),
    (95, "Ishval", "ATK", 0.15, "Les Ishvals sont un peuple pacifique qui a ete decime par les alchimistes d'Amestris.", image_temporaire, "#FF0000"),
    (96, "Bradley", "ATK", 0.15, "La famille Bradley comporte deux Homonculus et est au pouvoir du pays.", image_temporaire, "#FFA500"),
    (97, "Unite Mustang", "ATK", 0.15, "L'Unite Mustang est une unite de l'armee d'Amestris dirigee par Roy Mustang.", image_temporaire, "#0000FF"),
    (98, "U.A.", "ATK", 0.15, "L'U.A. est une ecole de heros où les etudiants apprennent à devenir des heros professionnels.", "ua.gif", "#800080"),
    (99, "Zoldyck", "ATK", 0.15, "La famille Zoldyck est une famille d'assassins qui sont les plus redoutes du monde.", "zoldyck.png", "#fde9e0"),
    (100, "Dix Commandements", "ATK", 0.15, "Les Dix Commandements sont les dix demons les plus puissants de l'Empire de Britannia.", "https://i.imgur.com/SMEji4z.jpeg", "#FF0000"),
    (101, "Les Sept Peches Capitaux", "ATK", 0.15, "Les Sept Peches Capitaux sont un groupe de chevaliers qui ont trahi le royaume de Liones.", "https://i.imgur.com/CnvtvuO.jpeg", "#FFA500"),
    (102, "Dieu de la Destruction", "ATK", 0.15, "Les Dieux de la Destruction sont des divinites qui detruisent les planetes pour maintenir l'equilibre de l'univers.", "https://i.imgur.com/uxo372k.png", "#0000FF"),
    (103, "Ange", "ATK", 0.15, "Les Anges sont des etres celestes qui servent les dieux et protegent l'univers.", "https://i.imgur.com/xt9Tn0P.jpeg", "#800080"),
    (104, "Famille de Son Goku", "ATK", 0.15, "La famille de Son Goku est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/cChWxf7.jpeg", "#FF0000"),
    (105, "Famille de Vegeta", "ATK", 0.15, "La famille de Vegeta est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/eyN6Qg9.jpeg", "#FFA500"),
    (106, "Section 4 Anti-Demon", "ATK", 0.15, "La Section 4 Anti-Demon est une unite speciale de la police qui lutte contre les demons.", "https://i.imgur.com/dijQZFN.jpeg", "#0000FF"),
    (107, "Freecss", "ATK", 0.15, "La famille Freecss est une famille de chasseurs qui cherchent des tresors et des creatures rares.", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/12/Gon-and-Ging-Freecss.jpg", "#800080"),
    (108, "Hunter étoilé", "ATK", 0.15, "L'Association Hunter est une organisation de chasseurs qui traquent les creatures rares et les criminels. Les hunters étoilés sont leurs meilleurs atouts.", "https://i.imgur.com/fHvGkwX.jpeg", "#f40000"),
    (109, "Zodiac", "ATK", 0.15, "Les Zodiacs sont les douze membres du conseil des Hunters qui sont les plus puissants et les plus influents de l'Association Hunter.", "https://i.imgur.com/fHvGkwX.jpeg", "#FFA500"),
    (110, "Brigade Fantome", "ATK", 0.15, "La Brigade Fantome est une organisation criminelle qui lutte contre l'Association Hunter.", "https://i.imgur.com/2KZe6ug.gif", "#00000"),
    (111, "Forme de vie ultime", "ATK", 0.15, "Les formes de vie ultime sont des créatures ultimes qui dépassent les limites de l'humanité.", image_temporaire, "#00000"),
    (112, "Voleur de Pouvoir", "ATK", 0.15, "Les Voleurs de Pouvoir sont des individus qui volent les pouvoirs des autres pour les utiliser à leur avantage.", image_temporaire, "#00000"),
    

]

# FAIRE FAMILLY KUCHIKI 

all_link_synergies = {
    112 : ["Kuroro Lucifer","All For One","Yhwach"], # Voleur de Pouvoir
    111 : ["Kars","Meruem","Pere"], # Forme de vie ultime
    110: ["Kuroro Lucifer", "Hisoka", "Nobunaga", "Machi", "Shizuku", "Franklin", "Feitan", "Phinks", "Shalnark", "Bonolenov", "Karuto Zoldyck", "Uvogin"], # Brigade Fantome
    109 : ["Leorio","Ging Freecs", "Batobai Gigante", "Pariston","Kurapika"], # Zodiac
    108 : ["Menchi","Tsezugera", "Morel","Ging Freecss","Biscuit Kruger","Botobai Gigante","Pariston Hill"], # Hunter étoilé
    107 : ["Mito Freecss","Gon Freecss", "Ging Freecss"],
    106 : ["Aki Hanakawa","Denji","Kishibe","Power","Himeno","Kobeni Higashiyama","Hirokazu Arai","Angel","Beam", "Galgali","Fushi","Madoka"], # Section 4 Anti-Demon
    105 : ["Vegeta","Bulma","Trunks","Roi Vegeta"], # Famille de Vegeta
    104 : ["Son Goku", "Raditz", "Bardock", "Chichi" ,"Goten"], # Famille de Son Goku
    103 : ["Whis","Vados","Grand pretre"], # Anges
    102 : ["Beerus","Champa","Belmod"], # Dieu de la Destruction
    101 : ["Meliodas","Ban","King","Diane","Gowther","Merlin","Escanor"], # Les Sept Peches Capitaux
    100 : ["Derrierie","Estaossa","Zeldris","Gloxinia","Drole","Grayroad","Fraudrin","Monspiet","Melascula","Galand"], # Dix Commandements
    99 : ["Kirua Zoldyck" , "Irumi Zoldyck", "Milluki Zoldyck", "Alluka Zoldyck", "Zeno Zoldyck", "Silva Zoldyck", "Kikyo Zoldyck","Karuto Zoldyck"], # Zoldyck
    98 : ["Izuku Midoriya","Katsuki Bakugo","Ochaco Uraraka","Tenya Iida","Shoto Todoroki","Momo Yaoyorozu","Eijiro Kirishima","Denki Kaminari","Mina Ashido","Tsuyu Asui","Fumikage Tokoyami","Kyoka Jiro","Hanta Sero","Yuga Aoyama","Toru Hagakure","Mezo Shoji","Koji Koda","Rikido Sato","Mashirao Ojiro","Eri","Mirio Togata","Tamaki Amajiki","Nejire Hado","Hawks","Endeavor","All Might","Shota Aizawa","Present Mic","Midnight","Snipe","Vlad King","Eraser Head","Power Loader"], # U.A.
    97 : ["Roy Mustang", "Havoc", "Riza Hawkeye","Heymans","Fuery","Falman"], # Unite Mustang
    96 : ["King Bradley","Selim"], # Bradley
    95 : ["Scar","Frere de Scar","Miles"], # Ishval
    94 : ["Edward","Paninya","Lan Fan"], # Automail
    93 : ["Hohenheim","Edward","Alphonse","Trisha"], # Elric
    92 : ["Ling Yao","Mei Chang","Lan Fan","Fu","Xiao Mei"], # Xing
    91 : ["Edward Elric","Alphonse Elric","Roy Mustang","Kimbley","Olivia Mira Armstrong","Alex Louis Armstrong"], # Alchimist d'Etat
    90 : ["Lust","Glutonny","Envy","Sloth","Greed","Wrath","Pride","Pere"], # Homonculus
    89 : ["Olivia Mira Armstrong","Alex Louis Armstrong"], # Armstrong
    88 : ["Kenjaku","Okuyasu","Yuki","Fujitora","Pain"], # Maitre de la Gravite
    87 : ["Dio Brando","Diego Brando","Giorno Giovanna","Dario Brando"], # Brando
    86 : ["Kyogai","Kanamue","Rui","Mukago","Wakuraba","Hairo","Rokuro","Enmu","Daki","Gyutaro","Kaigaku","Gyokko","Akaza","Doma","Kokushibo"], # Lune
    85 : ["Kanae","Kanao"], # Souffle de la Fleur
    84 : ["Sakonji","Giyu","Sabito","Makomo","Tanjiro","Murata"], # Souffle de l'Eau
    83 : ["Zenitsu","Kaigaku","Jigoro"], # Souffle de la Foudre
    82 : ["Tanjiro", "Yoriichi","Sumiyoshi","Tanjuro"], #Kamado
    81 : ["Tanjiro","Nezuko","Kanao","Sumiyoshi","Tanjuro"], #Kamado
    80 : ["Muzan","Nezuko","Tamayo","Yushiro","Susamaru","Yahaba","Fille Araignee","Mere Araignee","Shinzu"], # Demons
    79 : ["Aoi Kanzaki","Sumi","Kiyo","Naho","Goto"], # Domaine des Papillons
    78 : ["Kanao","Tanjiro","Zenitsu","Inosuke","Nezuko","Genya","Murata","Ozaki","Yoriichi"], # Pourfendeur de demons
    77 : ["Giyu","Mitsuri","Obanai","Sanemi","Gyomei","Muichiro","Shinobu Kocho","Rengoku","Kanae Kocho","Uzui"], # Hashira
    76 : ["Kagaya Ubuyashiki","Amane Ubuyashiki","Hinaki Ubuyashiki","Nichika Ubuyashiki","Kiriya Ubuyashiki","Kanata Ubuyashiki"], # Ubuyashiki
    75 : ["Toji","Megumi","Tsumiki Fushiguro"], # Fushiguro
    74 : ["Noritoshi","Kenjaku"], # Kamo
    73 : ["Toji", "Naobito","Mai","Maki","Megumi"], # Zenin
    72 : ["Gakukanji","Utahime","Arata Nitta","Mai","Miwa","Mechamaru","Aoi Todo","Noritoshi","Momo","Akari Nitta"], # ecole de Kyoto
    71 : ["Yaga","Ijichi","Gojo","Kusakabe","Sheko Ieri","Akari Nitta","Megumi","Yuji","Nobara","Maki","Toge Inumaki","Panda","Yuta","Hakari","Nanami","Geto","Yu Haibara"], # ecole de Tokyo
    70 : ["Sukuna", "Mahito", "Jogo", "Dagon", "Hanami", "Choso","Eso","Kechizu"], # Fleaux
    69 : ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne", "Johnny"], # JoJo
    68 : ["Genos","Cyborgorilla","C-17","C-18","C-16"], # Cyborg
    67 : ["Grimasse","Garou","Charanko","Bang"], # Dojo de Bang
    66 : ["Fujitora","Toph","Tosen","Komugi","Shaka","N'Doul","Yomi"], # Aveugle 
    65 : ["Minato", "Tobirama", "Yoruichi", "Gran Torino","Sonic"], # Speedster TODO
    64 : ["Kaido","Ryukyu","Toshiro","Shenron","Botobai Gigante"], # Draconique TODO  ,"Acnologia","Igneel"
    63 : ["Big Mom", "Katakuri"], # equipage de Big Mom
    62 : ["Kaido", "King", "Queen", "Jack"], # equipage de Kaido
    61 : ["Shanks","Yasopp","Lucky Roo","Benn Beckman","Rockstar"], # equipage de Shanks
    60 : ["Ussop","Kaya","Kuro","Merry","Yassop"],
    59 : ["Speedwagon","Caesar","Kakyoin","Polnareff","Mohamed Abdul","Stroheim","Okuyasu","Rohan","Koichi","Gyro","Bucciarati","Yasuho","Foo Fighter"], # JoBros
    1 : ["Itachi", "Kisame", "Deidara", "Sasori", "Hidan", "Kakuzu", "Pain", "Konan", "Zetsu", "Tobi"], # Akatsuki
    2 : ["Son Goku", "Vegeta", "Gohan", "Trunks", "Goten","Gotenks", "Bardock", "Raditz", "Nappa", "Broly", "Cabba","Caulifla","Kale","Kefla"], # Saiyan
    4 : ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"], # Mugiwara
    5 : ["Itachi", "Sasuke", "Madara", "Obito", "Shisui", "Fugaku", "Indra", "Izuna", "Sarada"], # Uchiha
    7 : ["Akainu", "Aokiji", "Kizaru", "Sengoku", "Garp", "Fujitora", "Ryokugyu", "Kong"], # Amiraux
    10 : ["Barbe Blanche", "Kaido", "Big Mom", "Shanks", "Barbe Noire","Luffy","Mihawk","Crocodile"], # Yonko
    14 : ["Yamamoto", "Unohana", "Byakuya", "Kenpachi", "Ukitake", "Kyoraku", "Sajin", "Mayuri", "Toshiro", "Rukia"], # Gotei 13
    15 : ["Hashirama", "Tobirama", "Hiruzen", "Minato", "Tsunade", "Kakashi", "Naruto","Mei Terumi", "Onoki", "Gaara"], # Kage
    16 : ["Crocodile", "Doflamingo", "Mihawk", "Kuma", "Boa Hancock", "Jinbe", "Buggy", "Law", "Barbe Noire"], # Shichibukai,
    17 : ["Jiraya","Orochimaru","Tsunade"], # Sannin
    18 : ["Dragon", "Ivankov", "Kuma", "Sabo", "Koala", "Hack", "Inazuma", "Belo Betty", "Lindbergh", "Karasu"], # Revolutionnaires
    19 : ["Luffy", "Garp", "Roger", "Ace", "Dragon", "Sabo", "Law", "Barbe Noire","Portgas D. Rouge","Vivi","Cobra"], # Volonte du D
    20 : ["Kiba", "Akamaru", "Karin", "Rob Lucci", "Chopper", "Kaido", "Marco", "Jabra", "Kaku","Cyborgorilla","Crablante", "Tonton","Pakkun", "Laboon","Sajin","Chachamaru","Kaburamaru","Lindbergh","Appa","Tama"], # Animal TODO
    21 : ["Sasuke", "Suigetsu", "Karin (naruto)", "Jugo"], # Taka
    22 : ["Nagato", "Pain", "Obito", "Madara", "Sasuke", "Momoshiki", "Kaguya"], # Rinnegan
    23 : ["Naruto", "Sakura", "Sasuke", "Kakashi", "Shikamaru", "Choji", "Ino", "Hinata", "Kiba", "Shino", "Neji", "Rock Lee", "Tenten"], # Konoha TODO
    24 : ["Gaara", "Temari", "Kankuro", "Rasa", "Yashamaru"], # Suna TODO
    25 : ["Kisame", "Zabuza", "Haku", "Mei Terumi", "Ao", "Chojuro", "Yagura", "Mangetsu", "Suigetsu"], # Kiri TODO
    26 : ["Darui", "C", "Omoi", "Killer Bee", "Samui", "Atsui", "Akatsuchi", "Onoki"], # Kumo TODO
    27 : ["Akatsuchi", "Kurotsuchi", "Onoki", "Deidara", "Kurotsuchi", "Akatsuchi", "Onoki", "Deidara"], # Iwa TODO
    28 : ["Naruto", "Bee", "Yugito", "Yagura", "Roshi", "Han", "Utakata", "Fu", "Ginkaku", "Kinkaku", "Itadori"], # Receptacle TODO
    29 : ["Aang", "Ace","Shoto Todoroki", "Sabo", "Iroh", "Zuko", "Ozai", "Azula", "Itachi", "Madara", "Sasuke","Kakuzu","Jogo","Mohamed Abdul"],# Maitre du Feu TODO
    30 : ["Aang", "Katara", "Korra", "Unalaq", "Ming-Hua", "Ghazan", "Kya", "Suigetsu", "Mei Terumi","Kakuzu","Tobirama","Kisame","Haku"], # Maitre de l'Eau TODO
    31 : ["Aang", "Toph", "Kuvira", "Suyin", "Lin", "Yamato (ANBU)", "Hashirama","Kakuzu"], # Maitre de la Terre TODO
    32 : ["Aang","Temari"], # Maitre de l'Air TODO
    33 : ["Zuko", "Iroh", "Azula", "Ozai", "Kakashi","Sasuke", "Killer Bee", "Darui", "A", "Kakuzu", "Ener"], # Maitre de l'eclair TODO
    34 : ["Shoto","Aokiji", "Toshiro Hitsugaya", "Rukia"], # Maitre de la Glace TODO Gray Fullbuster

    36 : ["Akainu", "Jogo","Mei Terumi","Kurotsuchi"], # Maitre de la Lave TODO

    40 : ["Zoro", "Mihawk","Toji","Maki", "Killer Bee", "Kuina", "Tashigi", "Kaku", "Sasuke","Kisame", "Suigetsu", "Zabuza","Shanks", "Gol D. Roger", "Stain", "Ichigo Kurosaki", "Aizen", "Kenpachi", "Unohana", "Gin", "Erza", "Dabi", "Darui", "Guts", "Yamamoto", "Trunks", "Tapion", "Gohan", "Rukia", "Byakuya", "Oden", "Law", "Brook","Cavendish","Fujitora","Shiryu", "Yhwach","Haruta Shigemo"], # epeiste
    41 : ["Mob", "Ritsu", "Teruki", "Sho Suzuki", "Tome Kurata", "Dimple","Tatsumaki"], # Telekinesiste
    42 : ["Barbe Noire", "Shiryu", "Lafitte", "Van Augur", "Doc Q", "Avalo Pizarro", "Catarina Devon", "Vasco Shot"], # Equipage de Barbe Noire
    43 : ["Barbe Blanche", "Marco", "Joz", "Vista", "Blamenco", "Rakuyo", "Namur", "Ace", "Haruta", "Fossa", "Izo", "Atmos"], # Equipage de Barbe Blanche
    44 : ["Naruto Uzumaki", "Kushina Uzumaki", "Nagato", "Karin", "Mito Uzumaki", "Boruto Uzumaki", "Himawari Uzumaki"], # Uzumaki
    45 : ["Neji", "Hinata", "Hiashi", "Hanabi","Himawari", "Boruto"], # Hyuga
    46 : ["Hashirama", "Tobirama", "Tsunade", "Nawaki"], # Senju
    47 : ["Kaguya", "Rikudo", "Hamura", "Urashiki", "Momoshiki", "Kinshiki", "Toneri", "Isshiki"], # Ototsuki
    48 : ["Shino", "Meruem", "Pufu", "Youpi", "Neferopito"], # Insecte
    49 : ["Meruem", "Neferopito", "Youpi", "Pufu"], # Garde Royale
    # 50 Zeppeli
    50 : ["Will Zeppeli", "Caesar", "Gyro","Mario"], # Zeppeli

    53 : ["Dio","Diavolo", "Jotaro","Nighteye","Kira Yoshikage","Enrico Pucci"], # Maitre du Temps
    54 : ["Kira Yoshikage", "Bakugo"], # Maitre de l'Explosion
    55 : ["Ghiaccio", "Prosciutto", "Pesci", "Melone", "Illuso", "Formaggio", "Gelato", "Sorbet", "Cioccolata", "Secco"], # Squadra Esecuzioni
    56 : ["Jonathan", "William Zeppeli", "Joseph", "Caesar", "Lisa Lisa", "Poco"], # Hamon
    57 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo", "Abbacchio","Diavolo","Fugo","Luca","Polpo"], # Passione
    58 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo", "Abbacchio"], # Team Bucciarati
    
}

all_techniques = {
    "All Might" : [
        ["United States of Smash", "utilise l''","https://i.imgur.com/tGRgG5e.mp4", "#FF0000"], #TOREVIEW format mp4
    ],
    "Sasuke" : [
        ["Rinnegan", "active son", "https://i.imgur.com/qJ5mfnz.gif", "#d100ff"],
    ],
    "Hit" : [
        ["Point Vitaux", "vise les", "https://i.imgur.com/vi0Kg6z.gif", "#ff3bde"],
    ],
    "Son Goku" : [
        ["Teleportation", "utilise sa", "https://i.imgur.com/skth3A1.gif", "#ff0000"],
    ],
    "Pere": [
        ["Alchimie", "utilise l'", "https://i.imgur.com/KzMK7Xu.gif", "#ec000e"],
    ],
    "Morel": [
        ["Ecran de fumee", "lance un", "https://i.imgur.com/sNGqJb3.gif", "#d100ff"],
    ],
    "Aang": [
        ["Colonnes de flamme", "envoie des", "https://i.imgur.com/nqUJVqG.gif", "#f55a42"],
    ],
}