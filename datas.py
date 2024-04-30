from constantes import CONSTANTS


image_temporaire = "https://picsum.photos/900/500"
all_characters_templates = {
            "Dragon Ball" : [ # ✅
            ("Super Shenron", "X", "https://i.imgur.com/W7V2Oru.gif", 1500, 1500, 1500),
            ("Son Goku", "X", "https://i.imgur.com/1dpz2hV.gif", 905, 1050, 900),
            ("Zeno", "X", "https://i.imgur.com/W579wtw.gif", 800, 1300, 800),
            ("Grand Pretre", "X", "https://i.imgur.com/XFKPYIb.gif", 1000, 1200, 1000),
            ("Whis", "X", 'https://i.imgur.com/UHCV2D1.gif', 1050, 1040, 1000),
            ("Vados", "X", 'https://i.imgur.com/6WuAjqS.gif',1010, 1050, 1000),
            ("Beerus", "X", 'https://i.imgur.com/9ZLOxBK.gif', 920, 1150, 910),
            ("Son Gohan", "X", 'https://i.imgur.com/SJPfZLY.gif', 950, 960, 970),

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
            ("Trunks", "S", 'https://i.imgur.com/4j08x7s.gif', 530, 520, 540),

            # Personnages A
            ("Freezer", "A", 'https://i.imgur.com/dqV5UcM.gif', 430, 425, 450),
            ("Caulifla", "A", 'https://i.imgur.com/38lAUJ6.gif', 420, 430, 415),
            ("Kid Buu", "A", 'https://i.imgur.com/Aycebhm.gif', 410, 440, 420),

            # Personnages B
            ("Cooler", "B", 'https://i.imgur.com/BZcWjPn.gif', 350, 340, 330),
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
            ("Roi Cold", "C", 'https://i.imgur.com/EWJ8rdH.png', 270, 260, 250),
            ("Dabra", "C", 'https://i.imgur.com/bzYsWfm.jpeg', 260, 265, 255),
            ("Bardock", "C", 'https://i.imgur.com/MSTYpQg.jpeg', 260, 280, 250),
            ("Roi Vegeta", "C", "https://i.imgur.com/mtsE4Cy.jpeg", 255, 270, 245),
            ("Uub", "C", "https://i.imgur.com/fZvqk1U.jpeg", 250, 250, 235),
            ("Kaio Shin", "C", "https://i.imgur.com/NNcDlai.jpeg", 230, 240, 270),
            ("Goten", "C", 'https://i.imgur.com/LaP4Y5P.jpeg', 240, 255, 270),
            ("Tapion", "C", 'https://i.imgur.com/CGw5aGC.jpeg', 250, 260, 270),

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
            ("Pan", "E", "https://i.imgur.com/RiNEaKR.jpeg", 90, 100, 85),
            ("Maitre Kaio", "E", "https://i.imgur.com/aCVE7Du.jpeg", 90, 100, 85),

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
            "Naruto" : [ # ✅
            # Personnages X
            ("Kaguya Otsutsuki", "X", "https://i.imgur.com/P3M8HQH.gif", 950, 940, 950),
            ("Madara Uchiha", "X", "https://i.imgur.com/c0NF2KN.gif", 945, 955, 950),
            ("Rikudo", "X", "https://i.imgur.com/bn7KwyD.gif", 1003, 1002, 1001),
            ("Obito Uchiha", "X", "https://i.imgur.com/A6roLXk.gif", 920, 940, 935),
            ("Boruto Uzumaki", "X", "https://i.imgur.com/zRYpAKC.gif", 980, 970, 960), 
            ("Isshiki Otsutsuki", "X", "https://i.imgur.com/BX1WxS1.gif", 945, 950, 955),
            
            # Personnages SS
            ('Kawaki', 'SS', 'https://i.imgur.com/ipJLKqO.gif', 720, 740, 750),
            ('Sasuke Uchiha', 'SS', 'https://i.imgur.com/PYEEX2h.gif', 730, 750, 740),
            ('Naruto Uzumaki', 'SS', 'https://i.imgur.com/n8cS6mP.gif', 725, 745, 745),
            ('Indra Otsutsuki', 'SS', 'https://i.imgur.com/dlXLwgN.gif', 730, 750, 740),
            ('Ashura Otsutsuki', 'SS', 'https://i.imgur.com/aRMeDPa.gif', 725, 745, 745),
            ('Hashirama Senju', 'SS', 'https://i.imgur.com/MV6VGfx.gif', 735, 750, 740),
            ('Tobirama Senju', 'SS', 'https://i.imgur.com/lc99oDg.gif', 720, 720, 710),
            ('Toneri Otsutsuki', 'SS', 'https://i.imgur.com/RC3B2rR.gif', 675, 715, 735),
            ('Pain', 'SS', 'https://i.imgur.com/GvovLg8.gif', 700, 720, 675),
            ('Itachi Uchiha', 'SS', 'https://i.imgur.com/Jhc5tcj.gif', 700, 730, 695),
            ('Minato Namikaze', 'SS', 'https://i.imgur.com/CZd4NkY.gif', 690, 720, 735),
            ('Guy', 'SS', 'https://i.imgur.com/Iocgqpz.gif', 730, 725, 700),
            ('Momoshiki Otsutsuki', 'SS', 'https://i.imgur.com/OnBJXu9.gif', 665, 685, 665),
            ('Kakashi Hatake', 'SS', 'https://i.imgur.com/DFD8eEL.gif', 710, 700, 71),

            # Personnages S
            ('Danzo Shimura', 'S', 'https://i.imgur.com/rsM0pCB.gif', 555, 525, 580),
            ('Kabuto Yakushi', 'S', 'https://i.imgur.com/zCf0Etf.gif', 535, 540, 580),
            ('Shisui Uchiha', 'S', 'https://media1.tenor.com/m/_To3NtVgZv0AAAAC/shisui-uchiha-shisui.gif', 580, 590, 540),
            ('Hidan', 'S', 'https://gifdb.com/images/high/naruto-shippuden-akatsuki-hidan-yj5u9lmg4se7nuz4.gif', 525, 580, 570),
            ('Hiruzen Sarutobi', 'S', 'https://media1.tenor.com/m/j6hgBpYSrL4AAAAC/hiruzen-sarutobi.gif', 565, 560, 580),
            ('Onoki', 'S', 'https://pa1.aminoapps.com/8436/0050341a556d26a1e018daa2d679190837ffd8a2r1-500-281_hq.gif', 585, 580, 580),
            ('Gaara', 'S', 'https://i.imgur.com/GlPqkEg.gif', 580, 555, 545),
            ('Killer Bee', 'S', 'https://i.imgur.com/fct31yS.gif', 560, 575, 525),
            ('Orochimaru', 'S', 'https://i.imgur.com/betllia.gif', 550, 525, 570),
            ('Tsunade', 'S', 'https://i.imgur.com/F3nORVn.gif', 520, 565, 570),
            ('Jiraya', 'S', 'https://i.imgur.com/VKP25gr.gif', 530, 565, 580),
            ('Izuna Uchiha', 'S', 'https://i.imgur.com/RP8gHg3.gif', 585, 560, 540),
            ('Hanzo', 'S', 'https://i.imgur.com/fN5R7A7.gif', 580, 560, 540),

            # Personnages A 
            ('Fû', 'A', 'https://i.imgur.com/M18N3wg.gif', 400, 445, 435),
            ('Rock Lee', 'A', 'https://i.imgur.com/1V4WwG9.png', 445, 440, 420),
            ('Shikamaru Nara', 'A', 'https://i.imgur.com/KySPqGV.gif', 390, 425, 420),
            ('Mei Terumi', 'A', 'https://i.imgur.com/JTaGhQQ.gif', 430, 415, 425),
            ('Asuma Sarutobi', 'A', 'https://i.imgur.com/lGIqLP3.gif', 405, 420, 405),
            ('Kisame', 'A', 'https://i.imgur.com/50KuDl3.gif', 450, 445, 435),
            ('Darui', 'A', 'https://i.imgur.com/4agHAoM.gif', 395, 415, 450),
            ('Sasori', 'A', 'https://i.imgur.com/RlpI6Rd.gif', 445, 390, 390),
            ('Deidara', 'A', 'https://i.imgur.com/k83MFjs.gif', 425, 440, 450),
            ('Konan', 'A', 'https://i.imgur.com/3mOmZ0v.gif', 415, 410, 405),
            ('Kakuzu', 'A', 'https://i.imgur.com/BKf04A1.gif', 415, 405, 410),
            ('Sai', 'A', 'https://i.imgur.com/03ICbLj.gif', 395, 440, 430),
            ('Zetsu', 'A', 'image_temporaire', 390, 420, 450),

            # Personnages B
            
            ("Temari", "B", 'https://cdn.discordapp.com/attachments/805054171661336590/817119251750977566/TEMARI.gif', 310, 355, 305),
            ("Yamato (naruto)", "B", "https://i.imgur.com/ysZw0Ep.jpeg", 355, 315, 340), 
            ("Neji Hyuga", "B", "https://i.imgur.com/acFMgGN.png", 325, 330, 305),
            ("Kankuro", "B", 'https://i.imgur.com/6h0fZTJ.png', 355, 305, 355),
            ("Chiyo", "B", 'https://i.imgur.com/FTca3VV.jpeg', 305, 355, 310),
            ("Choji", "B", 'https://media1.tenor.com/m/FAqetz7SiCEAAAAd/choji.gif', 305, 345, 365), 
            ("Shino", "B", 'https://i.imgur.com/mVxNOAM.png', 355, 305, 355),
            ("Kiba", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808361778567970876/KIBA.gif', 305, 355, 305),
            ("Ino", "B", 'https://media1.tenor.com/m/tdptC0lOIB4AAAAC/ino-yamanaka-ino.gif', 325, 305, 315),
            ("Sakura Haruno", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808354355744342026/SAKUA.gif', 305, 355, 335),
            ("Hinata Hyuga", "B", 'https://i.imgur.com/VsFYMA1.gif', 355, 325, 350),
            ("Suigetsu", "B", 'https://i.imgur.com/E6d3rSt.gif', 305, 355, 310),
            ("Jugo", "B", 'https://i.imgur.com/lfSps90.png', 370, 325, 365),
            ("Kurenai", "B", 'https://i.imgur.com/1E2Ux2a.png', 305, 335, 310),
            ("Zabuza Momochi", "B", "https://i.imgur.com/ntmenx6.png", 310, 355, 320),
            ("Mito Uzumaki", "B", "https://i.imgur.com/rSHfKaR.jpeg", 310, 355, 320),

            # Personnages C
            ("Konohamaru Sarutobi", "C", "https://i.imgur.com/8rusox0.jpeg", 260, 265, 240),
            ("Fugaku Uchiha", "C", "https://i.imgur.com/UAg1uqa.jpeg", 260, 265, 240), #TO REVIEW
            ("Haku", "C", 'https://i.imgur.com/vqQD56N.png', 240, 260, 250),
            ("Kimimaro", "C", 'https://i.imgur.com/OEKnkD4.png', 235, 250, 245),
            ("Anko", "C", "https://static.wikia.nocookie.net/narutoinuyashapokemnyharrypotter/images/0/08/Anko_Mitarashi.jpg/revision/latest?cb=20130327192458&path-prefix=es", 230, 235, 240),
            ("Guren", "C", "https://static.wikia.nocookie.net/naruto/images/9/90/Guren.png/revision/latest?cb=20171125162907&path-prefix=fr", 250, 260, 260),
            ("Tenten", "C", "https://i.imgur.com/s6MEz46.png", 239, 270, 230),
            ("Karin (naruto)", "C", "https://i.imgur.com/9wE2B1h.jpeg", 230, 220, 210),
            ("Yugao uzuki", "C", "https://i.imgur.com/Hcvleq0.png", 260, 265, 260),
            ("Kushina Uzumaki", "C", "https://i.imgur.com/segkPzo.png", 250, 260, 240),

            # Personnages D
            ("Mitsuki", "D", "https://i.imgur.com/oK1gF6f.jpeg", 170, 200, 175),
            ("Sarada Uchiha", "D", "https://i.imgur.com/glraFLL.jpeg", 180, 200, 175),
            ("Iruka", "D", 'https://i.imgur.com/p0YmijL.png', 170, 180, 175),
            ("Hanabi Hyuga", "D", 'https://i.imgur.com/EKSsprP.jpeg', 160, 170, 165),
            ("Shizune", "D", 'https://i.imgur.com/53rdzBL.png', 160, 170, 165),

            # Personnages E
            ("Himawari Uzumaki", "E", "https://i.imgur.com/XcHkz6j.png", 130, 140, 120),
            ("Ebisu", "E", 'https://i.imgur.com/qWpczNK.png', 110, 130, 115),
            ("Mizuki", "E", "https://static.wikia.nocookie.net/naruto/images/9/9c/Mizuki.png/revision/latest?cb=20210529210947&path-prefix=fr", 120, 125, 115),

            # Personnages F
            ("Nawaki", "F", "https://i.imgur.com/k5iscPr.png", 30, 50, 10),
            ("Tonton", "F", "https://static.wikia.nocookie.net/xianb/images/f/fa/60t.png/revision/latest/scale-to-width-down/579?cb=20141101233045", 10, 10, 10),
            ("Pakkun", "F", "https://lh4.googleusercontent.com/vh79H5M8vWfVyuSiNnhk27N59eFH-ukdQUT028m5kmqGsPHp5pO74qpVbTpkhdX80w3utduzz1PaUVEj8ZMAblZXV9n-R4_Z7wdhX1PHxHJDEY7DQbDWOaIVeztagZRM_9WTEYqdRHpawafgywENVw", 30, 25, 40),
            ("Inari", "F", "https://static.wikia.nocookie.net/naruto/images/a/af/Inari_Parte_I_Anime.png/revision/latest?cb=20130829123658&path-prefix=es", 20, 30, 20),
],
            "One Piece" : [ # ✅
            # Personnages X
            ("Kaido", "X", "https://i.imgur.com/BMDbkl8.gif", 1000, 990, 1010),
            ("Monkey D. Luffy", "X", "https://i.imgur.com/EmzijMq.gif", 950, 940, 930), # TOREVIEW
            ("Big Mom", "X", "https://i.imgur.com/tPjCbUc.gif", 1005, 910, 1000),
            ("Marshall D. Teach", "X", "https://i.imgur.com/Y4vdAQ4.gif", 970, 1000, 965),
            ("Barbe Blanche", "X", "https://i.imgur.com/BdnDfQj.gif", 1000, 1050, 1010),
            ("Shanks", "X", "https://i.imgur.com/faZclqg.gif", 930, 970, 930),
            ("Monkey D. Dragon", "X", "https://i.imgur.com/Zy9hmOz.gif", 930, 950, 915),
            ("Gol D. Roger", "X", "https://i.imgur.com/jhHkjfz.gif", 940, 970, 930),
            ("Dracule Mihawk", "X", 'https://i.imgur.com/UICGMYV.gif', 935, 980, 915),
            
            # Personnages SS
            ("Akainu", "SS", "https://i.imgur.com/OkB0Vk3.gif", 730, 790, 745), # high ss
            ("Aokiji", "SS", 'https://i.imgur.com/LCqY9UI.gif', 700, 720, 725),
            ("Kizaru", "SS", 'https://i.imgur.com/nTGQsXq.png', 720, 780, 760),
            ("Fujitora", "SS", 'https://i.imgur.com/OxgHvz2.gif', 720, 760, 725),#TO REVIEW
            ("Rayleigh", "SS", 'https://i.imgur.com/HzaJdFI.gif', 790, 830, 730), # high ss
            ("Katakuri", "SS", 'https://i.imgur.com/5z0sR8N.gif', 725, 770, 735),
            ("Ryokugyu", "SS", 'https://i.imgur.com/27FScKO.jpg', 710, 720, 700),
            ("Monkey D. Garp", "SS", 'https://i.imgur.com/ZLd4sdw.gif', 750, 780, 750),
            ("Don Quichotte Doflamingo", "SS", 'https://i.imgur.com/HHCqR9J.jpg', 730, 720, 725),
            ("Trafalgar D. Law", "SS", 'https://i.imgur.com/xJpnwDU.png', 715, 740, 710),
            ("Eustass Kid", "SS", 'https://i.imgur.com/5WxLV4L.gif', 715, 740, 720),
            ("Roronoa Zoro", "SS", 'https://i.imgur.com/fPok6pt.gif', 715, 750, 720),
            ("Oden", "SS", 'https://i.imgur.com/mACnc1L.jpg', 710, 745, 720),
            ("King", "SS", 'https://i.imgur.com/wq5sEZ7.png', 715, 720, 710),
            ("Jaygarcia Saturn", "SS", 'https://i.imgur.com/fyHMKWB.png', 710,666,710),
            ("Marcus Mars", "SS", 'https://i.imgur.com/wq5OAwa.png', 710,666,710),
            ("Topman Warcury", "SS", 'https://i.imgur.com/xOVHWfz.jpeg', 710,666,710),
            ("Ethanbaron Nusjuro", "SS", 'https://i.imgur.com/btlRYmL.jpeg', 710,666,710),
            ("Shepherd Ju Peter", "SS", 'https://i.imgur.com/A0MDH1W.png', 710,666,710),
            ("Yamato", "SS", "https://i.imgur.com/JD7nx4U.gif", 700, 720, 740),
            ("Benn Beckman", "SS", "https://i.imgur.com/DzyPGvS.gif", 700, 740, 710),
            
            # Personnages S
            ("Queen", "S", "https://i.imgur.com/A2gDuBn.gif", 600, 590, 590),
            ("Sengoku", "S", "https://i.imgur.com/AJEnLGM.gif",600, 530, 600),
            ("Crocodile", "S", 'https://i.imgur.com/H1BwUuK.gif', 550, 600, 620),
            ("Ener", "S", 'https://i.imgur.com/s9LuY59.png', 540, 590, 610),
            ("Shiryu", "S", "https://i.imgur.com/RTUxvAI.gif", 530,550,540),
            ("Smoker", "S", "https://i.imgur.com/3vJPaRx.gif", 550, 520, 600),
            ("Sabo", "S", "https://i.imgur.com/vjcu8Gg.gif", 540, 595, 535),
            ("Boa Hancock", "S", 'https://i.imgur.com/ZWtbLYH.gif', 535, 545, 555),
            ("Marco", "S", 'https://i.imgur.com/LOo1j5P.gif', 580, 550, 575),
            ("Sanji", "S", 'https://i.imgur.com/hkob0Vu.jpg', 540, 555, 550),
            ("Portgas D. Ace", "S", "https://i.imgur.com/8AGmDrS.gif", 550, 600, 620),
            ("Rob Lucci", "S", "https://i.imgur.com/aewCvhP.gif", 560, 570, 560),

            # Personnages A
            ("Jewelry Bonney","A","https://i.imgur.com/HBR63xX.gif", 4200, 415, 425),
            ("Caesar Clown", "A", "https://i.imgur.com/YxmbkTD.gif", 430, 415, 425),
            ("Vergo", "A", "https://i.imgur.com/qSwhEar.gif", 445, 420, 395),
            ("Urouge", "A", "https://i.imgur.com/qqVrtD6.jpeg", 430, 415, 425),
            ("Kuma", "A", "https://i.imgur.com/chLQErz.gif", 395, 420, 445),
            ("Kong", "A", "https://i.imgur.com/9KBCQoO.jpeg", 440, 420, 445),
            ("Ivankov", "A", "https://i.imgur.com/5LxBHGh.jpeg", 445, 420, 395),
            ("Brook", "A", "https://i.imgur.com/Dusk4ZW.gif", 445, 420, 395),
            ("Robin", "A", 'https://i.imgur.com/tiC5mlA.gif', 395, 420, 445),
            ("Jinbe", "A", 'https://i.imgur.com/5ktjcxG.png', 440, 420, 445),
            ("Karasu", "A", "https://i.imgur.com/M4BBxgI.gif", 395, 420, 445),
            ("Yassop", "A","https://i.imgur.com/KjovWi0.gif", 395, 410, 445),

            # Personnages B
            ("Chopper", "B", 'https://i.imgur.com/J4PGB24.gif', 300, 330, 365),
            ("Nami", "B", 'https://i.imgur.com/VAbsCsh.gif', 335, 330, 305),
            ("Usopp", "B", "https://i.imgur.com/dhRNN1S.jpeg", 330, 350, 315),
            ("Hina", "B", 'https://i.imgur.com/2tbPDP4.png', 315, 335, 345),
            ("Buggy", "B", "https://i.imgur.com/9aeBJHQ.jpeg", 355, 330, 305),
            ("Lindbergh", "B", "https://i.imgur.com/a8tSh0n.jpeg", 330, 355, 305),
            ("Koala", "B", "https://i.imgur.com/WiiPoza.jpeg", 330, 355, 305),
            ("Inazuma", "B", 'https://i.imgur.com/PyUiXXv.png', 305, 330, 355),
            ("Belo Betty", "B", "https://i.imgur.com/RSckfSk.jpeg", 355, 330, 305),
            ("Franky", "B", 'https://i.imgur.com/U08oSKn.gif', 340, 305, 355),
            ("Koby", "B", 'https://i.imgur.com/OtsQuBI.png', 305, 330, 355),
            ("Kaku", "B", 'https://i.imgur.com/9jRznLq.png', 305, 330, 345),
            ("Tsuru", "B", 'https://i.imgur.com/9KaHWA4.jpeg', 305, 330, 345),
            ("Doll", "B", "https://i.imgur.com/0yJtSwk.jpeg", 305, 330, 345),
            ("Magellan", "B", "https://i.imgur.com/5keN9ye.png", 335, 360, 355),

            # Personnages C
            ("Vivi", "C", "https://i.imgur.com/16YOCq0.jpeg", 285, 260, 235),
            ("Kumadori", "C", "https://i.imgur.com/EXrO0fr.png", 235, 260, 285),
            ("Arlong", "C", 'https://i.imgur.com/MXsMw7m.jpg', 235, 260, 285),
            ("Don Krieg", "C", "https://i.imgur.com/JvWP2oH.jpeg", 285, 260, 235),
            ("Tashigi", "C", "https://i.imgur.com/Kkum0d7.jpeg", 235, 260, 285),
            ("Corazon","C", "https://i.imgur.com/TN4CrB6.jpeg", 285, 260, 235),
            ("Cobra", "C", "https://i.imgur.com/NbrtIm5.png", 285, 260, 235),
            ("Hack", "C", "https://i.imgur.com/SFJ2nKt.jpeg", 235, 260, 285),
            ("Haguar D. Sauro", "C", "https://i.imgur.com/d7eeL5L.jpeg", 235, 260, 285),

            # Personnages D
            ("Dorry", "D", "https://i.imgur.com/daws2KL.jpeg", 155, 180, 205),
            ("Brogy", "D", "https://i.imgur.com/LlwBlC8.jpeg", 205, 180, 155),
            ("Hermep", "D", "https://i.imgur.com/jTc7VYu.jpeg", 150, 170, 145),

            # Personnages E
            ("Hatchan", "E", "https://i.imgur.com/NOhupN5.png", 145, 120, 95),
            ("Kuro", "E", "https://i.imgur.com/SUoZvEu.jpeg", 105, 120, 145),
            ("Wapol", "E", "https://i.imgur.com/PSrXqQ6.jpeg", 145, 120, 95),

            # Personnages F
            ("Shimotsuki Kuina", "F", "https://i.imgur.com/JBtwdN0.jpeg", 25, 50, 30),
            ("Merry","F","https://i.imgur.com/elYgXrH.png", 25, 50, 75),
            ("Gaimon", "F", "https://i.imgur.com/DmyqVEz.jpeg", 75, 50, 25),
            ("Kaya", "F", "https://i.imgur.com/aZcF3en.jpeg", 25, 50, 75),
            ("Laboon", "F", "https://i.imgur.com/dqVZ8RB.png", 75, 50, 25),
            ("Portgas D. Rouge", "F", "https://i.imgur.com/PsLtwjG.jpeg", 25, 50, 75),
            ],
            "Bleach" : [ # ✅
            # Personnages X
            ("Yhwach", "X", "https://i.imgur.com/OLYulIP.gif", 950, 1200, 1000), 
            ("Ichigo Kurosaki", "X", "https://i.imgur.com/5LJbZtC.gif", 1000, 1200, 1000),
            ("Sosuke Aizen", "X", 'https://i.imgur.com/8xq9dtV.gif', 950, 1100, 970),
            ("Yamamoto", "X", 'https://i.imgur.com/EGYHcBd.gif', 900, 1300, 900),
            ("Ichibe Hyosube", "X", "https://i.imgur.com/dg916bt.gif", 1100, 950, 1000),

            # Personnages SS
            ("Kenpachi", "SS", "https://i.imgur.com/DCS6I2N.gif", 705, 770, 715),
            ("Jugram", "SS", "https://i.imgur.com/kXmvoS6.gif", 705, 750, 695),
            ("Kyoraku", "SS", "https://i.imgur.com/7DGfP2z.gif", 745, 850, 705),
            ("Byakuya Kuchiki", "SS", "https://i.imgur.com/VZrc8mU.gif", 695, 800, 725),
            ("Urahara", "SS", "https://i.gifer.com/53FX.gif", 725, 800, 715),
            ("Yoruichi", "SS", "https://i.gifer.com/3flV.gif", 705, 770, 715),
            ("Unohana", "SS", "https://i.imgur.com/b1x9GUC.gif", 695, 850, 755),
            ("Ulquiorra", "SS", "https://i.imgur.com/OaYNXCg.gif", 690, 800, 710),
            ("Gin", "SS", "https://i.imgur.com/kveTtpS.gif", 705, 750, 715),
            ("Starrk", "SS", "https://i.imgur.com/SNpSgRB.gif", 700, 780, 720),
            ("Renji", "SS", "https://i.imgur.com/RptZEBF.gif", 725, 705, 720),
            ("Senjumaru", "SS", "https://i.imgur.com/EKWGM3I.gif", 715, 800, 725),

            # Personnages S
            ("Toshiro Hitsugaya", "S", "https://i.imgur.com/R9S0Qa4.gif", 705, 720, 695),
            ("Mayuri", "S", "https://i.imgur.com/n8BNWm7.gif", 550, 600, 535),
            ("Sajin", "S", "https://i.imgur.com/6cf4JEH.gif", 600, 500, 550),
            ("Isshin Kurosaki", "S", "https://i.imgur.com/GTYbLGY.gif", 550, 550, 530),
            ("Rukia Kuchiki", "S", "https://i.imgur.com/IDjAqqP.gif", 550, 620, 560),
            ("Shinji", "S", 'https://i.imgur.com/9vxW0IN.gif', 550, 650, 540), 
            ("Soi Fon", "S", 'https://i.imgur.com/EVH34qM.gif', 550, 580, 545),
            ("Tosen", "S", 'https://i.imgur.com/4GA76X1.gif', 550, 550, 540),
            ("Baraggan", "S", 'https://i.imgur.com/k89CHqN.gif', 550, 570, 530),
            ("Grimmjow", "S", 'https://i.imgur.com/nj464jc.gif', 580, 600, 540),
            ("Uryu Ishida", "S", "https://i.imgur.com/AC2f6Ey.gif", 550, 600, 540),
            ("Ryuken Ishida", "S", 'https://i.imgur.com/turdL6j.gif', 540, 550, 520),

            # Personnages A
            ("Ukitake", "A", 'https://i.imgur.com/PqGvVzv.gif', 395, 420, 405), 
            ("Halibel", "A", 'https://i.imgur.com/2OGaKON.gif', 410, 420, 430),
            ("Nnoitra", "A", 'https://i.imgur.com/z5SAM9h.gif', 440, 450, 460),
            ("Shuhei", "A", 'https://i.imgur.com/rkQNMQX.gif', 415, 435, 420),
            ("Orihime", "A", 'https://i.imgur.com/xGhy8ky.gif', 430, 420, 460),
            ("Ginjo", "A", 'https://i.imgur.com/xLPLs5Q.gif', 410, 420, 430),
                
            # Personnages B
            ("Kira", "B", 'https://i.imgur.com/H5EQmb0.png', 330, 340, 320),
            ("Ikkaku", "B", 'https://i.imgur.com/wWd1Z4z.png', 345, 360, 335),
            ("Kensei", "B", 'https://i.imgur.com/fHD5IZV.png', 335, 345, 330),
            ("Chad", "B", "https://i.imgur.com/o4eSlWY.jpeg", 340, 360, 330),
            ("Yumichika", "B", "https://i.imgur.com/mC8r7ka.jpeg", 320, 330, 340),
            ("Ginrei Kuchiki", "B", "https://i.imgur.com/Gdg23jz.png", 330, 340, 320),

            # Personnages C
            ("Ganju", "C", 'https://i.imgur.com/4HYU47B.png', 245, 255, 240),
            ("Marechiyo", "C", 'https://i.imgur.com/QdU2qIp.png', 250, 260, 270),
            ("Soken Ishida", "C", "https://i.imgur.com/C3fEyfa.png", 240, 255, 260),
            ("Masaki Kurosaki","C","https://i.imgur.com/o6oX1Q6.jpeg", 250, 230, 270),
            
            # Personnages D
            ("Hanataro", "D", 'https://i.imgur.com/MPaOL4G.png', 185, 170, 180),
            ("Yachiru", "D", 'https://i.imgur.com/6mO9KFd.jpeg', 180, 190, 175),

            # Personnages E


            # Personnages F
            ("Keigo Asano", "F", 'https://i.imgur.com/D8dqhs2.png', 40, 35, 35),
            ("Yuzu Kurosaki", "F", 'https://i.imgur.com/Spca2oo.png', 40, 35, 35),
            ("Kon", "F", 'https://i.imgur.com/t1az2SQ.png', 45, 50, 55),
            ("Karin Kurosaki", "F", 'https://i.imgur.com/Spca2oo.png', 50, 55, 45),
            ("Yuzu", "F", 'https://i.imgur.com/plnofeu.png', 55, 45, 50),
            ("Tatsuki", "F", 'https://i.imgur.com/mSvWp2O.png', 50, 55, 50),
            ("Mizuiro", "F", 'https://i.imgur.com/b4sfzoT.png', 45, 55, 50),
            
            ],
            "My Hero Academia" : [ # ✅
            # Personnages X
            ("All Might", "X", "https://i.imgur.com/CUUh7Cd.gif", 950, 955, 950),
            ("Tomura Shigaraki", "X", "https://i.imgur.com/4G7TwKg.gif", 930, 1000, 940),
            ("All For One", "X", "https://i.imgur.com/rR1sQPU.gif", 930, 960, 950),

            # Personnages SS
            ("Star And Stripe", "SS", "https://i.imgur.com/awX9W1z.gif", 700, 730, 740),
            ("Izuku Midoriya", "SS", "https://i.imgur.com/sfcQ2nE.gif", 720, 740, 730),
            ("Endeavor", "SS", "https://i.imgur.com/Y2olaBF.gif", 720, 740, 710),
            ("Chisaki Kai", "SS", "https://i.imgur.com/dcPHh3I.gif", 680, 790, 680),
            ("Nana Shimura", "SS", "https://i.imgur.com/ct2j0jN.gif", 720, 730, 715),
            ("Mirio Togata", "SS", "https://i.imgur.com/gOMDPVp.gif", 710, 735, 700),
            ("Re-Destro", "SS", "https://i.imgur.com/HQp99hz.gif", 690, 700, 700),
            ("Katsuki Bakugo", "SS", "https://i.imgur.com/NK0LePb.gif", 690, 720, 700),
            ('Gigantomachia', 'SS', 'https://i.imgur.com/joOFOuN.gif', 730, 720, 680),
            
            # Personnages S
            ('Dabi', 'S', 'https://i.imgur.com/BjDR5Yi.gif', 530, 600, 555) ,
            ("Shinji Nishiya", "S", "https://i.imgur.com/J2ebGS2.gif", 500, 555, 510),
            ('Beast Jeanist', 'S', 'https://i.imgur.com/YomRbmO.gif', 535, 550, 550) ,
            ('Hawks', 'S', 'https://i.imgur.com/X15PwP6.gif', 545, 595, 590) ,
            ('Twice', 'S', 'https://i.imgur.com/aTXRvNJ.gif', 535, 555, 560) ,
            ('Shoto Todoroki', 'S', 'https://i.imgur.com/SYm3EIh.gif', 535, 565, 545) ,
            ('Shota Aizawa', 'S', 'https://i.imgur.com/kPsHrCm.gif', 530, 580, 535) ,
            ('Tamaki Amajiki', 'S', 'https://i.imgur.com/PrRON0k.gif', 555, 525, 535) ,
            ('Stain', 'S', 'https://i.imgur.com/bLlQH1S.gif', 530, 595, 555) ,
            ('Fumikage Tokoyami', 'S', 'https://i.imgur.com/75sU4v8.gif', 530, 535, 540) ,
            ('Mirko', 'S', 'https://i.imgur.com/uaH6Nth.gif', 545, 570, 600) ,
            ('Lady Nagant', 'S', 'https://i.imgur.com/XTarup4.gif', 585, 620, 535) ,
            ('Ryukyu', 'S', 'https://i.imgur.com/jUEf20r.gif', 565, 515, 565) ,
            ('Shinso Hitoshi', 'S', 'https://i.imgur.com/6KR8YEl.gif', 500, 555, 510) ,
            ('Nejire Hado', 'S', 'https://i.imgur.com/L3C8OLl.gif', 540, 550, 545) ,
            

            # Personnages A
            
            ('Mt. Lady', 'A', 'https://i.imgur.com/BGdhXVd.gif', 405, 400, 450) ,
            ('Gran Torino', 'A', 'https://i.imgur.com/pHGoXST.gif', 405, 440, 395) ,
            ('Nighteye', 'A', 'https://i.imgur.com/fgO8qfb.gif', 375, 380, 415) ,
            ('Midnight', 'A', 'https://i.imgur.com/L4S7dNo.jpeg', 375, 450, 385) ,
            ('Himiko Toga', 'A', 'https://i.imgur.com/YWZtjvt.gif', 410, 385, 430) ,
            ('Snipe', 'A', 'https://i.imgur.com/C5qxDQC.gif', 455, 465, 430) ,
            
            # Personnages B
            ('Tenya Iida', 'B', 'https://i.imgur.com/XAE3t5c.gif', 365, 360, 375) ,
            ('Denki Kaminari', 'B', 'https://i.imgur.com/aq2fHI5.png', 340, 350, 315) ,
            ('Testutetsu', 'B', 'https://i.imgur.com/06KllgA.jpeg', 335, 320, 375) ,
            ('Momo Yaoyorozu', 'B', 'https://i.imgur.com/3knQkZJ.jpeg', 380, 305, 360) ,
            ('Neito Monoma', 'B', 'https://i.imgur.com/Px0oEH3.jpeg', 335, 280, 330) ,
            ('Ochaco Uraraka', 'B', 'https://i.imgur.com/GqBcqOI.jpeg', 335, 285, 315) ,

            # Personnages C
            ("Ibara Shiozaki", "C", "https://i.imgur.com/psEieZz.jpeg", 285, 260, 235),
            ('Shindo', 'C', 'https://i.imgur.com/I7uLCYw.jpeg', 285, 285, 270) ,
            ('Rock Lock', 'C', 'https://i.imgur.com/s3iBS2y.jpeg', 305, 300, 250) ,
            ('Vlad King', 'C', 'https://i.imgur.com/v4AGxIS.jpeg', 295, 215, 245) ,
            ('Snipe', 'C', 'https://i.imgur.com/urx0HwQ.jpeg', 250, 265, 305) ,
            ('Shoji', 'C', 'https://i.imgur.com/lCTpZJE.jpeg', 255, 260, 305) ,
            ('Spinner', 'C', 'https://i.imgur.com/MeW1vaE.jpeg', 295, 210, 275) ,
            ('Shihai', 'C', 'https://i.imgur.com/SIaA75c.jpeg', 280, 230, 295) ,
            ('Kyoka Jiro', 'C', 'https://i.imgur.com/R8DEMdM.jpeg', 220, 255, 215) ,
            
            # Personnages D
            ("Mustard", "D", 'https://i.imgur.com/XXetteA.jpeg', 160, 130, 150),
            ("Mineta", "D", 'https://i.imgur.com/gORmmMX.jpeg', 160, 130, 150),
            ("Fuyumi Todoroki", "D", 'https://i.imgur.com/N2lcbwf.jpeg', 150, 130, 160),
            
            # Personnages E
            ("Natsuo Todoroki", "E", 'https://i.imgur.com/Z1u0j5j.jpeg', 110, 120, 115),
            ("Rei Todoroki", "E", 'https://i.imgur.com/HkXkdzC.jpeg', 105, 120, 90),

            # Personnages F
            ('Nezu', 'F', 'https://i.imgur.com/1Y3GUG5.png', 25, 10, 35) ,
            ('Eri', 'F', 'https://i.imgur.com/thiVSIU.jpeg', 20, 25, 25) ,
            ('Kenji', 'F', 'https://i.imgur.com/BGeI2LC.jpeg', 35, 35, 40) ,
            ("Recovery Girl", "F", 'https://i.imgur.com/STQibdM.png', 25, 10, 35) ,
            ('Sansa', 'F', 'https://i.imgur.com/bKASPVp.jpeg', 30, 35, 30) ,
            
            ],
            "Hunter x Hunter" : [ # ✅
            # Personnages X
            ("Meruem", "X", "https://i.imgur.com/knC0hFT.gif", 1000, 1000, 1000),
            ("Gon Freecss", "X", "https://i.imgur.com/BiklKkz.gif", 950, 1050, 950),
            ("Kuroro Lucifer", "X", 'https://i.imgur.com/3TjMAKv.gif', 950, 960, 950),
            ("Isaac Netero", "X", 'https://i.imgur.com/vtkowxL.gif', 920, 980, 950),
            ("Ging Freecss", "X", "https://i.imgur.com/VOtkd0O.gif", 900, 930, 960),
            ("Aruka Zoldyck", "X", "https://i.imgur.com/DHIbvOx.gif", 1000, 1000, 1000),

            # Personnages SS
            ("Zeno Zoldyck", "SS", "https://i.imgur.com/inIqhEg.gif", 730, 780, 740),
            ("Irumi Zoldyck", "SS", 'https://i.imgur.com/tFOQgXs.gif', 710, 720, 725),
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
            ("Uvogin", "S", 'https://i.imgur.com/WNRMtlT.gif', 540, 590, 560),
            ("Nobunaga", "S", 'https://i.imgur.com/1UMIlo3.gif', 520, 580, 520),
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
            ("Sharnalk", "A", 'https://i.imgur.com/EwSJxbs.gif', 420, 430, 400),
            ("Franklin", "A", "https://i.imgur.com/xoln4Ly.gif", 410, 420, 400),
            ("Shizuku", "A", "https://i.imgur.com/f0Yt32C.gif", 410, 415, 405),
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
            ("Ikarugo", "B", "https://i.imgur.com/P3Jc5JY.png", 300, 350, 315),
            ("Welfin", "B", "https://i.imgur.com/JfNtetM.jpeg", 345, 350, 340),
            ("Tsezugera", "B", "https://i.imgur.com/3WvsTfn.png", 320, 350, 320),
            
            # Personnages C
            ("Pokkle", "C", "https://i.imgur.com/7A9UCci.png", 240, 275, 235),
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
            ("Vezze", "D", "https://i.imgur.com/4sIsZtP.jpeg", 150, 180, 160),

            # Personnages E
            ("Tompa", "E", "https://i.imgur.com/ms2R2ki.png", 115, 105, 110),
            ("Todo", "E", "https://i.imgur.com/DAVdi3M.jpeg", 125, 100, 105),
            ("Majtani", "E", "https://i.imgur.com/DmJoWX5.jpeg", 95, 120, 115),
            ("Leluto", "E", "https://i.imgur.com/wgyMHWc.png", 110, 110, 110),
            ("Jones", "E", "https://i.imgur.com/MShzS9R.png", 120, 105, 105),
            ("Zebulo", "E", "https://i.imgur.com/nuTPuxR.png", 105, 110, 115),
            ("Ciquento", "E", "https://i.imgur.com/rfiLrO7.png", 100, 115, 115),
            ("Miruki Zoldyck", "E", "https://i.imgur.com/IcwaCHD.jpeg", 110, 110, 110),
            ("Neon Nostrad", "E", 'https://i.imgur.com/Rz5HGeZ.png', 95, 115, 120),
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

            # Personnages SS7
            ("Korra", "SS", "https://i.imgur.com/VQDla9K.gif", 750, 800, 775),
            ("Lord Ozai", "SS", "https://i.imgur.com/guyw0WL.gif", 710, 760, 705),
            ("Iroh", "SS", "https://i.imgur.com/KSigNP8.gif", 690,740,695),
            ("Azula", "SS", "https://i.imgur.com/GT1KSqZ.gif", 660, 720, 685),
            ("Zuko", "SS", "https://i.imgur.com/VLqP4QM.gif", 670, 710, 700),
            ("Katara", "SS", "https://i.imgur.com/4hOIpNj.gif", 700, 720, 725),

            # Personnage S
            ("Hama", "S", "https://i.imgur.com/zY9YU3f.jpeg", 550, 600, 555),

            # Personnages A
            ("Mai", "A", "https://i.imgur.com/opVoND8.gif", 400, 440, 410),
            ("Toph", "A", "https://i.imgur.com/Bjbn4ew.gif", 390, 430, 420),

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
            ("Satoru Gojo", "X", "https://i.imgur.com/ZRlOmKu.gif", 999, 1050, 999),
            ("Kenjaku", "X", "https://i.imgur.com/40tFQKc.gif", 910, 920, 925),

            # Personnages SS
            ("Yuta Okkotsu", "SS", "https://i.imgur.com/zG66ujn.gif", 750, 790, 785),
            ("Mahoraga", "SS", "https://i.imgur.com/X3JpLMk", 850, 850, 850),
            ("Toji Fushiguro", "SS", 'https://i.imgur.com/W479ima.png', 720, 780, 760),
            ("Aoi Todo", "SS", 'https://i.imgur.com/SpLV3Qv.png', 700, 730, 720),
            ("Suguru Geto", "SS", 'https://i.imgur.com/ZetAyjs.gif', 700, 750, 670),
            ("Choso", "SS", 'https://i.imgur.com/tPHJtTO.gif', 730, 740, 760),
            ("Mahito", "SS", 'https://i.imgur.com/a2gCQIC.gif', 650, 730, 700),
            ("Jogo", "SS", 'https://i.imgur.com/iyNljeL.gif', 700, 750, 700),
            ("Uraume", "SS", 'https://i.imgur.com/Ay1WmqD.gif', 705, 740, 700),
            ("Kinji Hakari", "SS", 'https://i.imgur.com/OSTYTVF.png', 777, 777, 777),
            ("Yuki Tsukumo", "SS", 'https://i.imgur.com/WlIBwGu.png', 700, 800, 700),
            ("Hanami","SS","https://i.imgur.com/eO8Ezjm.gif", 700, 730, 700),
            ("Dagon", "SS", 'https://i.imgur.com/Arh6UMF.gif', 700, 760, 700),

            # Personnages S
            ("Megumi Fushiguro", "S", "https://i.imgur.com/ZrNNA55.gif", 550, 610, 515),
            ("Maki Zenin", "S", 'https://i.imgur.com/zGKPJI9.png', 590, 505, 685),
            ("Nanami", "S", 'https://i.imgur.com/phtWBmN.png', 580, 610, 570),
            ("Higuruma", "S", 'https://i.imgur.com/VnEkm6V.jpeg', 550, 585, 525),
            ("Naobito Zenin", "S", 'https://i.imgur.com/FTRAhNn.png', 505, 595, 545),
            ("Miguel", "S", 'https://i.imgur.com/a8zQRsZ.png', 575, 540, 575), 
            ("Mei mei", "S", 'https://i.imgur.com/KoWiulR.png', 525, 565, 535),
            ("Naoya", "S", 'https://i.imgur.com/LiKy4we.png', 510, 590, 540),
            ("Yuji Itadori", "S", "https://i.imgur.com/75H1WqO.gif", 600, 570, 600),
            
            #Personnages A
            ("Toge Inumaki", "A", 'https://i.imgur.com/D7071yc.gif', 400, 420, 400), 
            ("Noritoshi Kamo", "A", 'https://i.pinimg.com/originals/2d/3c/53/2d3c5328dffe60e4905ec51c4c50026d.gif', 400, 450, 420),
            ("Mechamaru", "A", 'https://i.imgur.com/bjBDlk6.gif', 430, 400, 440),

            # Personnages B
            ("Panda", "B", 'https://i.imgur.com/32zGh1W.jpeg', 340, 320, 330),
            ("Nobara", "B", "https://i.imgur.com/ToHbnHv.jpeg", 320, 350, 320),
            ("Kusakabe", "B", 'https://i.imgur.com/6rujX3t.png', 320, 335, 330),
            ("Takuma Ino", "B", 'https://i.imgur.com/W3diIlg.png', 310, 360, 320),
            ("Yaga", "B", 'https://i.imgur.com/R8Rq12y.png', 330, 310, 330),
            ("Gakuganji", "B", 'https://i.imgur.com/uAnAEms.png', 310, 340, 320),
            ("Eso", "B", 'https://i.imgur.com/zdA6uXn.jpeg', 330, 320, 330),
            
            # Personnages C
            ("Mai Zenin", "C", 'https://i.imgur.com/1mbSfCf.jpeg', 240, 260, 250),
            ("Junpei", "C", 'https://i.imgur.com/7sVsWn3.png', 240, 260, 220),
            ("Momo", "C", "https://i.imgur.com/q0viuTx.png", 240, 260, 230),
            ("Utahime", "C", 'https://i.imgur.com/IPp6E9q.png', 240, 280, 260),
            ("Juzo", "C", "https://i.imgur.com/lkcQCxs.png", 250, 270, 260),
            ("Haruta Shigemo", "C", "https://i.imgur.com/IY5zel0.jpeg", 240, 255, 220),
            
            # Personnages D
            ("Kechizu", "D", "https://i.imgur.com/fwEMmNC.png", 200, 200, 175),
            ("Miwa", "D", "https://i.imgur.com/M0twNwm.png", 180, 200, 165),

            # Personnages E
            ("Ijichi", "E", "https://i.imgur.com/6EKKkX3.jpeg", 110, 120, 125),
            ("Yu Haibara", "E", "https://i.imgur.com/Ab850TD.jpeg", 120, 110, 130),
            ("Arata Nitta", "E", "https://i.imgur.com/1Z2Z2Zv.jpeg", 120, 80, 130),
            # Personnages F
            ("Akari Nitta", "F", "https://i.imgur.com/1Z2Z2Zv.jpeg", 35, 50, 50),
            ("Riko Amanai", "F", "https://i.imgur.com/WkfCzwy.jpeg", 20, 15, 20),
            ("Tsumiki Fushiguro", "F", "https://i.imgur.com/wNU5qjd.png", 15, 30, 30),          
            ],
            "Jojo's Bizarre Adventure" : [ # ✅
            # Personnages X
            ("Giorno Giovanna", "X", 'https://i.imgur.com/iJ9oUE1.gif', 900, 1200, 950),
            ("Enrico Pucci", "X", 'https://i.imgur.com/lAyHni9.gif', 950, 1200, 900),
            ("Funny Valentine", "X", "https://i.imgur.com/4ugvBxu.jpeg", 950, 1050, 950),
            ("Johnny", "X", "https://i.imgur.com/cgLbkoE.gif", 950, 1100, 900),

            # Personnages SS
            ("Gyro Zeppeli", "SS", "https://i.imgur.com/qDnzVD7.gif", 700, 750, 700),
            ("Kars", "SS", 'https://i.imgur.com/4xhIuVK.gif', 850, 850, 850),
            ("Diavolo", "SS", 'https://i.imgur.com/90RxqGR.gif', 750, 850, 700),
            ("Jotaro Kujo", "SS", 'https://i.imgur.com/XzBAKKf.gif', 750, 800, 750),
            ("Diego Brando", "SS", "https://i.imgur.com/Ncp5cvE.jpeg", 740, 800, 730), #TOREVIEW
            ("Dio Brando", "SS", 'https://i.imgur.com/xngzKOg.gif', 800, 850, 750),
            ("Kira Yoshikage", "SS", 'https://i.imgur.com/ZQPBO3Q.gif', 700, 800, 700),

            # Personnages S
            ("Josuke Higashikata", "S", 'https://i.imgur.com/AcnhlnJ.gif', 550, 580, 550), #TOREVIEW
            ("Fugo (Purple Haze)", "S", 'https://i.imgur.com/gBcvGNj.gif', 550, 600, 550), #TOREVIEW
            ("Vanilla Ice", "S", "https://i.imgur.com/VoH5XBm.gif", 550, 570, 550),#TOREVIEW
            ("Jolyne Kujo", "S", 'https://i.imgur.com/T2yg742.gif', 500, 550, 550),
            ("Weather Report", "S", "https://i.imgur.com/zHlZilS.gif", 550, 550, 550),

            # Personnages A
            ("Anasui", "A", "https://i.imgur.com/cQtCTf7.gif", 400, 450, 440),
            ("Bucciarati", "A", 'https://i.imgur.com/zaBAVFx.gif', 450, 470, 430),
            ("Risotto", "A", 'https://i.imgur.com/hQxmpqR.gif', 440, 480, 400),
            ("Rohan", "A", 'https://i.imgur.com/UJgfmGg.gif', 410, 440, 430),
            ("Kakyoin", "A", 'https://i.imgur.com/ZsxN3PG.gif', 440, 420, 400),
            ("Polnareff", "A", 'https://i.imgur.com/eZjHHa9.gif', 430, 450, 410),
            ("Okuyasu", "A", 'https://i.imgur.com/BiveNFJ.gif', 430, 450, 410),
            ("Ghiaccio", "A", 'https://i.imgur.com/LNoxXyi.gif', 440, 420, 400),
            ("Prosciutto", "A", 'https://i.imgur.com/CsSR05A.gif', 410, 420, 430),
            ("Mohamed Abdul", "A", "https://i.imgur.com/2fIG9TF.gif", 430, 420, 410),
            ("Illuso", "A", "https://i.imgur.com/4oeiAEJ.gif", 400, 420, 440),
            ("Cioccolata", "A", 'https://i.imgur.com/XAu2MDR.gif', 420, 400, 420),

            # Personnages B
            ("Koichi", "B", 'https://i.imgur.com/HZ9vn1d.png', 350, 360, 310),
            ("Emporio", "B", 'https://i.imgur.com/KBZCTy6.png', 320, 340, 310),
            ("Akira Otoishi", "B", 'https://i.imgur.com/xn6pX9Z.png', 290, 370, 330),
            ("Narancia", "B", 'https://i.imgur.com/ndZcfok.png', 310, 350, 310),
            ("Yukako", "B", 'https://i.imgur.com/JZKQ2KS.png', 340, 330, 310),
            ("Miyamoto", "B", 'https://i.imgur.com/lZLlEhu.png', 310, 330, 320),
            ("Wamuu", "B", 'https://i.imgur.com/2Jc0FTu.png', 330, 320, 350),
            ("Esidisi", "B", 'https://i.imgur.com/mdsI4Ir.png', 360, 320, 320),
            ("Pesci", "B", 'https://i.imgur.com/RiqetYG.png', 320, 320, 310),
            ("Melone", "B", 'https://i.imgur.com/EMitGnp.png', 310, 320, 330),
            ("Squalo", "B", 'https://i.imgur.com/1DP3U16.png', 310, 340, 330),
            ("Mista", "B", 'https://i.imgur.com/ab9sgfg.png', 340, 360, 320),

            # Personnages C
            ("Joseph Joestar", "C", 'https://i.imgur.com/YiGGszt.png', 240, 265, 265),
            ("N'Doul", "C", 'https://i.imgur.com/Jn3ZtDS.jpeg', 250, 270, 260),
            ("Caesar Zeppeli", "C", 'https://i.imgur.com/3nzbH8Y.png', 250, 270, 260),
            ("Lisa Lisa", "C", 'https://i.imgur.com/YAcAs5c.jpeg', 260, 260, 250),
            ("Shigechi", "C", 'https://i.imgur.com/6JKniYe.png', 240, 230, 220),
            ("Mikitaka", "C", 'https://i.imgur.com/mMs5O78.png', 270, 240, 230),
            ("Iggy", "C", 'https://i.imgur.com/HTb59id.png', 250, 260, 220),
            ("Formaggio", "C", 'https://i.imgur.com/WCQtqwq.png', 260, 270, 220),
            ("Stroheim", "C", 'https://i.imgur.com/OvyOZy3.png', 280, 230, 240),
            ("Foo Fighters", "C", 'https://i.imgur.com/ZlCOCPn.png', 270, 240, 250),
            ("Trish", "C", 'https://i.imgur.com/I4nMHqt.png', 250, 270, 260),
            ("Hermes Costello", "C", 'https://i.imgur.com/TbkuZDj.jpeg', 290, 250, 240),
            ("Polpo", "C", 'https://i.imgur.com/2xxnmT8.jpeg', 260, 270, 250),

            # Personnages D
            ("Abbacchio", "D", 'https://i.imgur.com/5FahNJl.png', 200, 180, 170),
            ("Daniel Darby", "D", 'https://i.imgur.com/w1Qu1p2.jpeg', 160, 170, 180),
            ("Jonathan Joestar", "D", 'https://i.imgur.com/dqGKC1P.png', 220, 200, 160),

            # Personnages E
            ("Straizo", "E", 'https://i.imgur.com/D4muQp5.png', 100, 130, 110),
            ("Will Zeppeli", "E", 'https://i.imgur.com/SVm9I2K.png', 120, 130, 110),
            ("Boingo", "E", 'https://i.imgur.com/I1GDLQ9.jpeg', 100, 120, 130),
            ("Oingo", "E", 'https://i.imgur.com/4t8W7rq.jpeg', 140, 130, 120),

            # Personnages F
            ("Tonio", "F", 'https://i.imgur.com/PIXbcZb.png', 40, 60, 50),
            ("Luca", "F", 'https://i.imgur.com/3HamVjM.png', 40, 60, 50),
            ("Anne", "F", 'https://i.imgur.com/AkQ1PV2.jpeg', 70, 40, 50),
            ("Speedwagon", "F", 'https://i.imgur.com/Q4pR4ws.png', 50, 60, 70),
            ("Poco", "F", 'https://i.imgur.com/qeYo0He.png', 50, 60, 30),
            ("Dario Brando", "F", "https://i.imgur.com/LjMHPwB.png", 60, 40, 20),
            ("Tama", "F", 'https://i.imgur.com/1cQyIW5.jpeg', 70, 30, 50),
            ("Holy Kujo", "F", 'https://i.imgur.com/CcyZwcf.jpeg', 20, 15, 30),
            ],
            "One Punch Man" : [
            # Personnages X
            ("Saitama", "X", "https://steamuserimages-a.akamaihd.net/ugc/945077695993694686/15A47D5D02A75DB7700CBBC61706AB3CFD8FEEE2/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", 0, 0, 0),
            ("Garou", "X", "https://i.pinimg.com/originals/a2/21/f2/a221f289576e45a0ed2fc3a5f6cb311e.gif", 0, 0, 0),
            ("Boros", "X", "https://i.imgur.com/ehpRyuO.gif", 0, 0, 0),
            
            # Personnages SS
            ("Watchdog Man", "SS", "https://wallpapercave.com/wp/wp8404550.jpg", 0, 0, 0), #TOREVIEW
            ("Tatsumaki", "SS", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0a290752-d7eb-45e3-aa31-8e71b544cde0/ddx9bq9-b00980a3-8482-4791-bf64-f558046bb68f.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBhMjkwNzUyLWQ3ZWItNDVlMy1hYTMxLThlNzFiNTQ0Y2RlMFwvZGR4OWJxOS1iMDA5ODBhMy04NDgyLTQ3OTEtYmY2NC1mNTU4MDQ2YmI2OGYuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.tQyMqurmzcRYBak3ZNXQli2kTvbsZen9MPklCMs4dsw", 0, 0, 0),
            #("Blast", "SS", image_temporaire, 0, 0, 0),
            ("King (OPM)", "S", "https://64.media.tumblr.com/bfa88447c156e886f4499efd2e85a436/tumblr_o7une2LCul1t11lc1o3_r2_500.gif", 0, 0, 0),

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
            ("Cyborgorilla", "D", "https://i.ytimg.com/vi/HJAt5DujlIw/maxresdefault.jpg", 180, 180, 180),

            # Personnages E
            ("Grimasse", "E", "https://static.wikia.nocookie.net/onepunchman/images/a/a4/Saitama_flippe_devant_Grimasse.png/revision/latest?cb=20190501171126&path-prefix=fr", 120, 120, 120),
            ("Crablante", "E", "https://static.wikia.nocookie.net/villains/images/a/a5/Crabrante.jpg/revision/latest?cb=20151214015216", 120, 120, 120),

            # Personnages F
            ("Mumen Rider", "F", "https://i.redd.it/diszh9zoizoa1.jpg", 50, 50, 50),
            ],
            "Demon Slayer" : [ # ✅ Ⓜ️
            # Personnages X
            ("Tanjiro Kamado", "X", "https://i.imgur.com/0ZbB8tr.gif", 950, 970, 930),
            ("Muzan", "X", "https://i.imgur.com/zXvC5Uj.gif", 940, 950, 930),
            ("Yoriichi Tsugikuni", "X", "https://i.imgur.com/q7ak3HD.gif", 950, 980, 950),
            ("Kokushibo", "X", "https://i.imgur.com/LZJio0L.gif", 940, 950, 950),

            # Personnages SS
            ('Gyomei', 'SS', 'https://i.imgur.com/lk7V07x.gif', 725, 655, 675) ,
            ('Doma', 'SS', 'https://i.imgur.com/ypkjkIk.gif', 695, 670, 740) ,
            ('Akaza', 'SS', 'https://i.imgur.com/uBwhGcG.gif', 710, 670, 665) ,

            # Personnages S
            ('Sanemi', 'S', image_temporaire, 535, 570, 540) ,
            ('Muichiro', 'S', image_temporaire, 530, 585, 550) ,
            ('Obanai', 'S', image_temporaire, 585, 570, 525) ,
            ('Giyu', 'S', image_temporaire, 540, 595, 510) ,

            # Personnages A
            ('Rengoku', 'A', 'https://i.imgur.com/6HL02sP.gif', 425, 390, 465) ,
            ('Uzui Tengen', 'A', image_temporaire, 410, 385, 440) ,
            ('Mitsuri', 'A', image_temporaire, 410, 405, 445) ,
            ('Nezuko', 'A', image_temporaire, 420, 375, 470) ,
            ('Kanao', 'A', image_temporaire, 460, 410, 430) ,
            ('Tamayo', 'A', 'https://i.imgur.com/GVvrYyr.gif', 430, 430, 380) ,
            ('Shinobu Kocho', 'A', 'https://i.imgur.com/TK1yera.gif', 450, 420, 460) ,

            # Personnages B
            ("Sumiyoshi", "B", 'https://i.imgur.com/vpx7b2g.jpeg', 355, 330, 345),
            ('Zenitsu', 'B', 'https://i.imgur.com/1hxD21J.jpeg', 355, 330, 345) ,
            ('Sakonji Urokodaki', 'B', 'https://i.imgur.com/DPD6gfY.jpeg', 355, 330, 345) ,
            ('Inosuke', 'B', 'https://i.imgur.com/h1Ek7Aa.jpeg', 300, 330, 315) ,
            ('Kaigaku', 'B', 'https://i.imgur.com/QmDeP6I.jpeg', 300, 380, 350) ,
            ('Genya', 'B', 'https://i.imgur.com/kE7DIxE.jpeg', 375, 305, 340) ,
            ('Daki', 'B', 'https://i.imgur.com/dNUE89G.jpeg', 380, 310, 305) ,
            ('Enmu', 'B', 'https://i.imgur.com/Ey0jwGH.jpeg', 330, 370, 305) ,

            # Personnages C
            ("Sabito", "C", 'https://i.imgur.com/YpzmuoS.jpeg', 255, 285, 265),
            ('Rui', 'C', 'https://i.imgur.com/bFzI5bu.jpeg', 220, 290, 250) ,
            ('Mukago', 'C', 'https://i.imgur.com/EH3xfU2.png', 220, 225, 285) ,
            ('Fille Araignee', 'C', 'https://i.imgur.com/8ExcM9G.jpeg', 255, 285, 265) ,
            ('Mere Araignee', 'C', 'https://i.imgur.com/ag5zn5R.png', 245, 225, 275) ,
            ('Susamaru', 'C', 'https://i.imgur.com/jtutEcc.png', 235, 235, 220) ,
            ('Jigoro', 'C', 'https://i.imgur.com/kijkJU1.jpeg', 300, 230, 245) ,

            # Personnages D
            ("Tanjuro", "D", 'https://i.imgur.com/ksFH87B.jpeg', 170, 180, 150),
            ("Ozaki", "D", 'https://i.imgur.com/z8e44Fl.jpeg', 160, 190, 140),

            # Personnages E
            ('Shinzu', 'E', 'https://i.imgur.com/OM3Yn5j.jpeg', 145, 100, 90) ,
            ('Murata', 'E', 'https://i.imgur.com/lNC5rbm.jpeg', 145, 140, 105) ,
            ('Kyogai', 'E', 'https://i.imgur.com/7VFZLBx.jpeg', 145, 115, 95) ,
            ('Kanamue', 'E', 'https://i.imgur.com/WYQmh9H.jpeg', 100, 115, 100) ,
            ('Kagaya Ubuyashiki', 'E', 'https://i.imgur.com/96vapZl.jpeg', 120, 150, 105) ,

            # Personnages F
            ('Kiriya Ubuyashiki', 'F', 'https://i.imgur.com/TSP73o7.jpeg', 55, 50, 25) ,
            ('Nichika Ubuyashiki', 'F', 'https://i.imgur.com/von4C2M.png', 50, 30, 40) ,
            ('Chachamaru', 'F', 'https://i.imgur.com/F5RzFaL.png', 35, 60, 45) ,
            ('Aoi Kanzaki', 'F', 'https://i.imgur.com/QWv5qQG.jpeg', 30, 20, 20) ,
            ('Sumi Nakahara', 'F', 'https://i.imgur.com/WcLXKs0.gif', 20, 40, 50) ,
            ('Kiyo', 'F', 'https://i.imgur.com/l9MjiEs.jpeg', 45, 25, 30) ,
            ('Naho', 'F', 'https://i.imgur.com/LyTz20q.gif', 60, 30, 60) ,
            ('Goto', 'F', 'https://i.imgur.com/3cYKi06.jpeg', 30, 20, 30) ,
            ('Kaburamaru', 'F', 'https://i.imgur.com/ZtQxLvw.jpeg', 60, 20, 40) ,
            ],
            "Full Metal Alchemist" : [ # ✅
            # Personnages X
            ("Pere", "X", "https://i.imgur.com/X617w07.gif", 963, 963, 963),

            # Personnages SS
            ("Hohenheim", "SS", "https://i.imgur.com/bMNh7n0.gif", 720, 730, 735),
            ("King Bradley", "SS", "https://i.imgur.com/Di7mjqq.gif", 750, 770, 750),

            # Personnages S
            ("Edward Elric", "S", "https://i.imgur.com/Lmbb9ZT.gif", 540, 555, 530),
            ("Izumi Curtis", "S", "https://i.imgur.com/WBcqtWl.gif", 535, 540, 530),
            ("Alphonse Elric", "S", 'https://i.imgur.com/q6IW5xU.gif', 560, 570, 600),
            ("Roy Mustang", "S", 'https://i.imgur.com/Oyk2Pp4.gif', 550, 700, 540), # high S
            ("Scar", "S", 'https://i.imgur.com/9dw5ri9.gif', 580, 600, 790), # high S
            ("Solf J. Kimblee", "S", 'https://i.imgur.com/r9nB7SF.gif', 530, 555, 535),
            ("Selim Bradley", "S", 'https://i.imgur.com/XYj2ZtU.gif', 545, 560, 540),
            ("Ling Yao", "S", 'https://i.imgur.com/cEoziXY.gif', 420, 430, 410),

            # Personnages A
            ("Isaac McDougal", "A", 'https://i.imgur.com/CGtaVQj.gif', 400, 420, 440),
            ("Envy", "A", 'https://i.imgur.com/rRFT3ec.gif', 440, 430, 420),
            ("Sloth", "A", 'https://i.imgur.com/sltbpFK.gif', 450, 430, 410),
            ("Glutonny", "A", "https://i.imgur.com/16YlN6x.gif", 430, 420, 440),
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
            ("Tim Marcoh", "C", 'https://i.imgur.com/6hbihPy.png', 260, 255, 265),
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
            ("Kain Fuery", "E", "https://i.imgur.com/6dCkq7z.jpeg", 120, 120, 120),

            # Personnages F
            ("Yoki", "F", 'https://i.imgur.com/pPbOaqJ.jpeg', 35, 50, 35),
            ("Nina Tucker", "F", 'https://i.imgur.com/gOeHUXg.jpeg', 50, 45, 35),
            ("Trisha Elric", "F", 'https://i.imgur.com/QVYbkRB.jpeg', 35, 50, 35),
            ("Xiao Mei", "F", 'https://i.imgur.com/FAQHPlD.gif', 30, 55, 35),
            ("Winry", "F", 'https://i.imgur.com/mbX301B.jpeg', 35, 55, 30),
            ],
            "Attack On Titan" : [ # ✅
            # """ PERSONNAGES SNK """
            # Personnages X
            ("Eren Yeager", "X", "https://i.imgur.com/izA5HAI.gif", 960, 950, 945),

            # Personnages SS
            ("Armin Arlert", "SS", "https://i.imgur.com/CFmYNyt.gif", 750, 655, 750),
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
            ("Falco Grice", "A", "https://i.imgur.com/KYUnpQb.gif", 420, 390, 430),
            ("Kenny Ackerman", "A", "https://i.imgur.com/QQwRAlM.gif", 380, 500, 385),
            ("Porco Galliard", "A", "https://i.imgur.com/b78cQir.gif", 410, 430, 420),
            ("Erwin Smith", "A", "https://i.imgur.com/0WfIayb.gif", 330, 360, 390),

            # Personnages B
            ("Mike Zacharias", "B", "https://i.imgur.com/CdhigbE.png", 300, 400, 300),
            ("Frieda Reiss", "B", "https://i.imgur.com/CScADUO.png", 290, 340, 300),
            ("Jean Kirstein", "B", "https://i.imgur.com/7erh7rA.png", 310, 320, 280),
            ("Hange Zoe", "B", "https://i.imgur.com/IiSqnok.png", 300, 320, 310),
            ("Rhodes Reiss", "B", "https://i.imgur.com/fzsHl7c.png", 500, 200, 400),

            # Personnages C
            ("Hannes", "C", "https://i.imgur.com/XtZvC0L.jpeg", 280, 330, 290),
            ("Historia Reiss", "C", "https://i.imgur.com/u6tCLmq.jpeg",230, 245, 230),
            ("Floch", "C", "https://i.imgur.com/K79IX3o.jpeg", 240, 250, 220 ),
            ("Pixis", "C", "https://i.imgur.com/Vx416zK.png", 220, 210, 210),
            ("Sasha Braus", "C", "https://i.imgur.com/XHs9rWi.png", 230, 260, 230),
            ("Conny Springer", "C", "https://i.imgur.com/7MNFSc1.jpeg", 220, 240, 230),
            
            # Personnages D
            ("Gabi Braun", "D", "https://i.imgur.com/iBw8k6t.png", 160, 180, 140),
            ("Udo", "D", "https://i.imgur.com/p1NWLXE.png", 140, 160, 120),
            ("Zofia", "D", "https://i.imgur.com/99zdhK5.png", 145, 165, 125),

            # Personnages E
            ("Theo Magath", "E", "https://i.imgur.com/0cq6zdB.png", 100, 110, 100),
            ("Yelena", "E", "https://i.imgur.com/9LfUJq0.png", 90, 120, 90),

            # Personnages F
            ("Carla Yeager", "F", "https://i.imgur.com/Z5dDpTT.jpeg", 20, 35, 30),
            ("Willy", "F", "https://i.imgur.com/M8eXW0o.jpeg", 40, 50, 40),
            ("Onyankopon", "F", "https://i.imgur.com/wylRQBl.jpeg", 50, 50, 50),
            ("Nicolo", "F", "https://i.imgur.com/cXQk7KZ.jpeg", 40, 45, 45)
            ],
            "Seven Deadly Sins" : [
            # """ PERSONNAGES NNT """
            # Personnages X
            ("Meliodas", "X", "https://i.imgur.com/raYGlJ7.gif", 940, 950, 920),
            ("Arthur Pendragon", "X", "https://i.imgur.com/0hVVugw.gif", 950, 970, 990),

            # Personnages SS
            ("Ban", "SS", "https://i.imgur.com/qJYVTXT.gif", 690, 720, 700),
            ("Estarossa", "SS", "https://i.imgur.com/eXY3zUp.gif", 710, 720, 710),
            ("Escanor", "SS", "https://i.imgur.com/PVS7bUU.gif", 750, 770, 720),
            ("Zeldris", "SS", "https://i.imgur.com/qsRrdsM.gif  ", 710, 720, 690),
            ("King (NNT)", "SS", "https://i.imgur.com/TvSBMxY.jpeg", 720, 730, 710),
            ("Merlin", "SS", "https://i.imgur.com/2JIsj8m.gif", 705, 720, 710),
            ("Gowther", "SS", "https://i.imgur.com/uQlBrOy.gif", 720, 710, 700),
            ("Diane", "SS", "https://i.imgur.com/bVlSky7.gif", 750, 705, 730),

            # Personnages S
            ("Derrierie", "S", "https://i.imgur.com/Led5JQO.gif", 540, 550, 530),
            ("Gloxinia", "S", "https://i.imgur.com/IIR8AnU.gif", 520, 510, 540),

            # Personnages A
            ("Hendrickson", "A", "https://i.imgur.com/t3Xw4zr.gif", 420, 430, 425),

            # Personnages B
            ("Gilthunder", "B", "https://i.imgur.com/GUDkN6I.jpeg", 330, 320, 315),

            # Personnage F
            ("Hawk", "F", "https://i.imgur.com/SNsqYD3.jpeg", 40, 55, 50),
            ],
            "Chainsaw Man" : [ # ✅
            # Personnages X
            ("Denji", "X", "https://i.imgur.com/YnDFcsy.gif", 940, 960, 945),
            ("Makima", "X", "https://i.imgur.com/UCcRxPY.gif", 910, 950, 920),

            # Personnages SS
            ("Kishibe", "SS", "https://i.imgur.com/woFsMsu.gif", 720, 730, 715),

            # Personnages S  
            ("Aki Hanakawa", "S", "https://i.imgur.com/bnGI6vv.gif", 510, 570, 540),
            ("Himeno", "S", "https://i.imgur.com/qyBRHdk.gif", 520, 540, 530),
            ("Angel", "S", "https://i.imgur.com/rtJFtA9.gif", 530, 560, 555),
            ("Samourai Sword", "S", "https://i.imgur.com/8Bj3B08.gif", 565, 580, 575),
            ("Akane Sawatari", "S", "https://i.imgur.com/mbr0WZ8.gif", 540, 565, 545),
                
            # Personnages A
            ("Power", "A", "https://i.imgur.com/WzSAOuy.gif", 410, 430, 425),

            # Personnages B
            ("Kobeni Higashiyama", "B", "https://i.imgur.com/yB3UtcT.jpeg", 330, 320, 315),
            ("Beam", "B", "https://i.imgur.com/LmkjMXS.png", 340, 320, 315),
            ("Galgali", "B", "https://i.imgur.com/hzsrj4W.png", 330, 340, 310),

            # Personnages C
            ("Michiko Tendo", "C", "https://i.imgur.com/vsE0OlY.png", 240, 250, 255),
            ("Yutaro Kurose", "C", "https://i.imgur.com/Ks0x4qp.png", 255, 250, 240),

            # Personnages F
            ("Hirokazu Arai", "F", "https://i.imgur.com/74g6mPD.png", 40, 55, 50),
            ],
        "Saint Seiya" : [ # ✅
            # Personnages X
            ("Athena", "X", "https://i.imgur.com/Mhn9qP8.gif", 1000, 1000, 1000),

            # Personnages SS
            ("Shaka", "SS", "https://i.imgur.com/tkAVOuQ.gif", 700, 720, 700),
            ],
        "Autre" : [ # ✅
            ("Moshi", "C", "https://i.imgur.com/OUyDLg1.jpeg", 213, 213, 213),
        ],
}

all_synergies = [
    (1, "Akatsuki", "ATK", 0.55,"L'akatsuki est une organisation criminelle de ninjas déserteurs.", 'https://static.wikia.nocookie.net/naruto/images/6/61/Membres_Akatsuki.png/revision/latest/scale-to-width-down/1200?cb=20130511192621&path-prefix=fr', "#FF0000"),
    (2, "Saiyan", "ATK", 0.40, "Les Saiyans sont connus pour leur force et leur capacité à se transformer en Super Saiyan.", image_temporaire, "#FFA500"),
    (3, "Hollow", "ATK", 0.25, "Les Hollows sont des âmes corrompues qui ont perdu leur coeur et leur raison.", image_temporaire, "#0000FF"),
    (4, "Mugiwara", "HP", 0.45, "Les Mugiwara sont l'équipage de Monkey D. Luffy, un pirate qui cherche le One Piece.", 'https://steamuserimages-a.akamaihd.net/ugc/481145984302804192/29529359BC636378F426946B2D859F7EB46561BB/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false', "#800080"),
    (5, "Uchiha", "ATK", 0.30, "Le clan Uchiha est connu pour ses capacites de combat et son Sharingan.", 'https://cherry.img.pmdstatic.net/fit/https.3A.2F.2Fimg.2Egaming.2Egentside.2Ecom.2Fs3.2Ffrgsg.2F1280.2Fmanga.2Fdefault_2022-12-21_5b4dbf77-0203-48b1-bfff-103263f3bc90.2Epng/1200x675/quality/80/clan-uchiwa.jpg', "#FF0000"),
    (6, "Quincy", "ATK", 0.35, "Les Quincy sont des chasseurs de Hollows qui utilisent des arcs pour combattre.", 'https://static1.srcdn.com/wordpress/wp-content/uploads/2022/10/Bleach-Quincy-featured.jpg', "#FFA500"), #TOREVIEW 
    (7, "Amiral", "ATK", 0.75, "Les Amiraux sont les trois plus puissants marins de la Marine.", 'https://steamuserimages-a.akamaihd.net/ugc/914674978440099035/39C53679BC6727A9D6074B90BCD0C9BC72D1DEDD/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false', "#0000FF"), #TOREVIEW
    (8, "Espada", "ATK", 0.55, "Les Espadas sont les dix plus puissants Hollows sous les ordres d'Sosuke Aizen.", 'https://i.redd.it/d2umjaymimsa1.jpg', "#800080"),
    (9, "Vongola", "ATK", 0.15, "La famille Vongola est une organisation mafieuse italienne qui utilise des anneaux pour combattre.", 'https://images2.wikia.nocookie.net/__cb20100422034551/reborn/images/e/e8/Tsuna_And_The_Guardians.PNG', "#FF0000"),
    (10, "Yonko", "ATK", 0.55, "Les Yonkos sont les quatre plus puissants pirates du Nouveau Monde.", 'https://www.univers-otaku.com/wp-content/uploads/2021/03/one-piece-Yonko.jpg', "#FFA500"),
    (11, "Akimichi", "ATK", 0.15, "Le clan Akimichi est connu pour sa technique de transformation en geant.", 'https://staticg.sportskeeda.com/editor/2022/06/d5daf-16559000633224.png', "#0000FF"), #TOREVIEW 
    (12, "Vizard", "ATK", 0.15, "Les Vizards sont des Shinigamis qui ont acquis des pouvoirs de Hollows.", 'https://i.pinimg.com/originals/b9/54/72/b95472a06de8ce83188fa0c2723c05cc.gif', "#800080"),
    (13, "Varia", "ATK", 0.15, "La Varia est un groupe d'assassins de la famille Vongola.", 'https://static.wikia.nocookie.net/reborn/images/5/5c/Past_Varia.PNG/revision/latest?cb=20111107024622', "#FF0000"),
    (14, "Gotei 13", "ATK", 0.65, "Le Gotei 13 est une organisation de Shinigamis qui protège le monde des âmes.", 'https://i.redd.it/myfksl030a991.gif', "#FFA500"),
    (15, "Kage", "ATK", 0.50, "Les Kages sont les plus puissants ninjas de leur village.", image_temporaire, "#0000FF"),
    (16, "Shichibukai", "ATK", 0.55, "Les Shichibukai sont des pirates qui ont accepté de servir la Marine.", 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/04/Featured-Image-Shichibukai-Cropped.jpg', "#800080"),
    (17, "Sannin", "HP", 0.75, "Les Sannins sont les trois ninjas légendaires de Konoha.", 'https://64.media.tumblr.com/0d74a734f45f35a984288446fee484a4/tumblr_omf0oel6qW1rqe0rbo3_540.gifv', "#FF0000"),
    (18, "Revolutionnaires", "ATK", 0.50, "Les Révolutionnaires sont un groupe qui lutte contre le Gouvernement Mondial.", image_temporaire, "#FFA500"),
    (19, "Volonté du D", "ATK", 0.50, "La Volonté du D est une mystérieuse lignee de pirates qui défient le Gouvernement Mondial.", image_temporaire, "#0000FF"),
    (20, "Animal", "ATK", 0.38, "Les Animaux sont des créatures qui possèdent des pouvoirs spéciaux.", image_temporaire, "#800080"),
    (21, "Taka", "ATK", 0.50, "La Taka est un groupe de ninjas qui a été formé par Sasuke Uchiha.", 'https://i.pinimg.com/originals/d0/14/1c/d0141c035bd6a5a3956e5b8161bda71c.gif', "#FF0000"),
    (22, "Rinnegan", "ATK", 0.40, "Le Rinnegan est le dōjutsu le plus puissant de l'univers Naruto.", 'https://editors.dexerto.fr/wp-content/uploads/sites/2/2023/05/23/naruto-rinnegan.jpg', "#FFA500"),
    (23, "Konoha", "HP", 0.15, "Konoha est le village caché de la Feuille, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (24, "Suna", "HP", 0.15, "Suna est le village caché du Sable, l'un des cinq grands villages ninjas.", image_temporaire, "#800080"),
    (25, "Kiri", "HP", 0.15, "Kiri est le village caché de la Brume, l'un des cinq grands villages ninjas.", image_temporaire, "#FF0000"),
    (26, "Kumo", "HP", 0.15, "Kumo est le village caché des Nuages, l'un des cinq grands villages ninjas.", image_temporaire, "#FFA500"),
    (27, "Iwa", "HP", 0.15, "Iwa est le village caché de la Roche, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (28, "Receptacle", "ATK", 0.40, "Les Receptacles sont des personnes qui ont un Monstre scellé en eux.", image_temporaire, "#800080"),
    (29, "Maitre du Feu", "ATK", 0.25, "Les Maîtres du Feu sont des personnages qui maîtrisent le feu.", image_temporaire, "#FFA500"),
    (30, "Maitre de l'Eau", "ATK", 0.25, "Les Maîtres de l'Eau sont des personnages qui maîtrisent l'eau.", image_temporaire, "#0000FF"),
    (31, "Maitre de la Terre", "ATK", 0.25, "Les Maîtres de la Terre sont des personnages qui maîtrisent la terre.", image_temporaire, "#800080"),
    (32, "Maitre de l'Air", "ATK", 0.25, "Les Maîtres de l'Air sont des personnages qui maîtrisent l'air.", image_temporaire, "#FF0000"),
    (33, "Maitre de la Foudre", "ATK", 0.35, "Les Maîtres de la Foudre sont des personnages qui maîtrisent l'éclair.", image_temporaire, "#FFA500"),
    (34, "Maitre de la Glace", "ATK", 0.35, "Les Maîtres de la Glace sont des personnages qui maîtrisent la glace.", image_temporaire, "#0000FF"),
    (36, "Maitre de la Lave", "ATK", 0.45, "Les Maîtres de la Lave sont des personnages qui maîtrisent la lave.", image_temporaire, "#FF0000"),
    (37, "Maitre du Bois", "ATK", 0.50, "Les Maîtres du Bois sont des personnages qui maîtrisent le bois.", image_temporaire, "#FFA500"),
    (38, "Maitre du Vent", "ATK", 0.50, "Les Maîtres du Vent sont des personnages qui maîtrisent le vent.", image_temporaire, "#0000FF"),
    (39, "Maitre du Sable", "ATK", 0.50, "Les Maîtres du Sable sont des personnages qui maîtrisent le sable.", image_temporaire, "#800080"),
    (40, "Epeiste", "ATK", 0.15, "Les épeistes sont des combattants qui utilisent une épée pour se battre.", image_temporaire, "#FF0000"),
    (41, "Telekinesiste", "ATK", 0.40, "Les Télékinésistes sont des personnes qui peuvent déplacer des objets par la pensée ou ont des pouvoirs psychiques.", image_temporaire, "#FFA500"),
    (42, "Equipage de Barbe Noire", "ATK", 0.40, "L'équipage de Barbe Noire est un groupe de pirates dirigé par Barbe Noire.", image_temporaire, "#0000FF"),
    (43, "Equipage de Barbe Blanche", "ATK", 0.40, "L'équipage de Barbe Blanche est un groupe de pirates dirigé par Barbe Blanche.", image_temporaire, "#800080"),
    (44, "Uzumaki", "ATK", 0.40, "Le clan Uzumaki est connu pour sa longevité et ses capacités de guerison.", 'https://static1.srcdn.com/wordpress/wp-content/uploads/2022/03/Uzumaki-Clan.jpg', "#FF0000"),
    (45, "Hyuga", "ATK", 0.40, "Le clan Hyuga est connu pour son Byakugan et ses techniques de combat douces.", image_temporaire, "#FFA500"),
    (46, "Senju", "DEF", 0.55, "Le clan Senju est connu pour son Mokuton et sa capacité à maîtriser les Bijuus.", image_temporaire, "#0000FF"),
    (47, "Otsutsuki", "ATK", 0.35, "Le clan Otsutsuki est une famille de ninjas extraterrestres qui cherchent à absorber des planètes pour obtenir du chakra.", image_temporaire, "#800080"),
    (48, "Insecte", "DEF", 0.25, "Les Insectes sont des créatures qui possèdent des pouvoirs spéciaux.", image_temporaire, "#FF0000"),
    (49, "Garde Royale", "DEF", 0.55, "La Garde Royale est un groupe qui s'assure de la sécurité du roi.", image_temporaire, "#FFA500"),
    (50, "Zeppeli", "ATK", 0.40, "Les Zeppelis sont une famille de maîtres de l'Onde qui combattent les vampires.", image_temporaire, "#0000FF"),
    (52, "Homme du pillier", "HP", 0.6, "Les Pillars sont des guerriers qui servent les vampires et protègent la pierre rouge de l'Aja.", image_temporaire, "#FF0000"),
    (53, "Maitre du Temps", "HP", 0.5, "Les Maîtres du Temps sont des personnages qui peuvent contrôler le temps.", image_temporaire, "#FFA500"),
    (54, "Maitre de l'Explosion", "ATK", 0.5, "Les Maîtres de l'Explosion sont des personnages qui peuvent créer des explosions.", image_temporaire, "#0000FF"),
    (55, "Squadra Esecuzioni", "ATK", 0.35, "La Squadra Esecuzioni est un groupe de tueurs à gages qui travaillent pour la Passione.", image_temporaire, "#0000FF"),
    (56, "Hamon", "ATK", 0.4, "Le Hamon est une technique de combat qui utilise l'énergie du soleil pour attaquer les vampires.", image_temporaire, "#800080"),
    (57, "Mafioso", "ATK", 0.3, "La Passione est une organisation criminelle italienne qui contrôle le trafic de drogue.", image_temporaire, "#FF0000"),
    (58, "Team Bucciarati", "ATK", 0.3, "La Team Bucciarati est un groupe de gangsters qui travaillent pour la Passione.", image_temporaire, "#FFA500"),
    (59, "JoBros", "HP", 0.4, "Les JoBros sont les amis et allies des Joestars qui les aident dans leur combat contre le mal.", image_temporaire, "#0000FF"),
    (60, "Ile de Sirop", "DEF", 0.35, "L'ile de Sirop est une ile paradisiaque où les habitants vivent en paix et en harmonie.", image_temporaire, "#800080"),
    (61, "Equipage de Shanks", "ATK", 0.40, "L'equipage de Shanks est un groupe de pirates dirige par Shanks le Roux.", image_temporaire, "#0000FF"),
    (62, "Equipage de Kaido", "DEF", 0.45, "L'equipage de Kaido est un groupe de pirates dirige par Kaido le Cent betes.", image_temporaire, "#800080"),
    (63, "Equipage de Big Mom", "HP", 0.45, "L'equipage de Big Mom est un groupe de pirates dirige par Big Mom.", image_temporaire, "#FF0000"),
    (64, "Draconique", "ATK", 0.45, "Les Dragons sont des creatures mythiques qui possedent des pouvoirs magiques.", image_temporaire, "#FFA500"),
    (65, "Monstre de vitesse", "ATK", 0.50, "Les Monstre de vitesse sont des personnages qui peuvent se deplacer à une vitesse supersonique.", image_temporaire, "#0000FF"),
    (66, "Aveugle", "ATK", 0.40 , "Les Aveugles sont des personnages qui ont perdu la vue mais qui ont developpe d'autres sens pour compenser.", image_temporaire, "#800080"),
    (67, "Dojo de Bang", "ATK", 0.35, "Le Dojo de Bang est un lieu d'entrainement où les disciples apprennent les techniques de combat de Bang.", image_temporaire, "#FF0000"),
    (68, "Cyborg", "DEF", 0.40, "Les Cyborgs sont des etres humains qui ont ete ameliores avec des technologies cybernetiques.", image_temporaire, "#FFA500"),
    (69, "JoJo", "DEF", 0.45, "Les JoJos sont les membres de la famille Joestar qui luttent contre les forces du mal.", image_temporaire, "#0000FF"),
    (70, "Fleau", "ATK", 0.45, "Les Fleaux sont des creatures malefiques qui apportent la destruction et la mort partout où ils passent.", image_temporaire, "#800080"),
    (71, "Ecole de Tokyo", "HP", 0.30, "L'école de Tokyo est un etablissement scolaire où les eleves apprennent à maitriser leurs pouvoirs surnaturels.", image_temporaire, "#FF0000"),
    (72, "Ecole de Kyoto", "HP", 0.30, "L'école de Kyoto est un etablissement scolaire rival de l'ecole de Tokyo.", image_temporaire, "#FFA500"),
    (73, "Zenin", "ATK", 0.40, "Le clan Zenin est une famille de sorciers qui possede des pouvoirs magiques.", image_temporaire, "#0000FF"),
    (74, "Kamo", "ATK", 0.40, "Le clan Kamo est une famille de sorciers qui possede des pouvoirs magiques.", image_temporaire, "#800080"),
    (75, "Fushiguro", "ATK", 0.40, "La lignée Fushiguro est une lignee d'originaire humaine.", image_temporaire, "#FF0000"),
    (76, "Ubuyashiki", "HP", 0.25, "La famille Ubuyashiki est une famille de demons qui dirige le clan des pourfendeurs de demons.", image_temporaire, "#FFA500"),
    (77, "Hashira", "ATK", 0.40, "Les Hashiras sont les piliers de l'organisation des pourfendeurs de demons.", image_temporaire, "#0000FF"),
    (78, "Pourfendeur de démons", "ATK", 0.35, "Les Pourfendeurs de demons sont une organisation secrete qui lutte contre les demons.", image_temporaire, "#800080"),
    (79, "Domaine des Papillons", "ATK", 0.45, "Le Domaine des Papillons est un lieu mysterieux où les demons se rassemblent pour se nourrir.", image_temporaire, "#FF0000"),
    (80, "Démon", "ATK", 0.35, "Les Demons sont des creatures malefiques qui se nourrissent de la chair humaine.", image_temporaire, "#FFA500"),
    (81, "Kamado", "ATK", 0.45, "La famille Kamado est une famille de pourfendeurs de demons qui a ete decimee par les demons.", image_temporaire, "#0000FF"),
    (82, "Souffle du Soleil", "ATK", 0.55, "Le Souffle du Soleil est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#800080"),
    (83, "Souffle de la Foudre", "ATK", 0.55, "Le Souffle de la Foudre est une technique de combat utilisee par les pourfendeurs de demons.", image_temporaire, "#FF0000"),
    (84, "Souffle de l'Eau", "ATK", 0.55, "Le Souffle de l'Eau est une technique de combat utilisée par les pourfendeurs de demons.", image_temporaire, "#FFA500"),
    (85, "Souffle de la Fleur", "ATK", 0.55, "Le Souffle de la Fleur est une technique de combat utilisée par les pourfendeurs de demons.", image_temporaire, "#0000FF"),
    (86, "Lune", "ATK", 0.50, "Les Lunes sont des demons puissants qui servent Muzan.", image_temporaire, "#800080"),
    (87, "Brando", "ATK", 0.50, "Les Brando sont une famille de vampires qui cherchent à dominer le monde.", image_temporaire, "#FF0000"),
    (88, "Maitre de la Gravite", "ATK", 0.50, "Les Maitres de la Gravite sont des personnages qui peuvent contrôler la gravite.", image_temporaire, "#FFA500"),
    (89, "Armstrong", "ATK", 0.45, "La famille Armstrog est une famille illustre et noble qui a servi Amestris pendant des generations.", image_temporaire, "#0000FF"),
    (90, "Homonculus", "ATK", 0.55, "Les Homonculus sont des etres artificiels crees par le Pere pour servir ses desseins.", image_temporaire, "#800080"),
    (91, "Alchimiste d'Etat", "HP", 0.40, "Les Alchimistes d'Etat sont des alchimistes qui servent le gouvernement d'Amestris.", image_temporaire, "#FF0000"),
    (92, "Xing", "HP", 0.45, "Le pays de Xing est un pays voisin d'Amestris qui pratique l'alchimie de l'est.", image_temporaire, "#FFA500"),
    (93, "Elric", "HP", 0.55, "La famille Elric est une famille d'alchilmistes (sauf la mere).", image_temporaire, "#0000FF"),
    (94, "Automail", "HP", 0.55, "L'Automail est une prothese mecanique qui remplace un membre perdu.", image_temporaire, "#800080"),
    (95, "Ishval", "ATK", 0.40, "Les Ishvals sont un peuple pacifique qui a ete decime par les alchimistes d'Amestris.", image_temporaire, "#FF0000"),
    (96, "Bradley", "ATK", 0.40, "La famille Bradley comporte deux Homonculus et est au pouvoir du pays.", image_temporaire, "#FFA500"),
    (97, "Unite Mustang", "ATK", 0.35, "L'Unité Mustang est une unite de l'armee d'Amestris dirigee par Roy Mustang.", image_temporaire, "#0000FF"),
    (98, "U.A.", "HP", 0.35, "L'U.A. est une école de heros où les etudiants apprennent à devenir des heros professionnels.", "ua.gif", "#800080"),
    (99, "Zoldyck", "ATK", 0.40, "La famille Zoldyck est une famille d'assassins qui sont les plus redoutes du monde.", "zoldyck.png", "#fde9e0"),
    (100, "Dix Commandements", "ATK", 0.60, "Les Dix Commandements sont les dix demons les plus puissants de l'Empire de Britannia.", "https://i.imgur.com/SMEji4z.jpeg", "#FF0000"),
    (101, "Les Sept Peches Capitaux", "ATK", 0.45, "Les Sept Péchés Capitaux sont un groupe de chevaliers qui ont trahi le royaume de Liones.", "https://i.imgur.com/CnvtvuO.jpeg", "#FFA500"),
    (102, "Destructeur", "ATK", 0.60, "Les Dieux de la Destruction sont des divinites qui detruisent les planetes pour maintenir l'equilibre de l'univers.", "https://i.imgur.com/uxo372k.png", "#0000FF"),
    (103, "Ange", "ATK", 0.50, "Les Anges sont des etres celestes qui servent les dieux et protegent l'univers.", "https://i.imgur.com/xt9Tn0P.jpeg", "#ddeaef"),
    (104, "Famille de Son Goku", "ATK", 0.45, "La famille de Son Goku est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/cChWxf7.jpeg", "#FF0000"),
    (105, "Famille de Vegeta", "ATK", 0.45, "La famille de Vegeta est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/eyN6Qg9.jpeg", "#FFA500"),
    (106, "Section 4 Anti-Demon", "ATK", 0.40, "La Section 4 Anti-Demon est une unite speciale de la police qui lutte contre les demons.", "https://i.imgur.com/dijQZFN.jpeg", "#0000FF"),
    (107, "Freecss", "HP", 0.50, "La famille Freecss est une famille de chasseurs qui cherchent des tresors et des creatures rares.", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/12/Gon-and-Ging-Freecss.jpg", "#800080"),
    (108, "Hunter étoilé", "HP", 0.40, "L'Association Hunter est une organisation de chasseurs qui traquent les creatures rares et les criminels. Les hunters étoilés sont leurs meilleurs atouts.", "https://i.imgur.com/fHvGkwX.jpeg", "#f40000"),
    (109, "Zodiac", "DEF", 0.40, "Les Zodiacs sont les douze membres du conseil des Hunters qui sont les plus puissants et les plus influents de l'Association Hunter.", "https://i.imgur.com/fHvGkwX.jpeg", "#FFA500"),
    (110, "Brigade Fantome", "ATK", 0.30, "La Brigade Fantome est une organisation criminelle qui lutte contre l'Association Hunter.", "https://i.imgur.com/2KZe6ug.gif", "#00000"),
    (111, "Forme de vie ultime", "DEF", 0.40, "Les formes de vie ultime sont des créatures ultimes qui dépassent les limites de l'humanité.", image_temporaire, "#00000"),
    (112, "Voleur de Pouvoir", "ATK", 0.70, "Les Voleurs de Pouvoir sont des individus qui volent les pouvoirs des autres pour les utiliser à leur avantage.", image_temporaire, "#00000"),
    (113, "Todoroki", "ATK", 0.40, "La famille Todoroki est une famille de heros qui possedent des pouvoirs de glace et de feu.", "https://i.imgur.com/69aINzI.jpeg", "#00000"),
    (114, "Héritier du One For All", "ATK", 0.70, "Les Heritiers du One For All sont des individus qui ont herite du pouvoir du One For All pour proteger le monde des vilains.", image_temporaire, "#00000"),
    (115, "Kuchiki", "ATK", 0.5, "La famille Kuchiki est une famille de nobles qui sont les gardiens du clan Kuchiki.", image_temporaire, "#00000"),
    (116, "Shimura" , "ATK", 0.4, "La famille Shimura est consituée de , sah flemme de finir mdrr", image_temporaire, "#00000"),
    (117, "Big 3", "HP", 0.50, "Le Big 3 est un groupe de trois etudiants de l'U.A. qui sont les plus forts de leur generation.", "https://i.imgur.com/195h0KM.png", "#00000"),
    (118, "Sniper", "ATK", 0.55, "Les Snipers sont des tireurs d'elite qui peuvent atteindre des cibles à longue distance.", image_temporaire, "#00000"),
    (119, "Intangible", "DEF", 0.65, "Les Intangibles sont des individus qui peuvent devenir intangibles et traverser les objets solides.", image_temporaire, "#00000"),
    (120, "Kurosaki", "HP", 0.40, "La famille Kurosaki est une famille de chasseurs de Hollows qui protegent les humains des attaques des Hollows.", image_temporaire, "#00000"),
    (121, "Cinq Doyen", "HP", 0.40, "Les cinq doyens sont la Plus Haute Instance du Gouvernement Mondial.", "https://static.wikia.nocookie.net/onepiece/images/f/f9/Cinq_Doyens_Anime_Post_Ellipse_Infobox.png/revision/latest?cb=20221119194241&path-prefix=fr", "#00000"),
    (122, "Foetus des Neuf Phases", "HP", 0.65, "Les Foetus des Neuf Phases sont à l'origine neuf fœtus avortés issus du mélange entre une humaine et des fléaux. Mort-nés, ils sont devenus des reliques.", image_temporaire, "#00000"),
    (123, "Famille de Luffy", "HP", 0.40, "La famille de Luffy est une famille de pirates qui navigue sur les mers pour trouver le One Piece.", image_temporaire, "#00000"),
    (124, "ANBU", "ATK", 0.45, "Les ANBU sont une unite speciale de ninjas qui travaillent pour le Hokage.", image_temporaire, "#00000"),
    (125, "Tout Puissant", "ATK", 0.5, "Les Tout Puissants sont des individus qui possedent des pouvoirs divins et qui peuvent detruire des planetes entieres.", image_temporaire, "#00000"),
    (126, "Kujo", "ATK", 0.45, "La famille Kujo est une famille de Stand Users qui combattent les forces du mal.", image_temporaire, "#00000"),
    (127, "Manipulateur de Sang", "ATK", 0.65, "Les Manipulateurs de Sang sont des individus qui peuvent manipuler le sang pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (128, "CP-0", "DEF", 0.45, "Le CP-0 est une unite speciale de la Marine qui traque les criminels les plus dangereux du monde.", "https://staticg.sportskeeda.com/editor/2023/12/556eb-17027667692782-1920.jpg", "#00000"),
    (129, "Maître du Brouillard", "DEF", 0.45, "Les Maîtres du Brouillard sont des ninjas qui peuvent manipuler le brouillard pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (130, "Maitre des Fleaux", "ATK", 0.45, "Les Maitres des Fleaux sont des individus qui possedent des pouvoirs de fleaux et qui peuvent detruire des villes entieres.", image_temporaire, "#00000"),
    (131, "Dépourvu d'énergie occulte", "ATK", 0.45, "Les Dépourvus d'énergie occulte sont des individus qui n'ont pas d'énergie occulte et qui doivent utiliser des armes pour combattre.", image_temporaire, "#00000"),
    (132, "Classe S", "ATK", 0.50, "Les exorcistes de classe S sont les exorcistes les plus dangereux, ils sont capables de battre un pays entier", image_temporaire, "#00000"),
    (133, "Roi", "ATK", 0.50, "Un roi est un individu qui a le pouvoir absolu sur son royaume et qui peut faire ce qu'il veut.", image_temporaire, "#00000"),
    (134, "Prisonnier", "DEF", 0.45, "Les prisonniers sont des individus qui ont ete emprisonnes pour leurs crimes et qui doivent purger leur peine.", image_temporaire, "#00000"),
    (135, "Marionnettiste", "ATK", 0.65, "Les Marionnettistes sont des individus qui peuvent controler les autres par la force de leur volonte.", image_temporaire, "#00000"),
    (136, "Masqué", "DEF", 0.45, "Les Masqués sont des individus qui portent un masque pour cacher leur identite et proteger leur famille.", image_temporaire, "#00000"),
    (137, "Chanceux", "DEF", 0.45, "Les Chanceux sont des individus qui ont de la chance et qui reussissent toujours dans tout ce qu'ils entreprennent.", image_temporaire, "#00000"),
    (138, "Yandere", "DEF", 0.45, "Les Yandere sont des individus qui sont obsedes par leur amour pour quelqu'un et qui sont prets à tout pour le proteger.", image_temporaire, "#00000"),
    (139, "Réssucité", "DEF", 0.20, "Les Resuscités sont des individus qui ont ete ramenes a la vie apres leur mort.", image_temporaire, "#00000"),
    (140, "Sarutobi", "DEF", 0.45, "Les Sarutobis sont une famille de ninjas qui ont servi le village de Konoha pendant des generations.", image_temporaire, "#00000"),
    (141, "Métamorphe", "DEF", 0.70, "Les Métamorphes sont des individus qui peuvent changer de forme pour se fondre dans leur environnement.", image_temporaire, "#00000"),
    (142, "Berserker", "ATK", 0.75, "Les Berserkers sont des individus qui entrent dans une rage meurtriere et qui attaquent tout ce qui se trouve sur leur chemin.", image_temporaire, "#00000"),
    (143, "Imposteur", "DEF", 0.45, "Les Imposteurs sont des individus qui se font passer pour quelqu'un d'autre pour tromper leurs ennemis.", image_temporaire, "#00000"),
    (144, "Archer", "ATK", 0.55, "Les Archers sont des tireurs d'elite qui peuvent atteindre des cibles à longue distance.", image_temporaire, "#00000"),
    (145, "Prince", "DEF", 0.45, "Les Princesses sont des jeunes filles de la noblesse qui sont protegees par des gardes du corps.", image_temporaire, "#00000"),
    (146, "Medecin", "HP", 0.45, "Les Medecins sont des medecins qui soignent les blessures et les maladies des autres.", image_temporaire, "#00000"),
    (147, "Manipulateur de l'ombre", "DEF", 0.45, "Les Manipulateurs de l'ombre sont des individus qui peuvent manipuler les ombres pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (148, "Glouton", "HP", 0.45, "Les Gloutons sont des individus qui ont un appetit insatiable et qui peuvent manger n'importe quoi.", image_temporaire, "#00000"),
    (149, "Professeur", "DEF", 0.45, "Les Professeurs sont des enseignants qui enseignent aux eleves les matieres scolaires et les techniques de combat.", image_temporaire, "#00000"),
    (150, "Rival Eternel", "ATK", 0.50, "Les Rivaux Eternels sont des individus qui se battent l'un contre l'autre depuis des generations.", image_temporaire, "#00000"),
    (151, "Secrétaire", "DEF", 0.35, "Les Secrétaires sont des individus qui assistent les dirigeants et les aident dans leurs taches administratives.", image_temporaire, "#00000"),
    (152, "Titan", "HP", 0.60, "Les Titans sont des creatures gigantesques qui attaquent les humains et les devorent.", image_temporaire, "#00000"),
    (153, "Yeager", "ATK", 0.45, "Les Yeagers sont une famille de guerriers qui se battent pour proteger l'humanite des Titans.", image_temporaire, "#00000"),
    (154, "Chef Cuisinier", "HP", 0.45, "Les Chefs Cuisiniers sont des individus qui cuisinent des plats delicieux pour nourrir les autres.", image_temporaire, "#00000"),
    (155, "Z Fighters", "ATK", 0.40, "Les Z Fighters sont un groupe de guerriers qui se battent pour proteger la Terre des forces du mal.", image_temporaire, "#00000"),
    (156, "Maitre du climat", "ATK", 0.70, "Les Maitres du climat sont des individus qui peuvent controler le climat pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (157, "Âme", "DEF", 0.45, "Les Âmes sont des entites spirituelles qui peuvent posseder les corps des autres pour les controler.", image_temporaire, "#00000"),
    (158, "Minable et perfide", "DEF", 0.30, "Les Perfides sont des individus qui sont sournois et qui utilisent des ruses pour tromper leurs ennemis.", image_temporaire, "#00000"),
    (159, "Maitre des serpents", "ATK", 0.50, "Les Ophidiens sont des individus qui ont des pouvoirs de serpent et qui peuvent se transformer en serpents.", image_temporaire, "#00000"),
    (160, "Pervers", "ATK", 0.40, "Les Pervers sont des individus qui ont des penchants pervers et qui sont obsedes.", image_temporaire, "#00000"),
    (161, "Double personnalité", "DEF", 0.80, "Les Troubles de la personnalité sont des individus qui ont des personnalites multiples et qui peuvent changer de personnalite à tout moment.", image_temporaire, "#00000"),
    (162, "Intendant", "DEF", 0.25, "Les Intendants sont des individus qui gerent les affaires d'une organisation et qui s'assurent que tout fonctionne correctement.", image_temporaire, "#00000"),
    (163, "Vétéran", "DEF", 0.55, "Les Vétérans sont des individus qui ont de l'experience dans le combat et qui sont capables de se battre contre n'importe qui.", image_temporaire, "#00000"),
    (164, "Pouvoir de Bouddha", "ATK", 0.80, "Les utilisateurs du pouvoir de Bouddha sont des individus qui peuvent utiliser le pouvoir de Bouddha pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (165, "Team 7", "ATK", 0.40, "La Team 7 est une equipe de ninjas qui travaillent ensemble pour proteger le village de Konoha.", image_temporaire, "#00000"),
    (166, "Géant", "HP", 0.60, "Les Géants sont des creatures gigantesques qui attaquent les humains et les devorent.", image_temporaire, "#00000"),
    (167, "Maitre des corbeaux", "ATK", 0.45, "Les Maitres des corbeaux sont des individus qui peuvent controler les corbeaux pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (168, "Manipulateur de cheveux", "ATK", 0.60, "Les Manipulateurs de cheveux sont des individus qui peuvent controler les cheveux pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (170, "Bataillon d'Exploration", "ATK", 0.40, "Le Bataillon d'Exploration est une unite speciale de l'armee qui explore les territoires inconnus et qui combat les Titans.", image_temporaire, "#00000"),
    (171, "Reiss", "HP", 0.40, "La famille Reiss est une famille royale qui dirige le pays de Paradis et qui possede le pouvoir du Titan Originel.", image_temporaire, "#00000"),
    (172, "Maitre du papier", "ATK", 0.75, "Les Maitres du papier sont des individus qui peuvent controler le papier pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (173, "Front de Libération du Paranormal", "ATK", 0.55, "Le Front de Libération du Paranormal est une organisation criminelle qui lutte contre l'Association Hunter.", image_temporaire, "#00000"),
    (174, "Cross Guild", "ATK", 0.45, "La Cross Guild est une guilde de chasseurs de demons qui traque les demons et les tue pour proteger les humains.", image_temporaire, "#00000"),
    (175, "Vice Amiral", "DEF", 0.45, "Les Vice-Amiraux sont des officiers de la Marine qui ont le pouvoir de capturer les pirates et de maintenir l'ordre dans le monde.", image_temporaire, "#00000"),
    (176, "Colonel", "DEF", 0.40, "Les Colonels sont des officiers de l'armee qui commandent des unites de soldats et qui dirigent les operations militaires.", image_temporaire, "#00000"),
    (177, "Lieutenant", "DEF", 0.35, "Les Lieutenants sont des officiers de l'armee qui assistent les Colonels dans leurs taches et qui dirigent les soldats au combat.", image_temporaire, "#00000"),
    (178, "Soldat", "DEF", 0.30, "Les Soldats sont des membres de l'armee qui combattent sur le front pour proteger leur pays et leur famille.", image_temporaire, "#00000"),
    (179, "Magicien", "ATK", 0.55, "Les Magiciens sont des individus qui possedent des pouvoirs magiques et qui peuvent lancer des sorts pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (180, "Commandant", "ATK", 0.50, "Les Commandants sont des officiers de l'armee qui dirigent des unites de soldats et qui commandent les operations militaires.", image_temporaire, "#00000"),
    (181, "Envoûteuse", "DEF", 0.75, "Les Envoûteuses sont des femmes fatales qui utilisent leur charme pour manipuler les hommes et les amener à faire ce qu'elles veulent.", image_temporaire, "#00000"),
    (182, "Stratège", "DEF", 0.60, "Les Stratèges sont des individus qui planifient les operations militaires et qui dirigent les troupes sur le champ de bataille.", image_temporaire, "#00000"),
    (183, "Sans cheveux", "DEF", 0.45, "Les Sans cheveux sont des individus qui n'ont pas de cheveux et qui devraient porter une perruque pour cacher leur calvitie.", image_temporaire, "#00000"),
    (184, "Moine", "ATK", 0.60, "Les Moines sont des religieux qui consacrent leur vie à la priere et à la meditation pour atteindre l'illumination.", image_temporaire, "#00000"),
    (185, "Génération Terrible", "ATK", 0.45, "La Génération Terrible est une generation qui fait des DINGUERIES.", image_temporaire, "#00000"),
    (186, "Dissecteur", "ATK", 0.45, "Les Dissecteurs sont des individus qui peuvent découper les choses grâce à leurs pouvoirs.", image_temporaire, "#00000"),
    (187, "Univers Alternatif", "DEF", 0.45, "Les Univers Alternatifs sont des mondes paralleles qui existent en dehors de notre realite.", image_temporaire, "#00000"),
    (188, "Immortel", "DEF", 0.60, "Les Immortels sont des individus qui ne peuvent pas mourir et qui vivent pour toujours.", image_temporaire, "#00000"),
    (189, "Empoisonneur", "ATK", 0.45, "Les Empoisonneurs sont des individus qui utilisent des poisons pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (190, "Tueur à gage", "ATK", 0.45, "Les Tueurs à gage sont des individus qui tuent des gens pour de l'argent.", image_temporaire, "#00000"),
    (191, "Fusion", "ATK", 0.45, "Les Fusions sont des individus qui peuvent fusionner avec d'autres pour augmenter leur puissance.", image_temporaire, "#00000"),
    (192, "Manipulateur d'Esprit", "DEF", 0.45, "Les Manipulateurs d'Esprit sont des individus qui peuvent controler les esprits des autres pour les manipuler.", image_temporaire, "#00000"),
    (193, "Aspirant Guerrier", "ATK", 0.45, "Les Aspirants Guerriers sont des individus qui s'entrainent pour devenir des guerriers puissants.", image_temporaire, "#00000"),
    (194, "Ackerman", "ATK", 0.65, "Les Ackermans sont une famille de guerriers qui servent la famille royale de Paradis.", image_temporaire, "#00000"),
    (195, "Duplicateur", "HP", 0.55, "Les Duplicateurs sont des individus qui peuvent creer des copies d'eux-memes pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (196, "Kaio", "HP", 0.45, "Les Kaios sont des divinites qui protegent l'univers et qui veillent à ce que l'equilibre soit maintenu.", image_temporaire, "#00000"),
    (197, "Race de Freezer", "DEF", 0.60, "Les membres de la race de Freezer sont des guerriers puissants qui sont issus de la même race que Freezer.", image_temporaire, "#00000"),
    (198, "Héro Professionel", "DEF", 0.45, "Les Heros Professionnels sont des individus qui protegent les citoyens des vilains et qui combattent le crime.", image_temporaire, "#00000"),
    (199, "Lancier", "ATK", 0.45, "Les Lanciers sont des soldats qui combattent avec des lances et qui sont capables de percer les armures de leurs ennemis.", image_temporaire, "#00000"),
    (200, "Fée", "DEF", 0.45, "Les Fees sont des creatures magiques qui vivent dans les forets et qui protegent la nature.", image_temporaire, "#00000"),
    (201, "Pouvoir du soleil", "ATK", 0.70, "Les utilisateurs du pouvoir du soleil sont des individus qui peuvent utiliser le pouvoir du soleil pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (202, "Maitre de la nature", "DEF", 0.60, "Les utilisateurs du pouvoir de la nature sont des individus qui peuvent utiliser le pouvoir de la nature pour proteger la foret.", image_temporaire, "#00000"),
    (203, "Scientifique", "DEF", 0.45, "Les Scientifiques sont des individus qui etudient la science et qui inventent des technologies pour ameliorer la vie des gens.", image_temporaire, "#00000"),
    (204, "Famille Don Quichotte", "DEF", 0.50, "La famille Don Quichotte est une famille de pirates qui sont les plus redoutes du monde.", image_temporaire, "#00000"),
    (205, "Armure d'Or", "DEF", 0.75, "Les Armures d'Or sont des armures magiques qui protegent leur porteur des attaques ennemies.", image_temporaire, "#00000"),
    (206, "Tireur", "ATK", 0.40, "Les Tireurs sont des tireurs d'elite qui peuvent atteindre des cibles à longue distance.", image_temporaire, "#00000"),
    (207, "Sens de la direction douteux", "HP", 0.80, "Les individus avec un sens de la direction douteux sont des personnes qui se perdent facilement et qui ont du mal à trouver leur chemin.", image_temporaire, "#00000"),
    (208, "Utilisateur de Nunchaku", "ATK", 0.45, "Les Utilisateurs de Nunchaku sont des individus qui maitrisent l'art du nunchaku pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (209, "Famille de Méliodas", "HP", 0.45, "La famille de Meliodas est une famille de demons qui protegent le royaume de Britannia.", image_temporaire, "#00000"),
    (210, "Avare", "DEF", 0.45, "Les Avares sont des individus qui sont obsedes par l'argent et qui sont prets à tout pour le proteger.", image_temporaire, "#00000"),
    (211, "Prêtre", "DEF", 0.65, "Les Prêtres sont des religieux qui servent les dieux et qui prient pour le salut de l'humanite.", image_temporaire, "#00000"),
    (212, "Utilisateur de Hache", "ATK", 0.45, "Les Utilisateurs de Hache sont des individus qui maitrisent l'art de la hache pour combattre leurs ennemis.", image_temporaire, "#00000"),
    
    
]

# Utilisateur de dague

all_link_synergies = {
    212 : ["Escanor", "Mei Mei","Barragan","Brogy"], # Utilisateur de Hache
    211 : ["Grand Pretre", "Enrico Pucci"], # Prêtre
    210 : ["Leorio", "Shigechi"], # Avare
    209 : ["Estarossa","Meliodas","Zeldris"], # Famille de Méliodas
    208 : ["Ban","Maki Zenin","Guy","Rock Lee","Kurapika","Toji Fushiguro","Ikkaku"], # Utilisateur de Nunchaku
    207 : ["Roronoa Zoro","Kenpachi","Yachiru",], # Sens de la direction douteux
    206 : ["Riza Hawkeye","Mustard","Miles","Conny Springer","Narancia","Maria Ross","Starrk","Franklin"], # Tireur
    205 : ["Don Krieg","Shaka"], # Armure d'Or
    204 : ["Caesar Clown","Don Quichotte Doflamingo","Corazon","Vergo"], # Famille Don Quichotte
    203 : ["Caesar Clown","Tim Marcoh","Mayuri","Urahara","Hange Zoe"], # Scientifique
    202 : ["Hanami","King (NNT)","Ibara Shiozaki","Hashirama Senju","Yamato (naruto)", "Shinji Nishiya","Danzo Shimura", "Ryokugyu"], # Maitre de la nature
    201 : ["Escanor","Pere","Feitan"], # Pouvoir du soleil
    200 : ["King (NNT)","Gloxinia"], # Fée
    199 : ["Stinger","Maki Zenin","King (NNT)"], # Lancier
    198 : ["Saitama", "Mumen Rider","Fubuki", "Watchdog Man", "Tatsumaki", "King (OPM)", "Bang", "Flashy Flash", "Atomic Samurai", "Child Emperor", "Metal Knight", "Zombieman", "Genos", "Metal Bat", "Tanktop Master", "Puri Puri Prisoner", "Stinger", "Sneck", "All Might", "Star And Stripe", "Endeavor","Nana Shimura","Beast Jeanist","Hawks","Shota Aizawa","Ryukyu","Mt. Lady", "Gran Torino","Midnight", "Rock Lock", "Snipe"], # Héro Professionel
    197 : ["Freezer", "Cooler", "Roi Cold", "Frost"], # Race de Freezer
    196 : ["Zamasu", "Maitre Kaio", "Kaio Shin", "Black Goku"], # Kaio
    195 : ["Momo Yaoyorozu", "Twice", "Hermes Costello", "Korutopi"], # Duplicateur
    194 : ["Mikasa Ackerman", "Levi Ackerman", "Kenny Ackerman"], # Ackerman
    193 : ["Sieg Yeager", "Annie Leonhart", "Reiner Braun", "Bertholdt Hoover", "Pieck Finger", "Porco Galliard", "Gabi Braun", "Falco Grice", "Udo", "Zofia"], # Aspirant Guerrier
    192 : ["Sharnalk","Makima","Irumi Zoldyck","Shinso Hitoshi","Kuroro Lucifer","Ino","Sosuke Aizen","Itachi Uchiha","Madara Uchiha","Sasuke Uchiha","Shisui Uchiha"], # Manipulateur d'Esprit
    191 : ["Gogeta","Vegeto","Zamasu","Gotenks"], # Fusion
    190 : ["Toji Fushiguro", "Hit","Zabuza Momochi","Tao Pai Pai","Zeno Zoldyck","Silva Zoldyck","Kirua Zoldyck","Karuto Zoldyck", "Ghiaccio", "Prosciutto", "Pesci", "Melone", "Illuso", "Formaggio", "Cioccolata"], # Tueur à gage
    189 : ["Fugo (Purple Haze)","Mayuri","Mustard","Orochimaru","Magellan","Shizune","Kabuto Yakushi","Sasori","Shinobu Kocho","Soi Fon","Chiyo","Caesar Clown","Gloxinia","Zazan","Don Krieg","Hanzo","Eso","Frost","Kechizu"], # Empoisonneur
    188 : ["Hidan", "Kakuzu","Sosuke Aizen","Isshiki Otsutsuki","Ban","Kars","Pere"], # Immortel
    187 : ["Jiren", "Champa","Vados","Belmod", "Toppo", "Kefla", "Hit", "Black Goku", "Kale", "Caulifla", "Cabba", "Frost", "Trunks"], # Univers Alternatif
    186 : ["Sukuna","Danzo Shimura"], # Dissecteur
    185 : ["Trafalgar D. Law", "Eustass Kid", "Monkey D. Luffy", "Roronoa Zoro", "Marshall D. Teach", "Urouge", "Jewelry Bonney"], # Génération Terrible
    184 : ["Isaac Netero","Ichibe Hyosube","Gyomei","Urouge","Uraume"], # Moine
    183 : ["Saitama","Ichibe Hyosube","Ikkaku","Tortue Geniale"], # Sans cheveux
    182 : ["Momo Yaoyorozu", "Shikamaru Nara", "Pegui","Armin Arlert","Erwin Smith","Momo Yaoyorozu","Sosuke Aizen","Kabuto Yakushi"], # Stratège
    181 : ["Vezze","Boa Hancock","Makima"], # Envoûteuse
    180 : ["Ivankov","Karasu","Belo Betty","Lindbergh","Olivia Mira Armstrong","Erwin Smith","Magellan","Ginyu"], # Commandant
    179 : ["Merlin","Momo"], # Magicien
    178 : ["Ikarugo","Kain Fuery","Falman","Heinkel","Hannes","Maria Ross","Zofia","Darius"], # Soldat
    177 : ["Hermep","Corazon","Maes Hughes", "Cheetu", "Zazan","Meleoron","Koruto","Levi Ackerman","Miles","Buccaneer"], # Lieutenant
    176 : ["Tashigi", "Hina", "Koby","Roy Mustang"], # Colonel
    175 : ["Smoker","Haguar D. Sauro","Tsuru","Doll","Vergo"], # Vice Amiral
    174 : ["Crocodile","Dracule Mihawk", "Buggy"], # Cross Guild
    173 : ["Tomura Shigaraki", "All For One", "Dabi", "Spinner", "Himiko Toga", "Twice", "Re-Destro", "Gigantomachia","Mustard"], # Front de Libération du Paranormal
    172 : ["Konan","Karuto Zoldyck"], # Maitre du papier
    171 : ["Historia Reiss", "Frieda Reiss", "Rhodes Reiss"], # Reiss
    170 : ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman", "Hange Zoe", "Erwin Smith", "Jean Kirstein", "Conny Springer", "Sasha Braus", "Historia Reiss", "Ymir", "Reiner Braun", "Bertholdt Hoover", "Annie Leonhart","Mike Zacharias"], # Bataillon d'Exploration
    168 : ["Daki","Jiraya","Kumadori","Pamu Shiberia","Yukako"], # Manipulateur de cheveux
    167 : ["Itachi Uchiha","Karasu","Mei mei","Shisui Uchiha"], # Maitre des corbeaux
    166 : ["Mt. Lady", "Gigantomachia", "Diane","Armin Arlert","Bertholdt Hoover","Rhodes Reiss","Brogy","Dorry","Haguar D. Sauro","Magellan"], # Géant
    165 : ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Sai","Boruto Uzumaki","Sarada Uchiha","Konohamaru Sarutobi","Mitsuki","Kawaki"], # Team 7
    164 : ["Sengoku", "Isaac Netero","Hashirama Senju"], # Pouvoir de Bouddha
    163 : ["Zeno Zoldyck","Isaac Netero", "Yamamoto","Tsuru","Monkey D. Garp","Sengoku","Jigoro","Ichibe Hyosube","Iroh","Kyoraku"], # Vétéran
    162 : ["Kanaria","Gotoh"], # Intendant
    161 : ["Diavolo","Twice","Ling Yao","Escanor"], # Double personnalité
    160 : ["Jiraya","Ebisu","Tortue Geniale","Denji","Mineta","Hisoka","Sanji","Meliodas","Brook","Kon","Midnight","Haruta Shigemo"], # Pervers
    159 : ["Orochimaru", "Kabuto Yakushi", "Sasuke Uchiha","Mitsuki","Anko","Akane Sawatari"], # Maitre des serpents
    158 : ["Tompa","Mizuki","Miruki Zoldyck","Guido","Riluberto","Sadaso","Mineta","Cell JR","Shigechi"], # Minable et perfide
    157 : ["Alphonse Elric", "Barry The Chopper"], # Âme
    156 : ["Weather Report","Nami","Monkey D. Dragon"], # Maitre du climat
    155 : ["Son Goku","Son Gohan", "Tortue Geniale", "Krillin", "Yamcha", "Ten Shin Han", "Chaozu", "Piccolo", "Vegeta", "Trunks", "Goten", "Bulma", "Videl", "Pan", "Yajirobe", "C-18","C-17","Majin Buu"], # Z Fighters
    154 : ["Sanji","Tonio","Menchi","Nicolo"], # Chef Cuisinier
    153 : ["Eren Yeager", "Grisha Yeager", "Sieg Yeager", "Carla Yeager"], # Yeager 
    152 : ["Eren Yeager", "Grisha Yeager", "Sieg Yeager", "Ymir", "Annie Leonhart", "Reiner Braun", "Bertholdt Hoover", "Pieck Finger", "Porco Galliard", "Falco Grice","Frieda Reiss"], # Titan
    151 : ["Shizune","Ijichi"], # Secrétaire
    149 : ["Kakashi Hatake","Satoru Gojo","Shota Aizawa","Vlad King","Iruka","Wing","Tortue Geniale","All Might","Snipe","Maitre Kaio","Izumi Curtis","Midnight","Ebisu","Rayleigh","Dracule Mihawk","Sakonji Urodaki"], # Professeur
    148 : ["Glutonny","Majin Buu","Big Mom","Wapol", "Miruki Zoldyck","Menchi","Todo","Inosuke","Monkey D. Luffy","Son Goku","Sasha Braus","Portgas D. Ace","Choji","Hawk","Beerus","Whis","Yajirobe","Polpo"], # Glouton
    147 : ["Shikamaru Nara","Fumikage Tokoyami","Kyoraku"], # Manipulateur de l'ombre
    146 : ["Tim Marcoh", "Neferopito","Tsunade","Sakura Haruno","Ryuken Ishida","Leorio","Shizune","Kabuto Yakushi","Recovery Girl","Karin (naruto)"], # Medecin
    145 : ["Vivi","Boa Hancock","Vegeta","Ling Yao","Elizabeth Liones","Arthur Pendragon"], # Princesse
    144 : ["Pokkle","Uryu Ishida","Gowther","Noritoshi Kamo","Sasha Braus"], # Archer
    143 : ["Mr. Satan","King (OPM)"], # Imposteur
    142 : ["Broly","Kale","Uvogin"], # Berserker
    141 : ["Envy","Oingo","Ginyu","Irumi Zoldyck","Muzan","Yoruichi","King (NNT)","Chopper","Rob Lucci","Heinkel","Darius"], # Métamorphe
    140 : ["Hiruzen Sarutobi", "Asuma Sarutobi", "Konohamaru Sarutobi"], # Sarutobi
    139 : ["Toji Fushiguro","Son Goku","Hashirama Senju","Tobirama Senju","Hiruzen Sarutobi", "Minato Namikaze", "Asuma Sarutobi","Deidara","Itachi Uchiha","Haku","Zabuza Momochi","Madara Uchiha","Sasori","Kimimaro","Hanzo","Chiyo","Freezer","Shenron","Son Gohan","Trunks","Tortue Geniale","Chaozu","Vegeta","Yamcha","Ten Shin Han","Cell","C-17","Piccolo","Krillin"], # Réssucité
    138 : ["Yukako","Pamu Shiberia","Himiko Toga"], # Yandere
    137 : ["Haruta Shigemo","Daniel Darby"], # Chanceux
    136 : ["Kakashi Hatake","Satoru Gojo","Takuma Ino","Galgali","Karasu","King","Shoji","Shinji Nishiya","Hermep","Beam","Mustard","Inosuke","Spinner","Sabito","Sakonji Urokodaki"], # Masqué
    135 : ["Kankuro", "Sasori","Chiyo","Don Quichotte Doflamingo"], # Marionnettiste
    134 : ["Jones","Leluto","Hermes Costello","Jolyne Kujo","Isaac McDougal","Solf J. Kimblee","Lady Nagant","Polpo"], # Prisonnier
    133 : ["Sukuna", "Meruem", "Yhwach","Zeno","Roi Vegeta","Roi Cold","Dabra","Historia Reiss","Wapol","Cobra","King (NNT)","Zeldris","Gol D. Roger"], # Roi
    132 : ["Suguru Geto","Satoru Gojo","Yuki Tsukumo","Yuta Okkotsu","Jogo","Hanami","Dagon","Mahito"], # Classe S
    131 : ["Toji Fushiguro","Maki Zenin"], # Dépourvu d'énergie occulte
    130 : ["Suguru Geto","Miguel","Juzo","Uraume","Haruta Shigemo","Kenjaku","Junpei"], # Maitre des Fleaux
    129 : ["Smoker","Morel","Zabuza Momochi"], # Maître du Brouillard
    128 : ["Kaku","Rob Lucci","Kumadori"], # CP-0
    127 : ["Choso","Kechizu", "Katara","Hama","Vlad King","Rui","Noritoshi Kamo","Power","Nezuko","Esidisi","Eso"], # Manipulateur de Sang
    126 : ["Jotaro Kujo","Jolyne Kujo"], # Famille Kujo
    125 : ["Zeno", "Rikudo","Pere","Athena","Saitama","Super Shenron"], # Tout Puissant
    124 : ["Kakashi Hatake","Shisui Uchiha","Yugao Uzuki","Sai","Yamato (naruto)","Danzo Shimura","Itachi Uchiha"], # ANBU
    123 : ["Monkey D. Luffy","Monkey D. Dragon", "Monkey D. Garp"], # Famille de Luffy
    122 : ["Choso","Eso","Kechizu"], # Foetus des Neuf Phases
    121 : ["Jaygarcia Saturn","Marcus Mars","Topman Warcury", "Ethanbaron Nusjuro","Shepherd Ju Peter"], # Doyen
    120 : ["Ichigo Kurosaki", "Masaki Kurosaki", "Karin Kurosaki", "Yuzu Kurosaki", "Isshin Kurosaki"], # Famille Kurosaki
    3 : ["Ichigo Kurosaki"], # Hollow
    6 : ["Uryu Ishida", "Soken Ishida", "Ryuken Ishida", "Masaki Kurosaki", "Yhwach","Ichigo Kurosaki"], # Quincy
    8 : ["Grimmjow", "Ulquiorra", "Nnoitra", "Halibel", "Baraggan", "Starrk"], # Espada
    119 : ["Obito Uchiha", "Mirio Togata","Zetsu"], # Intangible
    118 : ["Lady Nagant", "Riza Hawkeye", "Ikarugo","Mista","Mai Zenin","Benn Beckman","Usopp","Snipe","Sasha Braus"], # Sniper
    117 : ["Mirio Togata","Tamaki Amajiki","Nejire Hado"], # Big 3
    116 : ["Tomura Shigaraki", "Nana Shimura"], # Shimura
    115 : ["Rukia Kuchiki","Byakuya Kuchiki","Ginrei Kuchiki"], # Famille Kuchiki
    114 : ["Izuku Midoriya","All Might", "Nana Shimura"],
    113 : ["Shoto Todoroki", "Endeavor", "Fuyumi Todoroki", "Natsuo Todoroki", "Rei Todoroki","Dabi"], # Famille Todoroki
    112 : ["Kuroro Lucifer","All For One","Yhwach", "Neito Monoma","Enrico Pucci","Ging Freecss","Yuta Okkotsu","Makima","Marshall D. Teach"], # Voleur de Pouvoir
    111 : ["Kars","Meruem","Pere"], # Forme de vie ultime
    110: ["Kuroro Lucifer", "Hisoka", "Nobunaga", "Machi", "Shizuku", "Franklin", "Feitan", "Phinks", "Sharnalk", "Bonolenov Ndongo", "Karuto Zoldyck", "Uvogin","Korutopi"], # Brigade Fantome
    109 : ["Leorio","Ging Freecss", "Botobai Gigante", "Pariston Hill","Kurapika"], # Zodiac
    108 : ["Menchi","Tsezugera", "Morel","Ging Freecss","Biscuit Kruger","Botobai Gigante","Pariston Hill"], # Hunter étoilé
    107 : ["Mito Freecss","Gon Freecss", "Ging Freecss"],
    106 : ["Aki Hanakawa","Denji","Kishibe","Power","Himeno","Kobeni Higashiyama","Hirokazu Arai","Angel","Beam", "Galgali"], # Section 4 Anti-Demon
    105 : ["Vegeta","Bulma","Trunks","Roi Vegeta"], # Famille de Vegeta
    104 : ["Son Goku", "Raditz", "Bardock", "Chichi" ,"Goten"], # Famille de Son Goku
    103 : ["Whis","Vados","Grand Pretre","Angel","Konan"], # Anges
    102 : ["Beerus","Champa","Belmod","Tomura Shigaraki","Chisaki Kai"], # Destructeur
    101 : ["Meliodas","Ban","King (NNT)","Diane","Gowther","Merlin","Escanor"], # Les Sept Peches Capitaux
    100 : ["Derrierie","Estarossa","Zeldris","Gloxinia","Drole","Grayroad","Fraudrin","Monspiet","Melascula","Galand"], # Dix Commandements
    99 : ["Kirua Zoldyck" , "Irumi Zoldyck", "Miruki Zoldyck", "Aruka Zoldyck", "Zeno Zoldyck", "Silva Zoldyck", "Kikyo Zoldyck","Karuto Zoldyck"], # Zoldyck
    98 : ["Izuku Midoriya","Katsuki Bakugo","Ochaco Uraraka","Tenya Iida","Shoto Todoroki","Momo Yaoyorozu","Eijiro Kirishima","Denki Kaminari","Mina Ashido","Tsuyu Asui","Fumikage Tokoyami","Kyoka Jiro","Hanta Sero","Yuga Aoyama","Toru Hagakure","Mezo Shoji","Koji Koda","Mirio Togata","Tamaki Amajiki","Nejire Hado","Hawks","Endeavor","All Might","Shota Aizawa","Midnight","Snipe","Vlad King","Shoji","Neito Monoma","Mineta","Recovery Girl"], # U.A.
    97 : ["Roy Mustang", "Havoc", "Riza Hawkeye","Heymans","Kain Fuery","Falman"], # Unite Mustang
    96 : ["King Bradley","Selim Bradley"], # Bradley
    95 : ["Scar","Frere de Scar","Miles"], # Ishval
    94 : ["Edward Elric","Paninya","Lan Fan","Buccaneer"], # Automail
    93 : ["Hohenheim","Edward Elric","Alphonse Elric","Trisha Elric"], # Elric
    92 : ["Ling Yao","Mei Chang","Lan Fan","Fu","Xiao Mei"], # Xing
    91 : ["Edward Elric","Roy Mustang","Solf J. Kimblee","Alex Louis Armstrong","Tim Marcoh","Isaac McDougal"], # Alchimiste d'Etat
    90 : ["Lust","Glutonny","Envy","Sloth","Ling Yao","King Bradley","Selim Bradley","Pere"], # Homonculus
    89 : ["Olivia Mira Armstrong","Alex Louis Armstrong"], # Armstrong
    88 : ["Kenjaku","Okuyasu","Yuki Tsukumo","Fujitora","Pain","Ochaco Uraraka","Enrico Pucci","Satoru Gojo"], # Maitre de la Gravite
    87 : ["Dio Brando","Diego Brando","Giorno Giovanna","Dario Brando"], # Brando
    86 : ["Kyogai","Kanamue","Rui","Mukago","Wakuraba","Hairo","Rokuro","Enmu","Daki","Gyutaro","Kaigaku","Gyokko","Akaza","Doma","Kokushibo"], # Lune
    85 : ["Kanae Kocho","Kanao"], # Souffle de la Fleur
    84 : [], # Souffle de l'Eau
    83 : [], # Souffle de la Foudre
    82 : ["Tanjiro Kamado", "Yoriichi Tsugikuni","Sumiyoshi","Tanjuro"], #Kamado
    81 : ["Tanjiro Kamado","Nezuko","Kanao","Sumiyoshi","Tanjuro"], # Souffle du Soleil
    80 : ["Muzan","Nezuko","Tamayo","Yushiro","Susamaru","Yahaba","Fille Araignee","Mere Araignee","Shinzu","Dabra","Denji","Makima","Power","Meliodas","Estarossa","Zeldris","Gloxinia","Hendrickson","Monspeet","Gowther","Derieri","Galand","Hendrickson","Samourai Sword"], # Demon
    79 : ["Aoi Kanzaki","Sumi Nakahara","Kiyo","Naho","Goto (KNY)","Shinobu Kocho"], # Domaine des Papillons
    78 : ["Kanao","Tanjiro Kamado","Zenitsu","Inosuke","Nezuko","Genya","Murata","Ozaki","Yoriichi Tsugikuni","Shinobu Kocho", "Uzui Tengen","Yutaro Kurose","Aki Hanakawa","Angel","Beam","Denji","Galgali","Himeno","Hirokazu Arai","Kishibe","Makima","Power","Samourai Sword"], # Pourfendeur de demons
    77 : ["Giyu","Mitsuri","Obanai","Sanemi","Gyomei","Muichiro","Shinobu Kocho","Rengoku","Kanae Kocho","Uzui Tengen","Jigoro"], # Hashira
    76 : ["Kagaya Ubuyashiki","Amane Ubuyashiki","Hinaki Ubuyashiki","Nichika Ubuyashiki","Kiriya Ubuyashiki","Kanata Ubuyashiki"], # Ubuyashiki
    75 : ["Toji Fushiguro","Megumi Fushiguro","Tsumiki Fushiguro"], # Fushiguro
    74 : ["Noritoshi Kamo","Kenjaku"], # Kamo
    73 : ["Toji Fushiguro", "Naobito Zenin","Mai Zenin","Maki Zenin","Megumi Fushiguro"], # Zenin
    72 : ["Gakuganji","Utahime","Arata Nitta","Mai Zenin","Miwa","Mechamaru","Aoi Todo","Noritoshi Kamo","Momo","Akari Nitta"], # ecole de Kyoto
    71 : ["Yaga","Ijichi","Satoru Gojo","Kusakabe","Sheko Ieri","Akari Nitta","Megumi Fushiguro","Yuji Itadori","Nobara","Maki Zenin","Toge Inumaki","Panda","Yuta Okkotsu","Kinji Hakari","Nanami","Suguru Geto","Yu Haibara"], # ecole de Tokyo
    70 : ["Sukuna", "Mahito", "Jogo", "Dagon", "Hanami", "Choso","Kechizu"], # Fleaux
    69 : ["Jonathan Joestar", "Joseph Joestar", "Jotaro Kujo", "Josuke Higashikata", "Giorno Giovanna", "Jolyne Kujo", "Johnny"], # JoJo
    68 : ["Genos","Cyborgorilla","C-17","C-18"], # Cyborg
    67 : ["Grimasse","Garou","Charanko","Bang"], # Dojo de Bang
    66 : ["Fujitora","Toph","Tosen","Komugi","Shaka","N'Doul","Kagaya Ubuyashiki"], # Aveugle 
    65 : ["Minato Namikaze", "Tobirama Senju", "Yoruichi", "Gran Torino","Sonic"], # Monstre de vitesse TODO
    64 : ["Kaido","Ryukyu","Toshiro Hitsugaya","Shenron","Botobai Gigante","Super Shenron"], # Draconique TODO  ,"Acnologia","Igneel"
    63 : ["Big Mom", "Katakuri"], # equipage de Big Mom
    62 : ["Kaido", "King", "Queen"], # equipage de Kaido
    61 : ["Shanks","Yasopp","Lucky Roo","Benn Beckman","Rockstar"], # equipage de Shanks
    60 : ["Usopp","Kaya","Kuro","Merry","Yassop"], # Ile de Sirop
    59 : ["Speedwagon","Caesar Zeppeli","Kakyoin","Polnareff","Mohamed Abdul","Stroheim","Okuyasu","Rohan","Koichi","Gyro Zeppeli","Bucciarati","Foo Fighters"], # JoBros
    1 : ["Itachi Uchiha", "Kisame", "Deidara", "Sasori", "Hidan", "Kakuzu", "Pain", "Konan", "Zetsu"], # Akatsuki
    2 : ["Son Goku", "Vegeta", "Son Gohan", "Trunks", "Goten","Gotenks", "Bardock", "Raditz", "Nappa", "Broly", "Cabba","Caulifla","Kale","Kefla","Pan","Roi Vegeta","Black Goku"], # Saiyan
    4 : ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"], # Mugiwara
    5 : ["Itachi Uchiha", "Sasuke Uchiha", "Madara Uchiha", "Obito Uchiha", "Shisui Uchiha", "Fugaku Uchiha", "Indra Otsutsuki", "Izuna Uchiha", "Sarada Uchiha"], # Uchiha
    7 : ["Akainu", "Aokiji", "Kizaru", "Sengoku", "Monkey D. Garp", "Fujitora", "Ryokugyu", "Kong","Pixis","Theo Magath"], # Amiral
    10 : ["Barbe Blanche", "Kaido", "Big Mom", "Shanks", "Marshall D. Teach","Monkey D. Luffy","Buggy"], # Yonko
    14 : ["Yamamoto", "Unohana", "Byakuya Kuchiki", "Kenpachi", "Ukitake", "Kyoraku", "Sajin", "Mayuri", "Toshiro Hitsugaya", "Rukia Kuchiki"], # Gotei 13
    15 : ["Hashirama Senju", "Tobirama Senju", "Hiruzen Sarutobi", "Minato Namikaze", "Tsunade", "Kakashi Hatake", "Naruto Uzumaki","Mei Terumi", "Onoki", "Gaara","Danzo Shimura"], # Kage
    16 : ["Crocodile", "Don Quichotte Doflamingo", "Dracule Mihawk", "Kuma", "Boa Hancock", "Jinbe", "Buggy", "Trafalgar D. Law", "Marshall D. Teach"], # Shichibukai,
    17 : ["Jiraya","Orochimaru","Tsunade"], # Sannin
    18 : ["Monkey D. Dragon", "Ivankov", "Kuma", "Sabo", "Koala", "Hack", "Inazuma", "Belo Betty", "Lindbergh", "Karasu","Grisha Yeager"], # Revolutionnaires
    19 : ["Monkey D. Luffy", "Monkey D. Garp", "Gol D. Roger", "Portgas D. Ace", "Monkey D. Dragon", "Sabo", "Trafalgar D. Law", "Marshall D. Teach","Portgas D. Rouge","Vivi","Cobra","Haguar D. Sauro"], # Volonte du D
    20 : ["Kiba", "Karin", "Rob Lucci", "Chopper", "Kaido", "Marco", "Kaku","Cyborgorilla","Crablante", "Tonton","Pakkun", "Laboon","Sajin","Chachamaru","Kaburamaru","Lindbergh","Appa","Tama","Mirko","Kiriko","Nezu","Xiao Mei","Spinner","Ikarugo","Fumikage Tokoyami","Oolong","Sansa","Cheetu","Panda","Heinkel","Mike", "Zazan","Meleoron","Hatchan","Tamaki Amajiki","Pegui","Kenji","Yoruichi","Hawk","Heinkel","Darius","Moshi"], # Animal TODO
    21 : ["Sasuke Uchiha", "Suigetsu", "Karin (naruto)", "Jugo"], # Taka
    22 : ["Pain", "Obito Uchiha", "Madara Uchiha", "Sasuke Uchiha"], # Rinnegan
    23 : ["Naruto Uzumaki", "Sakura Haruno", "Sasuke Uchiha", "Kakashi Hatake", "Shikamaru Nara", "Choji", "Ino", "Hinata Hyuga", "Kiba", "Shino", "Neji Hyuga", "Rock Lee", "Tenten","Kawaki","Danzo Shimura","Jiraya","Mitsuki","Shizune"], # Konoha TODO
    24 : ["Gaara", "Temari", "Kankuro", "Yashamaru","Chiyo"], # Suna TODO
    25 : ["Kisame", "Zabuza Momochi", "Haku", "Mei Terumi", "Suigetsu"], # Kiri TODO
    26 : ["Darui", "Omoi", "Killer Bee", "Samui", "Atsui", "Onoki"], # Kumo TODO
    27 : [ "Onoki", "Deidara", "Onoki", "Deidara"], # Iwa TODO
    28 : ["Naruto Uzumaki", "Killer Bee", "Yugito","Fû", "Yuji Itadori","Madara Uchiha","Obito Uchiha","Gaara","Mito Uzumaki","Kushina Uzumaki"], # Receptacle TODO
    29 : ["Aang","Korra", "Portgas D. Ace","Shoto Todoroki", "Sabo", "Iroh", "Zuko", "Lord Ozai", "Azula", "Itachi Uchiha", "Madara Uchiha", "Sasuke Uchiha","Kakuzu","Jogo","Mohamed Abdul","Dabi","Sukuna","Yamamoto","Roy Mustang","Kyujuro Rengoku","Escanor","Sanji","Endeavor"],# Maitre du Feu TODO
    30 : ["Aang","Korra", "Katara", "Korra", "Suigetsu", "Mei Terumi","Kakuzu","Tobirama Senju","Kisame","Hama","Halibel","Jinbe","Sakonji Urokodaki","Giyu","Sabito","Tanjiro Kamado","Murata","Zabuza Momochi","N'Doul","Isaac McDougal","Boruto Uzumaki"], # Maitre de l'Eau TODO
    31 : ["Aang","Korra", "Toph", "Yamato (naruto)","Kakuzu"], # Maitre de la Terre TODO
    32 : ["Aang","Korra","Temari","Mei Terumi","Danzo Shimura","Boruto Uzumaki","Monkey D. Dragon","Wamuu"], # Maitre de l'Air TODO
    33 : ["Zuko", "Iroh", "Azula", "Lord Ozai", "Kakashi Hatake","Sasuke Uchiha", "Killer Bee", "Darui", "Kakuzu", "Ener","Athena","Denki Kaminari","Zenitsu","Kaigaku","Jigoro","Kirua Zoldyck","Yoruichi","Akira Otoishi","Boruto Uzumaki"], # Maitre de la foudre TODO
    34 : ["Shoto Todoroki","Aokiji", "Toshiro Hitsugaya", "Rukia Kuchiki","Natsuo Todoroki","Fuyumi Todoroki","Rei Todoroki", "Uraume","Haku","Isaac McDougal","Ghiaccio"], # Maitre de la Glace TODO Gray Fullbuster

    36 : ["Akainu", "Jogo","Mei Terumi"], # Maitre de la Lave TODO
    37 : [], # Maitre du Bois 
    39 : ["Gaara"], # Maitre du Sable 
    40 : ["Roronoa Zoro", "Dracule Mihawk","Toji Fushiguro","Maki Zenin", "Killer Bee", "Tashigi", "Kaku", "Sasuke Uchiha","Kisame", "Suigetsu", "Zabuza Momochi","Shanks", "Gol D. Roger", "Stain", "Ichigo Kurosaki", "Sosuke Aizen", "Kenpachi", "Unohana", "Gin", "Darui", "Yamamoto", "Trunks", "Tapion", "Son Gohan", "Rukia Kuchiki", "Byakuya Kuchiki", "Oden", "Trafalgar D. Law", "Brook","Cavendish","Fujitora","Shiryu", "Yhwach","Haruta Shigemo","Yugao Uzuki","Ling Yao","Halibel","Yajirobe","Miwa","Spinner","Hatchan","Inazuma","Dorry","Uzui Tengen","Dabra","Meliodas", "Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman", "Hange Zoe", "Erwin Smith", "Jean Kirstein", "Conny Springer", "Sasha Braus", "Historia Reiss", "Ymir", "Reiner Braun", "Bertholdt Hoover","Mike Zacharias","Zeldris","Gilthunder","Samourai Sword","Shimotsuki Kuina","Sakonji Urodaki","Sabito","Kyoraku","Starrk"], # epeiste
    # 41 : ["Mob", "Ritsu", "Teruki", "Sho Suzuki", "Tome Kurata", "Dimple","Tatsumaki"], # Telekinesiste
    42 : ["Marshall D. Teach", "Shiryu", "Aokiji"], # Equipage de Barbe Noire
    43 : ["Barbe Blanche", "Marco", "Portgas D. Ace"], # Equipage de Barbe Blanche
    44 : ["Naruto Uzumaki", "Kushina Uzumaki", "Pain", "Karin (naruto)", "Mito Uzumaki", "Boruto Uzumaki", "Himawari Uzumaki","Tsunade"], # Uzumaki
    45 : ["Neji Hyuga", "Hinata Hyuga", "Hanabi Hyuga","Himawari Uzumaki", "Boruto Uzumaki"], # Hyuga
    46 : ["Hashirama Senju", "Tobirama Senju", "Tsunade", "Nawaki"], # Senju
    47 : ["Kaguya Otsutsuki", "Rikudo", "Urashiki Otsutsuki", "Momoshiki Otsutsuki", "Toneri Otsutsuki", "Isshiki Otsutsuki"], # Otsutsuki
    48 : ["Shino", "Meruem", "Pufu", "Yupi", "Neferopito","Koruto"], # Insecte
    49 : ["Neferopito", "Yupi", "Pufu","Ichibe Hyosube","Senjumaru Shutara","Kirio Hikifune","Oetsu Nimaiya","Tenjiro Kirinji","Fu","Lan Fan"], # Garde Royale
    # 50 Zeppeli
    50 : ["Will Zeppeli", "Caesar Zeppeli", "Gyro Zeppeli"], # Zeppeli
    52 : ["Kars", "Wamuu", "Esidisi"], # Pillier
    53 : ["Dio Brando","Diavolo", "Jotaro Kujo","Nighteye","Kira Yoshikage","Enrico Pucci","Katakuri","Athena","Boingo","Neon Nostrad","Hit","Eri","Baraggan"], # Maitre du Temps
    54 : ["Kira Yoshikage", "Katsuki Bakugo","Solf J. Kimblee","Genthru"], # Maitre de l'Explosion
    55 : ["Ghiaccio", "Prosciutto", "Pesci", "Melone", "Illuso", "Formaggio", "Cioccolata"], # Squadra Esecuzioni
    56 : ["Jonathan Joestar", "Will Zeppeli", "Joseph Joestar", "Caesar Zeppeli", "Lisa Lisa", "Poco"], # Hamon
    57 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo (Purple Haze)", "Abbacchio","Diavolo","Luca","Polpo","Trish","Neon Nostrad","Samourai Sword"], # Mafioso
    58 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo (Purple Haze)", "Abbacchio","Trish"], # Team Bucciarati
    
}

all_techniques = {
    "All Might" : [
        ["United States of Smash", "utilise l''","https://i.imgur.com/tGRgG5e.mp4", "#FF0000"], #TOREVIEW format mp4
    ],
    "Sasuke Uchiha" : [
        ["Rinnegan", "active son", "https://i.imgur.com/qJ5mfnz.gif", "#d100ff"],
    ],
    "Hit" : [
        ["Point Vitaux", "vise les", "https://i.imgur.com/vi0Kg6z.gif", "#ff3bde"],
    ],
    "Son Goku" : [
        ["Teleportation", "utilise sa", "https://i.imgur.com/skth3A1.gif", "#ff0000"],
    ],
    "Pere": [
        ["Alchimie", "utilise l''", "https://i.imgur.com/KzMK7Xu.gif", "#ec000e"],
    ],
    "Morel": [
        ["Ecran de fumee", "lance un", "https://i.imgur.com/sNGqJb3.gif", "#d100ff"],
    ],
    "Aang": [
        ["Colonnes de flamme", "envoie des", "https://i.imgur.com/nqUJVqG.gif", "#f55a42"],
    ],
    "Tanjiro Kamado" : [
        ["Souffle de l''eau", "utilise le", "https://media.giphy.com/media/RK4qNmmMj17yX80MOY/giphy.gif", "#0000FF"],
    ],
    "Kakashi Hatake" : [
        ["Sharingan", "active son", "https://i.imgur.com/mKlr2SI.gif", "#d14a4a"],
    ],
    "Tsunade" : [
        ["Katsuyu", "invoque", "https://i.gifer.com/8UZi.gif", "#FFFFFF"],
    ],
    "Momoshiki Otsutsuki" : [
        ["Orbe de pouvoir", "lance une", "https://i.pinimg.com/originals/80/fb/83/80fb83d0d9e5a3952e3e4783d37b7107.gif", "#1c0929"],
    ],
    "Toneri Otsutsuki" : [
        ["Tenseigan", "active son", "https://img.wattpad.com/781e99656c0e111d5b62f0d429e6375643c11c52/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6e75637a524c6b576234317237673d3d2d3633342e313539653338383066633861346265333638353430373530343730382e676966", "#0000FF"],
    ],
    "Itachi Uchiha" : [
        ["Mangekyo Sharingan", "active son", "https://i.pinimg.com/originals/ef/84/fa/ef84fafc22ae9b319c63f29ea696119b.gif", "#d14a4a"],
    ],
    "Shisui Uchiha" : [
        ["Téléportation", "utilise la", "https://i.pinimg.com/originals/f4/d5/a5/f4d5a58f5ffde5c1afabe2096af7bc5e.gif", "#d14a4a"],
        ["Sharingan", "active son", "https://64.media.tumblr.com/2140ccf11ade92f5be44e63093c1efd6/tumblr_o6y19xdcfs1rqe0rbo1_540.gif", "#d14a4a"],
        ["Mouvements", "lis les", "https://i.pinimg.com/originals/66/73/4b/66734b28689f5a12243c55f01c43e8a8.gif", "#d14a4a"],
    ],
    "Hidan" : [
        ["Rituel", "active son", "https://steamuserimages-a.akamaihd.net/ugc/171539824338951013/8404D4DB507AA5BEB65400641D3D784130B261FA/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "#000000"],
    ],
    "Haku" : [
        ["Miroirs de Glace", "plonge tout le monde dans les", "", "#61c8ed"],
        ["Aiguilles de Glace", "lance des", "", "#61c8ed"],
        ["Dome de Glace", "enferme tout le monde dans le", "", "#61c8ed"],
        ["Prisons de Glace", "condamne l''opposant aux", "", "#61c8ed"],
    ],
    "Rui" : [
        ["Prison de fils", "créé une", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/85/RuiSang1.gif/revision/latest?cb=20200627145048&path-prefix=fr", "#490c11"],
        ["Cage du regard assassin", "créé la", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/5f/RuiSang2.gif/revision/latest?cb=20200627145112&path-prefix=fr", "#490c11"],
        ["Fils à Trancher Rotatif", "créé une roue rotative de", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/86/RuiSang3.gif/revision/latest?cb=20200627145143&path-prefix=fr", "#490c11"],
    ],
    "Franklin" : [
        ["Déluge de Balles", "déverse un", "https://i.imgur.com/0KyJyzH.gif", "#5c3307"],
        ["Recharge", "", "", "#5c3307"],
    ],
    "Uvogin" : [
        ["Big Bang Impact", "lance un", "https://i.imgur.com/I8LlLN5.gif", "#5c3307"],
        ["Nen", "déploie son", "https://i.imgur.com/CsGYEAi.gif", "#5c3307"],
    ],
    "Meliodas" : [
        ["Frappe avec son épée", "", "https://www.icegif.com/wp-content/uploads/meliodas-icegif-19.gif", "#371745"],
        ["Tranche", "", "https://i.imgur.com/l3Ua1ba.gif", "#000000"],
        ["Full Counter", "lance", "https://i.imgur.com/lSZXOrf.gif", "#000000"],
    ],
    "Estarossa" : [
        ["Epee", "plante une", "https://i.pinimg.com/originals/c8/8e/a6/c88ea6198780a971c2ef029306fe6f65.gif", "#000000"],
    ],
    "Merlin" : [
        ["Explosion", "lance une", "https://i.imgur.com/rVcGRf4.gif", "#000000"],
        ["Vortex", "déploie un", "https://i.imgur.com/lFmGsbR.gif", "#3d2956"],
    ],
    "Escanor" : [
        ["Ultime coup", "lance un", "https://i.imgur.com/1Z2Z9Zv.gif", "#febb11"],
        ["Coup de hache", "balance un" , "https://i.imgur.com/dYI3yWg.gif", "#a53c20"]
    ],
    "Ban" : [
        ["Rafale de coup", "afflige une", "https://i.imgur.com/yAtLcqO.gif", "#cd1e50"],
    ],
    "King (NNT)" : [
        ["Pare les coups", "", "https://i.imgur.com/rviUbxr.gif","#e8925a"],
        ["Lance", "envoie sa", "https://i.imgur.com/voCXYbF.gif", "#e8925a"],
    ],
    "Derrierie" : [
        ["Coup de poing", "balance un", "https://i.imgur.com/ViIMq0U.gif", "#371745"],
    ],
    "Gowther" : [
        ["Projectiles", "lance des", "https://i.imgur.com/fJMs9RN.gif", "#d64e74"],
    ]
    
}