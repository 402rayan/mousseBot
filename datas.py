from constantes import CONSTANTS


image_temporaire = "https://picsum.photos/900/500"
hexadecimal_temporaire = "#000000"

all_characters_templates = {
            "Dragon Ball" : [ # ✅
            ("Super Shenron", "X", "https://i.imgur.com/W7V2Oru.gif", 1500, 1500, 1500),
            ("Son Goku", "X", "https://i.imgur.com/1dpz2hV.gif", 905, 950, 900),
            ("Zeno", "X", "https://i.imgur.com/W579wtw.gif", 800, 1300, 800),
            ("Grand Pretre", "X", "https://i.imgur.com/XFKPYIb.gif", 1000, 1200, 1000),
            ("Whis", "X", 'https://i.imgur.com/UHCV2D1.gif', 1050, 1040, 1000),
            ("Vados", "X", 'https://i.imgur.com/6WuAjqS.gif',1010, 1050, 1000),
            ("Beerus", "X", 'https://i.imgur.com/9ZLOxBK.gif', 920, 1150, 910),
            ("Son Gohan", "X", 'https://i.imgur.com/SJPfZLY.gif', 950, 960, 970),
            ("Vegetto", "X", "https://i.imgur.com/DBewj1R.gif", 930, 950, 955),

            # Personnages SS
            ("Belmod", "SS", "https://i.imgur.com/Yeq7JQY.gif", 800, 900, 800),
            ("Piccolo", "SS", "https://i.imgur.com/srHRyMX.gif", 800, 850, 800), #TOCHECK
            ("Champa", "SS", 'https://i.imgur.com/F7Q78tL.gif', 800, 1000, 800),
            ("Gogeta", "SS", "https://i.imgur.com/JFrolYA.gif", 750, 800, 760),
            ("Broly", "SS", "https://i.imgur.com/gstppUE.gif", 750, 780, 730), 
            ("Jiren", "SS", 'https://i.imgur.com/K7M25Xe.gif', 740, 750, 745),
            ("Zamasu", "SS", 'https://i.imgur.com/Cz6XOfz.gif', 730, 750, 735),
            ("Vegeta", "SS", "https://i.imgur.com/CkK8SBp.gif", 700, 750, 680),
            ("Toppo", "SS", 'https://i.imgur.com/PIp2SBH.gif', 710, 730, 720),
            
            # Personnages S
            ("Kefla", "S", 'https://i.imgur.com/VjmzJvV.gif', 630, 640, 620),
            ("Goku Black", "S", 'https://i.imgur.com/20z0F8R.gif', 550, 620, 560),
            ("Hit", "S", 'https://i.imgur.com/vPZDJKq.gif', 620, 650, 660),
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
            ("Krilin", "B", 'https://i.imgur.com/9RsmzSP.jpeg', 310, 305, 290),
            ("Ten Shin Han", "B", 'https://i.imgur.com/74avz2G.jpeg', 305, 300, 290),
            ("Tortue Geniale", "B", 'https://i.imgur.com/DCbiqFg.jpeg', 320, 320, 295),
            ("Shenron", "B", "https://i.imgur.com/DiVySQ9.gif", 333, 333, 333),

            # Personnages C
            ("Grand Roi Cold", "C", 'https://i.imgur.com/EWJ8rdH.png', 270, 260, 250),
            ("Dabra", "C", 'https://i.imgur.com/bzYsWfm.jpeg', 260, 265, 255),
            ("Bardock", "C", 'https://i.imgur.com/MSTYpQg.jpeg', 260, 280, 250),
            ("Roi Vegeta", "C", "https://i.imgur.com/mtsE4Cy.jpeg", 255, 270, 245),
            ("Uub", "C", "https://i.imgur.com/fZvqk1U.jpeg", 250, 250, 235),
            ("Kaio Shin", "C", "https://i.imgur.com/NNcDlai.jpeg", 230, 240, 270),
            ("Son Goten", "C", 'https://i.imgur.com/LaP4Y5P.jpeg', 240, 255, 270),
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
            ('Asura Otsutsuki', 'SS', 'https://i.imgur.com/aRMeDPa.gif', 725, 745, 745),
            ('Hashirama Senju', 'SS', 'https://i.imgur.com/MV6VGfx.gif', 735, 750, 740),
            ('Tobirama Senju', 'SS', 'https://i.imgur.com/lc99oDg.gif', 720, 720, 710),
            ('Toneri Otsutsuki', 'SS', 'https://i.imgur.com/RC3B2rR.gif', 675, 715, 735),
            ('Pain', 'SS', 'https://i.imgur.com/GvovLg8.gif', 700, 720, 675),
            ('Itachi Uchiha', 'SS', 'https://i.imgur.com/Jhc5tcj.gif', 700, 730, 695),
            ('Minato Namikaze', 'SS', 'https://i.imgur.com/CZd4NkY.gif', 690, 720, 735),
            ('Gai Maito', 'SS', 'https://i.imgur.com/Iocgqpz.gif', 730, 725, 700),
            ('Momoshiki Otsutsuki', 'SS', 'https://i.imgur.com/OnBJXu9.gif', 665, 685, 665),
            ('Kakashi Hatake', 'SS', 'https://i.imgur.com/DFD8eEL.gif', 710, 700, 710),
            ('Shisui Uchiha', 'SS', 'https://media1.tenor.com/m/_To3NtVgZv0AAAAC/shisui-uchiha-shisui.gif', 680, 690, 640),

            # Personnages S
            ('Danzo Shimura', 'S', 'https://i.imgur.com/rsM0pCB.gif', 555, 525, 580),
            ('Kabuto Yakushi', 'S', 'https://i.imgur.com/zCf0Etf.gif', 535, 540, 580),
            ('Hidan', 'S', 'https://gifdb.com/images/high/naruto-shippuden-akatsuki-hidan-yj5u9lmg4se7nuz4.gif', 525, 580, 570),
            ('Hiruzen Sarutobi', 'S', 'https://i.imgur.com/Oa4QUQc.gif', 565, 560, 580),
            ('Onoki', 'S', 'https://pa1.aminoapps.com/8436/0050341a556d26a1e018daa2d679190837ffd8a2r1-500-281_hq.gif', 585, 580, 580),
            ('Gaara', 'S', 'https://i.imgur.com/GlPqkEg.gif', 580, 555, 545),
            ('Killer Bee', 'S', 'https://i.imgur.com/fct31yS.gif', 560, 575, 525),
            ("A", "S", "https://i.imgur.com/f2QuNfH.gif", 560, 575, 525),
            ('Orochimaru', 'S', 'https://i.imgur.com/betllia.gif', 550, 525, 570),
            ('Tsunade', 'S', 'https://i.imgur.com/F3nORVn.gif', 520, 565, 570),
            ('Jiraya', 'S', 'https://i.imgur.com/VKP25gr.gif', 530, 565, 580),
            ('Izuna Uchiha', 'S', 'https://i.imgur.com/RP8gHg3.gif', 585, 560, 540),
            ('Hanzo', 'S', 'https://i.imgur.com/fN5R7A7.gif', 580, 560, 540),
            ('Darui', 'S', 'https://i.imgur.com/4agHAoM.gif', 550, 525, 560),

            # Personnages A 
            ('Fû', 'A', 'https://i.imgur.com/M18N3wg.gif', 400, 445, 435),
            ('Rock Lee', 'A', 'https://i.imgur.com/1V4WwG9.png', 445, 440, 420),
            ('Shikamaru Nara', 'A', 'https://i.imgur.com/yu8NUPK.gif', 390, 425, 420),
            ('Mei Terumi', 'A', 'https://i.imgur.com/JTaGhQQ.gif', 430, 415, 425),
            ('Asuma Sarutobi', 'A', 'https://i.imgur.com/lGIqLP3.gif', 405, 420, 405),
            ('Kisame', 'A', 'https://i.imgur.com/50KuDl3.gif', 450, 445, 435),
            ('Sasori', 'A', 'https://i.imgur.com/RlpI6Rd.gif', 445, 390, 390),
            ('Deidara', 'A', 'https://i.imgur.com/k83MFjs.gif', 425, 440, 450),
            ('Konan', 'A', 'https://i.imgur.com/3mOmZ0v.gif', 415, 410, 405),
            ('Kakuzu', 'A', 'https://i.imgur.com/BKf04A1.gif', 415, 405, 410),
            ('Sai', 'A', 'https://i.imgur.com/03ICbLj.gif', 395, 440, 430),

            # Personnages B
            
            ("Temari", "B", 'https://i.imgur.com/mDu5YOp.png', 310, 355, 305),
            ("Tenzo", "B", "https://i.imgur.com/ysZw0Ep.jpeg", 355, 315, 340), 
            ("Neji Hyuga", "B", "https://i.imgur.com/acFMgGN.png", 325, 330, 305),
            ("Kankuro", "B", 'https://i.imgur.com/6h0fZTJ.png', 355, 305, 355),
            ("Chiyo", "B", 'https://i.imgur.com/FTca3VV.jpeg', 305, 355, 310),
            ("Choji Akimichi", "B", 'https://media1.tenor.com/m/FAqetz7SiCEAAAAd/choji.gif', 305, 345, 365), 
            ("Shino Aburame", "B", 'https://i.imgur.com/efEUsM9.jpeg', 355, 305, 355),
            ("Kiba Inuzuka", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808361778567970876/KIBA Inuzuka.gif', 305, 355, 305),
            ("Ino Yamanaka", "B", 'https://media1.tenor.com/m/tdptC0lOIB4AAAAC/ino-yamanaka-ino.gif', 325, 305, 315),
            ("Sakura Haruno", "B", 'https://cdn.discordapp.com/attachments/804401351080542269/808354355744342026/SAKUA.gif', 305, 355, 335),
            ("Hinata Hyuga", "B", 'https://i.imgur.com/VsFYMA1.gif', 355, 325, 350),
            ("Suigetsu Hozuki", "B", 'https://i.imgur.com/E6d3rSt.gif', 305, 355, 310),
            ("Jugo", "B", 'https://i.imgur.com/lfSps90.png', 370, 325, 365),
            ("Kurenai Yuhi", "B", 'https://i.imgur.com/1E2Ux2a.png', 305, 335, 310),
            ("Zabuza Momochi", "B", "https://i.imgur.com/ntmenx6.png", 310, 355, 320),
            ("Mito Uzumaki", "B", "https://i.imgur.com/rSHfKaR.jpeg", 310, 355, 320),
            ("Kimimaro", "B", "https://i.imgur.com/eo5zyPh.png", 310, 355, 320),

            # Personnages C
            ("Konohamaru Sarutobi", "C", "https://i.imgur.com/8rusox0.jpeg", 260, 265, 240),
            ("Haku", "C", 'https://i.imgur.com/vqQD56N.png', 240, 260, 250),
            ("Anko", "C", "https://i.imgur.com/AkVeaHD.png", 230, 235, 240),
            ("Guren", "C", "https://i.imgur.com/gSqZiqy.jpeg", 250, 260, 260),
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
            ("Mizuki", "E", "https://i.imgur.com/Qa4UTvW.png", 120, 125, 115),

            # Personnages F
            ("Nawaki", "F", "https://i.imgur.com/k5iscPr.png", 30, 50, 10),
            ("Tonton", "F", "https://i.imgur.com/Jbrlu7U.jpeg", 10, 10, 10),
            ("Pakkun", "F", "https://i.imgur.com/VBxE1Z8.png", 30, 25, 40),
            ("Inari", "F", "https://i.imgur.com/ce76C3Z.png", 20, 30, 20),
],
            "One Piece" : [ # ✅
            # Personnages X
            ("Kaido", "X", "https://i.imgur.com/BMDbkl8.gif", 1000, 990, 1010),
            ("Monkey D. Luffy", "X", "https://i.imgur.com/EmzijMq.gif", 950, 940, 930), # TOREVIEW
            ("Big Mom", "X", "https://i.imgur.com/tPjCbUc.gif", 1005, 910, 1000),
            ("Marshall D. Teach", "X", "https://i.imgur.com/Y4vdAQ4.gif", 970, 1000, 965),
            ("Edward Newgate", "X", "https://i.imgur.com/BdnDfQj.gif", 1000, 1050, 1010),
            ("Shanks", "X", "https://i.imgur.com/faZclqg.gif", 930, 970, 930),
            ("Monkey D. Dragon", "X", "https://i.imgur.com/Zy9hmOz.gif", 930, 950, 915),
            ("Gol D. Roger", "X", "https://i.imgur.com/jhHkjfz.gif", 940, 970, 930),
            ("Dracule Mihawk", "X", 'https://i.imgur.com/UICGMYV.gif', 935, 980, 915),
            
            # Personnages SS
            ("Akainu", "SS", "https://i.imgur.com/OkB0Vk3.gif", 730, 790, 745), # high ss
            ("Aokiji", "SS", 'https://i.imgur.com/LCqY9UI.gif', 700, 720, 725),
            ("Kizaru", "SS", 'https://i.imgur.com/q0a4tsq.gif', 720, 780, 760),
            ("Fujitora", "SS", 'https://i.imgur.com/OxgHvz2.gif', 720, 760, 725),#TO REVIEW
            ("Silvers Rayleigh", "SS", 'https://i.imgur.com/HzaJdFI.gif', 790, 830, 730), # high ss
            ("Charlotte Katakuri", "SS", 'https://i.imgur.com/5z0sR8N.gif', 725, 770, 735),
            ("Ryokugyu", "SS", 'https://i.imgur.com/0QTPpqW.gif', 710, 720, 700),
            ("Monkey D. Garp", "SS", 'https://i.imgur.com/ZLd4sdw.gif', 750, 780, 750),
            ("Don Quichotte Doflamingo", "SS", 'https://i.imgur.com/ci7HIam.gif', 730, 720, 725),
            ("Trafalgar D. Water Law", "SS", 'https://i.imgur.com/xJpnwDU.png', 715, 740, 710),
            ("Eustass Kid", "SS", 'https://i.imgur.com/5WxLV4L.gif', 715, 740, 720),
            ("Roronoa Zoro", "SS", 'https://i.imgur.com/fPok6pt.gif', 715, 750, 720),
            ("Kozuki Oden", "SS", 'https://i.imgur.com/mACnc1L.jpg', 710, 745, 720),
            ("King", "SS", 'https://i.imgur.com/Rk55TO7.gif', 715, 720, 710),
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
            ("Sanji", "S", 'https://i.imgur.com/tngG5vW.gif', 540, 555, 550),
            ("Portgas D. Ace", "S", "https://i.imgur.com/8AGmDrS.gif", 550, 600, 620),
            ("Rob Lucci", "S", "https://i.imgur.com/aewCvhP.gif", 560, 570, 560),

            # Personnages A
            ("Jewelry Bonney","A","https://i.imgur.com/HBR63xX.gif", 420, 415, 425),
            ("Caesar Clown", "A", "https://i.imgur.com/YxmbkTD.gif", 430, 415, 425),
            ("Vergo", "A", "https://i.imgur.com/qSwhEar.gif", 445, 420, 395),
            ("Urouge", "A", "https://i.imgur.com/qqVrtD6.jpeg", 430, 415, 425),
            ("Bartholomew Kuma", "A", "https://i.imgur.com/chLQErz.gif", 395, 420, 445),
            ("Emporio Ivankov", "A", "https://i.imgur.com/5LxBHGh.jpeg", 445, 420, 395),
            ("Brook", "A", "https://i.imgur.com/Dusk4ZW.gif", 445, 420, 395),
            ("Nico Robin", "A", 'https://i.imgur.com/tiC5mlA.gif', 395, 420, 445),
            ("Jinbe", "A", 'https://i.imgur.com/5ktjcxG.png', 440, 420, 445),
            ("Karasu", "A", "https://i.imgur.com/M4BBxgI.gif", 395, 420, 445),
            ("Gecko Moria", "A", "https://i.imgur.com/6Xwg3x3.gif", 395, 420, 445),
            ("Yasopp", "A","https://i.imgur.com/KjovWi0.gif", 395, 410, 445),
            ("Nekomamushi", "A", "https://i.imgur.com/ssSfMFj.gif", 395, 420, 445),

            # Personnages B
            ("Chopper", "B", 'https://i.imgur.com/J4PGB24.gif', 300, 330, 365),
            ("Nami", "B", 'https://i.imgur.com/VAbsCsh.gif', 335, 330, 305),
            ("Usopp", "B", "https://i.imgur.com/dhRNN1S.jpeg", 330, 350, 315),
            ("Hina", "B", 'https://i.imgur.com/2tbPDP4.png', 315, 335, 345),
            ("Baggy", "B", "https://i.imgur.com/uervCQy.png", 355, 330, 305),
            ("Lindbergh", "B", "https://i.imgur.com/a8tSh0n.jpeg", 330, 355, 305),
            ("Inazuma", "B", 'https://i.imgur.com/PyUiXXv.png', 305, 330, 355),
            ("Belo Betty", "B", "https://i.imgur.com/RSckfSk.jpeg", 355, 330, 305),
            ("Franky", "B", 'https://i.imgur.com/U08oSKn.gif', 340, 305, 355),
            ("Kaku", "B", 'https://i.imgur.com/9jRznLq.png', 305, 330, 345),
            ("Tsuru", "B", 'https://i.imgur.com/9KaHWA4.jpeg', 305, 330, 345),
            ("Doll", "B", "https://i.imgur.com/0yJtSwk.jpeg", 305, 330, 345),
            ("Magellan", "B", "https://i.imgur.com/5keN9ye.png", 335, 360, 355),

            # Personnages C
            ("Koby", "C", 'https://i.imgur.com/OtsQuBI.png', 305, 280, 240),
            ("Nefertari Vivi", "C", "https://i.imgur.com/16YOCq0.jpeg", 255, 260, 235),
            ("Kumadori", "C", "https://i.imgur.com/EXrO0fr.png", 235, 260, 285),
            ("Don Krieg", "C", "https://i.imgur.com/JvWP2oH.jpeg", 285, 260, 235),
            ("Tashigi", "C", "https://i.imgur.com/owoWRA7.jpeg", 235, 260, 285),
            ("Don Quichotte Rossinante","C", "https://i.imgur.com/TN4CrB6.jpeg", 285, 260, 235),
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
            ("Kenpachi Zaraki", "SS", "https://i.imgur.com/DCS6I2N.gif", 705, 770, 715),
            ("Jugram", "SS", "https://i.imgur.com/kXmvoS6.gif", 705, 750, 695),
            ("Shunsui Kyoraku", "SS", "https://i.imgur.com/7DGfP2z.gif", 745, 850, 705),
            ("Byakuya Kuchiki", "SS", "https://i.imgur.com/VZrc8mU.gif", 695, 800, 725),
            ("Kisuke Urahara", "SS", "https://i.gifer.com/53FX.gif", 725, 800, 715),
            ("Yoruichi Shihoin", "SS", "https://i.imgur.com/RgC1S8V.gif", 705, 770, 715),
            ("Retsu Unohana", "SS", "https://i.imgur.com/b1x9GUC.gif", 695, 850, 755),
            ("Ulquiorra", "SS", "https://i.imgur.com/OaYNXCg.gif", 690, 800, 710),
            ("Gin Ichimaru", "SS", "https://i.imgur.com/kveTtpS.gif", 705, 750, 715),
            ("Coyote Stark", "SS", "https://i.imgur.com/SNpSgRB.gif", 700, 780, 720),
            ("Renji Abarai", "SS", "https://i.imgur.com/RptZEBF.gif", 725, 705, 720),
            ("Senjumaru Shutara", "SS", "https://i.imgur.com/EKWGM3I.gif", 715, 800, 725),
            ("Toshiro Hitsugaya", "SS", "https://i.imgur.com/R9S0Qa4.gif", 705, 720, 695),

            # Personnages S
            ("Mayuri", "S", "https://i.imgur.com/n8BNWm7.gif", 550, 600, 535),
            ("Sajin Komamura", "S", "https://i.imgur.com/6cf4JEH.gif", 600, 500, 550),
            ("Isshin Kurosaki", "S", "https://i.imgur.com/GTYbLGY.gif", 550, 550, 530),
            ("Rukia Kuchiki", "S", "https://i.imgur.com/IDjAqqP.gif", 550, 620, 560),
            ("Shinji Hirako", "S", 'https://i.imgur.com/9vxW0IN.gif', 550, 650, 540), 
            ("Soi Fon", "S", 'https://i.imgur.com/EVH34qM.gif', 550, 580, 545),
            ("Kaname Tosen", "S", 'https://i.imgur.com/4GA76X1.gif', 550, 550, 540),
            ("Baraggan", "S", 'https://i.imgur.com/k89CHqN.gif', 550, 570, 530),
            ("Grimmjow", "S", 'https://i.imgur.com/nj464jc.gif', 580, 600, 540),
            ("Uryu Ishida", "S", "https://i.imgur.com/AC2f6Ey.gif", 550, 600, 540),
            ("Ryuken Ishida", "S", 'https://i.imgur.com/turdL6j.gif', 540, 550, 520),

            # Personnages A
            ("Shukuro Tsukishima", "A", 'https://i.imgur.com/fBdRioG.gif', 420, 430, 410),
            ("Jushiro Ukitake", "A", 'https://i.imgur.com/PqGvVzv.gif', 395, 420, 405), 
            ("Halibel", "A", 'https://i.imgur.com/2OGaKON.gif', 410, 420, 430),
            ("Nnoitra Gilga", "A", 'https://i.imgur.com/900y7K5.gif', 440, 450, 460),
            ("Shuhei", "A", 'https://i.imgur.com/rkQNMQX.gif', 415, 435, 420),
            ("Orihime Inoue", "A", 'https://i.imgur.com/mbLrky4.gif', 430, 420, 460),
            ("Kugo Ginjo", "A", 'https://i.imgur.com/xLPLs5Q.gif', 410, 420, 430),
                
            # Personnages B
            ("Rangiku Matsumoto", "B", 'https://i.imgur.com/g2kazQy.jpeg', 320, 330, 310),
            ("Izuru Kira", "B", 'https://i.imgur.com/H5EQmb0.png', 330, 340, 320),
            ("Ikkaku", "B", 'https://i.imgur.com/wWd1Z4z.png', 345, 360, 335),
            ("Chad", "B", "https://i.imgur.com/o4eSlWY.jpeg", 340, 360, 330),
            ("Yumichika", "B", "https://i.imgur.com/mC8r7ka.jpeg", 320, 330, 340),
            ("Ginrei Kuchiki", "B", "https://i.imgur.com/Gdg23jz.png", 330, 340, 320),

            # Personnages C
            ("Ganju Shiba", "C", 'https://i.imgur.com/4HYU47B.png', 245, 255, 240),
            ("Soken Ishida", "C", "https://i.imgur.com/C3fEyfa.png", 240, 255, 260),
            ("Masaki Kurosaki","C","https://i.imgur.com/o6oX1Q6.jpeg", 250, 230, 270),
            
            # Personnages D
            ("Hanataro", "D", 'https://i.imgur.com/MPaOL4G.png', 185, 170, 180),
            ("Yachiru Kusajishi", "D", 'https://i.imgur.com/6mO9KFd.jpeg', 180, 190, 175),

            # Personnages E
            ("Kanae Katagiri", "E", 'https://i.imgur.com/6U0m5dX.jpeg', 135, 150, 125),

            # Personnages F
            ("Keigo Asano", "F", 'https://i.imgur.com/D8dqhs2.png', 40, 35, 35),
            ("Yuzu Kurosaki", "F", 'https://i.imgur.com/Spca2oo.png', 40, 35, 35),
            ("Kon", "F", 'https://i.imgur.com/t1az2SQ.png', 45, 50, 55),
            ("Karin Kurosaki", "F", 'https://i.imgur.com/J0b52LT.jpeg', 30, 35, 35),
            ("Mizuiro Kojima", "F", 'https://i.imgur.com/b4sfzoT.png', 45, 55, 50),
            
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
            ("Shinji Hirako Nishiya", "S", "https://i.imgur.com/J2ebGS2.gif", 500, 555, 510),
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
            
            ('Mount Lady', 'A', 'https://i.imgur.com/BGdhXVd.gif', 405, 400, 450) ,
            ('Gran Torino', 'A', 'https://i.imgur.com/pHGoXST.gif', 405, 440, 395) ,
            ('Nighteye', 'A', 'https://i.imgur.com/fgO8qfb.gif', 375, 380, 415) ,
            ('Midnight', 'A', 'https://i.imgur.com/RywB3Hh.gif', 375, 450, 385) ,
            ('Himiko Toga', 'A', 'https://i.imgur.com/YWZtjvt.gif', 410, 385, 430) ,
            ('Snipe', 'A', 'https://i.imgur.com/C5qxDQC.gif', 455, 465, 430) ,
            
            # Personnages B
            ('Tenya Iida', 'B', 'https://i.imgur.com/XAE3t5c.gif', 365, 360, 375) ,
            ('Denki Kaminari', 'B', 'https://i.imgur.com/aq2fHI5.png', 340, 350, 315) ,
            ('Momo Yaoyorozu', 'B', 'https://i.imgur.com/3knQkZJ.jpeg', 380, 305, 360) ,
            ('Neito Monoma', 'B', 'https://i.imgur.com/Px0oEH3.jpeg', 335, 280, 330) ,
            ('Ochaco Uraraka', 'B', 'https://i.imgur.com/GqBcqOI.jpeg', 335, 285, 315) ,
            ("Sajin Higawara", "B", "https://i.imgur.com/65Xg5il.png", 300, 350, 305),

            # Personnages C
            ("Ibara Shiozaki", "C", "https://i.imgur.com/psEieZz.jpeg", 285, 260, 235),
            ('Shindo', 'C', 'https://i.imgur.com/I7uLCYw.jpeg', 285, 285, 270) ,
            ('Rock Lock', 'C', 'https://i.imgur.com/s3iBS2y.jpeg', 305, 300, 250) ,
            ('Vlad King', 'C', 'https://i.imgur.com/v4AGxIS.jpeg', 295, 215, 245) ,
            ('Mezo Shoji', 'C', 'https://i.imgur.com/lCTpZJE.jpeg', 255, 260, 305) ,
            ('Spinner', 'C', 'https://i.imgur.com/MeW1vaE.jpeg', 295, 210, 275) ,
            ('Shihai Kuroiro', 'C', 'https://i.imgur.com/SIaA75c.jpeg', 280, 230, 295) ,
            ('Kyoka Jiro', 'C', 'https://i.imgur.com/R8DEMdM.jpeg', 220, 255, 215) ,
            
            # Personnages D
            ("Mustard", "D", 'https://i.imgur.com/XXetteA.jpeg', 160, 130, 150),
            ("Mineta", "D", 'https://i.imgur.com/gORmmMX.jpeg', 160, 130, 150),
            ("Fuyumi Todoroki", "D", 'https://i.imgur.com/N2lcbwf.jpeg', 150, 130, 160),
            
            # Personnages E
            ("Toru Hagakure", "E", 'https://i.imgur.com/xLnDIV4.png', 110, 120, 115),
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
            ("Silva Zoldyck", "SS", "https://i.imgur.com/wPRq2Yr.gif", 720, 760, 730),
            ("Hisoka", "SS", 'https://i.imgur.com/l69c0NZ.gif', 720, 730, 725),
            ("Neferopito", "SS", "https://i.imgur.com/5PkF2QA.gif", 800, 780, 790), # SS+
            ("Pufu", "SS", "https://i.imgur.com/CfoSEeD.gif", 780, 700, 800),
            # ("Razor", "SS", 'https://i.imgur.com/LZ1bwdl.gif', 700, 730, 700), #TOREVIEW 
            ("Yupi", "SS", "https://i.imgur.com/tWZDibP.gif", 790, 800, 810),
            ("Kurapika", "SS", 'https://i.imgur.com/57tv3pj.gif', 720, 710, 700),

            # Personnages S
            ("Kaito", "S", "https://i.imgur.com/RehnXP7.gif", 530, 580, 535),
            ("Feitan", "S", "https://i.imgur.com/X3AVK76.gif", 525, 650, 515),
            ("Kirua Zoldyck", "S", 'https://i.imgur.com/2sLrUqa.gif', 520, 610, 520),
            ("Uvogin", "S", 'https://i.imgur.com/WNRMtlT.gif', 540, 590, 560),
            ("Nobunaga", "S", 'https://i.imgur.com/1UMIlo3.gif', 520, 580, 520),
            ("Machi", "S", "https://i.imgur.com/HCAKZfB.gif", 520, 575, 520),
            ("Phinks", "S", "https://i.imgur.com/5ZBeio4.gif", 530, 575, 525),
            ("Bonolenov Ndongo", "S", "https://i.imgur.com/WNj1k2B.gif", 520, 565, 530), #TOREVIEW 
            ("Biscuit Kruger", "S", 'https://i.imgur.com/3WUyIRV.gif', 560, 570, 555),
            
            # Personnages A
            ("Botobai Gigante", "A", "https://i.imgur.com/mjz1Chv.png", 430, 450, 440),
            ("Morel Mackernasey", "A", 'https://i.imgur.com/FnQu94R.gif', 430, 400, 420),
            ("Knuckle Bine", "A", 'https://i.imgur.com/sMDxcKR.gif', 420, 415, 410), 
            ("Karuto Zoldyck", "A", "https://i.imgur.com/gHUEoiA.gif", 415, 420, 410),
            ("Sharnalk", "A", 'https://i.imgur.com/EwSJxbs.gif', 420, 430, 400),
            ("Franklin", "A", "https://i.imgur.com/xoln4Ly.gif", 410, 420, 400),
            ("Shizuku Murasaki", "A", "https://i.imgur.com/f0Yt32C.gif", 410, 415, 405),
            ("Genthru", "A", 'https://i.imgur.com/WtnOU7k.gif', 400, 440, 420),
            ("Cheetu", "A", "https://i.imgur.com/ZqFKcDD.gif", 420, 430, 410),
            ("Zazan", "A", "https://i.imgur.com/LpXVPsM.gif", 430, 420, 430),   
            ("Shoot", "A", 'https://i.imgur.com/tU2Fwq6.gif', 410, 430, 430),
            ("Pariston Hill", "A", 'https://i.imgur.com/71ouSTW.gif', 420, 440, 420),
            ("Pamu Shiberia", "A", 'https://i.imgur.com/AJTBunT.gif', 430, 440, 420),

            # Personnages B
            ("Leorio", "B", 'https://i.imgur.com/NBFxlLS.gif', 320, 350, 325),
            ("Gotoh", "B", 'https://i.imgur.com/hYXIzdH.png', 330, 350, 330),
            ("Mike", "B", 'https://i.imgur.com/Opybqgn.jpeg', 330, 340, 335),
            ("Wing", "B", 'https://i.imgur.com/h8Btyhj.png', 320, 310, 315),
            ("Pakunoda", "B", "https://i.imgur.com/IxWVTzo.gif", 330, 340, 320),
            ("Korutopi", "B", "https://i.imgur.com/uqHvQrZ.jpeg", 325, 335, 315),
            ("Koruto", "B", "https://i.imgur.com/QwL2k3G.png", 340, 330, 340),
            ("Meleoron", "B", "https://i.imgur.com/tcEdwmU.jpeg", 325, 335, 330),
            ("Ikarugo", "B", "https://i.imgur.com/P3Jc5JY.png", 300, 350, 315),
            ("Tsezugera", "B", "https://i.imgur.com/3WvsTfn.png", 320, 350, 320),
            
            # Personnages C
            ("Satotsu", "C", 'https://i.imgur.com/QQS66Kw.jpeg', 250, 270, 260),
            ("Pokkle", "C", "https://i.imgur.com/7A9UCci.png", 240, 275, 235),
            ("Menchi", "C", "https://i.imgur.com/OYoD8tt.jpeg", 270, 260, 255),
            ("Kanaria", "C", "https://i.imgur.com/tSSM35N.jpeg", 270, 260, 255),
            ("Zushi", "C", "https://i.imgur.com/zFDjx8z.png", 265, 275, 255),
            ("Guido", "C", "https://i.imgur.com/6EeZcNz.png", 245, 250, 240),
            ("Sadaso", "C", "https://i.imgur.com/e2ppqVH.jpeg", 250, 260, 240),
            ("Senritsu", "C", "https://i.imgur.com/1PhNNbj.jpeg", 250, 230, 240),

            # Personnages D
            ("Ponzu", "D", 'https://i.imgur.com/f4vOKAP.png', 150, 190, 140),
            ("Kikyo Zoldyck", "D", "https://i.imgur.com/AoZVrw6.png", 160, 180, 170),
            ("Vezze", "D", "https://i.imgur.com/4sIsZtP.jpeg", 150, 180, 160),

            # Personnages E
            ("Tompa", "E", "https://i.imgur.com/ms2R2ki.png", 115, 105, 110),
            ("Todo", "E", "https://i.imgur.com/DAVdi3M.jpeg", 125, 100, 105),
            ("Majtani", "E", "https://i.imgur.com/DmJoWX5.jpeg", 95, 120, 115),
            ("Leluto", "E", "https://i.imgur.com/wgyMHWc.png", 110, 110, 110),
            ("Jones", "E", "https://i.imgur.com/MShzS9R.png", 120, 105, 105),
            ("Miruki Zoldyck", "E", "https://i.imgur.com/IcwaCHD.jpeg", 110, 110, 110),
            ("Neon Nostrad", "E", 'https://i.imgur.com/Rz5HGeZ.png', 95, 115, 120),
            ("Pegui", "E", 'https://i.imgur.com/u2tYaqs.jpeg', 100, 110, 120),
            
            # Personnages F
            ("Mito Freecss", "F", 'https://i.imgur.com/Yy7iG5d.png', 45, 50, 45),
            ("Capitaine", "F", 'https://i.imgur.com/Q3iev4b.png', 50, 45, 45),
            ("Beans", "F", 'https://i.imgur.com/ZH36bXI.jpeg', 40, 50, 50),
            ("Komugi", "F", 'https://i.imgur.com/4VchruE.png', 55, 45, 40),
            ("Kon (hxh)", "F", 'https://i.imgur.com/rMn0Ukz.png', 40, 45, 55),
            ],
            "Avatar" : [ # ✅
            # Personnages X
            ("Aang", "X", "https://i.imgur.com/TqtpU5Q.gif", 930, 920, 925),

            # Personnages SS7
            ("Korra", "SS", "https://i.imgur.com/VQDla9K.gif", 750, 800, 775),
            ("Ozai", "SS", "https://i.imgur.com/guyw0WL.gif", 710, 760, 705),
            ("Iroh", "SS", "https://i.imgur.com/KSigNP8.gif", 690,740,695),
            ("Azula", "SS", "https://i.imgur.com/GT1KSqZ.gif", 660, 720, 685),
            ("Zuko", "SS", "https://i.imgur.com/VLqP4QM.gif", 670, 710, 700),
            ("Katara", "SS", "https://i.imgur.com/4hOIpNj.gif", 700, 720, 725),

            # Personnage S
            ("Hama", "S", "https://i.imgur.com/zY9YU3f.jpeg", 550, 600, 555),
            ("Toph Beifong", "S", "https://i.imgur.com/Bjbn4ew.gif", 530, 580, 535),

            # Personnages A
            ("Mai", "A", "https://i.imgur.com/opVoND8.gif", 400, 440, 410),

            # Personnages 
            ("Ty Lee", "B", "https://i.imgur.com/XFnYb26.jpeg", 390, 320, 400),
            ("Sokka", "B", "https://i.imgur.com/VMVIHVh.png", 350, 380, 360),
            # Personnages C
            
            # Personnages D   

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
            ("Yuta Okkotsu", "SS", "https://i.imgur.com/sOVy5yY.gif", 750, 790, 785),
            ("Mahoraga", "SS", "https://i.imgur.com/X3JpLMk.gif", 850, 850, 850),
            ("Toji Fushiguro", "SS", 'https://i.imgur.com/ADEDLzY.gif', 720, 780, 760),
            ("Aoi Todo", "SS", 'https://i.imgur.com/bxOhA1a.gif', 700, 730, 720),
            ("Suguru Geto", "SS", 'https://i.imgur.com/ZetAyjs.gif', 700, 750, 670),
            ("Choso", "SS", 'https://i.imgur.com/tPHJtTO.gif', 730, 740, 760),
            ("Mahito", "SS", 'https://i.imgur.com/PkMQGso.gif', 650, 730, 700),
            ("Jogo", "SS", 'https://i.imgur.com/iyNljeL.gif', 700, 750, 700),
            ("Uraume", "SS", 'https://i.imgur.com/Ay1WmqD.gif', 705, 740, 700),
            ("Kinji Hakari", "SS", 'https://i.imgur.com/zko2NRY.jpeg', 777, 777, 777),
            ("Yuki Tsukumo", "SS", 'https://i.imgur.com/WlIBwGu.png', 700, 800, 700),
            ("Hanami","SS","https://i.imgur.com/eO8Ezjm.gif", 700, 730, 800),
            ("Dagon", "SS", 'https://i.imgur.com/Arh6UMF.gif', 700, 760, 700),

            # Personnages S
            ("Megumi Fushiguro", "S", "https://i.imgur.com/ZrNNA55.gif", 550, 610, 515),
            ("Maki Zenin", "S", 'https://i.imgur.com/Lq88cmA.gif', 590, 505, 685),
            ("Kento Nanami", "S", 'https://i.imgur.com/phtWBmN.png', 580, 610, 570),
            ("Hiromi Higuruma", "S", 'https://i.imgur.com/VnEkm6V.jpeg', 550, 585, 525),
            ("Naobito Zenin", "S", 'https://i.imgur.com/kZIq6lC.gif', 505, 595, 545),
            ("Mei mei", "S", 'https://i.imgur.com/KoWiulR.png', 525, 565, 535),
            ("Naoya Zenin", "S", 'https://i.imgur.com/LiKy4we.png', 510, 590, 540),
            ("Yuji Itadori", "S", "https://i.imgur.com/75H1WqO.gif", 600, 570, 600),
            
            #Personnages A
            ("Toge Inumaki", "A", 'https://i.imgur.com/D7071yc.gif', 400, 420, 400), 
            ("Noritoshi Kamo", "A", 'https://i.pinimg.com/originals/2d/3c/53/2d3c5328dffe60e4905ec51c4c50026d.gif', 400, 450, 420),
            ("Kokichi Muta", "A", 'https://i.imgur.com/bjBDlk6.gif', 430, 400, 440),
            ("Atsuya Kusakabe", "A", 'https://i.imgur.com/8pLkOzr.gif', 390, 400, 410),

            # Personnages B
            ("Panda", "B", 'https://i.imgur.com/32zGh1W.jpeg', 340, 320, 330),
            ("Nobara Kugisaki", "B", "https://i.imgur.com/ToHbnHv.jpeg", 320, 350, 320),
            ("Takuma Ino", "B", 'https://i.imgur.com/W3diIlg.png', 310, 360, 320),
            ("Masamichi Yaga", "B", 'https://i.imgur.com/R8Rq12y.png', 330, 310, 330),
            ("Yoshinobu Gakuganji", "B", 'https://i.imgur.com/uAnAEms.png', 310, 340, 320),
            ("Eso", "B", 'https://i.imgur.com/zdA6uXn.jpeg', 330, 320, 330),
            
            # Personnages C
            ("Mai Zenin", "C", 'https://i.imgur.com/1mbSfCf.jpeg', 240, 260, 250),
            ("Junpei", "C", 'https://i.imgur.com/7sVsWn3.png', 240, 260, 220),
            ("Momo Nishimiya", "C", "https://i.imgur.com/q0viuTx.png", 240, 260, 230),
            ("Utahime Iori", "C", 'https://i.imgur.com/IPp6E9q.png', 240, 280, 260),
            ("Juzo Kumiya", "C", "https://i.imgur.com/lkcQCxs.png", 250, 270, 260),
            ("Haruta Shigemo", "C", "https://i.imgur.com/IY5zel0.jpeg", 240, 255, 220),
            ("Kechizu", "C", "https://i.imgur.com/fwEMmNC.png", 220, 220, 195),

            # Personnages D
            ("Shoko Ieiri", "D", 'https://i.imgur.com/uGNxheA.jpeg', 160, 180, 150),
            ("Kasumi Miwa", "D", "https://i.imgur.com/M0twNwm.png", 180, 200, 165),

            # Personnages E
            ("Ijichi", "E", "https://i.imgur.com/6EKKkX3.jpeg", 110, 120, 125),
            ("Yu Haibara", "E", "https://i.imgur.com/Ab850TD.jpeg", 120, 110, 130),
            ("Arata Nitta", "E", "https://i.imgur.com/FTzWovu.png", 120, 80, 130),
            # Personnages F
            ("Akari Nitta", "F", "https://i.imgur.com/jpzTp42.png", 35, 50, 50),
            ("Riko Amanai", "F", "https://i.imgur.com/WkfCzwy.jpeg", 20, 15, 20),
            ("Tsumiki Fushiguro", "F", "https://i.imgur.com/wNU5qjd.png", 15, 30, 30),          
            ],
            "Jojo's Bizarre Adventure" : [ # ✅
            # Personnages X
            ("Giorno Giovanna", "X", 'https://i.imgur.com/iJ9oUE1.gif', 900, 1200, 950),
            ("Enrico Pucci", "X", 'https://i.imgur.com/lAyHni9.gif', 950, 1200, 900),
            ("Funny Valentine", "X", "https://i.imgur.com/4ugvBxu.jpeg", 950, 1050, 950),
            ("Johnny Joestar", "X", "https://i.imgur.com/cgLbkoE.gif", 950, 1100, 900),

            # Personnages SS
            ("Gyro Zeppeli", "SS", "https://i.imgur.com/qDnzVD7.gif", 700, 750, 700),
            ("Kars", "SS", 'https://i.imgur.com/4xhIuVK.gif', 850, 850, 850),
            ("Diavolo", "SS", 'https://i.imgur.com/90RxqGR.gif', 750, 850, 700),
            ("Jotaro Kujo", "SS", 'https://i.imgur.com/XzBAKKf.gif', 750, 800, 750),
            ("Diego Brando", "SS", "https://i.imgur.com/Ncp5cvE.jpeg", 740, 800, 730), #TOREVIEW
            ("Dio Brando", "SS", 'https://i.imgur.com/xngzKOg.gif', 800, 850, 750),
            ("Kira Yoshikage", "SS", 'https://i.imgur.com/o5EUpnv.gif', 700, 800, 700),

            # Personnages S
            ("Josuke Higashikata", "S", 'https://i.imgur.com/AcnhlnJ.gif', 550, 580, 550), #TOREVIEW
            ("Fugo (Purple Haze)", "S", 'https://i.imgur.com/gBcvGNj.gif', 550, 600, 550), #TOREVIEW
            ("Vanilla Ice", "S", "https://i.imgur.com/VoH5XBm.gif", 550, 570, 550),#TOREVIEW
            ("Jolyne Kujo", "S", 'https://i.imgur.com/T2yg742.gif', 500, 550, 550),
            ("Weather Report", "S", "https://i.imgur.com/zHlZilS.gif", 550, 550, 550),

            # Personnages A
            ("Narciso Anasui", "A", "https://i.imgur.com/cQtCTf7.gif", 400, 450, 440),
            ("Bucciarati", "A", 'https://i.imgur.com/zaBAVFx.gif', 450, 470, 430),
            ("Risotto Nero", "A", 'https://i.imgur.com/hQxmpqR.gif', 440, 480, 400),
            ("Rohan Kishibe", "A", 'https://i.imgur.com/UJgfmGg.gif', 410, 440, 430),
            ("Kakyoin", "A", 'https://i.imgur.com/ZsxN3PG.gif', 440, 420, 400),
            ("Jean-Pierre Polnareff", "A", 'https://i.imgur.com/qhSRONk.gif', 430, 450, 410),
            ("Okuyasu Nijimura", "A", 'https://i.imgur.com/BiveNFJ.gif', 430, 450, 410),
            ("Ghiaccio", "A", 'https://i.imgur.com/LNoxXyi.gif', 440, 420, 400),
            ("Prosciutto", "A", 'https://i.imgur.com/CsSR05A.gif', 410, 420, 430),
            ("Mohamed Abdul", "A", "https://i.imgur.com/2fIG9TF.gif", 430, 420, 410),
            ("Cioccolata", "A", 'https://i.imgur.com/XAu2MDR.gif', 420, 400, 420),

            # Personnages B
            ("Koichi Hirose", "B", 'https://i.imgur.com/HZ9vn1d.png', 350, 360, 310),
            ("Akira Otoishi", "B", 'https://i.imgur.com/xn6pX9Z.png', 290, 370, 330),
            ("Narancia", "B", 'https://i.imgur.com/ndZcfok.png', 310, 350, 310),
            ("Yukako Yamagishi", "B", 'https://i.imgur.com/JZKQ2KS.png', 340, 330, 310),
            ("Wamuu", "B", 'https://i.imgur.com/2Jc0FTu.png', 330, 320, 350),
            ("Esidisi", "B", 'https://i.imgur.com/mdsI4Ir.png', 360, 320, 320),
            ("Mista", "B", 'https://i.imgur.com/ab9sgfg.png', 340, 360, 320),

            # Personnages C
            ("Joseph Joestar", "C", 'https://i.imgur.com/YiGGszt.png', 240, 265, 265),
            ("N'Doul", "C", 'https://i.imgur.com/Jn3ZtDS.jpeg', 250, 270, 260),
            ("Caesar Zeppeli", "C", 'https://i.imgur.com/3nzbH8Y.png', 250, 270, 260),
            ("Lisa Lisa", "C", 'https://i.imgur.com/YAcAs5c.jpeg', 260, 260, 250),
            ("Shigechi", "C", 'https://i.imgur.com/6JKniYe.png', 240, 230, 220),
            ("Iggy", "C", 'https://i.imgur.com/HTb59id.png', 250, 260, 220),
            ("Formaggio", "C", 'https://i.imgur.com/WCQtqwq.png', 260, 270, 220),
            ("Rudol Von Stroheim", "C", 'https://i.imgur.com/OvyOZy3.png', 280, 230, 240),
            ("Foo Fighters", "C", 'https://i.imgur.com/ZlCOCPn.png', 270, 240, 250),
            ("Trish", "C", 'https://i.imgur.com/I4nMHqt.png', 250, 270, 260),
            ("Hermes Costello", "C", 'https://i.imgur.com/TbkuZDj.jpeg', 290, 250, 240),
            ("Polpo", "C", 'https://i.imgur.com/2xxnmT8.jpeg', 260, 270, 250),

            # Personnages D
            ("Abbacchio", "D", 'https://i.imgur.com/5FahNJl.png', 200, 180, 170),
            ("Daniel J. D'Arby", "D", 'https://i.imgur.com/w1Qu1p2.jpeg', 160, 170, 180),
            ("Jonathan Joestar", "D", 'https://i.imgur.com/dqGKC1P.png', 220, 200, 160),

            # Personnages E
            ("Straizo", "E", 'https://i.imgur.com/D4muQp5.png', 100, 130, 110),
            ("Will Zeppeli", "E", 'https://i.imgur.com/SVm9I2K.png', 120, 130, 110),
            ("Boingo", "E", 'https://i.imgur.com/I1GDLQ9.jpeg', 100, 120, 130),
            ("Oingo", "E", 'https://i.imgur.com/4t8W7rq.jpeg', 140, 130, 120),

            # Personnages F
            ("Emporio", "F", 'https://i.imgur.com/KBZCTy6.png', 20, 20, 25),
            ("Tonio Trussardi", "F", 'https://i.imgur.com/PIXbcZb.png', 40, 60, 50),
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
            ("Saitama", "X", "https://steamuserimages-a.akamaihd.net/ugc/945077695993694686/15A47D5D02A75DB7700CBBC61706AB3CFD8FEEE2/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", 1050, 1300, 1050),
            ("Garou", "X", "https://i.pinimg.com/originals/a2/21/f2/a221f289576e45a0ed2fc3a5f6cb311e.gif", 1000,1000,1000),
            ("Boros", "X", "https://i.imgur.com/ehpRyuO.gif", 950, 940, 945),
            
            # Personnages SS
            ("Tatsumaki", "SS", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0a290752-d7eb-45e3-aa31-8e71b544cde0/ddx9bq9-b00980a3-8482-4791-bf64-f558046bb68f.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBhMjkwNzUyLWQ3ZWItNDVlMy1hYTMxLThlNzFiNTQ0Y2RlMFwvZGR4OWJxOS1iMDA5ODBhMy04NDgyLTQ3OTEtYmY2NC1mNTU4MDQ2YmI2OGYuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.tQyMqurmzcRYBak3ZNXQli2kTvbsZen9MPklCMs4dsw", 650, 800, 670),
            #("Blast", "SS", image_temporaire, 0, 0, 0),

            # Personnages S
            ("Metal Knight", "S", "https://64.media.tumblr.com/5366a39ff74f49fa99b3b75ddcdbbe5e/tumblr_nxv9s1PRxS1s4tq6xo1_500.gif", 555,555,555),
            ("Flashy Flash", "S", "https://i.pinimg.com/originals/65/d9/aa/65d9aaac5b9be737a85f1e3321a31751.gif", 500, 550, 540),
            ("Bang", "S", "https://www.serieously.com/app/uploads/2021/10/sylver.gif",550, 600, 550),
            ("Atomic Samurai", "S", "https://64.media.tumblr.com/cec8d995e77353273ab04fae8dc843bf/tumblr_o0nbzf0oCI1uxe4abo3_500.gif", 500, 550, 550),
            ("Genos", "S", "https://i.imgur.com/smmaKAc.gif", 580, 600, 550),

            # Personnages A
            ("Zombieman", "A", "https://64.media.tumblr.com/220b8ea9980e47660ccad29010900975/1c5ae4e6d2c27fda-14/s540x810/c999ca2299c96b4d60267133cd29a2de376586a9.gif",450, 400, 450),
            ("Metal Bat", "A", "https://img.wattpad.com/50bbff7a70c378858c50f33d312d7e9163bc23b2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f41385a745f354872705631354c773d3d2d33352e313566633933666232666339383461663232323833353634353235382e676966", 420, 430, 420),
            ("Sonic", "A", "https://i.imgur.com/jBcZEjt.gif", 390, 400, 390),
            
            # Personnages B
            ("Fubuki", "B", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/02/OK6W-koKDTOqqqLDbIoPArZF0g0L4GyCjAjQGnT5hNk-Cropped.png", 310, 330, 315),
            ("Child Emperor", "B", "https://i.imgur.com/Q0af6zO.jpeg",320, 350, 320),
            ("Puri Puri Prisoner", "B", "https://i.redd.it/1zy1fprswuk41.jpg", 340, 320, 330),

            # Personnages C
            ("Stinger", "C", "https://i.imgur.com/T5x0Azb.jpeg", 230, 220, 235),
            ("Sneck", "C", "https://static.wikia.nocookie.net/onepunchman/images/6/67/SneckProfile.png/revision/latest?cb=20161112181329", 220, 230, 225),

            # Personnages D
            ("Cyborgorilla", "D", "https://i.ytimg.com/vi/HJAt5DujlIw/maxresdefault.jpg", 180, 180, 180),

            # Personnages E
            ("Grimasse", "E", "https://static.wikia.nocookie.net/onepunchman/images/a/a4/Saitama_flippe_devant_Grimasse.png/revision/latest?cb=20190501171126&path-prefix=fr", 120, 120, 120),
            ("Crablante", "E", "https://static.wikia.nocookie.net/villains/images/a/a5/Crabrante.jpg/revision/latest?cb=20151214015216", 120, 120, 120),

            # Personnages F
            ("Mumen Rider", "F", "https://i.redd.it/diszh9zoizoa1.jpg", 45, 50, 55),
            ("King (OPM)", "F", "https://i.imgur.com/pGZbP5v.png", 50, 50, 50),
            ],
            "Demon Slayer" : [ # ✅ Ⓜ️
            # Personnages X
            ("Tanjiro Kamado", "X", "https://i.imgur.com/0ZbB8tr.gif", 950, 970, 930),
            ("Muzan", "X", "https://i.imgur.com/zXvC5Uj.gif", 940, 950, 930),
            ("Yoriichi Tsugikuni", "X", "https://i.imgur.com/q7ak3HD.gif", 990, 1050, 1000),
            ("Kokushibo", "X", "https://i.imgur.com/LZJio0L.gif", 940, 950, 950),

            # Personnages SS
            ('Gyomei Himejima', 'SS', 'https://i.imgur.com/lk7V07x.gif', 725, 655, 675) ,
            ('Doma', 'SS', 'https://i.imgur.com/ypkjkIk.gif', 695, 670, 740) ,
            ('Akaza', 'SS', 'https://i.imgur.com/uBwhGcG.gif', 710, 670, 665) ,

            # Personnages S
            ('Sanemi Shinazugawa', 'S', "https://i.imgur.com/gsRhxBO.gif", 535, 570, 540) ,
            ('Muichiro Tokito', 'S', "https://i.imgur.com/tha4jTx.gif", 530, 585, 550) ,
            ('Obanai Iguro', 'S', "https://i.imgur.com/bwibOHS.gif", 585, 570, 525) ,
            ('Giyu Tomioka', 'S', "https://i.imgur.com/7plvqYg.gif", 540, 595, 510) ,

            # Personnages A
            ('Kyojuro Rengoku', 'A', 'https://i.imgur.com/6HL02sP.gif', 425, 390, 465) ,
            ('Tengen Uzui', 'A', "https://i.imgur.com/oRjrWE4.gif", 410, 385, 440) ,
            ('Mitsuri Kanroji', 'A', "https://i.imgur.com/JypPx5K.gif", 410, 405, 445) ,
            ('Nezuko Kamado', 'A', "https://i.imgur.com/Vk0Bc6F.gif", 420, 375, 470) ,
            ('Kanao Tsuyuri', 'A', "https://i.imgur.com/nYnalOh.gif", 460, 410, 430) ,
            ('Tamayo', 'A', 'https://i.imgur.com/GVvrYyr.gif', 430, 430, 380) ,
            ('Shinobu Kocho', 'A', 'https://i.imgur.com/TK1yera.gif', 450, 420, 460) ,

            # Personnages B
            ('Kanae Kocho', 'B', 'https://i.imgur.com/fvwXtM1.png', 355, 330, 345) ,
            ('Zenitsu', 'B', 'https://i.imgur.com/ksfxArD.png', 355, 330, 345) ,
            ('Sakonji Urokodaki', 'B', 'https://i.imgur.com/DPD6gfY.jpeg', 355, 330, 345) ,
            ('Inosuke', 'B', 'https://i.imgur.com/h1Ek7Aa.jpeg', 300, 330, 315) ,
            ('Genya Shinazugawa', 'B', 'https://i.imgur.com/kE7DIxE.jpeg', 375, 305, 340) ,
            ('Daki', 'B', 'https://i.imgur.com/dNUE89G.jpeg', 380, 310, 305) ,
            ("Gyutaro", "B", "https://i.imgur.com/6JSHh00.jpeg", 380, 310, 305),
            ('Enmu', 'B', 'https://i.imgur.com/Ey0jwGH.jpeg', 330, 370, 305) ,

            # Personnages C
            ("Yahaba", "C", 'https://i.imgur.com/CkIj6SU.png', 255, 285, 265),
            ("Sabito", "C", 'https://i.imgur.com/YpzmuoS.jpeg', 255, 285, 265),
            ('Rui', 'C', 'https://i.imgur.com/bFzI5bu.jpeg', 220, 290, 250) ,
            ('Mukago', 'C', 'https://i.imgur.com/EH3xfU2.png', 220, 225, 285) ,
            ('Fille Araignee', 'C', 'https://i.imgur.com/8ExcM9G.jpeg', 255, 285, 265) ,
            ('Mere Araignee', 'C', 'https://i.imgur.com/ag5zn5R.png', 245, 225, 275) ,
            ('Jigoro Kuwajima', 'C', 'https://i.imgur.com/kijkJU1.jpeg', 300, 230, 245) ,

            # Personnages D
            ("Tanjuro Kamado", "D", 'https://i.imgur.com/ksFH87B.jpeg', 170, 180, 150),
            ("Ozaki", "D", 'https://i.imgur.com/z8e44Fl.jpeg', 160, 190, 140),

            # Personnages E
            ("Sumiyoshi", "E", 'https://i.imgur.com/vpx7b2g.jpeg', 120, 130, 110),
            ('Shinzu', 'E', 'https://i.imgur.com/OM3Yn5j.jpeg', 145, 100, 90) ,
            ('Murata', 'E', 'https://i.imgur.com/lNC5rbm.jpeg', 145, 140, 105) ,
            ('Kyogai', 'E', 'https://i.imgur.com/7VFZLBx.jpeg', 145, 115, 95) ,
            ('Kanamue', 'E', 'https://i.imgur.com/WYQmh9H.jpeg', 100, 115, 100) ,
            ('Kagaya Ubuyashiki', 'E', 'https://i.imgur.com/96vapZl.jpeg', 120, 150, 105) ,

            # Personnages F
            ('Chachamaru', 'F', 'https://i.imgur.com/F5RzFaL.png', 35, 60, 45) ,
            ('Aoi Kanzaki', 'F', 'https://i.imgur.com/QWv5qQG.jpeg', 30, 20, 20) ,
            ('Sumi Nakahara', 'F', 'https://i.imgur.com/WcLXKs0.gif', 20, 40, 50) ,
            ('Kiyo', 'F', 'https://i.imgur.com/l9MjiEs.jpeg', 45, 25, 30) ,
            ('Naho', 'F', 'https://i.imgur.com/LyTz20q.gif', 60, 30, 60) ,
            ('Kaburamaru', 'F', 'https://i.imgur.com/ZtQxLvw.jpeg', 60, 20, 40) ,
            ],
            "Full Metal Alchemist" : [ # ✅
            # Personnages X
            ("Père", "X", "https://i.imgur.com/X617w07.gif", 963, 963, 963),

            # Personnages SS
            ("Van Hoheinheim", "SS", "https://i.imgur.com/bMNh7n0.gif", 720, 730, 735),
            ("King Bradley", "SS", "https://i.imgur.com/Di7mjqq.gif", 750, 770, 750),

            # Personnages S
            ("Edward Elric", "S", "https://i.imgur.com/Lmbb9ZT.gif", 540, 555, 530),
            ("Izumi Curtis", "S", "https://i.imgur.com/WBcqtWl.gif", 535, 540, 530),
            ("Alphonse Elric", "S", 'https://i.imgur.com/q6IW5xU.gif', 560, 570, 600),
            ("Roy Mustang", "S", 'https://i.imgur.com/Oyk2Pp4.gif', 550, 700, 540), # high S
            ("Scar", "S", 'https://i.imgur.com/9dw5ri9.gif', 580, 600, 730), # high S
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
            ("Jean Havoc", "E", 'https://i.imgur.com/rM9I8Ot.jpeg', 120, 125, 115),
            ("Heymans", "E", 'https://i.imgur.com/jJdB2II.png', 125, 115, 120),
            ("Kain Fuery", "E", "https://i.imgur.com/6dCkq7z.jpeg", 120, 120, 120),
            ("Grumman", "E", 'https://i.imgur.com/ovxgZHa.png', 120, 120, 120),

            # Personnages F
            ("Yoki", "F", 'https://i.imgur.com/pPbOaqJ.jpeg', 35, 50, 35),
            ("Nina Tucker", "F", 'https://i.imgur.com/gOeHUXg.jpeg', 50, 45, 35),
            ("Trisha Elric", "F", 'https://i.imgur.com/QVYbkRB.jpeg', 35, 50, 35),
            ("Xiao Mei", "F", 'https://i.imgur.com/FAQHPlD.gif', 30, 55, 35),
            ("Winry Rockbell", "F", 'https://i.imgur.com/mbX301B.jpeg', 35, 55, 30),
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
            ("Tom Xaver", "A", "https://i.imgur.com/qr62Ecp.jpeg", 500, 330, 500),
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
            ("Dinah Yeager", "B", "https://i.imgur.com/RtgcmlR.jpeg", 300, 300, 300),

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
            ("Willy Teyber", "F", "https://i.imgur.com/M8eXW0o.jpeg", 40, 50, 40),
            ("Onyankopon", "F", "https://i.imgur.com/wylRQBl.jpeg", 50, 50, 50),
            ("Nicolo", "F", "https://i.imgur.com/cXQk7KZ.jpeg", 40, 45, 45)
            ],
            "Seven Deadly Sins" : [
            # """ PERSONNAGES NNT """
            # Personnages X
            ("Meliodas", "X", "https://i.imgur.com/raYGlJ7.gif", 940, 950, 920),
            ("Arthur Pendragon", "X", "https://i.imgur.com/0hVVugw.gif", 950, 970, 990),
            ("Estarossa", "X", "https://i.imgur.com/eXY3zUp.gif", 910, 950, 910),

            # Personnages SS
            ("Ban", "SS", "https://i.imgur.com/qJYVTXT.gif", 690, 720, 700),
            ("Escanor", "SS", "https://i.imgur.com/PVS7bUU.gif", 750, 770, 720),
            ("Zeldris", "SS", "https://i.imgur.com/qsRrdsM.gif  ", 710, 720, 690),
            ("King (NNT)", "SS", "https://i.imgur.com/TvSBMxY.jpeg", 720, 730, 710),
            ("Merlin", "SS", "https://i.imgur.com/2JIsj8m.gif", 705, 720, 710),
            ("Gowther", "SS", "https://i.imgur.com/uQlBrOy.gif", 720, 710, 700),
            ("Diane", "SS", "https://i.imgur.com/bVlSky7.gif", 750, 705, 730),

            # Personnages S
            ("Elizabeth Liones", "S", "https://i.imgur.com/ZZ4aO3i.gif", 620, 600, 620),
            ("Derrierie", "S", "https://i.imgur.com/Led5JQO.gif", 540, 550, 530),
            ("Gloxinia", "S", "https://i.imgur.com/IIR8AnU.gif", 520, 510, 540),
            ("Drole", "S", "https://i.imgur.com/CmH2Hrv.gif", 530, 520, 600),
            ("Galand", "S", "https://i.imgur.com/jOUsixh.gif", 520, 530, 525),

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
            ("Katana Man", "S", "https://i.imgur.com/8Bj3B08.gif", 565, 580, 575),
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
            ("Shaka", "S", "https://i.imgur.com/tkAVOuQ.gif", 620, 660, 640),
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
    (56, "Maitre du Hamon", "ATK", 0.4, "Le Hamon est une technique de combat qui utilise l'énergie du soleil pour attaquer les vampires.", image_temporaire, "#800080"),
    (57, "Mafioso", "ATK", 0.3, "La Passione est une organisation criminelle italienne qui contrôle le trafic de drogue.", image_temporaire, "#FF0000"),
    (58, "Team Bucciarati", "ATK", 0.3, "La Team Bucciarati est un groupe de gangsters qui travaillent pour la Passione.", image_temporaire, "#FFA500"),
    (59, "JoBros", "HP", 0.4, "Les JoBros sont les amis et allies des Joestars qui les aident dans leur combat contre le mal.", image_temporaire, "#0000FF"),
    (60, "Ile de Sirop", "DEF", 0.35, "L'ile de Sirop est une ile paradisiaque où les habitants vivent en paix et en harmonie.", image_temporaire, "#800080"),
    (61, "Equipage de Shanks", "ATK", 0.40, "L'equipage de Shanks est un groupe de pirates dirige par Shanks le Roux.", image_temporaire, "#0000FF"),
    (62, "Equipage de Kaido", "DEF", 0.45, "L'equipage de Kaido est un groupe de pirates dirige par Kaido le Cent betes.", image_temporaire, "#800080"),
    (63, "Equipage de Big Mom", "HP", 0.45, "L'equipage de Big Mom est un groupe de pirates dirige par Big Mom.", image_temporaire, "#FF0000"),
    (64, "Draconique", "ATK", 0.45, "Les Dragons sont des creatures mythiques qui possedent des pouvoirs magiques.", image_temporaire, "#FFA500"),
    (65, "Monstre de vitesse", "ATK", 0.50, "Les Monstre de vitesse sont des personnages qui ont un pouvoir leur permettant d'aller vite.", image_temporaire, "#0000FF"),
    (66, "Aveugle", "ATK", 0.40 , "Les Aveugles sont des personnages qui ont perdu la vue mais qui ont developpe d'autres sens pour compenser.", image_temporaire, "#800080"),
    (67, "Dojo de Bang", "ATK", 0.35, "Le Dojo de Bang est un lieu d'entrainement où les disciples apprennent les techniques de combat de Bang.", image_temporaire, "#FF0000"),
    (68, "Cyborg", "DEF", 0.40, "Les Cyborgs sont des etres humains qui ont ete ameliores avec des technologies cybernetiques.", image_temporaire, "#FFA500"),
    (69, "JoJo", "DEF", 0.45, "Les JoJos sont les membres de la famille Joestar qui luttent contre les forces du mal.", image_temporaire, "#0000FF"),
    (70, "Fléau", "ATK", 0.45, "Les Fleaux sont des creatures malefiques qui apportent la destruction et la mort partout où ils passent.", image_temporaire, "#800080"),
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
    (91, "Alchimiste", "HP", 0.40, "Les Alchimistes d'Etat sont des alchimistes qui servent le gouvernement d'Amestris.", image_temporaire, "#FF0000"),
    (92, "Xing", "HP", 0.45, "Le pays de Xing est un pays voisin d'Amestris qui pratique l'alchimie de l'est.", image_temporaire, "#FFA500"),
    (93, "Elric", "HP", 0.55, "La famille Elric est une famille d'alchilmistes (sauf la mere).", image_temporaire, "#0000FF"),
    (94, "Automail", "HP", 0.55, "L'Automail est une prothese mecanique qui remplace un membre perdu.", image_temporaire, "#800080"),
    (95, "Ishval", "ATK", 0.40, "Les Ishvals sont un peuple pacifique qui a ete decime par les alchimistes d'Amestris.", image_temporaire, "#FF0000"),
    (96, "Bradley", "ATK", 0.40, "La famille Bradley comporte deux Homonculus et est au pouvoir du pays.", image_temporaire, "#FFA500"),
    (97, "Unité Mustang", "ATK", 0.65, "L'Unité Mustang est une unite de l'armee d'Amestris dirigee par Roy Mustang.", image_temporaire, "#0000FF"),
    (98, "Lycée Yuei", "HP", 0.35, "L'U.A. est une école de heros où les etudiants apprennent à devenir des heros professionnels.", "ua.gif", "#800080"),
    (99, "Zoldyck", "ATK", 0.40, "La famille Zoldyck est une famille d'assassins qui sont les plus redoutes du monde.", "zoldyck.png", "#fde9e0"),
    (100, "Dix Commandements", "ATK", 0.60, "Les Dix Commandements sont les dix demons les plus puissants de l'Empire de Britannia.", "https://i.imgur.com/SMEji4z.jpeg", "#FF0000"),
    (101, "Péché capital", "ATK", 0.55, "Les Sept Péchés Capitaux sont un groupe de chevaliers qui ont trahi le royaume de Liones.", "https://i.imgur.com/CnvtvuO.jpeg", "#FFA500"),
    (102, "Annihilateur", "ATK", 0.60, "Les Dieux de la Destruction sont des divinites qui detruisent les planetes pour maintenir l'equilibre de l'univers.", "https://i.imgur.com/uxo372k.png", "#0000FF"),
    (103, "Ange", "ATK", 0.50, "Les Anges sont des etres celestes qui servent les dieux et protegent l'univers.", "https://i.imgur.com/xt9Tn0P.jpeg", "#ddeaef"),
    (104, "Famille de Son Goku", "ATK", 0.45, "La famille de Son Goku est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/cChWxf7.jpeg", "#FF0000"),
    (105, "Famille de Vegeta", "ATK", 0.45, "La famille de Vegeta est une famille de guerriers Saiyans qui protegent la Terre.", "https://i.imgur.com/eyN6Qg9.jpeg", "#FFA500"),
    (106, "Section 4 Anti-Demon", "ATK", 0.40, "La Section 4 Anti-Demon est une unite speciale de la police qui lutte contre les demons.", "https://i.imgur.com/dijQZFN.jpeg", "#0000FF"),
    (107, "Freecss", "HP", 0.50, "La famille Freecss est une famille de chasseurs qui cherchent des tresors et des creatures rares.", "https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/12/Gon-and-Ging-Freecss.jpg", "#800080"),
    (108, "Hunter étoilé", "HP", 0.40, "L'Association Hunter est une organisation de chasseurs qui traquent les creatures rares et les criminels. Les hunters étoilés sont leurs meilleurs atouts.", "https://i.imgur.com/fHvGkwX.jpeg", "#f40000"),
    (109, "Zodiac", "DEF", 0.40, "Les Zodiacs sont les douze membres du conseil des Hunters qui sont les plus puissants et les plus influents de l'Association Hunter.", "https://i.imgur.com/fHvGkwX.jpeg", "#FFA500"),
    (110, "Brigade Fantome", "ATK", 0.30, "La Brigade Fantome est une organisation criminelle qui lutte contre l'Association Hunter.", "https://i.imgur.com/2KZe6ug.gif", "#00000"),
    (111, "Forme de vie ultime", "DEF", 0.70, "Les formes de vie ultime sont des créatures ultimes qui dépassent les limites de l'humanité.", image_temporaire, "#00000"),
    (112, "Voleur de Pouvoir", "ATK", 0.65, "Les Voleurs de Pouvoir sont des individus qui volent les pouvoirs des autres pour les utiliser à leur avantage.", image_temporaire, "#00000"),
    (113, "Todoroki", "ATK", 0.40, "La famille Todoroki est une famille de heros qui possedent des pouvoirs de glace et de feu.", "https://i.imgur.com/69aINzI.jpeg", "#00000"),
    (114, "Héritier du One For All", "ATK", 0.70, "Les Heritiers du One For All sont des individus qui ont herite du pouvoir du One For All pour proteger le monde des vilains.", image_temporaire, "#00000"),
    (115, "Kuchiki", "ATK", 0.5, "La famille Kuchiki est une famille de nobles qui sont les gardiens du clan Kuchiki.", image_temporaire, "#00000"),
    (116, "Shimura" , "ATK", 0.4, "La famille Shimura est consituée de , sah flemme de finir mdrr", image_temporaire, "#00000"),
    (117, "Big 3", "HP", 0.80, "Le Big 3 est un groupe de trois etudiants de l'U.A. qui sont les plus forts de leur generation.", "https://i.imgur.com/195h0KM.png", "#00000"),
    (118, "Tireur d'Elite", "ATK", 0.55, "Les Snipers sont des tireurs d'elite qui peuvent atteindre des cibles à longue distance.", image_temporaire, "#00000"),
    (119, "Intangible", "DEF", 0.80, "Les Intangibles sont des individus qui peuvent devenir intangibles et traverser les objets solides.", image_temporaire, "#00000"),
    (120, "Kurosaki", "HP", 0.40, "La famille Kurosaki est une famille de chasseurs de Hollows qui protegent les humains des attaques des Hollows.", image_temporaire, "#00000"),
    (121, "Cinq Doyen", "HP", 0.60, "Les cinq doyens sont la Plus Haute Instance du Gouvernement Mondial.", "https://static.wikia.nocookie.net/onepiece/images/f/f9/Cinq_Doyens_Anime_Post_Ellipse_Infobox.png/revision/latest?cb=20221119194241&path-prefix=fr", "#00000"),
    (122, "Foetus des Neuf Phases", "HP", 0.65, "Les Foetus des Neuf Phases sont à l'origine neuf fœtus avortés issus du mélange entre une humaine et des fléaux. Mort-nés, ils sont devenus des reliques.", image_temporaire, "#00000"),
    (123, "Famille de Luffy", "HP", 0.40, "La famille de Luffy est une famille de pirates qui navigue sur les mers pour trouver le One Piece.", image_temporaire, "#00000"),
    (124, "ANBU", "ATK", 0.45, "Les ANBU sont une unite speciale de ninjas qui travaillent pour le Hokage.", image_temporaire, "#00000"),
    (125, "Tout Puissant", "ATK", 0.5, "Les Tout Puissants sont des individus qui possedent des pouvoirs divins et qui peuvent detruire des planetes entieres.", image_temporaire, "#00000"),
    (126, "Kujo", "ATK", 0.45, "La famille Kujo est une famille de Stand Users qui combattent les forces du mal.", image_temporaire, "#00000"),
    (127, "Manipulateur de Sang", "ATK", 0.65, "Les Manipulateurs de Sang sont des individus qui peuvent manipuler le sang pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (128, "CP-0", "DEF", 0.45, "Le CP-0 est une unite speciale de la Marine qui traque les criminels les plus dangereux du monde.", "https://staticg.sportskeeda.com/editor/2023/12/556eb-17027667692782-1920.jpg", "#00000"),
    (129, "Maître du Brouillard", "DEF", 0.45, "Les Maîtres du Brouillard sont des ninjas qui peuvent manipuler le brouillard pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (130, "Maitre des Fleaux", "ATK", 0.45, "Les Maitres des Fleaux sont des individus qui possedent des pouvoirs de fleaux et qui peuvent detruire des villes entieres.", image_temporaire, "#00000"),
    (131, "Dépourvu de pouvoir", "ATK", 0.65, "Les Dépourvus de pouvoir sont des individus qui n'ont pas de pouvoir et qui doivent utiliser des armes pour combattre.", image_temporaire, "#00000"),
    (132, "Classe S", "ATK", 0.50, "Les exorcistes de classe S sont les exorcistes les plus dangereux, ils sont capables de battre un pays entier", image_temporaire, "#00000"),
    (133, "Roi", "ATK", 0.50, "Un roi est un individu qui a le pouvoir absolu sur son royaume et qui peut faire ce qu'il veut.", image_temporaire, "#00000"),
    (134, "Prisonnier", "DEF", 0.45, "Les prisonniers sont des individus qui ont ete emprisonnes pour leurs crimes et qui doivent purger leur peine.", image_temporaire, "#00000"),
    (135, "Marionnettiste", "ATK", 0.65, "Les Marionnettistes sont des individus qui peuvent controler les autres par la force de leur volonte.", image_temporaire, "#00000"),
    (136, "Masqué", "DEF", 0.45, "Les Masqués sont des individus qui portent un masque pour cacher leur identite et proteger leur famille.", image_temporaire, "#00000"),
    (137, "Chanceux", "DEF", 0.45, "Les Chanceux sont des individus qui ont de la chance et qui reussissent toujours dans tout ce qu'ils entreprennent.", image_temporaire, "#00000"),
    (138, "Yandere", "DEF", 0.45, "Les Yandere sont des individus qui sont obsedes par leur amour pour quelqu'un et qui sont prets à tout pour le proteger.", image_temporaire, "#00000"),
    (139, "Ressuscité", "DEF", 0.20, "Les Ressuscités sont des individus qui ont ete ramenes a la vie apres leur mort.", image_temporaire, "#00000"),
    (140, "Sarutobi", "DEF", 0.45, "Les Sarutobis sont une famille de ninjas qui ont servi le village de Konoha pendant des generations.", image_temporaire, "#00000"),
    (141, "Changeur de Forme", "DEF", 0.55, "Les Métamorphes sont des individus qui peuvent changer de forme pour se fondre dans leur environnement.", image_temporaire, "#00000"),
    (142, "Berserker", "ATK", 0.75, "Les Berserkers sont des individus qui entrent dans une rage meurtriere et qui attaquent tout ce qui se trouve sur leur chemin.", image_temporaire, "#00000"),
    (143, "Imposteur", "DEF", 1, "Les Imposteurs sont des individus qui se font passer pour quelqu'un d'autre pour tromper leurs ennemis.", image_temporaire, "#00000"),
    (144, "Archer", "ATK", 0.55, "Les Archers sont des tireurs d'elite qui peuvent atteindre des cibles à longue distance.", image_temporaire, "#00000"),
    (145, "Prince", "DEF", 0.45, "Les Princesses sont des jeunes filles de la noblesse qui sont protegees par des gardes du corps.", image_temporaire, "#00000"),
    (146, "Soigneur", "HP", 0.45, "Les Soigneurs sont des medecins qui soignent les blessures et les maladies des autres.", image_temporaire, "#00000"),
    (147, "Manipulateur de l'ombre", "DEF", 0.45, "Les Manipulateurs de l'ombre sont des individus qui peuvent manipuler les ombres pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (148, "Glouton", "HP", 0.45, "Les Gloutons sont des individus qui ont un appetit insatiable et qui peuvent manger n'importe quoi.", image_temporaire, "#00000"),
    (149, "Mentor", "DEF", 0.45, "Les Mentors sont des enseignants qui enseignent aux eleves les matieres scolaires et les techniques de combat.", image_temporaire, "#00000"),
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
    (162, "Serviteur", "DEF", 0.65, "Les Serviteurs sont des individus qui gerent les affaires d'une organisation et qui s'assurent que tout fonctionne correctement.", image_temporaire, "#00000"),
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
    (179, "Magicien Traditionnel", "ATK", 0.55, "Les Magiciens sont des individus qui possedent des pouvoirs magiques et qui peuvent lancer des sorts pour attaquer leurs ennemis.", image_temporaire, "#00000"),
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
    (211, "Spirituel", "DEF", 0.65, "Les Prêtres sont des religieux qui servent les dieux et qui prient pour le salut de l'humanite.", image_temporaire, "#00000"),
    (212, "Utilisateur de Hache", "ATK", 0.45, "Les Utilisateurs de Hache sont des individus qui maitrisent l'art de la hache pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (213, "Résident de Morio", "HP", 0.60, "Les Habitants de Morio sont des habitants de la ville de Morio qui sont proteges par les Stand Users.", image_temporaire, "#00000"),
    (214, "Calamité", "ATK", 0.70, "Les Calamités sont des individus qui apportent la destruction et la mort partout où ils passent.", image_temporaire, "#00000"),
    (215, "Führer", "ATK", 0.90, "Les Führers sont des dictateurs qui dirigent leur pays d'une main de fer et qui oppriment leur peuple.", image_temporaire, "#00000"),
    (216, "Manieur de couteau", "ATK", 0.40, "Les Manieurs de couteau sont des individus qui maitrisent l'art du couteau pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (217, "Faucheur", "ATK", 0.75, "Les Faucheurs sont des individus qui utilisent des faux pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (218, "Arme dans chaque main", "ATK", 0.40, "Les individus qui ont une arme dans chaque main sont des combattants qui utilisent deux armes pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (219, "Esprit de Vengeance", "ATK", 0.60, "Les Esprits de Vengeance sont des personnes OMNIBULES par la vengeance.", image_temporaire, "#00000"),
    (220, "Voyou", "ATK", 0.45, "Les Voyous sont des individus qui vivent en marge de la societe et qui commettent des crimes pour survivre.", image_temporaire, "#00000"),
    (221, "Aîné", "DEF", 0.60, "Les Grands Freres sont des individus qui protegent leurs freres et soeurs et qui les aident à grandir.", image_temporaire, "#00000"),
    (222, "Coalition de l'Avatar", "DEF", 0.70, "La coalition de l'avatar représente les amis qui se regroupent pour mettre fin aux folies d'Ozan.", image_temporaire, "#00000"),
    (223, "Expert en Art Martial", "ATK", 0.33, "Les Experts en Arts Martiaux sont des combattants qui maitrisent l'art du combat pour vaincre leurs ennemis.", image_temporaire, "#00000"),
    (224, "Clown", "DEF", 0.45, "Les Clowns sont des individus qui portent un masque pour cacher leur identite et proteger leur famille.", image_temporaire, "#00000"),
    (225, "Divin", "ATK", 0.70, "Les Divins sont des individus qui possedent des pouvoirs divins et qui peuvent detruire des planetes entieres.", image_temporaire, "#00000"),
    (226, "Jumeau", "DEF", 0.45, "Les Jumeaux sont des individus qui sont nes en meme temps et qui partagent un lien special.", image_temporaire, "#00000"),
    (227, "Marque des pourfendeurs", "ATK", 0.45, "Les Marques des Pourfendeurs sont des marques qui apparaissent sur le corps des Pourfendeurs pour les proteger des attaques ennemies.", image_temporaire, "#00000"),
    (228, "Chef d'Organisation Criminelle", "DEF", 0.45, "Les Chefs d'Organisation sont des individus qui dirigent des organisations criminelles et qui controlent le crime dans leur ville.", image_temporaire, "#00000"),
    (229, "Byakugan", "DEF", 0.45, "Les utilisateurs du Byakugan sont des individus qui peuvent voir à travers les objets et les personnes pour detecter les ennemis.", image_temporaire, "#00000"),
    (230, "Enfant", "DEF", 0.45, "Les Enfants sont des individus qui sont jeunes et qui doivent etre proteges des dangers du monde.", image_temporaire, "#00000"),
    (231, "Nen de Renforcement", "ATK", 0.45, "Les utilisateurs du Nen du Renforcement sont des individus qui peuvent renforcer leur corps pour augmenter leur force et leur vitesse.", image_temporaire, "#00000"),
    (232, "Nen de Transformation", "ATK", 0.45, "Les utilisateurs du Nen de Transformation sont des individus qui peuvent transformer leur corps pour augmenter leur puissance et leur vitesse.", image_temporaire, "#00000"),
    (233, "Nen d'Emission", "ATK", 0.45, "Les utilisateurs du Nen d'Emission sont des individus qui peuvent emettre leur aura pour attaquer leurs ennemis à distance.", image_temporaire, "#00000"),
    (234, "Nen de Manipulation", "ATK", 0.45, "Les utilisateurs du Nen de Manipulation sont des individus qui peuvent manipuler les objets et les personnes pour les controler.", image_temporaire, "#00000"),
    (235, "Classe 1", "DEF", 0.45, "Sah je sais pas quoi mettre en description la team", image_temporaire, "#00000"),
    (236, "Ishida", "DEF", 0.45, "Les Ishidas sont une famille de Quincy qui combattent les Hollows pour proteger les humains.", image_temporaire, "#00000"),
    (237, "Maladie Incurable", "HP", 0.45, "Les Maladies Incurables sont des maladies qui ne peuvent pas etre gueries et qui tuent les gens lentement.", image_temporaire, "#00000"),
    (238, "Marque Maudite", "DEF", 0.70, "Les Marques Maudites sont des marques qui apparaissent sur le corps des individus pour les maudire et les tuer lentement.", image_temporaire, "#00000"),
    (239, "Trop MIGNOOON!!!", "HP", 0.45, "Les Trop MIGNOOON!!! sont des creatures adorables qui sont protegees par les heros et les guerriers.", image_temporaire, "#00000"),
    (240, "Artiste", "DEF", 0.45, "Les Artistes sont des individus qui creent des oeuvres d'art pour exprimer leurs emotions et leur creativite.", image_temporaire, "#00000"),
    (241, "Vice-Capitaine", "DEF", 0.45, "Les Vice-Capitaines sont des officiers de la Marine qui assistent les Capitaines dans leurs taches et qui dirigent les soldats au combat.", image_temporaire, "#00000"),
    (242, "Matérialiseur", "ATK", 0.45, "Les Materialiseurs sont des individus qui peuvent creer des objets à partir de leur aura pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (243, "Nation Du Feu", "DEF", 0.45, "La Nation du Feu est une nation qui est dirigee par le Seigneur du Feu et qui est protegee par les Maitres du Feu.", image_temporaire, "#00000"),
    (244, "Rival", "ATK", 0.45, "Les Rivaux sont un parallèle du Protagoniste principale.", image_temporaire, "#00000"),
    (245, "Invocateur", "ATK", 0.45, "Les Invocateurs sont des individus qui se battent principalement avec des créatures puissantes qui peuvent invoquer des creatures pour les aider dans le combat.", image_temporaire, "#00000"),
    (246, "Lyceen", "DEF", 0.25, "Les Lyceens sont des eleves qui vont au lycee pour apprendre les matieres scolaires et les techniques de combat.", image_temporaire, "#00000"),
    (247, "Cadet", "HP", 0.40, "Les cadets sont les plus jeunes membres de leur famille.", image_temporaire, "#00000"),
    (248, "Noble", "DEF", 0.30, "Les Nobles sont des individus qui appartiennent à la noblesse et qui possedent des terres et des titres de noblesse.", image_temporaire, "#00000"),
    (249, "Vampire", "DEF", 0.45, "Les Vampires sont des creatures qui se nourrissent du sang des humains pour survivre.", image_temporaire, "#00000"),
    (250, "Utilisateur de Marteau", "ATK", 0.45, "Les Utilisateurs de Marteau sont des individus qui maitrisent l'art du marteau pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (251, "Utilisateur du Rayon Noir", "ATK", 0.45, "Les Utilisateurs du Rayon Noir sont des individus qui peuvent creer des rayons noirs pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (252, "Haki Des Rois", "ATK", 0.45, "Le Haki des Rois est une forme de Haki qui permet à l'utilisateur de controler les autres par la force de sa volonte.", image_temporaire, "#00000"),
    (253, "Héro du Top 5", "DEF", 0.45, "Les Top 5 Heros sont les cinq meilleurs heros du monde qui protegent les citoyens des vilains et qui combattent le crime.", image_temporaire, "#00000"),
    (254, "Maitre du Métal", "ATK", 0.45, "Les Maitres du Metal sont des individus qui peuvent controler le metal pour attaquer leurs ennemis.", image_temporaire, "#00000"),
    (255, "Pouvoir d'invisibilité", "DEF", 0.45, "Les Pouvoirs d'Invisibilite sont des pouvoirs qui permettent à l'utilisateur de devenir invisible pour se cacher de ses ennemis.", image_temporaire, "#00000"),
    (256, "Musicien", "DEF", 0.45, "Les Musiciens sont des individus qui jouent de la musique pour divertir les autres et pour exprimer leurs emotions.", image_temporaire, "#00000"),
    (257, "Transgenre", "DEF", 0.45, "Les Transgenres sont des individus qui ont un genre different de celui qui leur a ete assigne à la naissance.", image_temporaire, "#00000"),
    (258, "Classe 2", "DEF", 0.45, "Les Classe 2 sont des individus qui ont un niveau de puissance superieur à la moyenne.", image_temporaire, "#00000"),
    (259, "Classe 3", "DEF", 0.45, "Les Classe 3 sont des individus qui ont un niveau de puissance inferieur à la moyenne.", image_temporaire, "#00000"),
    (260, "Cache-Oeil", "DEF", 0.45, "Les Borgnes sont des individus qui ont perdu un oeil dans un combat et qui portent un cache-oeil pour proteger leur oeil restant.", image_temporaire, "#00000"),
    (261, "Support", "ATK", 0.45, "Les Boosteurs sont des individus qui peuvent augmenter leur puissance pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (262, "Forme de Buu", "ATK", 0.45, "Les Formes de Buu sont des transformations que Buu peut prendre pour augmenter sa puissance et sa vitesse.", image_temporaire, "#00000"),
    (263, "Sand Siblings", "DEF", 0.45, "Les Sand Siblings sont une famille de ninjas qui protegent le village de Suna.", image_temporaire, "#00000"),
    (264, "Équipage ASL", "ATK", 0.45, "L'equipage ASL est la contraction de \"Ace Sabo Luffy\" et est également le nom de l'équipage pirate inventé par les trois frères quand ils étaient petits..", image_temporaire, "#00000"),
    (265, "Nen de Specialisation", "ATK", 0.45, "Les utilisateurs du Nen de Specialisation sont des individus qui peuvent utiliser leur aura pour des taches specifiques.", image_temporaire, "#00000"),
    (266, "Sept Épéistes de la Brume", "ATK", 0.45, "Les Sept Epéistes de la Brume sont une organisation de ninjas qui protegent le village de Kiri.", image_temporaire, "#00000"),
    (267, "Garnison", "DEF", 0.45, "La Garnison est une unite de l'armee qui defend les murs de la ville contre les attaques des Titans.", image_temporaire, "#00000"),
    (268, "Team 8", "DEF", 0.45, "La Team 8 est une equipe de ninjas qui travaillent ensemble pour proteger le village de Konoha.", image_temporaire, "#00000"),
    (269, "Equipe Gai", "DEF", 0.45, "La Team 9 est une equipe de ninjas qui travaillent ensemble pour proteger le village de Konoha.", image_temporaire, "#00000"),
    (270, "Team 10", "DEF", 0.45, "La Team 10 est une equipe de ninjas qui travaillent ensemble pour proteger le village de Konoha.", image_temporaire, "#00000"),
    (271, "Second d'un Yonko", "DEF", 0.45, "Les Seconds des Yonkos sont des officiers de haut rang qui assistent les Yonkos dans leurs taches et qui dirigent les operations militaires.", image_temporaire, "#00000"),
    (272, "Témoin de la Porte de la Vérité", "DEF", 0.45, "Les visiteurs de la porte de la vérité sont des individus qui ont été confrontés à la vérité de leur existence et qui ont été transformés par cette révélation.", image_temporaire, "#00000"),
    (273, "Utilisateur de Baton", "ATK", 0.45, "Les Utilisateurs de Baton sont des individus qui maitrisent l'art du baton pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (274, "Equipe d'Ichigo", "HP", 0.45, "L'Equipe d'Ichigo est une equipe de bg qui travaillent ensemble pour proteger le monde des Hollows.", image_temporaire, "#00000"),
    (275, "Equipe d'Azula", "ATK", 0.45, "L'Equipe d'Azula est une équipe de femmes.", image_temporaire, "#00000"),
    (276, "Chevalier Sacré", "DEF", 0.45, "Les Chevaliers Sacres sont des guerriers qui servent les humains et qui protegent les humains des demons.", image_temporaire, "#00000"),
    (277, "Utilisateur de la Rotation", "ATK", 0.45, "Les Utilisateurs de la Rotation sont des individus qui maitrisent l'art de la rotation pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (278, "Navigateur", "HP", 0.45, "Les Navigateurs sont des individus qui dirigent les navires et qui naviguent sur les oceans pour explorer de nouveaux territoires.", image_temporaire, "#00000"),
    (279, "Amis de Gon", "DEF", 0.45, "Les Amis de Gon sont des individus qui sont amis avec Gon et qui l'accompagnent dans ses aventures.", image_temporaire, "#00000"),
    (280, "Pirates de Roger", "ATK", 0.45, "Les Pirates de Roger sont une equipe de pirates qui ont navigue sur les mers du monde entier et qui ont decouvert le One Piece.", image_temporaire, "#00000"),
    (281, "Entendeur de la Voix de Toute Chose", "ATK", 0.45, "La Voix de Toute Chose fait référence à des messages véhiculés par des objets inanimés ou des animaux qui ne parlent pas le langage humain. Seul un très petit nombre de personnes dans le monde possède la capacité d'entendre cette voix.", image_temporaire, "#00000"),
    (282, "Maitre en Kido", "ATK", 0.45, "Les Maitres en Kido sont des individus qui maitrisent l'art du Kido pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (283, "Expérimenté en Kido", "ATK", 0.45, "Les Experimentes en Kido sont des individus qui ont une grande experience dans l'art du Kido et qui peuvent l'utiliser pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (284, "Expert du Shunpo", "DEF", 0.45, "Les Experts en Shunpo sont des individus qui maitrisent l'art du Shunpo pour se deplacer rapidement et attaquer leurs ennemis.", image_temporaire, "#00000"),
    (285, "Top 1 Héro", "DEF", 0.45, "Les Top 1 Heros sont les meilleurs heros du monde qui protegent les citoyens des vilains et qui combattent le crime.", image_temporaire, "#00000"),
    (286, "Etendeur de Territoire", "DEF", 0.45, "Les Etendeurs de Territoire sont des individus qui peuvent etendre leur territoire pour proteger leur famille et leur pays.", image_temporaire, "#00000"),
    (287, "Fullbringer", "ATK", 0.45, "Les Fullbringers sont des individus qui peuvent manipuler les objets pour les utiliser comme armes.", image_temporaire, "#00000"),
    (288, "Stardust Crusaders", "ATK", 0.45, "Les Stardust Crusaders sont une equipe de Stand Users qui voyagent à travers le monde pour combattre les ennemis et proteger les innocents.", image_temporaire, "#00000"),
    (289, "Sosie d'Imran", "DEF", 0.45, "Les Sosies d'Imran sont des individus qui ressemblent à Imran et qui peuvent utiliser ses pouvoirs pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (290, "Triplement armé", "ATK", 0.45, "Les Triplement armés sont des individus qui utilisent 3 armes, une dans chaque main et une dans la bouche ou au visage.", image_temporaire, "#00000"),
    (291, "Maitre du Shunko", "ATK", 0.45, "Les Maitres du Shunko sont des individus qui maitrisent l'art du Shunko pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (292, "Mode Ermite", "DEF", 0.45, "Les Modes Ermite sont des individus qui peuvent utiliser le pouvoir du mode Ermite pour proteger leur famille et leur pays.", image_temporaire, "#00000"),
    (293, "Samouraï Traditionnel", "DEF", 0.45, "Les Samourais Traditionnels sont des guerriers qui suivent le code du Bushido et qui se battent pour proteger leur honneur et leur famille.", image_temporaire, "#00000"),
    (294, "Logia", "HP", 0.45, "Les Logias sont des fruits du demon qui permettent à l'utilisateur de se transformer en un element naturel pour attaquer ses ennemis.", image_temporaire, "#00000"),
    (295, "Paramécia", "HP", 0.45, "Les Paramécias sont des fruits du demon qui donnent à l'utilisateur des pouvoirs speciaux pour combattre ses ennemis.", image_temporaire, "#00000"),
    (296, "Maître des Fils", "DEF", 0.45, "Les Maitres des Fils sont des individus qui maitrisent l'art des fils pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (297, "Personnage de !histoire", "DEF", 0.45, "Les Personnages de l'histoire sont des individus qui sont présents dans le !histoire de mousse bot.", image_temporaire, "#00000"),
    (298, "Recousu", "DEF", 0.45, "Les Recousus sont des individus qui ont été recousus par des chirurgiens pour survivre à des blessures mortelles.", image_temporaire, "#00000"),
    (299, "Familier", "DEF", 0.45, "Les Familiers sont des creatures magiques qui protegent leur maitre et qui l'accompagnent dans ses aventures.", image_temporaire, "#00000"),
    (300,"Expérimenté en Shunpo","DEF",0.45,"Les Experimentes en Shunpo sont des individus qui ont une grande experience dans l'art du Shunpo et qui peuvent l'utiliser pour combattre leurs ennemis.",image_temporaire,"#00000"),
    (301, "Boutique d'Urahara", "DEF", 0.45, "La Boutique d'Urahara est une boutique qui vend des objets magiques et des armes pour aider les heros dans leur quete.", image_temporaire, "#00000"),
    (302, "Père Indigne", "DEF", 0.45, "Les Peres Indignes sont des individus qui ne s'occupent pas de leurs enfants et qui les abandonnent pour poursuivre leurs propres interets.", image_temporaire, "#00000"),
    (303, "Utilisateur d'Eventail", "ATK", 0.45, "Les Utilisateurs d'Eventail sont des individus qui maitrisent l'art de l'eventail pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (304, "Pride Troopers", "DEF", 0.45, "Les Pride Troopers sont une equipe de super-heros qui a pour mission de proteger l'univers des menaces extraterrestres.", image_temporaire, "#00000"),
    (305, "Avatar", "DEF", 0.45, "Les Avatars sont des individus qui peuvent maitriser les quatre elements pour combattre leurs ennemis.", image_temporaire, "#00000"),
    (306, "Kenpachi", "ATK", 0.45, "Le titre de Kenpachi.", image_temporaire, "#00000"),
]


# Utilisateur de dague # Traitre (Tosen,Gin) # Voleur d'énergie Angel Quincys 
# Shou Tucker et Rasa et Vinsmoke Judge

all_link_synergies = {
    306 : ["Kenpachi Zaraki","Retsu Unohana"], # Kenpachi
    305 : ["Korra","Aang"], # Avatar
    304 : ["Toppo","Jiren"], # Pride Troopers
    303 : ["Karuto Zolduck","Doma","Temari"], # Utilisateur d'Eventail
    302 : ["Endeavor", "Ging Freecss","Son Goku","Dario Brando","Grisha Yeager","Van Hohenheim","Diavolo","Ozai"], # Père Indigne
    301 : ["Kisuke Urahara","Yoruichi Shihoin"], # Boutique d'Urahara
    300 : ["Renji Abarai", "Ichigo Kurosaki","Shinji Hirako","Shuhei Hisagi","Toshiro Hitsugaya","Gin Ichimaru","Sajin Komamura","Ginrei Kuchiki","Rukia Kuchiki","Isshin Kurosaki","Mayuri","Tosen Kaname"], # Expérimenté en Shunpo
    299 : ["Mahoraga"], # Familier
    #298 : ["Crocodile","Mahito","Franklin"], # Recousu
    #297 : ["Kento Nanami","Rui","Zabuza","Haku","C-18","Baggy","Brogy","Dorry","Sanji","Yoruichi Shihoin","Eren"], # Personnage de !histoire
    296 : ["Jolyne Kujo","Machi","Don Quichotte Doflamingo","Sasori","Chiyo","Kankuro","Beast Jeanist","Rui","Senjumaru Shutara"], # Maître des Fils
    295 : ["Monkey D. Luffy","Baggy","Nico Robin","Wapol","Don Quichotte Doflamingo","Brook","Gecko Moria","Bartholomew Kuma","Jewelry Bonney","Eustass Kid","Trafalgar D. Water Law","Urouge","Boa Hancock","Emporio Ivankov","Inazuma","Edward Newgate","Tsuru","Marshall D. Teach","Fujitora","Don Quichotte Rossinante","Big Mom","Charlotte Katakuri","Shiryu"], # Paramécia
    294 : ["Smoker","Portgas D. Ace","Crocodile","Ener","Aokiji","Marshall D. Teach","Kizaru","Akainu","Caesar Clown","Sabo","Karasu","Ryokugyu"], # Logia
    293 : ["Nobunaga","Atomic Samurai","Kozuki Oden"], # Samouraï Traditionnel
    292 : ["Naruto Uzumaki","Mitsuki","Minato Namikaze","Kabuto Yakushi","Jiraya","Hashirama Senju"], # Mode Ermite
    291 : ["Yoruichi Shihoin","Soi Fon"], # Maitre du Shunko
    290 : ["Roronoa Zoro","Katana Man","Denji"], # Triplement armé
    289 : ["Pilaf"], # Sosie d'Imran
    288 : ["Jotaro Kujo","Iggy","Joseph Joestar","Mohamed Abdul","Kakyoin","Jean-Pierre Polnareff"], # Stardust Crusaders
    287 : ["Kugo Ginjo","Ichigo Kurosaki","Chad","Shukuro Tsukishima"], # Fullbringer
    286 : ["Megumi Fushiguro","Satoru Gojo","Sukuna","Jogo","Dagon","Mahito","Hiromi Higuruma","Kinji Hakari","Naoya Zenin","Kenjaku","Yuta Okkotsu","Hanami"], # Etendeur de Territoire
    285 : ["All Might","Endeavor","Star And Stripe"], # Top 1 Héro
    284 : ["Sosuke Aizen","Soi Fon","Ichibe Hyosube","Byakuya Kuchiki","Shunsui Kyoraku","Yoruichi Shihoin","Jushiro Ukitake","Kisuke Urahara","Yamamoto"], # Expert du Shunpo
    283 : ["Toshiro Hitsugaya","Shuhei","Yumichika","Izuru Kira","Rangiku Matsumoto","Shunsui Kyoraku","Isshin Kurosaki","Soi Fon","Kaname Tosen","Mayuri","Rukia Kuchiki","Ginrei Kuchiki"], # Experimenté en Kido
    282 : ["Yamamoto","Sosuke Aizen","Yoruichi Shihoin","Jushiro Ukitake","Retsu Unohana","Kisuke Urahara","Ichibe Hyosube","Byakuya Kuchiki"], # Maitre en Kido
    281 : ["Kozuki Oden","Monkey D. Luffy","Gol D. Roger",], # Voix de Toute Chose
    280 : ["Gol D. Roger","Silvers Rayleigh","Shanks","Baggy","Kozuki Oden","Nekomamushi"], # Pirates de Roger
    279 : ["Gon Freecss","Kurapika","Leorio","Kirua Zoldyck"], # Amis de Gon
    278 : ["Nami","Capitaine","Koby"], # Navigateur
    277 : ["Johnny Joestar","Gyro Zeppeli"], # Utilisateur de la Rotation
    276 : ["Gilthunder","Hendrickson"], # Chevalier Sacré
    275 : ["Azula","Mai","Ty Lee"], # Equipe d'Azula
    274 : ["Ichigo Kurosaki","Orihime Inoue","Chad","Uryu Ishida","Renji Abarai"], # Equipe d'Ichigo
    273 : ["Kumadori","Kanaria","Nami","Hiruzen Sarutobi","Ener","Yamato"], # Utilisateur de Baton A FAIRE
    272 : ["Edward Elric","Roy Mustang","Izumi Curtis","Van Hoheinheim","Alphonse Elric","Père"], # Témoin de la Porte de la Vérité
    271 : ["Benn Beckman","Charlotte Katakuri","Roronoa Zoro","Marco"], # Second d'un Yonko JACK et BURGES a ajouté
    270 : ["Shikamaru Nara","Ino Yamanaka","Choji Akimichi","Asuma Sarutobi"], # Team 10
    269 : ["Rock Lee","Neji Hyuga","Tenten","Gai Maito"], # Team 9
    268 : ["Kiba Inuzuka","Hinata Hyuga","Shino Aburame","Kurenai Yuhi"], # Team 8
    267 : ["Hannes","Pixis"], # Garnison
    266 : ["Zabuza Momochi","Kisame"], # Sept Épéistes de la Brume
    265 : ["Pariston Hill","Kurapika","Kuroro Lucifer","Neferopito","Pakunoda","Aruka Zoldyck","Neon Nostrad","Meleoron","Ging Freecss"], # Nen de Specialisation
    264 : ["Monkey D. Luffy","Portgas D. Ace","Sabo"], # Équipage ASL
    263 : ["Kankuro","Temari","Gaara"], # Sand Siblings
    262 : ["Kid Buu","Majin Buu"], # Forme de Buu
    261 : ["Belo Betty","Utahime Iori","Senritsu","Emporio Ivankov","Jugram"], # Support
    260 : ["Hange Zoe","Himeno","Kenpachi Zaraki","King Bradley","Kakashi Hatake","Denji"], # Borgne
    259 : ["Mai Zenin","Nobara Kugisaki","Kasumi Miwa"], # Classe 3
    258 : ["Panda","Momo Nishimiya","Takuma Ino","Megumi Fushiguro"], # Classe 2
    257 : ["Narciso Anasui","Emporio Ivankov","Puri Puri Prisoner","Yamato"], # Transgenre
    256 : ["Trish","Brook","Yoshinobu Gakuganji","Kyoka Jiro","Senritsu","Tapion","Akira Otoishi","Bonolenov Ndongo"], # Musicien
    255 : ["Risotto Nero","Toru Hagakure","Sosuke Aizen","Wamuu","Meleoron"], # Pouvoir d'invisibilité
    254 : ["Toph Beifong","Risotto Nero","Hina","Eustass Kid","Korra"], # Maitre du Metal
    253 : ["All Might","Endeavor","Mirko","Hawks","Beast Jeanist","Child Emperor","Atomic Samurai","Bang","Tatsumaki","Star and Stripe"], # Héro du top 5
    252 : ["Monkey D. Luffy","Shanks","Boa Hancock","Silvers Rayleigh","Portgas D. Ace","Edward Newgate","Don Quichotte Doflamingo","Big Mom","Charlotte Katakuri","Kozuki Oden","Eustass Kid","Sengoku","Kaido","Gol D. Roger","Yamato","Roronoa Zoro","Monkey D. Garp","Topman Warcury"], # Haki Des RoisF
    251 : ["Mahito","Aoi Todo","Nobara Kugisaki","Yuji Itadori","Kento Nanami","Yuta Okkotsu","Satoru Gojo"], # Utilisateur du Rayon Noir
    250 : ["Hiromi Higuruma","Diane","Nobara Kugisaki","Usopp","Speedwagon","Power"], # Utilisateur de Marteau
    249 : ["Dio Brando","Vanilla Ice","Straizo"], # Vampire
    248 : ["Alex Louis Armstrong", "Olivia Mira Armstrong","Sabo","Don Quichotte Rossinante","Don Quichotte Doflamingo","Nefertari Vivi","Cobra","Historia Reiss","Rhodes Reiss","Dinah Yeager","Willy Teyber","Frieda Reiss","Mikasa Ackerman","Zuko","Azula","Ozai","Iroh","Mai","Jaygarcia Saturn","Marcus Mars","Topman Warcury", "Ethanbaron Nusjuro","Shepherd Ju Peter","Yue"], # Noble
    247 : ["Alex Louis Armstrong","Caulifla","Izuna Uchiha","Katara","Daki","Boingo","Fubuki","Hanabi Hyuga","Karin Kurosaki","Yuzu Kurosaki","Gaara","Kechizu","Don Quichotte Rossinante","Son Goku","Shinobu Kocho","Zeldris","Scar","Azula","Genya Shinazugawa","Asura Otsutsuki","Arata Nitta","Orihime Inoue","Rukia Kuchiki","Falco Grice","Naoya Zenin","Killer Bee","Tobirama Senju","Estarossa","Ozai"], # Cadet
    246 : ["Megumi Fushiguro","Yuji Itadori","Aoi Todo","Maki Zenin","Kinji Hakari","Toge Inumaki","Yuta Okkotsu","Noritoshi Kamo","Kokichi Muta","Nobara Kugisaki","Mai Zenin","Momo Nishimiya","Junpei","Kasumi Miwa","Yu Haibara","Riko Amanai","Josuke Higashikata","Okuyasu Nijimura","Koichi Hirose","Yukako Yamagishi","Momo Yaoyorozu","Izuku Midoriya","Tamaki Amajiki","Shihai Kuroiro","Suguru Geto","Toru Hagakure","Keigo Asano","Kyoka Jiro","Denki Kaminari","Mizuiro Kojima","Shindo","Katsuki Bakugo","Ochaco Uraraka","Ibara Shiozaki","Neito Monoma","Tenya Iida","Shoto Todoroki","Nejire Hado","Panda","Orihime Inoue","Ichigo Kurosaki","Chad","Fumikage Tokoyami","Shinso Hitoshi","Mirio Togata"], # Lyceen
    245 : ["Sukuna","Megumi Fushiguro","Sai","Suguru Geto","Kabuto Yakushi","Takuma Ino","Junpei","Akane Sawatari","Orochimaru","Dagon"], # Invocateur
    244 : ["Katsuki Bakugo","Sasuke Uchiha","Vegeta","Zuko","Marshall D. Teach","Uryu Ishida","Shimotsuki Kuina","Sonic","Piccolo"], # Rival
    243 : ["Azula","Zuko","Ty Lee","Ozai","Iroh","Mai"], # Nation Du Feu
    242 : ["Genthru","Momo Yaoyorozu", "Twice", "Hermes Costello", "Korutopi","Nico Robin","Kaio Shin","Guren","Kaito","Shizuku Murasaki","Knuckle Bine","Bonolenov Ndongo","Cheetu","Rikudo","Meliodas","Angel","Edward Elric","Roy Mustang","Solf J. Kimblee","Alex Louis Armstrong","Tim Marcoh","Isaac McDougal","Alphonse Elric","Van Hoheinheim","Père","Scar","Mei Chang","Hisoka","Star and Stripe","Piccolo"], # Matérialiseur
    241 : ["Yachiru Kusajishi","Shuhei","Ikkaku","Izuru Kira"], # Vice-Capitaine TODO
    240 : ["Sai","Deidara","Rohan Kishibe"], # Artiste
    239 : ["Moshi","Nezu","Chopper","Son Goten","Sajin Komamura","Xiao Mei","Kon (hxh)","Hawk","Nina Tucker"], # Trop MIGNOOON!!!
    238 : ["Sasuke Uchiha","Kimimaro","Anko","Guren","Mizuki","Jugo"], # Marque Maudite
    237 : ["Itachi Uchiha","Tanjuro Kamado", "Kimimaro","Kaya","Trisha Elric","Jushiro Ukitake","Izumi Curtis","Gol D. Roger","Kokichi Muta"], # Maladie Incurable
    236 : ["Uryu Ishida", "Soken Ishida", "Ryuken Ishida","Kanae Katagiri"], # Ishida
    235 : ["Utahime Iori","Aoi Todo","Kento Nanami","Mei Mei","Atsuya Kusakabe","Naobito Zenin","Kokichi Muta","Naoya Zenin"], # Classe 1
    234 : ["Morel Mackernasey","Zushi","Sharnalk","Shoot","Vezze","Ponzu","Miruki Zoldyck","Irumi Zoldyck","Pufu","Karuto Zoldyck","Kikyo Zoldyck","Zazan"], # Nen de Manipulation
    233 : ["Pokkle","Senritsu","Franklin","Leorio","Silva Zoldyck","Meruem","Zeno Zoldyck"], # Nen d'Emission
    232 : ["Biscuit Kruger","Yupi","Machi","Feitan","Kirua Zoldyck","Hisoka"], # Nen de Transformation
    231 : ["Gon Freecss","Guido","Wing","Uvogin","Isaac Netero","Pamu Shiberia","Komugi","Nobunaga","Phinks","Gotoh","Ikarugo"], # Nen de Renforcement
    230 : ["Himawari Uzumaki","Hanabi Hyuga","Son Goten","Udo","Gabi Braun","Zofia","Zushi","Falco Grice","Yachiru Kusajishi","Gotenks","Mitsuki","Uub","Karin Kurosaki","Yuzu Kurosaki","Shigechi","Mei Chang","Kon (hxh)","Child Emperor","Sarada Uchiha","Emporio","Eri","Poco","Kiyo","Naho","Anne","Inari","Selim Bradley"], # Enfant
    229 : ["Himawari Uzumaki","Neji Hyuga","Hanabi Hyuga","Hinata Hyuga","Toneri Otsutsuki","Momoshiki Otsutsuki","Kaguya Otsutsuki","Isshiki Otsutsuki"], # Byakugan
    228 : ["Tomura Shigaraki","Pain", "Kuroro Lucifer","Don Quichotte Doflamingo", "Chisaki Kai","Re-Destro","Risotto Nero","Crocodile","Isshiki Otsutsuki","Kurapika","Diavolo","Chisaki Kai","Silva Zoldyck"], # Chef d'Organisation criminelle
    227 : ["Gyomei Himejima","Sanemi Shinazugawa","Obanai Iguro","Mitsuri Kanroji","Giyu Tomioka","Tanjiro Kamado","Muichiro Tokito","Yoriichi Tsugikuni","Kokushibo"], # Marque des pourfendeurs
    226 : ["Beerus","Champa","Kokushibo","Yoriichi Tsugikuni","Mai Zenin","Maki Zenin","Karin Kurosaki","Yuzu Kurosaki","Weather Report","Enrico Pucci","Père","Van Hoheinheim","Rikudo"], # Jumeau
    225 : ["Beerus","Champa","Belmod","Rikudo","Père","Athena","Zamasu", "Maitre Kaio", "Kaio Shin", "Goku Black","Toppo","Ener","Drole","Elizabeth Liones","Estarossa"], # Divin
    224 : ["Caesar Clown","Hisoka","Belmod","Baggy"], # Clown
    223 : ["Akaza","Bang","Son Goku","Tortue Geniale","Piccolo","Son Gohan","Vegeta","Hisoka","Maki Zenin","Toji Fushiguro","Rock Lee","Gai Maito","Annie Leonhart","Ling Yao","Shota Aizawa","Garou","Yoruichi Shihoin","Izumi Curtis","Trunks","Soi Fon","Lan Fan","Krilin","Jinbe","Mei Chang","Son Goten","Jonathan Joestar","Caesar Zeppeli","Videl","Cell","Lisa Lisa","Mr. Satan","Fu","Ten Shin Han","Yamcha","Will Zeppeli","Beerus","Pan","Wing","Zushi","Chaozu","Whis","Hit","Jiren","Sukuna","Satoru Gojo","C-17","C-18","Sneck","Ty Lee","Gogeta","Vegetto","Genos","Sabo","Shoot","Hack","Azula","Zuko","Orihime Inoue","Emporio Ivankov","Grand Pretre","Zeno Zoldyck","Doma","Toppo","Dio Brando"], # Expert en Art Martial
    222 : ["Katara","Aang","Zuko","Toph Beifong","Appa","Sokka"], # Coalition de l'Avatar
    221 : ["Itachi Uchiha", "Madara Uchiha","Hashirama Senju", "Metal Bat","Edward Elric","Ichigo Kurosaki","Tanjiro Kamado","Portgas D. Ace","Irumi Zoldyck","Byakuya Kuchiki","Son Gohan","Cooler","Sanemi Shinazugawa","Dabi","Fuyumi Todoroki","Natsuo Todoroki","Boruto Uzumaki","Olivia Mira Armstrong","Sokka","Gyutaro","Oingo","Tatsumaki","Hinata Hyuga","Temari","Choso","Don quichotte Doflamingo","Raditz","Kanae Kocho","Frere de Scar","Zuko","Daniel J. D'Arby","Indra Otsutsuki","Akari Nitta","Mei Mei","A","Aoi Todo","Meliodas","Iroh"], # Grand frère Light yagami
    220 : ["Josuke Higashikata","Metal Bat","Okuyasu Nijimura","Knuckle Bine","Speedwagon"], # Voyou
    219 : ["Sasuke Uchiha","Zuko","Jean-Pierre Polnareff","Kurapika","Scar","Freezer","Eren yeager","Roy Mustang","Caesar Zeppeli","Tanjiro Kamado","Genos","Gilthunder","Gabi Braun","Katana Man","Tomura Shigaraki","Enrico Pucci","Shoto Todoroki","Dabi","Grand Pretre","Shinso Hitoshi","Stain","Broly"], # Esprit de Vengeance Thorfinn
    218 : ["Asuma Sarutobi","Shunsui Kyoraku","Tengen Uzui","Mikasa Ackerman","Levi Ackerman","Inosuke","Roronoa Zoro","Riza Hawkeye","Coyote Stark","King Bradley","Hatchan","Kozuki Oden","Jushiro Ukitake","Ichigo Kurosaki","Tenten","Pakunoda","Barry The Chopper","Hermep","Mike Zacharias","Hanzo","Katana Man","Gecko Moria","Doma"], # Arme dans chaque main Thorfinn Kohaku Asta
    217 : ["Hidan","Goku Black","Zamasu","Nnoitra Gilga","Kaito","Shuhei","Crocodile","Hanzo"], # Faucheur
    216 : ["Kobeni Higashiyama","Killer Bee","Maes Hughes","Leorio","Himiko Toga","Barry The Chopper","Baggy","Kenny Ackerman","Spinner","Dracule Mihawk","Dio Brando","Tenten","Pamu Shiberia","Hermep","Menchi","Mai","Kars","Anne","Naoya Zenin"], # Manieur de couteau Sun jingwoo juuzou Thorfinn
    215 : ["Roy Mustang", "King Bradley","Grumman"], # Führer
    214 : ["King","Aruka Zoldyck","Queen"], # Calamité
    213 : ["Josuke Higashikata","Jotaro Kujo","Koichi Hirose","Okuyasu Nijimura","Rohan Kishibe","Yukako Yamagishi","Shigechi","Tonio Trussardi","Akira Otoishi","Kira Yoshikage","Tama"], # Résident de Morio
    212 : ["Escanor", "Mei Mei","Baraggan","Brogy","Juzo Kumiya","Zombieman","Gyomei Himejima","Kenpachi Zaraki"], # Utilisateur de Hache
    211 : ["Grand Pretre", "Enrico Pucci","Isaac Netero","Ichibe Hyosube","Gyomei Himejima","Urouge","Uraume","Yahaba","Hidan","Scar","Doma"], # Spirituel
    210 : ["Leorio", "Shigechi","Nami","Mei Mei"], # Avare
    209 : ["Estarossa","Meliodas","Zeldris"], # Famille de Méliodas
    208 : ["Ban","Maki Zenin","Gai Maito","Rock Lee","Kurapika","Toji Fushiguro","Ikkaku"], # Utilisateur de Nunchaku
    207 : ["Roronoa Zoro","Kenpachi Zaraki","Yachiru Kusajishi",], # Sens de la direction douteux
    206 : ["Riza Hawkeye","Mustard","Miles","Conny Springer","Narancia","Maria Ross","Franklin","Merry","Pakunoda","Kaito","Shepherd Ju Peter","Jean Havoc","Udo","Theo Magath","Rudol Von Stroheim","Genya Shinazugawa","Yelena","Jean Kirstein","Floch","Olivia Mira Armstrong","Shoot","Gaimon","Marcus Mars","Kikyo Zoldyck","Kenny Ackerman","Nejire Hado","Nobara Kugisaki","Gotoh","Jaco","Gol D. Roger","Zombieman","Eustass Kid","Queen","Metal Knight","Kizaru","Irumi Zoldyck","Gyro Zeppeli"], # Tireur
    205 : ["Don Krieg","Shaka"], # Armure d'Or
    204 : ["Caesar Clown","Don Quichotte Doflamingo","Don Quichotte Rossinante","Vergo"], # Famille Don Quichotte
    203 : ["Caesar Clown","Tim Marcoh","Mayuri","Kisuke Urahara","Hange Zoe","Winry Rockbell","Franky","Child Emperor","Frere De Scar","Bulma","Cioccolata","Kars","Tom Xaver","Edward Elric","Alphonse Elric","Ener","Queen","Metal Knight","Jaygarcia Saturn"], # Scientifique
    202 : ["Hanami","King (NNT)","Ibara Shiozaki","Hashirama Senju","Tenzo", "Shinji Hirako Nishiya","Danzo Shimura", "Ryokugyu","Kanae Kocho","Kanao Tsuyuri","Shinobu Kocho","Shino Aburame","Asura Otsutsuki","Gloxinia","Naruto Uzumaki"], # Maitre de la nature
    201 : ["Escanor","Père","Feitan","Tanjiro Kamado","Sumiyoshi","Tanjuro Kamado","Yoriichi Tsugikuni"], # Pouvoir du soleil
    200 : ["King (NNT)","Gloxinia"], # Fée
    199 : ["Stinger","Maki Zenin","King (NNT)","Gloxinia","Power","Angel","Galand","Ulquiorra"], # Lancier 
    198 : ["Saitama", "Mumen Rider","Fubuki", "Tatsumaki", "King (OPM)", "Bang", "Flashy Flash", "Atomic Samurai", "Child Emperor", "Metal Knight", "Zombieman", "Genos", "Metal Bat", "Puri Puri Prisoner", "Stinger", "Sneck", "All Might", "Star And Stripe", "Endeavor","Nana Shimura","Beast Jeanist","Hawks","Shota Aizawa","Ryukyu","Mount Lady", "Gran Torino","Midnight", "Rock Lock", "Snipe","Sajin Higawara","Mirko","Lady Nagant","Shinji Hirako Nishiya","Nighteye","Toppo","Jiren"], # Héro Professionel
    197 : ["Freezer", "Cooler", "Grand Roi Cold", "Frost"], # Race de Freezer
    196 : ["Zamasu", "Maitre Kaio", "Kaio Shin", "Goku Black"], # Kaio
    195 : [], # Duplicateur
    194 : ["Mikasa Ackerman", "Levi Ackerman", "Kenny Ackerman"], # Ackerman
    193 : ["Sieg Yeager", "Annie Leonhart", "Reiner Braun", "Bertholdt Hoover", "Pieck Finger", "Porco Galliard", "Gabi Braun", "Falco Grice", "Udo", "Zofia"], # Aspirant Guerrier
    192 : ["Sharnalk","Makima","Irumi Zoldyck","Shinso Hitoshi","Kuroro Lucifer","Ino Yamanaka","Sosuke Aizen","Itachi Uchiha","Madara Uchiha","Sasuke Uchiha","Shisui Uchiha","Kakyoin","Merlin","Enmu","Rohan Kishibe","Kurenai Yuhi","Gowther","Tamayo","Pakunoda","Shinji Hirako","Isshiki Otsutsuki","Shukuro Tsukishima","Kaname Tosen","Shaka","Gyutaro","Senjumaru Shutara","Diego Brando","Irumi Zoldyck","Estarossa","Pufu","Hashirama Senju"], # Manipulateur d'Esprit
    191 : [], # Fusion
    190 : ["Toji Fushiguro", "Hit","Zabuza Momochi","Tao Pai Pai","Zeno Zoldyck","Silva Zoldyck","Kirua Zoldyck","Karuto Zoldyck", "Ghiaccio", "Prosciutto", "Formaggio", "Cioccolata","Risotto Nero","Haku","Sonic","Irumi Zoldyck"], # Tueur à gage
    189 : ["Fugo (Purple Haze)","Mayuri","Mustard","Orochimaru","Magellan","Shizune","Kabuto Yakushi","Sasori","Shinobu Kocho","Soi Fon","Chiyo","Caesar Clown","Gloxinia","Zazan","Don Krieg","Hanzo","Eso","Frost","Kechizu","Junpei","Pokkle","Ponzu","Hanami","King (NNT)","Irumi Zoldyck","Gin Ichimaru","Choso"], # Empoisonneur
    188 : ["Hidan", "Kakuzu","Sosuke Aizen","Isshiki Otsutsuki","Ban","Kars","Père","Zombieman","Zamasu"], # Immortel Meliodas ou les homonculus
    187 : ["Jiren", "Champa","Vados","Belmod", "Toppo", "Kefla", "Hit", "Goku Black", "Kale", "Caulifla", "Cabba", "Frost", "Trunks"], # Univers Alternatif
    186 : ["Sukuna","Danzo Shimura","Bucciarati","Inazuma","Lust","Kars","Shukuro Tsukishima","Trafalgar D. Water Law","Gin Ichimaru"], # Dissecteur
    185 : ["Trafalgar D. Water Law", "Eustass Kid", "Monkey D. Luffy", "Roronoa Zoro", "Marshall D. Teach", "Urouge", "Jewelry Bonney"], # Génération Terrible
    184 : [], 
    183 : ["Saitama","Ichibe Hyosube","Ikkaku","Tortue Geniale","Juzo Kumiya","Nappa","Pixis","Yoshinobu Gakuganji","Krilin","Yamamoto","Karasu","Glutonny"], # Sans cheveux
    182 : ["Shikamaru Nara", "Pegui","Armin Arlert","Erwin Smith","Momo Yaoyorozu","Sosuke Aizen","Kabuto Yakushi","Orochimaru","Maes Hughes","Botobai Gigante","Merlin","Nezu","Sieg Yeager","Izuku Midoriya","Hiromi Higuruma","Tsuru","Shihai Kuroiro","Sokka","Nico Robin","Joseph Joestar","Benn Beckman","Child Emperor","Nighteye","Komugi","Meruem","Tsezugera","Yamamoto","Kokichi Muta","Grand Pretre","Queen","Kento Nanami","Kirua Zoldyck","Aoi Todo","Zeno Zoldyck","Hisoka","Silvers Rayleigh","Kurapika","Chisaki Kai","Doma","Pufu"], # Stratège
    181 : ["Vezze","Boa Hancock","Makima","Fubuki","Lust"], # Envoûteuse
    180 : ["Emporio Ivankov","Karasu","Belo Betty","Lindbergh","Olivia Mira Armstrong","Erwin Smith","Magellan","Ginyu","Grumman","Pixis","Theo Magath","Vergo","Jugram","Kozuki Oden","Re-Destro"], # Commandant
    179 : ["Merlin","Momo Nishimiya","Babidi"], # Magicien traditionnel
    178 : ["Ikarugo","Kain Fuery","Falman","Heinkel","Hannes","Maria Ross","Zofia","Darius","Pieck Finger","Nicolo","Heymans"], # Soldat
    177 : ["Hermep","Don Quichotte Rossinante","Maes Hughes", "Cheetu", "Zazan","Meleoron","Koruto","Levi Ackerman","Miles","Buccaneer","Hannes","Ikkaku","Renji Abarai","Rangiku Matsumoto"], # Lieutenant
    176 : ["Tashigi", "Hina", "Koby","Roy Mustang"], # Colonel
    175 : ["Smoker","Haguar D. Sauro","Tsuru","Doll","Vergo","Monkey D. Garp"], # Vice Amiral
    174 : ["Crocodile","Dracule Mihawk", "Baggy"], # Cross Guild
    173 : ["Tomura Shigaraki", "All For One", "Dabi", "Spinner", "Himiko Toga", "Twice", "Re-Destro", "Gigantomachia","Mustard","Lady Nagant"], # Front de Libération du Paranormal
    172 : ["Konan","Karuto Zoldyck"], # Maitre du papier
    171 : ["Historia Reiss", "Frieda Reiss", "Rhodes Reiss"], # Reiss
    170 : ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman", "Hange Zoe", "Erwin Smith", "Jean Kirstein", "Conny Springer", "Sasha Braus", "Historia Reiss", "Ymir", "Reiner Braun", "Bertholdt Hoover", "Annie Leonhart","Mike Zacharias","Yelena","Floch","Onyankopon"], # Bataillon d'Exploration
    168 : ["Daki","Jiraya","Kumadori","Pamu Shiberia","Yukako Yamagishi","Momoshiki Otsutsuki"], # Manipulateur de cheveux
    167 : ["Itachi Uchiha","Karasu","Mei mei","Shisui Uchiha"], # Maitre des corbeaux
    166 : ["Mount Lady", "Gigantomachia", "Diane","Armin Arlert","Bertholdt Hoover","Rhodes Reiss","Brogy","Dorry","Haguar D. Sauro","Magellan","Laboon","Sloth","Mike","Ryukyu","Choji Akimichi","Gecko Moria","Drole","Re-Destro"], # Géant
    165 : ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Sai","Boruto Uzumaki","Sarada Uchiha","Konohamaru Sarutobi","Mitsuki","Kawaki","Tenzo"], # Team 7
    164 : ["Sengoku", "Isaac Netero","Hashirama Senju","Doma"], # Pouvoir de Bouddha
    163 : ["Zeno Zoldyck","Isaac Netero", "Yamamoto","Tsuru","Monkey D. Garp","Sengoku","Jigoro Kuwajima","Ichibe Hyosube","Iroh","Shunsui Kyoraku","Bang","Jaygarcia Saturn","Marcus Mars","Topman Warcury", "Ethanbaron Nusjuro","Shepherd Ju Peter","Naobito Zenin","Capitaine","Soken Ishida","Pixis","Yoshinobu Gakuganji","Ginrei Kuchiki","Grumman","Hiruzen Sarutobi","Tortue Geniale","Recovery Girl","Gran Torino","Père","Onoki","Hama","Silvers Rayleigh","King Bradley","Toppo"], # Vétéran
    162 : ["Kanaria","Gotoh","Whis","Vados","Uraume","Kanae Katagiri","Vanilla Ice","Koruto","Merry","Sumi Nakahara","Kiyo"], # Serviteur
    161 : ["Diavolo","Twice","Ling Yao","Escanor", "Gogeta","Vegetto","Zamasu","Gotenks","Kefla","All Might","Panda","Coyote Stark"], # Double personnalité
    160 : ["Jiraya","Ebisu","Tortue Geniale","Denji","Mineta","Hisoka","Sanji","Meliodas","Brook","Kon","Midnight","Haruta Shigemo","Kira Yoshikage"], # Pervers
    159 : ["Orochimaru", "Kabuto Yakushi", "Sasuke Uchiha","Mitsuki","Anko","Akane Sawatari"], # Maitre des serpents
    158 : ["Tompa","Mizuki","Miruki Zoldyck","Guido","Sadaso","Mineta","Cell JR","Shigechi","Majtani","Genthru","Babidi", "Don Krieg","Kuro","Yoki","Pilaf"], # Minable et perfide
    157 : ["Alphonse Elric", "Barry The Chopper","Kon","Panda"], # Âme
    156 : ["Weather Report","Nami","Monkey D. Dragon"], # Maitre du climat
    155 : ["Son Goku","Son Gohan", "Tortue Geniale", "Krilin", "Yamcha", "Ten Shin Han", "Chaozu", "Piccolo", "Vegeta", "Trunks", "Son Goten", "Bulma", "Videl", "Pan", "Yajirobe", "C-18","C-17","Majin Buu"], # Z Fighters
    154 : ["Sanji","Tonio Trussardi","Menchi","Nicolo","Hatchan"], # Chef Cuisinier
    153 : ["Eren Yeager", "Grisha Yeager", "Sieg Yeager", "Carla Yeager","Dinah Yeager"], # Yeager 
    152 : ["Eren Yeager", "Grisha Yeager", "Sieg Yeager", "Ymir", "Annie Leonhart", "Reiner Braun", "Bertholdt Hoover", "Pieck Finger", "Porco Galliard", "Falco Grice","Frieda Reiss","Tom Xaver","Rhodes Reiss","Dinah Yeager","Gigantomachia","Armin Arlert"], # Titan
    151 : ["Shizune","Ijichi","Akari Nitta","Beans"], # Secrétaire
    149 : ["Kakashi Hatake","Jiraya","Satoru Gojo","Shota Aizawa","Vlad King","Iruka","Wing","Tortue Geniale","All Might","Snipe","Maitre Kaio","Izumi Curtis","Midnight","Ebisu","Silvers Rayleigh","Dracule Mihawk","Sakonji Urokodaki","Bang","Atomic Samurai","Jigoro Kuwajima","Morel Mackernasey","Utahime Iori","Atsuya Kusakabe","Lisa Lisa","Karin","Kurenai Yuhi","Gai Maito","Mizuki","Konohamaru Sarutobi","Biscuit Kruger","Lady Nagant","Masamichi Yaga","Beast Jeanist","Hiruzen Sarutobi","Asuma Sarutobi","Gran Torino","Hama","Kento Nanami","Gyomei Himejima","Nana Shimura","Kisuke Urahara","Iroh","Merlin","Piccolo","Katara","Monkey D. Garp"], # Mentor
    148 : ["Glutonny","Majin Buu","Big Mom","Wapol", "Miruki Zoldyck","Menchi","Todo","Inosuke","Monkey D. Luffy","Son Goku","Sasha Braus","Portgas D. Ace","Choji Akimichi","Hawk","Beerus","Whis","Yajirobe","Polpo","Champa","Appa","Jewelry Bonney"], # Glouton
    147 : ["Shikamaru Nara","Fumikage Tokoyami","Shunsui Kyoraku","Megumi Fushiguro","Shihai Kuroiro","Meliodas","Jiraya","Derrierie","Selim Bradley","Gecko Moria","Estarossa"], # Manipulateur de l'ombre
    146 : ["Tim Marcoh", "Neferopito","Tsunade","Sakura Haruno","Ryuken Ishida","Leorio","Shizune","Kabuto Yakushi","Recovery Girl","Karin (naruto)","Josuke Higashikata","Arata Nitta","Fû","Aoi Kanzaki","Kaio Shin","Foo Fighters","Hanataro","Isshin Kurosaki","Asura Otsutsuki","Chopper","Tamayo","Izuru Kira","Maitre Kaio","Orihime Inoue","Emporio Ivankov","Grand Pretre","Machi","Orochimaru","Marco","Shoko Ieiri","Elizabeth Liones","Trafalgar D. Water Law","Naruto Uzumaki","Hashirama Senju","Katara","Korra","Unohana"], # Medecin
    145 : ["Nefertari Vivi","Vegeta","Ling Yao","Elizabeth Liones","Arthur Pendragon","Mei Chang","Azula","Yue","Zuko"], # Princesse
    144 : ["Pokkle","Uryu Ishida","Gowther","Noritoshi Kamo","Sasha Braus","Ryuken Ishida","Soken Ishida"], # Archer
    143 : ["Mr. Satan","King (OPM)","Majtani","Oingo","Baggy"], # Imposteur
    142 : ["Broly","Kale","Uvogin","Kefla","Yupi","Gigantomachia","Sloth","Jugo","Fugo (Purple Haze)"], # Berserker
    141 : ["Envy","Oingo","Ginyu","Irumi Zoldyck","Muzan","Yoruichi Shihoin","King (NNT)","Chopper","Rob Lucci","Heinkel","Darius","Marco","Kaku","King","Queen","Kaido","Mahito","Ryukyu","Shepherd Ju Peter","Yupi","Pufu","Katana Man","Denji","Suigetsu Hozuki","Kimimaro","Freezer","Cooler","Yamato","Tamaki Amajiki","Kabuto Yakushi","Orochimaru","Baggy","Kid Buu","Kiba Inuzuka","Biscuit Kruger","Eren Yeager", "Grisha Yeager", "Sieg Yeager", "Ymir", "Annie Leonhart", "Reiner Braun", "Bertholdt Hoover", "Pieck Finger", "Porco Galliard", "Falco Grice","Frieda Reiss","Tom Xaver","Foo Fighters","Lindbergh","Bardock","Mezo Shoji","Roi Vegeta","Marcus Mars","Jaygarcia Saturn","Jugo","Mayuri","Lust","Nezuko Kamado","Kars","Isshiki Otsutsuki","Père","Kakuzu","Himiko Toga","Sengoku","Ethanbaron Nusjuro","Diego Brando","Naruto Uzumaki","Topman Warcury","Piccolo","Armin Arlert","Kawaki","Charlotte Katakuri"], # Métamorphe
    140 : ["Hiruzen Sarutobi", "Asuma Sarutobi", "Konohamaru Sarutobi"], # Sarutobi
    139 : ["Toji Fushiguro","Son Goku","Hashirama Senju","Tobirama Senju","Hiruzen Sarutobi", "Minato Namikaze", "Asuma Sarutobi","Deidara","Itachi Uchiha","Haku","Zabuza Momochi","Madara Uchiha","Sasori","Kimimaro","Hanzo","Chiyo","Freezer","Shenron","Son Gohan","Trunks","Tortue Geniale","Chaozu","Vegeta","Yamcha","Ten Shin Han","Cell","C-17","Piccolo","Krilin","Pamu Shiberia","Kaito","Fû","Suguru Geto","Katana Man","Galand","Uryu Ishida"], # Ressuscité
    138 : ["Yukako Yamagishi","Pamu Shiberia","Himiko Toga"], # Yandere
    137 : ["Haruta Shigemo","Daniel J. D'Arby","Kaito","Kinji Hakari"], # Chanceux
    136 : ["Kakashi Hatake","Satoru Gojo","Takuma Ino","Galgali","Karasu","King","Mezo Shoji","Shinji Hirako Nishiya","Hermep","Beam","Mustard","Inosuke","Spinner","Sabito","Sakonji Urokodaki","Sajin Higawara","Ryukyu","Halibel","Vlad King","Tamaki Amajiki","Sajin Komamura","Kikyo Zoldyck","Mount Lady","Twice","Grimmjow","Stain","Star and Stripe","Chisaki Kai"], # Masqué
    135 : ["Kankuro", "Sasori","Chiyo","Don Quichotte Doflamingo","Masamichi Yaga","Kokichi Muta","Neferopito"], # Marionnettiste
    134 : ["Jones","Leluto","Hermes Costello","Jolyne Kujo","Isaac McDougal","Solf J. Kimblee","Lady Nagant","Polpo","Majtani","Yamato","Narciso Anasui","Foo Fighters","Weather Report","Hama","Shiryu"], # Prisonnier
    133 : ["Sukuna", "Meruem", "Yhwach","Zeno","Roi Vegeta","Grand Roi Cold","Dabra","Historia Reiss","Wapol","Cobra","King (NNT)","Zeldris","Gol D. Roger","Emporio Ivankov","Ozai","Zazan","Gloxinia","Nekomamushi","Meliodas","Bartholomew Kuma","Baraggan","Boa Hancock","Drole","Elizabeth Liones","Ban"], # Roi
    132 : ["Suguru Geto","Satoru Gojo","Yuki Tsukumo","Yuta Okkotsu","Jogo","Hanami","Dagon","Mahito","Metal Bat","Flashy Flash","Genos","Puri Puri Prisoner","Choso","Zombieman","Deidara","Pain","Orochimaru","Sasori","Itachi Uchiha","Obito Uchiha","Kakuzu","Konan","Kisame","Hidan","Metal Knight","Tatsumaki"], # Classe S
    131 : ["Toji Fushiguro","Maki Zenin","Gai Maito","Rock Lee","Izuku Midoriya","All Might"], # Dépourvu d'énergie occulte
    130 : ["Suguru Geto","Juzo Kumiya","Uraume","Haruta Shigemo","Kenjaku","Junpei"], # Maitre des Fleaux
    129 : ["Smoker","Morel Mackernasey","Zabuza Momochi","Muichiro Tokito","Izuku Midoriya","Mei Terumi","Weather Report","Rangiku Matsumoto","Naruto Uzumaki"], # Maître du Brouillard
    128 : ["Kaku","Rob Lucci","Kumadori"], # CP-0
    127 : ["Choso","Kechizu", "Katara","Hama","Vlad King","Rui","Noritoshi Kamo","Power","Nezuko Kamado","Esidisi","Eso","Yahaba","Yuji Itadori","Tamayo","Stain","Korra","Retsu Unohana"], # Manipulateur de Sang
    126 : ["Jotaro Kujo","Jolyne Kujo","Holy Kujo"], # Famille Kujo
    125 : ["Zeno", "Rikudo","Père","Athena","Saitama","Super Shenron","Yhwach","Shenron"], # Tout Puissant
    124 : ["Kakashi Hatake","Shisui Uchiha","Yugao Uzuki","Sai","Tenzo","Danzo Shimura","Itachi Uchiha"], # ANBU
    123 : ["Monkey D. Luffy","Monkey D. Dragon", "Monkey D. Garp"], # Famille de Luffy
    122 : ["Choso","Eso","Kechizu"], # Foetus des Neuf Phases
    121 : ["Jaygarcia Saturn","Marcus Mars","Topman Warcury", "Ethanbaron Nusjuro","Shepherd Ju Peter"], # Doyen
    120 : ["Ichigo Kurosaki", "Masaki Kurosaki", "Karin Kurosaki", "Yuzu Kurosaki", "Isshin Kurosaki"], # Famille Kurosaki
    3 : ["Ichigo Kurosaki"], # Hollow
    6 : ["Uryu Ishida", "Soken Ishida", "Ryuken Ishida", "Masaki Kurosaki", "Yhwach","Ichigo Kurosaki","Kanae Katagiri","Jugram"], # Quincy
    8 : ["Grimmjow", "Ulquiorra", "Nnoitra Gilga", "Halibel", "Baraggan", "Coyote Stark"], # Espada
    119 : ["Obito Uchiha", "Mirio Togata"], # Intangible
    118 : ["Lady Nagant", "Riza Hawkeye", "Ikarugo","Mista","Mai Zenin","Benn Beckman","Usopp","Snipe","Sasha Braus","Gabi Braun","Uryu Ishida","Mai","Yasopp","Coyote Stark","Charlotte Katakuri"], # Sniper
    117 : ["Mirio Togata","Tamaki Amajiki","Nejire Hado"], # Big 3
    116 : ["Tomura Shigaraki", "Nana Shimura"], # Shimura
    115 : ["Rukia Kuchiki","Byakuya Kuchiki","Ginrei Kuchiki"], # Famille Kuchiki
    114 : ["Izuku Midoriya","All Might", "Nana Shimura"], # One For All
    113 : ["Shoto Todoroki", "Endeavor", "Fuyumi Todoroki", "Natsuo Todoroki", "Rei Todoroki","Dabi"], # Famille Todoroki
    112 : ["Kuroro Lucifer","All For One","Yhwach", "Neito Monoma","Enrico Pucci","Ging Freecss","Yuta Okkotsu","Makima","Marshall D. Teach","Tomura Shigaraki","Kid Buu","Kugo Ginjo","Kakashi Hatake","Kurapika","Momoshiki Otsutsuki"], # Voleur de Pouvoir
    111 : ["Kars","Meruem","Père","Cell","Mahoraga"], # Forme de vie ultime
    110: ["Kuroro Lucifer", "Hisoka", "Nobunaga", "Machi", "Shizuku Murasaki", "Franklin", "Feitan", "Phinks", "Sharnalk", "Bonolenov Ndongo", "Karuto Zoldyck", "Uvogin","Korutopi","Pakunoda","Majtani"], # Brigade Fantome
    109 : ["Leorio","Ging Freecss", "Botobai Gigante", "Pariston Hill","Kurapika"], # Zodiac
    108 : ["Menchi","Tsezugera", "Morel Mackernasey","Ging Freecss","Biscuit Kruger","Botobai Gigante","Pariston Hill"], # Hunter étoilé
    107 : ["Mito Freecss","Gon Freecss", "Ging Freecss"],
    106 : ["Aki Hanakawa","Denji","Kishibe","Power","Himeno","Kobeni Higashiyama","Hirokazu Arai","Angel","Beam", "Galgali","Makima"], # Section 4 Anti-Demon
    105 : ["Vegeta","Bulma","Trunks","Roi Vegeta","Gogeta","Vegetto","Gotenks"], # Famille de Vegeta
    104 : ["Son Goku", "Raditz", "Bardock", "Chichi" ,"Son Goten","Goku Black","Gogeta","Vegetto","Gotenks"], # Famille de Son Goku
    103 : ["Whis","Vados","Grand Pretre","Angel","Konan"], # Anges
    102 : ["Beerus","Champa","Belmod","Tomura Shigaraki","Chisaki Kai","Scar","Vanilla Ice","Johnny Joestar","Yamamoto","Grand Pretre","Zeno","Toppo","Baraggan"], # Annihilateur
    101 : ["Meliodas","Ban","King (NNT)","Diane","Gowther","Merlin","Escanor","Lust","Glutonny","Envy","Sloth","Ling Yao","King Bradley","Selim Bradley"], # Péché capital
    100 : ["Derrierie","Estarossa","Zeldris","Gloxinia","Drole","Galand","Gowther","Meliodas"], # Dix Commandements
    99 : ["Kirua Zoldyck" , "Irumi Zoldyck", "Miruki Zoldyck", "Aruka Zoldyck", "Zeno Zoldyck", "Silva Zoldyck", "Kikyo Zoldyck","Karuto Zoldyck"], # Zoldyck
    98 : ["Izuku Midoriya","Katsuki Bakugo","Ochaco Uraraka","Tenya Iida","Shoto Todoroki","Momo Yaoyorozu","Denki Kaminari","Fumikage Tokoyami","Kyoka Jiro","Toru Hagakure","Mezo Shoji","Mirio Togata","Tamaki Amajiki","Nejire Hado","All Might","Shota Aizawa","Midnight","Snipe","Vlad King","Neito Monoma","Mineta","Recovery Girl","Shihai Kuroiro","Shinso Hitoshi"], # Yuei
    97 : ["Roy Mustang", "Jean Havoc", "Riza Hawkeye","Heymans","Kain Fuery","Falman"], # Unité Mustang
    96 : ["King Bradley","Selim Bradley"], # Bradley
    95 : ["Scar","Frere de Scar","Miles"], # Ishval
    94 : ["Edward Elric","Paninya","Lan Fan","Buccaneer"], # Automail
    93 : ["Van Hoheinheim","Edward Elric","Alphonse Elric","Trisha Elric"], # Elric
    92 : ["Ling Yao","Mei Chang","Lan Fan","Fu","Xiao Mei"], # Xing
    91 : ["Edward Elric","Roy Mustang","Solf J. Kimblee","Alex Louis Armstrong","Tim Marcoh","Isaac McDougal","Alphonse Elric","Van Hoheinheim","Père","Scar","Mei Chang"], # Alchimiste
    90 : [], # Homonculus
    89 : ["Olivia Mira Armstrong","Alex Louis Armstrong"], # Armstrong
    88 : ["Kenjaku","Okuyasu Nijimura","Yuki Tsukumo","Fujitora","Pain","Ochaco Uraraka","Enrico Pucci","Satoru Gojo","Rikudo","Grand Pretre"], # Maitre de la Gravite
    87 : ["Dio Brando","Diego Brando","Giorno Giovanna","Dario Brando"], # Brando
    86 : ["Kyogai","Kanamue","Rui","Mukago","Enmu","Daki","Gyutaro","Akaza","Doma","Kokushibo"], # Lune
    85 : [], # Souffle de la Fleur
    84 : [], # Souffle de l'Eau
    83 : [], # Souffle de la Foudre
    82 : [], # Souffle du Soleil
    81 : ["Tanjiro Kamado","Sumiyoshi","Tanjuro Kamado","Nezuko Kamado"], # Kamado
    80 : ["Muzan","Nezuko Kamado","Tamayo","Yahaba","Fille Araignee","Mere Araignee","Shinzu","Dabra","Denji","Makima","Power","Meliodas","Estarossa","Zeldris","Gloxinia","Hendrickson","Gowther","Derrierie","Galand","Katana Man","Akaza","Mukago","Daki","Enmu","Rui","Kyogai","Yupi","Kanamue","Moshi","Doma"], # Demon
    79 : ["Aoi Kanzaki","Sumi Nakahara","Kiyo","Naho","Shinobu Kocho"], # Domaine des Papillons
    78 : ["Kanao Tsuyuri","Tanjiro Kamado","Zenitsu","Inosuke","Nezuko Kamado","Genya Shinazugawa","Murata","Ozaki","Yoriichi Tsugikuni","Shinobu Kocho", "Tengen Uzui","Yutaro Kurose","Aki Hanakawa","Angel","Beam","Denji","Galgali","Himeno","Hirokazu Arai","Kishibe","Makima","Power","Katana Man","Kobeni Higashiyama","Muichiro Tokito","Giyu Tomioka","Michiko Tendo","Aoi Kanzaki","Kyojuro Rengoku","Akane Sawatari"], # Pourfendeur de demons
    77 : ["Giyu Tomioka","Mitsuri Kanroji","Obanai Iguro","Sanemi Shinazugawa","Gyomei Himejima","Muichiro Tokito","Shinobu Kocho","Kyojuro Rengoku","Kanae Kocho","Tengen Uzui","Jigoro Kuwajima"], # Hashira
    76 : ["Kagaya Ubuyashiki"], # Ubuyashiki
    75 : ["Toji Fushiguro","Megumi Fushiguro","Tsumiki Fushiguro"], # Fushiguro
    74 : ["Noritoshi Kamo","Kenjaku"], # Kamo
    73 : ["Toji Fushiguro", "Naobito Zenin","Mai Zenin","Maki Zenin","Megumi Fushiguro","Naoya Zenin"], # Zenin
    72 : ["Yoshinobu Gakuganji","Utahime Iori","Arata Nitta","Mai Zenin","Kasumi Miwa","Kokichi Muta","Aoi Todo","Noritoshi Kamo","Momo Nishimiya"], # ecole de Kyoto
    71 : ["Masamichi Yaga","Ijichi","Satoru Gojo","Atsuya Kusakabe","Shoko Ieiri","Akari Nitta","Megumi Fushiguro","Yuji Itadori","Nobara Kugisaki","Maki Zenin","Toge Inumaki","Panda","Yuta Okkotsu","Kinji Hakari","Kento Nanami","Suguru Geto","Yu Haibara"], # ecole de Tokyo
    70 : ["Sukuna", "Mahito", "Jogo", "Dagon", "Hanami", "Choso","Kechizu"], # Fleaux
    69 : ["Jonathan Joestar", "Joseph Joestar", "Jotaro Kujo", "Josuke Higashikata", "Giorno Giovanna", "Jolyne Kujo", "Johnny Joestar"], # JoJo
    68 : ["Genos","Cyborgorilla","C-17","C-18","Rudol Von Stroheim","Franky","Bartholomew Kuma","Metal Knight"], # Cyborg
    67 : ["Grimasse","Garou","Bang"], # Dojo de Bang
    66 : ["Fujitora","Toph Beifong","Kaname Tosen","Komugi","Shaka","N'Doul","Kagaya Ubuyashiki","Yahaba","Gyomei Himejima"], # Aveugle 
    65 : ["Minato Namikaze", "Tobirama Senju", "Gran Torino","Sonic","Tenya Iida","Naobito Zenin","Flashy Flash","Shisui Uchiha","Izuku Midoriya","Mirko","Saitama", "Cheetu","Bonolenov Ndongo","Naoya Zenin","Feitan","Kirua Zoldyck","A","Tobirama Senju","Ethanbaron Nusjuro","Jugram","Yoruichi Shihoin","Kizaru","Akaza","Estarossa","Doma","Silva Zoldyck","Charlotte Katakuri"], # Monstre de vitesse TODO
    64 : ["Kaido","Ryukyu","Toshiro Hitsugaya","Shenron","Botobai Gigante","Super Shenron","Zeno Zoldyck"], # Draconique TODO  ,"Acnologia","Igneel"
    63 : ["Big Mom", "Charlotte Katakuri"], # equipage de Big Mom
    62 : ["Kaido", "King", "Queen"], # equipage de Kaido
    61 : ["Shanks","Yasopp","Benn Beckman"], # equipage de Shanks
    60 : ["Usopp","Kaya","Kuro","Merry","Yasopp"], # Ile de Sirop
    59 : ["Speedwagon","Caesar Zeppeli","Kakyoin","Jean-Pierre Polnareff","Mohamed Abdul","Rudol Von Stroheim","Okuyasu Nijimura","Rohan Kishibe","Koichi Hirose","Gyro Zeppeli","Bucciarati","Foo Fighters","Iggy","Hermes Costello"], # JoBros
    1 : ["Itachi Uchiha", "Kisame", "Deidara", "Sasori", "Hidan", "Kakuzu", "Pain", "Konan"], # Akatsuki
    2 : ["Son Goku", "Vegeta", "Son Gohan", "Trunks", "Son Goten","Gotenks", "Bardock", "Raditz", "Nappa", "Broly", "Cabba","Caulifla","Kale","Kefla","Pan","Roi Vegeta","Goku Black","Gogeta","Vegetto","Zamasu"], # Saiyan
    4 : ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Nico Robin", "Franky", "Brook", "Jinbe"], # Mugiwara
    5 : ["Itachi Uchiha", "Sasuke Uchiha", "Madara Uchiha", "Obito Uchiha", "Shisui Uchiha", "Izuna Uchiha", "Sarada Uchiha"], # Uchiha
    7 : ["Akainu", "Aokiji", "Kizaru", "Sengoku", "Fujitora", "Ryokugyu"], # Amiral
    10 : ["Edward Newgate", "Kaido", "Big Mom", "Shanks", "Marshall D. Teach","Monkey D. Luffy","Baggy"], # Yonko
    12 : ["Shinji Hirako","Ichigo Kurosaki"], # Vizard
    14 : ["Yamamoto", "Retsu Unohana", "Byakuya Kuchiki", "Kenpachi Zaraki", "Jushiro Ukitake", "Shunsui Kyoraku", "Sajin Komamura", "Mayuri", "Toshiro Hitsugaya", "Rukia Kuchiki","Kisuke Urahara","Yoruichi Shihoin","Ginrei Kuchiki","Isshin Kurosaki","Shinji Hirako","Soi Fon","Kaname Tosen","Gin Ichimaru"], # Gotei 13
    15 : ["Hashirama Senju", "Tobirama Senju", "Hiruzen Sarutobi", "Minato Namikaze", "Tsunade", "Kakashi Hatake", "Naruto Uzumaki","Mei Terumi", "Onoki", "Gaara","Danzo Shimura","Darui","A"], # Kage
    16 : ["Crocodile", "Don Quichotte Doflamingo", "Dracule Mihawk", "Bartholomew Kuma", "Boa Hancock", "Jinbe", "Baggy", "Trafalgar D. Water Law", "Marshall D. Teach","Gecko Moria"], # Shichibukai,
    17 : ["Jiraya","Orochimaru","Tsunade"], # Sannin
    18 : ["Monkey D. Dragon", "Emporio Ivankov", "Bartholomew Kuma", "Sabo", "Hack", "Inazuma", "Belo Betty", "Lindbergh", "Karasu","Grisha Yeager"], # Revolutionnaires
    19 : ["Monkey D. Luffy", "Monkey D. Garp", "Gol D. Roger", "Portgas D. Ace", "Monkey D. Dragon", "Sabo", "Trafalgar D. Water Law", "Marshall D. Teach","Portgas D. Rouge","Nefertari Vivi","Cobra","Haguar D. Sauro"], # Volonte du D
    20 : ["Kiba Inuzuka", "Karin", "Rob Lucci", "Chopper", "Kaido", "Marco", "Kaku","Cyborgorilla","Crablante", "Tonton","Pakkun", "Laboon","Sajin Komamura","Chachamaru","Kaburamaru","Lindbergh","Appa","Tama","Mirko","Nezu","Xiao Mei","Spinner","Ikarugo","Fumikage Tokoyami","Oolong","Sansa","Cheetu","Panda","Heinkel","Mike","Meleoron","Hatchan","Tamaki Amajiki","Pegui","Kenji","Yoruichi Shihoin","Hawk","Darius","Moshi","Champa","Tom Xaver","Grisha Yeager","King","Queen","Sieg Yeager","Shepherd Ju Peter","Beerus","Iggy","Yamato","Kon (hxh)","Hack","Marcus Mars","Neferopito","Jaygarcia Saturn","Koruto","Nekomamushi","Ethanbaron Nusjuro","Diego Brando","Topman Warcury","Dagon"], # Animal TODO
    21 : ["Sasuke Uchiha", "Suigetsu Hozuki", "Karin (naruto)", "Jugo"], # Taka
    22 : ["Pain", "Obito Uchiha", "Madara Uchiha", "Sasuke Uchiha","Momoshiki"], # Rinnegan
    23 : ["Naruto Uzumaki", "Sakura Haruno", "Sasuke Uchiha", "Kakashi Hatake", "Shikamaru Nara", "Choji Akimichi", "Ino Yamanaka", "Hinata Hyuga", "Kiba Inuzuka", "Shino Aburame", "Neji Hyuga", "Rock Lee", "Tenten","Kawaki","Danzo Shimura","Mitsuki","Shizune","Mizuki","Iruka","Sai","Himawari Uzumaki","Boruto Uzumaki","Minato Namikaze","Hashirama Senju","Tobirama Senju","Hiruzen Sarutobi","Tsunade","Jiraya","Tenzo","Shisui Uchiha","Pakkun","Kurenai Yuhi","Yugao Uzuki","Ebisu","Sarada Uchiha","Kushina Uzumaki","Nawaki","Asuma Sarutobi","Tonton"], # Konoha TODO
    24 : ["Gaara", "Temari", "Kankuro","Chiyo","Sasori"], # Suna TODO
    25 : ["Kisame", "Zabuza Momochi", "Haku", "Mei Terumi", "Suigetsu Hozuki"], # Kiri TODO
    26 : ["Darui", "Killer Bee"], # Kumo TODO
    27 : [ "Onoki", "Deidara"], # Iwa TODO
    28 : ["Naruto Uzumaki", "Killer Bee","Fû", "Yuji Itadori","Madara Uchiha","Obito Uchiha","Gaara","Mito Uzumaki","Kushina Uzumaki","Rikudo","Boruto Uzumaki","Kawaki"], # Receptacle TODO
    29 : ["Aang","Korra", "Portgas D. Ace","Shoto Todoroki", "Sabo", "Iroh", "Zuko", "Ozai", "Azula", "Itachi Uchiha", "Madara Uchiha", "Sasuke Uchiha","Kakuzu","Jogo","Mohamed Abdul","Dabi","Sukuna","Yamamoto","Roy Mustang","Kyojuro Rengoku","Escanor","Sanji","Endeavor","King","Yoriichi Tsugikuni","Merlin","Shisui Uchiha","Izuna Uchiha","Mitsuri Kanroji","Indra Otsutsuki","Toneri Otsutsuki","Hanzo","Danzo Shimura","Hiruzen Sarutobi","Rikudo","Meliodas","Jiraya","Onoki","Orochimaru","Minato Namikaze","Kakashi Hatake","Tobirama Senju","Naruto Uzumaki","Momoshiki Otsutsuki","Hashirama Senju","Kawaki"],# Maitre du Feu TODO
    30 : ["Aang","Korra", "Katara", "Suigetsu Hozuki", "Mei Terumi","Kakuzu","Tobirama Senju","Kisame","Hama","Halibel","Jinbe","Sakonji Urokodaki","Giyu Tomioka","Sabito","Tanjiro Kamado","Zabuza Momochi","N'Doul","Isaac McDougal","Boruto Uzumaki","Asura Otsutsuki","Toneri Otsutsuki","Hiruzen Sarutobi","Rikudo","Konan","Orochimaru","Kakashi Hatake","Itachi Uchiha","Naruto Uzumaki","Momoshiki Otsutsuki","Hashirama Senju","Dagon"], # Maitre de l'Eau TODO
    31 : ["Aang","Korra", "Toph Beifong", "Tenzo","Kakuzu","Asura Otsutsuki","Hashirama Senju","Toneri Otsutsuki","Danzo Shimura","Hiruzen Sarutobi","Rikudo","Konan","Jiraya","Onoki","Orochimaru","Drole","Kakashi Hatake","Tobirama Senju","Naruto Uzumaki","Momoshiki Otsutsuki","Diane"], # Maitre de la Terre TODO
    32 : ["Aang","Korra","Temari","Mei Terumi","Danzo Shimura","Boruto Uzumaki","Monkey D. Dragon","Wamuu","All For One","Tomura Shigaraki","Weather Report","Sanemi Shinazugawa","Asura Otsutsuki","Toneri Otsutsuki","Hiruzen Sarutobi","Rikudo","Asuma Sarutobi","Konan","Kakuzu","Onoki","Orochimaru","Minato Namikaze","Kakashi Hatake","Tobirama Senju","Naruto Uzumaki","Momoshiki Otsutsuki","Hashirama Senju"], # Maitre de l'Air TODO
    33 : ["Zuko", "Iroh", "Azula", "Ozai", "Kakashi Hatake","Sasuke Uchiha", "Killer Bee", "Darui", "Kakuzu", "Ener","Athena","Denki Kaminari","Zenitsu","Jigoro Kuwajima","Kirua Zoldyck","Yoruichi Shihoin","Akira Otoishi","Boruto Uzumaki","All For One","Tomura Shigaraki","Gilthunder","Lindbergh","Indra Otsutsuki","Toneri Otsutsuki","Hiruzen Sarutobi","Rikudo","Nekomamushi","Onoki","Orochimaru","A","Minato Namikaze","Tobirama Senju","Naruto Uzumaki","Momoshiki Otsutsuki","Hashirama Senju"], # Maitre de la foudre TODO
    34 : ["Shoto Todoroki","Aokiji", "Toshiro Hitsugaya", "Rukia Kuchiki","Natsuo Todoroki","Fuyumi Todoroki","Rei Todoroki", "Uraume","Haku","Isaac McDougal","Ghiaccio","Katara","Doma","Korra"], # Maitre de la Glace TODO Gray Fullbuster

    36 : ["Akainu", "Jogo","Mei Terumi","Onoki","Naruto Uzumaki"], # Maitre de la Lave TODO
    39 : ["Gaara","Iggy","Crocodile","Sajin Higawara","Ganju Shiba","Toph Beifong","Onoki"], # Maitre du Sable 
    40 : ["Roronoa Zoro", "Dracule Mihawk","Toji Fushiguro","Maki Zenin", "Killer Bee", "Tashigi", "Kaku", "Sasuke Uchiha","Kisame", "Suigetsu Hozuki", "Zabuza Momochi","Shanks", "Gol D. Roger", "Stain", "Ichigo Kurosaki", "Sosuke Aizen", "Kenpachi Zaraki", "Retsu Unohana", "Gin Ichimaru", "Darui", "Yamamoto", "Trunks", "Tapion", "Son Gohan", "Rukia Kuchiki", "Byakuya Kuchiki", "Kozuki Oden", "Trafalgar D. Water Law", "Brook","Fujitora","Shiryu", "Yhwach","Haruta Shigemo","Yugao Uzuki","Ling Yao","Halibel","Yajirobe","Kasumi Miwa","Spinner","Hatchan","Inazuma","Dorry","Tengen Uzui","Dabra","Meliodas", "Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman", "Hange Zoe", "Erwin Smith", "Jean Kirstein", "Conny Springer", "Sasha Braus", "Historia Reiss", "Ymir", "Reiner Braun", "Mike Zacharias","Zeldris","Gilthunder","Katana Man","Shimotsuki Kuina","Sakonji Urokodaki","Sabito","Shunsui Kyoraku","Coyote Stark","Kisuke Urahara","Barry The Chopper","Ganju Shiba","King","Jushiro Ukitake","Jean-Pierre Polnareff","Atomic Samurai","Kaito","Ryokugyu","Muichiro Tokito","Yoriichi Tsugikuni","Tanjuro Kamado","Kimimaro","Atsuya Kusakabe","Yachiru Kusajishi","Zenitsu","Genya Shinazugawa","Giyu Tomioka","Flashy Flash","Shisui Uchiha","Jugram","Hiromi Higuruma","Yuta Okkotsu","Izuna Uchiha","Sokka","Kyojuro Rengoku","Ozaki","Sajin Komamura","Kanao Tsuyuri","Olivia Mira Armstrong","Grand Roi Cold","Shinobu Kocho","Mitsuri Kanroji","Hanataro","Inosuke","Sanemi Shinazugawa","Hendrickson","Isshin Kurosaki","Indra Otsutsuki","Asura Otsutsuki","Yumichika","Shuhei","Mayuri","Danzo Shimura","Izuru Kira","Rikudo","Murata","Shinji Hirako","Sonic","Shukuro Tsukishima","Kugo Ginjo","Kaname Tosen","Angel","Nobunaga","Grimmjow","Feitan","Kento Nanami","Orochimaru","Kanae Kocho","Renji Abarai","Rangiku Matsumoto","Gecko Moria","Mahoraga","Ethanbaron Nusjuro","Yoruichi Shihoin","Vegetto","Kizaru","Silvers Rayleigh","Ulquiorra","Estarossa","Toshiro Hitsugaya"], # epeiste Cavendish
    41 : ["Fubuki","Tatsumaki","Himeno","Majin Buu","Babidi","Kaio Shin","Grand Roi Cold","Ginyu","Maitre Kaio","Whis","Vados","Grand Pretre"], # Telekinesiste
    42 : ["Marshall D. Teach", "Shiryu", "Aokiji"], # Equipage de Barbe Noire
    43 : ["Edward Newgate", "Marco", "Portgas D. Ace"], # Equipage de Barbe blanche
    44 : ["Naruto Uzumaki", "Kushina Uzumaki", "Pain", "Karin (naruto)", "Mito Uzumaki", "Boruto Uzumaki", "Himawari Uzumaki","Tsunade"], # Uzumaki
    45 : ["Neji Hyuga", "Hinata Hyuga", "Hanabi Hyuga","Himawari Uzumaki", "Boruto Uzumaki"], # Hyuga
    46 : ["Hashirama Senju", "Tobirama Senju", "Tsunade", "Nawaki"], # Senju
    47 : ["Kaguya Otsutsuki", "Rikudo", "Momoshiki Otsutsuki", "Toneri Otsutsuki", "Isshiki Otsutsuki","Indra Otsutsuki","Asura Otsutsuki"], # Otsutsuki
    48 : ["Meruem", "Pufu", "Yupi","Fû","Zazan"], # Insecte
    49 : ["Neferopito", "Yupi", "Pufu","Ichibe Hyosube","Senjumaru Shutara","Fu","Lan Fan","Gilthunder"], # Garde Royale Tenjiro Kirinji Ōetsu Nimaiya Kirio Hikifune
    # 50 Zeppeli
    50 : ["Will Zeppeli", "Caesar Zeppeli", "Gyro Zeppeli"], # Zeppeli
    52 : ["Kars", "Wamuu", "Esidisi"], # Pillier
    53 : ["Dio Brando","Diavolo", "Jotaro Kujo","Nighteye","Kira Yoshikage","Enrico Pucci","Charlotte Katakuri","Athena","Boingo","Neon Nostrad","Hit","Eri","Baraggan","Jugram","Yhwach","Momoshiki Otsutsuki","Grand Pretre","Whis","Vados","Diego Brando","Zamasu"], # Maitre du Temps
    54 : ["Kira Yoshikage", "Katsuki Bakugo","Solf J. Kimblee","Genthru","Deidara","Tengen Uzui","Bartholomew Kuma"], # Maitre de l'Explosion
    55 : ["Ghiaccio", "Prosciutto", "Formaggio", "Cioccolata","Risotto Nero"], # Squadra Esecuzioni
    56 : ["Jonathan Joestar", "Will Zeppeli", "Joseph Joestar", "Caesar Zeppeli", "Lisa Lisa", "Poco","Straizo","Kars"], # Hamon
    57 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo (Purple Haze)", "Abbacchio","Diavolo","Luca","Polpo","Trish","Neon Nostrad","Katana Man"], # Mafioso
    58 : ["Bucciarati","Giorno Giovanna", "Mista", "Narancia","Fugo (Purple Haze)", "Abbacchio","Trish"], # Team Bucciarati
    
}

all_techniques = {
    # Dragon Ball
    "Beerus" : [
        ["Hakai", "", "https://i.imgur.com/pAu6e7G.gif", "#e991f8"],
        ["Sphère Destructrice", "lance sa", "https://i.imgur.com/1YNIOFz.gif", "#bd8be2"],
        ["Éternue", "", "https://i.imgur.com/ZJNbnIH.gif","#cb6b7f"],
        ["Colère du Dieu de la destruction", "envoie la", "https://i.imgur.com/YhLMMCs.gif", "#f5a03e"],
        ["Enchainement", "envoie un", "https://i.imgur.com/gieaWmt.gif", "#84738d"],
        ["s''en fiche du combat et mange sa pizza", "", "https://i.imgur.com/lcT3lVL.gif", "#0662da"],
        ["Choqué de la nullité du combat", "", "https://i.imgur.com/Mqd6nVH.gif", "#9d7ea8"],
        ["N''en peut plus du combat", "", "https://i.imgur.com/O3a72WV.gif", "#5e2c97"],
    ],
    "Champa" : [
        ["Hakai", "", image_temporaire, hexadecimal_temporaire],
    ],
    "Gogeta" : [
        ["KAMEHAME-HAAAAAAAAAAA", "", "https://i.imgur.com/OnuTsTG.gif", "#371fde"],
        ["Punition divine", "utilise", "https://i.imgur.com/Ly5sMII.gif", "#654aba"],
        ["Punition divine", "utilise", "https://i.imgur.com/zRfP9iX.gif", "#fba009"],
        ["Combo météore", "enchaîne avec un", "https://i.imgur.com/CzRInJN.gif", "#456ae8"],
        ["Explosion météore", "charge son", "https://i.imgur.com/VoFhDpU.gif", "#1731df"],
        ["Combo météore", "réalise un", "https://i.imgur.com/dc7gIIj.gif", "#cd4a11"],
        ["Provoque l''ennemi", "", "https://i.imgur.com/w53p2Ly.gif", "#283b41"],
        ["Canon", "balance", "https://i.imgur.com/mZvXd1f.gif", "#7deef7"],
        ["Posture", "prend sa", "https://i.imgur.com/Qcgs5OY.gif", "#f2a877"],
    ],
    "Vegetto" : [
        ["Épée divine", "tranche avec son", image_temporaire, hexadecimal_temporaire],
        ["FINAL KAMEHAMEHAAAAAAA", "ENVOIE SON", "https://i.imgur.com/jXJQCP4.gif", "#59b1d5"],
        ["Attaque météore", "frappe avec", image_temporaire, hexadecimal_temporaire],
        ["God Impact", "fait un", "https://i.imgur.com/Gk4oMJP.gif", "#0d1313"],
        ["Provoque l''ennemi", "", "https://i.imgur.com/eEWWCNf.gif", "#053d17"],
        ["Se protège", "", "https://i.imgur.com/4ye5ZqT.gif", "#d8f7f9"],
    ],
    "Son Goku" : [
        ["Teleportation", "utilise sa", "https://i.imgur.com/skth3A1.gif", "#ff0000"],
        ["Kamehameha", "lance un", "https://i.imgur.com/ozIJcuK.gif", "#bcdef0"],
        ["Kamehameha", "lance un", "https://i.imgur.com/CuHFx5j.gif", "#49aad1"],
        ["Droite", "envoie une grosse", "https://i.imgur.com/7Dg7800.gif", "#d6d951"],
        ["Esquive", "tape des", "https://i.imgur.com/Rasq5gJ.gif", "#7e97eb"],
        ["Esquive", "", "https://i.imgur.com/XvK4qm2.gif", "#2c4322"],
        ["a pitié de son adversaire", "", "https://i.imgur.com/upTNZ6n.gif", "#516bc4"],
        ["Contre-attaque", "réalise une", "https://i.imgur.com/ApFWb3h.gif", "#a2c8e6"],
    ],
    "Son Gohan" : [
        ["Kamehameha", "lance son", "https://i.imgur.com/7v6zirc.gif", "#5bcbdd"],
        ["Makankosappo ultime", "utilise", "https://i.imgur.com/Q1ndqFd.gif", "#ad0027"],
        ["Contre-attaque", "effectue une", "https://i.imgur.com/pntJwnt.gif", "#e25cf0"],
        ["Déploie son Ki", "", "https://i.imgur.com/8dxkOae.gif", "#92eae3"],
    ],
    "Vegeta" : [
        ["Canon Garric", "lance", "https://i.imgur.com/goDqVvM.gif", "#c369e1"],
        ["Final Flash", "utilise", "https://i.imgur.com/yE2sHmK.gif", "#dedb4b"],
        ["Rayon de Ki", "envoie un", "https://i.imgur.com/ewiKMhh.gif", "#eb3d21"],
        ["Enchaînement", "fait un", "https://i.imgur.com/CHwCkX7.gif", "#dee385"],
        ["Frappe Flash", "envoie une", "https://i.imgur.com/JRk7aff.gif", "#fa8e20"],
    ],
    "Broly" : [
        ["Eraser cannon", "utilise", "https://i.imgur.com/4bMEl34.gif", "#050f04"],
        ["Destruction planétaire", "charge son", "https://i.imgur.com/IHSDGQl.gif", "#66fda7"],
        ["Souffle légendaire", "crache son", "https://i.imgur.com/8hrxYAO.gif", "#b7dd1f"],
        ["Enchaînement Berserker", "", "https://i.imgur.com/wnuSkOn.gif", "#7f1f07"],
        ["Traine l''adversaire", "", "https://i.imgur.com/kZM2y6y.gif", "#60b3e4"],
        ["Est Furieux", "", "https://i.imgur.com/GR5umvo.gif", "#5dba2c"],
    ],
    "Jiren" : [
        ["Impact de ki", "lance un", "https://i.imgur.com/v4Ipwkp.gif", "#c85d33"],
        ["Uppercut colossal", "envoie un", "https://i.imgur.com/3nVDoiI.gif", "#161318"],
        ["Ki invisible", "attaque avec du", image_temporaire, hexadecimal_temporaire],
        ["Contre avec ses yeux", "", "https://i.imgur.com/4OKu0yo.gif", "#140f1f"],
        ["Contre puissant", "effectue un", "https://i.imgur.com/pNVq3rr.gif", "#140f1f"],
        ["Brûle tout", "", "https://i.imgur.com/RHx6Eda.gif", "#d94533"]
    ],
    "Toppo" : [
        ["Hakai imparfait", "utilise son", "https://i.imgur.com/T8SJaT6.gif", "#58055b"],
        ["Boule de Hakai", "envoie des", "https://i.imgur.com/nHT7Zpz.gif", "#88057c"],
        ["Ki des Doigt", "balance du", "https://i.imgur.com/PR38V3H.gif", "#04070e"],
        ["Enchaînement téléporté", "", "https://i.imgur.com/Ox7McyB.gif", "#312371"],
        ["Vague de ki", "envoie une", "https://i.imgur.com/KnXpsyl.gif", "#a9312c"],
    ],
    "Goku Black" : [
        ["Faux de ki", "dégaine sa", "https://i.imgur.com/ar4YKPP.gif", "#f57ffa"],
        ["Black kamehameha", "utilise", "https://i.imgur.com/54GeAFB.gif", "#f906ef"],
        ["Explosion sacrée", "envoie une", "https://i.imgur.com/rPNct67.gif", "#203d21"],
        ["Annihilation", "", "https://i.imgur.com/LupZy1w.gif", "#6662bc"],
        ["Parade", "", "https://i.imgur.com/E035gaW.gif","#040205"],
    ],
    "Hit" : [
        ["Point Vitaux", "vise les", "https://i.imgur.com/vi0Kg6z.gif", "#ff3bde"],
        ["Fracture temporelle", "", "https://i.imgur.com/kklcPtu.gif", "#3603f6"],
        ["Saut temporel", "", "https://i.imgur.com/rP20Hmt.gif", "#071131"],
        ["Massacrer son adversaire", "arrête le temps pour", "https://i.imgur.com/HKcldBa.gif", "#44dfa3"],
    ],
    "Piccolo" : [
        ["Makankosappo", "charge son", "https://i.imgur.com/HBg2V3a.gif", "#827707"],
        ["Charge", "", "https://i.imgur.com/V4r06Ui.gif", "#361c67"],
        ["S''échauffe", "", "https://i.imgur.com/Gck6OH7.gif", "#2ad918"],
        ["Est sérieux", "", "https://i.imgur.com/npQbMoy.gif", "#f5e984"],
    ],
    "Trunks" : [
        ["Épée", "dégaine son", 'https://i.imgur.com/1GEs349.gif', "#394477"],
        ["Masenko", "envoie", "https://i.imgur.com/sRCIDcu.gif", "#c9cd50"],
        ["Attaque brûlante", "prépare son", "https://i.imgur.com/m29kdBa.gif", "#0e6b9f"]
    ],
    "Kefla" : [
        ["Boules de Ki", "balance des", "https://i.imgur.com/zF5aKBU.gif", "#d05d5a"],
        ["Charge son Ki", "", "https://i.imgur.com/BBsF4DS.gif", "#6ac452"],
        ["Disques berserk", "charge ses", "https://i.imgur.com/sJ6idlE.gif", "#0a1605"],
    ],
    # Full Metal Alchemist
    "Père": [
        ["Alchimie", "utilise l''", "https://i.imgur.com/KzMK7Xu.gif", "#ec000e"],
    ],
    # Avatar
    "Aang": [
        ["Colonnes de flamme", "envoie des", "https://i.imgur.com/nqUJVqG.gif", "#f55a42"],
    ],
    # Demon Slayer
    "Tanjiro Kamado" : [
        ["Souffle de l''eau", "utilise le", "https://media.giphy.com/media/RK4qNmmMj17yX80MOY/giphy.gif", "#0000FF"],
    ],
    "Rui" : [
        ["Prison de fils", "créé une", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/85/RuiSang1.gif/revision/latest?cb=20200627145048&path-prefix=fr", "#490c11"],
        ["Cage du regard assassin", "créé la", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/5f/RuiSang2.gif/revision/latest?cb=20200627145112&path-prefix=fr", "#490c11"],
        ["Fils à Trancher Rotatif", "créé une roue rotative de", "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/8/86/RuiSang3.gif/revision/latest?cb=20200627145143&path-prefix=fr", "#490c11"],
    ],
    # Naruto
    "Sasuke Uchiha" : [
        ["Rinnegan", "active son", "https://i.imgur.com/qJ5mfnz.gif", "#d100ff"],
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

    # Hunter x Hunter
    "Gon" : [
        ["Jajanken", "prépare son", image_temporaire, hexadecimal_temporaire],
        ["Recharge", "", "", "#5c3307"],
    ],
    "Franklin" : [
        ["Déluge de Balles", "déverse un", "https://i.imgur.com/0KyJyzH.gif", "#5c3307"],
        ["Recharge", "", "", "#5c3307"],
    ],
    "Uvogin" : [
        ["Big Bang Impact", "lance un", "https://i.imgur.com/I8LlLN5.gif", "#5c3307"],
        ["Nen", "déploie son", "https://i.imgur.com/CsGYEAi.gif", "#5c3307"],
        ["Enragé", "devient", "", "#5c3307"],
    ],
    "Morel Mackernasey": [
        ["Ecran de fumee", "lance un", "https://i.imgur.com/sNGqJb3.gif", "#d100ff"],
    ],
    # Bleach
    "Ichigo" : [
        ["Getsuga Tensho", "envoie un", "https://i.imgur.com/mHF2EnN.gif", "#360204"],
        ["Cero", "crache un", "https://i.imgur.com/70blaTc.gif", "#d1252b"],
        ["Slash de Reitasu", "envoie des", "https://i.imgur.com/PUwrStw.gif", "#58120b"],
        ["Furie", "est dans une", "https://i.imgur.com/X68C2XH.gif", "#c37f3c"],
        ["Mugetsu", "active", "https://i.imgur.com/oTTHb5B.gif", "#000000"],
        ["l''attaque de l''adversaire", "attrape", "https://i.imgur.com/amStjId.gif", "#040207"],
    ],
    "Yhwach" : [ #TOGIF
        ["The Almighty", "active", image_temporaire, hexadecimal_temporaire],
        ["Sankt Altar", "invoque", "https://i.imgur.com/R34bul2.png", "#1064bc"],
        ["Heilig Pfeil", "déchaine", image_temporaire, "#1064bc"],
        ["Épée de Reishi", "crée", "https://i.imgur.com/cJoydwT.png", "#30b1cb"]
    ],
    "Aizen" : [ #TOGIF
        ["Kanzen Saimin", "trompe avec", "https://i.imgur.com/mkttGe5.gif", "#3994a4"],
        ["Hakuda", "utilise son", image_temporaire, hexadecimal_temporaire],
        ["Hadō #99 : Goryūtenmetsu", "récite le", image_temporaire, hexadecimal_temporaire],
        ["Raikoho", "utilise", "https://i.imgur.com/wEqU1hb.gif", "#dfe107"],
        ["Pression Spirituelle", "utilise sa", image_temporaire, hexadecimal_temporaire],
    ],
    "Yamamoto" : [
        ["Zanka no Tachi : Est", "utilise", "https://imgur.com/zgVMTdr.gif", "#5e3026"],
        ["Zanka no Tachi : Ouest", "utilise", "https://imgur.com/CCH55ZX.gif", "#de981b"],
        ["Zanka no Tachi : Nord", "utilise", "https://imgur.com/zQZmGM3.gif", "#540a1d"],
        ["Zanka no Tachi : Sud", "utilise", "https://imgur.com/IRxf4ks.gif", "#e47a1c"],
    ],
    "Kyoraku" : [
        ["Kageoni", "manipule les ombres,", "https://i.imgur.com/RKm4Qqq.gif", "#7ebfc5"],
        ["Takaoni", "domine l''air,", "https://i.imgur.com/KAeJRad.gif", "#4490b5"],
        ["Bushōgoma", "tourbillone,", "https://i.imgur.com/cbmbqUY.gif", "#c1edf1"],
    ],
    "Ichibe Hyosube" : [
        ["Senri Tsūtenshō", "écrase avec", "https://i.imgur.com/Elu42jv.gif", "#000000"],
        ["Ichimonji", "coupe le nom avec ", "https://i.imgur.com/M0o4Abs.gif", "#000000"],
        ["Shirafude Ichimonji", "change le nom avec", "https://i.imgur.com/1vQpQJf.gif", "#000000"],
    ],
    "Senjumaru" : [
        ["Shatatsu Karagara Shigarami no Tsuji", "active son bankai,", "https://i.imgur.com/9jh8re0.gif", "#fb0c32"],
        ["Shide no Rokushiki Ukimon no Hata", "active", "https://i.imgur.com/frGkeC0.gif", "#fb0c32"],
        ["Shigarami : défense", "utilise", "https://i.imgur.com/RXvtOaN.gif", "#b19e98"], #TOCUT
        ["Destin", "écrit le", image_temporaire, hexadecimal_temporaire],
    ],
    "Kisuke Urahara" : [
        ["Hadō #91 : Senju Kōten Taihō", "incante", "https://i.imgur.com/ZabGk5k.gif", "#c84ea4"],#TOSPEED
        ["Nake, Benihime", "utilise", "https://i.imgur.com/Mozt8qm.gif", "#3f4e61"],
        ["Hiasobi, Benihime", "active", "https://i.imgur.com/PxsXbaN.gif", "#d33143"],
        ["Kamisori, Benihime", "envoie", "https://i.imgur.com/2NXRhZP.gif", "#ce6a4e"],
    ],
    "Byakuya Kuchiki" : [
        ["Senkei", "dévoile la vraie forme de son bankai...", "https://i.imgur.com/SI3rmzH.png", "#feccee"],
        ["Senbonzakura", "envoie", "https://i.imgur.com/4ZuadNQ.gif", "#feccee"],
        ["Byakurai", "incante", "https://i.imgur.com/6EOusS4.gif", "#88bad4"],
        ["Senka", "se déplace avec le", image_temporaire, hexadecimal_temporaire],
    ],
    "Jugram" : [
        ["The Balance", "relâche son", "https://i.imgur.com/n7dxZHp.gif", "#1d7e86"],
        ["Épée", "sort son", "https://i.imgur.com/xmPTmXs.gif", "#3f4e61"],
        ["parade", "réalise une", image_temporaire, hexadecimal_temporaire],
    ],
    "Kenpachi" : [
        ["Nozarashi", "appelle", "https://i.imgur.com/AKUkZjd.gif", "#670f32"],
        ["Reiatsu", "relâche son", "https://i.imgur.com/9srFwb8.gif", "#dfe107"],
        ["Slash", "envoie un", "https://i.imgur.com/XrfmTF1.gif", "#e3e0c0"],
    ],
    "Retsu Unohana" : [
        ["Minazuki", "attaque avec", "https://imgur.com/vAN5RVV.gif", "#400e10"],
        ["parade", "réalise une", image_temporaire, hexadecimal_temporaire],
        ["charge", "fait une", image_temporaire, hexadecimal_temporaire],
    ],
    "Ulquiorra" : [
        ["Cero ulquiorra", "relâche son", "https://i.imgur.com/zbAspmw.gif", "#23dca8"],
        ["Resureccion : Segunda", "se renforce avec", "https://i.imgur.com/fDcyC7u.gif", "#23dca8"],
        ["Lanza del Relámpago", "prépare sa", "https://i.imgur.com/4HTHgLe.gif", "#23dca8"],
    ],
    "Coyote Stark" : [
        ["Meute de loups", "relâche sa", "https://imgur.com/dk5nUz1.gif", "#468eb6"],
        ["Cero", "tire un", "https://imgur.com/LW5pio6.gif", "#11b2e2"],
        ["Cero Metralleta", "tire des", "https://imgur.com/zaILTvs.gif", "#1449c1"],
    ],
    "Gin Ichimaru" : [
        ["Shinsō", "relâche", "https://imgur.com/L3xpAp2.gif", "#0582b1"],
        ["Kamishini no Yari", "relâche", "https://imgur.com/fO4Lur4.gif", "#979694"],
    ],
    "Renji" : [
        ["Zabimaru", "fait hurler", "https://i.imgur.com/SOl62hI.gif", "#0b5664"],
        ["Sōō Zabimaru", "envoie chasser", "https://i.imgur.com/6vXLNo0.gif", "#99a2ad"],
        ["Zaga Teppō", "réduit l''ennemi en cendres avec", "https://i.imgur.com/ItRVkFP.gif", hexadecimal_temporaire],
    ],
        "Yoruichi Shihoin" : [
        ["Shunko", "active son", "https://i.imgur.com/eaBDVuu.gif", "#f0f0f0"],
        ["Coup de Poing", "balance un", "https://i.pinimg.com/originals/6c/e5/ae/6ce5ae1ee5b9f968094cf4a87e07a87d.gif", "#522949"],
        ["Hakuda", "détruit avec son", "https://i.imgur.com/3TvdfJS.gif", "#ea6b42"],
        ["Rafale", "balance une", "https://i.imgur.com/Qoz9ITj.gif", "#f2e8a8"],
    ],
    #Jujutsu Kaisen
    "Satoru Gojo" : [
        ["Infini", "active l''", "https://i.imgur.com/ZCJhdVh.gif", "#518c98"],
        ["Rouge", "utilise", "https://i.imgur.com/1EFWK0U.gif", "#f90727"],
        ["Bleu", "utilise", "https://i.imgur.com/3fXmK6l.gif", "#1365ca"],
        ["Violet", "forme un", "https://i.imgur.com/QcO2cfC.gif", "#a60ef1"],
        ["Extension du territoire : Sphère de l''infini", "active son", "https://i.imgur.com/NHUyKs8.gif", "#2d1a28"],
        ["Rayon noir", "réussit un", image_temporaire, hexadecimal_temporaire],
        ["Maîtrise du corps à corps", "montre sa", "https://i.imgur.com/OLo0crU.gif", "#17436d"],
    ],
    "Sukuna" : [
        ["Trancher sukuna", "utilise", "https://i.imgur.com/Kr5pygu.gif", "#040404"],
        ["Découper", "utilise", "https://i.imgur.com/jzZsHne.gif", "#8b9095"],
        ["Fuga", "utilise", "https://i.imgur.com/i0PQMY3.gif", "#df4012"],
        ["Rayon noir", "réussit un", image_temporaire, hexadecimal_temporaire],
        ["Extension du territoire : Autel démoniaque", "active son", "https://i.imgur.com/gvKzpbm.gif", "#863022"],
        ["Écrasement de tête", "fait un", "https://i.imgur.com/uMTONBX.gif", "#2a4c39"],
    ],
    "Kenjaku" : [
        ["Uzumaki", "dévoile sa technique ultime : ", "https://i.imgur.com/AQvIrP1.gif", "#5e197f"],
        ["Explosion des hématies", "utilise", "https://i.imgur.com/cQwFQR0.gif", "#c5a1a5"],
        ["Manipulation des esprits", "utilise la", "https://i.imgur.com/tJXtEav.gif", "#d00405"],
        ["Pression", "utilise sa", "https://i.imgur.com/dV7tETr.gif", "#eadace"],
        ["Extension du territoire : Profusion Utérine", "utilise son", "https://i.imgur.com/tdCIAAP.gif", "#ae9f9e"],
        ["Esquive", "", "https://i.imgur.com/r25zFby.gif", "#a56f8d"],
    ],
    "Toji Fushiguro" : [
        ["Taillade l''adversaire", "", "https://i.imgur.com/2EEqXgy.gif", "#714125"],
        ["Esquives", "fait des", "https://i.imgur.com/5YShl2n.gif", "#4c2e1f"],
        ["Contre", "effectue un", "https://i.imgur.com/zKHDC83.gif", "#587482"],
        ["Taillade Fulgurante", "effectue une", "https://i.imgur.com/jqglnGo.gif", "#2b4358"],
        ["Flashstep", "fait un", "https://i.imgur.com/m6ZionY.gif", "#223c56"],
        ["Extase", "est en", "https://i.imgur.com/7Whfwjf.gif", "#39c4e2"],
        ["Nuage", "affute", "https://i.imgur.com/BwVVOwJ.gif", "#f9bfa4"],
    ],
    "Yuta Okkotsu" : [
        ["Katana", "coupe avec son", "https://i.imgur.com/Ga15R1e.gif", "#aa9e88"],
        ["Se défend", "", "https://i.imgur.com/ZoQZnft.gif", "#4d4a4f"],
        ["Katana d''énergie", "charge son", "https://i.imgur.com/DcqaGRT.gif", "#a03364"],
        ["Rayon d''énergie occulte", "envoie un", "https://i.imgur.com/Rx2CfzF.gif", "#dd8fbf"],
        ["Rika", "invoque", "https://i.imgur.com/7rpjIBU.gif", "#fbedf5"],
        ["Attaque Coordonnée", "fait une", "https://i.imgur.com/fy48wQW.gif", "#b92090"],
        ["Énergie occulte", "relâche son", "https://i.imgur.com/7whSzsH.gif", "#a80729"],
    ],
    "Mahoraga" : [
        ["Adapté", "s''est", "https://i.imgur.com/2pqEuEd.gif", "#f9f8f9"],
        ["Est Invoqué", "", "https://i.imgur.com/wvQF3DE.gif", "#f5f7f4"],
        ["Rafale de poings", "envoie une", "https://i.imgur.com/6yHs8Sk.gif", "#080c0f"],
        ["Pourchasse l''ennemi", "", "https://i.imgur.com/aRsx59h.gif", "#2a2f35"],
    ],
    "Aoi Todo" : [
        ["Charge ultime", "fait sa", "https://i.imgur.com/EETlu3D.gif", "#61918b"],
        ["Boogie Woogie", "utilise son", "https://i.imgur.com/gOCAlHY.gif", "#676165"],
        ["dans le dos de l''ennemi", "se téléporte", "https://i.imgur.com/eanB7MB.gif", "#876a4a"],
        ["BLACK FLASH", "assène un", "https://i.imgur.com/6OYVEpW.gif", "#090d18"],
        ["Poing Fulgurant", "prépare son", "https://i.imgur.com/yYH3z4Z.gif","#4c0704"],
        ["Victoire", "élabore sa", "https://i.imgur.com/sPpAXab.gif", "#151b66"],
        ["Suplex", "fait un", "https://i.imgur.com/i7q4A5X.gif", "#c8c2bc"],
    ],
    "Suguru Geto" : [
        ["Nuage", "utilise", "https://i.imgur.com/L2cwdSt.gif", "#bd842f"],
        ["Dragon", "envoie son", "https://i.imgur.com/vENO65T.gif", "#8a5c45"],
        ["Taijutsu", "utilise son", "https://i.imgur.com/DMfeZCi.gif", "#6f7c76"],
        ["Manipulation des esprits", "utilise la", "https://i.imgur.com/naYL3Lf.gif", "#232022"],
        ["Ver", "envoie un", "https://i.imgur.com/WS1aZ3y.gif", "#908275"],
    ],
    "Choso" : [
        ["Dagues de sang", "crée des", "https://i.imgur.com/Z0krrYM.gif", "#ac4640"],
        ["Sekirin Yakudō", "augmente ses performances avec", "https://i.imgur.com/3HnD0Zz.gif", "#237960"],
        ["Convergence", "utilise", "https://i.imgur.com/p81PbSC.gif", "#9d180b"],
        ["Puissant coup de poing", "envoie un", "https://i.imgur.com/o1nVrCd.gif", "#381c23"],
        ["Senketsu", "lance son", "https://i.imgur.com/SoSD9Oa.gif", "#090203"],
    ],
    "Mahito" : [
        ["Super résistant", "est", "https://i.imgur.com/YiidnjI.gif", "#3a404f"],
        ["Black Flash", "envoie un", "https://i.imgur.com/6uHHzCS.gif", "#8f13aa"],
        ["Extension du territoire : altération divine", "ouvre son", "https://i.imgur.com/R3BstVT.gif", "#422079"],
        ["Rafale d''humains altérés", "tire une", "https://i.imgur.com/zFNPDWk.gif", "#252326"],
    ],
    "Jogo" : [
        ["Boule de feu", "prépare", "https://i.imgur.com/tu8qKsL.gif", "#e7672f"],
        ["Feu cataclysmique", "écrase avec son", "https://i.imgur.com/dx69mj1.gif", "#ed972f"],
        ["Tsunami de la fournaise", "utilise", "https://i.imgur.com/eNWy4QF.gif", "#e94d13"],
        ["Piège volcanique", "a placé un", "https://i.imgur.com/N1h2oCP.gif", "#faa410"],
        ["Maximum : Météore", "prépare son attaque", "https://i.imgur.com/ZLTscTz.gif", "#ef9a15"],
    ],
    "Uraume" : [
        ["Blizzard", "crée un", "https://i.imgur.com/n48aUYt.gif", "#7dd7f9"],
        ["Piliers de glace", "crée des", "https://i.imgur.com/sP7V4vW.gif", "#7dd7f9"],
        ["Se Protège avec de la glace", "", image_temporaire, hexadecimal_temporaire],
    ],
    "Kinji Hakari" : [
        ["Domaine", "se bat dans son", "https://i.imgur.com/Ll8PJQX.gif", "#e44b3d"],
        ["Extension du territoire : Pari Mortel Inutile", "active son", "https://i.imgur.com/sRtgcrA.gif", "#f638cc"],
        ["Boost d''énergie maudite", "a obtenu son", "https://i.imgur.com/h3BRPxK.gif", "#34cdab"],
        ["Frappe sous coc", "utilise une", "https://i.imgur.com/9DSyrOs.gif", "#fffdfe"],
    ],
    "Yuki Tsukumo" : [
        ["Garuda", "envoie", "https://i.imgur.com/ZM4fvvn.gif", "#b79ca5"],
        ["Maximum : Trou Noir", "utilise son attaque", "https://i.imgur.com/gOqsYHZ.gif", "#000000"],
        ["Domaine simple", "utilise", "https://i.imgur.com/mIcDtqJ.png", "#1a1a1a"],
    ],
    "Hanami" : [
        ["Champ de fleurs", "utilise", "https://i.imgur.com/sagxuqt.gif", "#c18944"],
        ["Aura roncière", "montre son", "https://i.imgur.com/XWKu20j.gif", "#d95246"],
        ["Posture défensive", "prend une", "https://i.imgur.com/VeAtE6h.gif", "#9f7f6f"],
        ["Extension du territoire : mer de lumière cérémonielle", "utilise son", "https://i.imgur.com/HneVwfk.gif", "#fafca4"],
    ],
    "Dagon" : [
        ["Boit l''ennemi", "", "https://i.imgur.com/GOIylfZ.gif", "#90918c"],
        ["Se transforme", "", "https://i.imgur.com/sAjievT.gif", "#f90000"],
        ["Shikigamis marins", "invoque ses", "https://i.imgur.com/jNVPupR.png", "#8eb740"],
        ["Escadron maritime", "invoque", "https://i.imgur.com/QxkmETz.png", "#85edec"],
        ["Extension du territoire : Horizon du Skandha Captivant", "utilise son", "https://i.imgur.com/bd0Wllg.gif", "#46dced"],
    ],
      "Naobito Zenin" : [
        ["Décomposition des mouvements", "pratique la", "https://i.imgur.com/6dtJ6ld.gif", "#677888"],
    ],
    "Kento Nanami" : [
        ["Attrape l''ennemi par les cheveux", "", "https://i.imgur.com/6dtJ6ld.gif", "#ddd8ae"],
        ["Attaquer","se prépare à", "https://i.imgur.com/XNH41aE.gif" ,"#14899f"],
        ["Attaque", "charge son", "https://i.imgur.com/P16NNUU.gif", "#14899f"],
        ["7/10ème", "attaque aux", "https://i.imgur.com/GcDA3Bg.gif", "#000000"],
        ["Attaque sans hésiter", "", "https://i.imgur.com/saF6Iht.gif", "#f3d6cb"],
        ["Heures sups","passe en", "https://i.imgur.com/z3USMrr.gif","#14899f"]
    ],
    # The Seven Deadly Sins
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
    ],
    
    # My Hero Academia
    "All Might" : [
        ["United States of Smash", "utilise l''","https://i.imgur.com/tGRgG5e.mp4", "#FF0000"], #TOREVIEW format mp4
    ],
}