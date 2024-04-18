image_temporaire = "https://picsum.photos/900/500"
all_characters_templates = [
            # """ PERSONNAGE DRAGON BALL"""
            # Personnages X
            ("Vegeta", "X", "https://i.imgur.com/sSjFzsz.jpeg", 0, 0, 0),
            ("Goku", "X", "https://i.imgur.com/k2T0SKd.gif", 0, 0, 0),
            ("Zeno", "X", "https://i.imgur.com/W579wtw.gif", 0, 0, 0),
            ("Grand Prêtre", "X", "https://pa1.aminoapps.com/6541/a48a166406b4a43ae04845d7c33aa93c35208c66_hq.gif", 0, 0, 0),
            # Personnages SS
            ("Broly", "SS", "https://www.dragon-ball-gif.com/wp-content/uploads/2022/01/Broly-Super-Saiyan.gif", 0, 0, 0), #TODO
            ("Golden Freezer", "SS", 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0a290752-d7eb-45e3-aa31-8e71b544cde0/dbm1yiz-525bf1bb-1bba-42e3-88bc-da271e0fc047.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBhMjkwNzUyLWQ3ZWItNDVlMy1hYTMxLThlNzFiNTQ0Y2RlMFwvZGJtMXlpei01MjViZjFiYi0xYmJhLTQyZTMtODhiYy1kYTI3MWUwZmMwNDcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.d2ovx3xnc5I44dQTZSSnyRLGuDKRZnyPp0m3qDlyHVo', 0, 0, 0),
            ("Beerus", "SS", 'https://media1.tenor.com/m/QlDaIzrNXNwAAAAC/beerus-stare.gif', 0, 0, 0),
            ("Champa", "SS", 'https://media1.tenor.com/m/cSbQJiwt5V4AAAAC/dbz-dbs.gif', 0, 0, 0),
            ("Vados", "SS", 'https://media1.tenor.com/m/-Ku4nzfbkX0AAAAC/dbz-dbs.gif', 0, 0, 0),
            ("Whis", "SS", 'https://media1.tenor.com/m/nFIwm1YB8XwAAAAC/dbz-training.gif', 0, 0, 0),
            ("Goku Black", "SS", 'https://media1.tenor.com/m/AL-nOjhTt4UAAAAC/goku-black-smile.gif', 0, 0, 0),
            ("Zamasu", "SS", 'https://media1.tenor.com/m/TY1_T_suBr4AAAAC/zamasu-goku.gif', 0, 0, 0),
            ("Jiren", "SS", 'https://media1.tenor.com/m/97ITDVHgUwoAAAAC/dragon-ball-stare.gif', 0, 0, 0),
            ("Gogeta", "SS", "https://i.imgur.com/5sTq4Q6.gif", 0, 0, 0),
            ("Vegeto", "SS", "https://i.imgur.com/DBewj1R.gif", 0, 0, 0),
            # Personnages S
            ("Hit", "S", 'https://media1.tenor.com/m/4TplENjWWCcAAAAd/hit-assassin.gif', 0, 0, 0),
            ("Kefla", "S", 'https://media1.tenor.com/m/kV_BbTxQANgAAAAC/dragon-ball-dragon-ball-super.gif', 0, 0, 0),
            ("Toppo", "S", 'https://media1.tenor.com/m/v6Yn-JgdX2gAAAAC/toppo-cartoon.gif', 0, 0, 0), #TOREVIEW
            ("Android 17", "S", 'https://media1.tenor.com/m/1EE6jYeD874AAAAC/android17-dbz.gif', 0, 0, 0),
            ("Gotenks", "S", 'https://media1.tenor.com/m/rqT2GpNIWfMAAAAd/goten-super-saiyan.gif', 0, 0, 0),
            ("Gohan", "S", 'https://media1.tenor.com/m/vGaQ4md93OwAAAAd/gohan-son.gif', 0, 0, 0), # TOREVIEW
            ("Kid Buu", "S", 'https://media1.tenor.com/m/YCONZC1xuUcAAAAC/majin-buu-evil-smile.gif', 0, 0, 0),
            ("Shenron", "S", "https://64.media.tumblr.com/ca4c3f59f970ad67d482f1f43bf3f326/tumblr_onwpfrpHmn1qzxv73o1_540.gif", 0, 0, 0),

            # Personnages A
            ("Cell", "A", 'https://media1.tenor.com/m/qGAi7YUulBcAAAAd/dragon-ball-z-perfect-cell.gif', 0, 0, 0),
            ("Majin Buu", "A", 'https://media1.tenor.com/m/Z_LDrqLUt34AAAAC/comiendo-eat.gif', 0, 0, 0),
            ("Kale", "A", 'https://media1.tenor.com/m/0x6K_lFUUdkAAAAC/dbs-kale.gif', 0, 0, 0),
            ("Caulifla", "A", 'https://media1.tenor.com/m/dPo3nmJ2NUsAAAAC/caulifla-dragon-ball-z.gif', 0, 0, 0),
            ("Trunks", "A", 'https://media1.tenor.com/m/JeLASItCa6UAAAAC/dbz-dragon-ball.gif', 0, 0, 0), # TOREVIEW
            # Personnages B
            ("Cabba", "B", 'https://static.wikia.nocookie.net/dragonball/images/1/1e/Cabb%C3%A9_en_Super_Saiyan.jpg/revision/latest?cb=20160403201037&path-prefix=fr', 0, 0, 0),
            ("C-18", "B", 'https://static.wikia.nocookie.net/dragonball/images/8/87/Dragon-Ball-Super-Episode-94-31-739x416.jpg/revision/latest?cb=20170702190036&path-prefix=fr', 0, 0, 0),
            ("Frost", "B", 'https://static.wikia.nocookie.net/dragonball/images/c/c4/Dragon-Ball-Super-Episode-108-image-104.jpg/revision/latest/scale-to-width-down/1000?cb=20170925170848&path-prefix=fr', 0, 0, 0),
            ("Bardock", "B", 'https://static.wikia.nocookie.net/dragonball/images/f/ff/Bardack_dans_le_film_DBS_Broly.jpg/revision/latest/scale-to-width-down/1000?cb=20220711114340&path-prefix=fr', 0, 0, 0),
            # Personnages C
            ("Ten Shin Han", "C", 'https://static.wikia.nocookie.net/dragonball/images/9/90/TienBuuSaga.png/revision/latest?cb=20130921104728&path-prefix=fr', 0, 0, 0),
            ("Pui Pui", "C", 'https://i.imgur.com/KCdTIUq.png', 0, 0, 0),
            ("Zarbon", "C", 'https://static.wikia.nocookie.net/dragonball/images/a/a0/Z%C3%A2bon_premi%C3%A8re_apparition.png/revision/latest?cb=20121014150058&path-prefix=fr', 0, 0, 0),
            ("Dodoria", "C", 'https://static.wikia.nocookie.net/dragonball/images/b/b0/Vlcap-2013-11-24-15h27m41s142.jpg/revision/latest?cb=20131124143313&path-prefix=fr', 0, 0, 0), #toreview
            ("Ginyu", "C", 'https://static.wikia.nocookie.net/dragonball/images/8/89/CapitaineGinyu.png/revision/latest?cb=20130718091929&path-prefix=fr', 0, 0, 0),
            ("Goten", "C", 'https://static.wikia.nocookie.net/dragonball/images/f/fc/GotenSaiyamanSaga02.png/revision/latest?cb=20130406215436&path-prefix=fr', 0, 0, 0),
            ("Babidi", "C", 'https://static.wikia.nocookie.net/dragonball/images/8/89/Vlcap-2013-11-24-17h05m47s123.jpg/revision/latest?cb=20131124160636&path-prefix=fr', 0, 0, 0),
            # Personnages D
            
            ("Chiaotzu", "D", 'https://static.wikia.nocookie.net/dragonball/images/7/70/381px-Chiaotzu23WMAT.png/revision/latest?cb=20130717190215&path-prefix=fr', 0, 0, 0),
            ("Raditz", "D", 'https://static.wikia.nocookie.net/dragonball/images/f/fa/Raditz_with_tail.jpg/revision/latest/scale-to-width-down/1000?cb=20130224144129&path-prefix=fr', 0, 0, 0),
            ("Nappa", "D", 'https://static.wikia.nocookie.net/dragonball/images/a/a0/Nappa2.jpg/revision/latest?cb=20121011190756&path-prefix=fr', 0, 0, 0),
            ("Saibaman", "D", 'https://static.wikia.nocookie.net/dragonball/images/9/99/SaiabamenInfoBox-1-.jpg/revision/latest?cb=20141016164645&path-prefix=fr', 0, 0, 0),
            # Personnages E
            ("Yamcha", "E", 'https://criticalhits.com.br/wp-content/uploads/2023/01/Yamcha-Scars-in-Dragon-Ball-910x455.jpg', 0, 0, 0),
            ("Oolong", "E", 'https://i.imgur.com/K00wC2U.png', 0, 0, 0),
            ("Karin", "E", 'https://static.wikia.nocookie.net/dragonball/images/f/fe/KorinBuuSagaNV.png/revision/latest?cb=20100513171706', 0, 0, 0),
            ("Dende", "E", 'https://static.wikia.nocookie.net/dragonball/images/4/45/Dende.png/revision/latest?cb=20150705191047&path-prefix=fr', 0, 0, 0),
            # Personnages F
            ("Mr. Satan", "F", 'https://static.wikia.nocookie.net/dragonball/images/d/d1/Mr_Satan_Artwork.png/revision/latest?cb=20170904190549&path-prefix=fr', 0, 0, 0),
            ("Yajirobe", "F", "https://i.imgur.com/7yk8rDr.png", 0, 0, 0),
            ("Pilaf", "F", 'https://static.wikia.nocookie.net/dragonball/images/b/b1/Pilaf_render_by_luishatakeuchiha-d69lqwy.png/revision/latest?cb=20170813173722&path-prefix=fr', 0, 0, 0),
            ("Plume", "F", 'https://static.wikia.nocookie.net/dragonball/images/c/c0/Pu_erh_vs_Oolong.png/revision/latest?cb=20150803173741&path-prefix=fr', 0, 0, 0),
            ("Chichi", "F", 'https://static.wikia.nocookie.net/dragonball/images/6/67/Chichi_et_Gok%C3%BB.jpg/revision/latest?cb=20221224154029&path-prefix=fr', 0, 0, 0),
            ("Bulma", "F", 'https://i.imgur.com/IlZlAEM.png', 0, 0, 0),
            ("Gyumao", "F", 'https://static.wikia.nocookie.net/dragonball/images/c/c2/300px-Ox-KingPresentsEp05-1-.png/revision/latest?cb=20150707150216&path-prefix=fr', 0, 0, 0),
            ("Dr. Brief", "F", 'https://static.wikia.nocookie.net/dragonball/images/8/87/Vlcap-2015-05-23-12h32m25s768.png/revision/latest?cb=20150523110821&path-prefix=fr', 0, 0, 0),

            # """ PERSONNAGE NARUTO"""
            # Personnages X
            ("Naruto", "X", "https://i.imgur.com/n8cS6mP.gif", 0, 0, 0),
            ("Sasuke", "X", "https://i.imgur.com/PYEEX2h.gif", 0, 0, 0),
            ("Kaguya", "X", "https://i.imgur.com/P3M8HQH.gif", 0, 0, 0),
            ("Madara", "X", "https://i.imgur.com/c0NF2KN.gif", 0, 0, 0),
            ("Rikudo", "X", "https://i.imgur.com/bn7KwyD.gif", 0, 0, 0),
            ("Indra", "X", "'https://i.imgur.com/dlXLwgN.gif'", 0, 0, 0),
            ("Ashura", "X", "https://i.imgur.com/aRMeDPa.gif", 0, 0, 0),
            ("Obito", "X", "https://i.imgur.com/A6roLXk.gif", 0, 0, 0),
            # Personnages SS
            ("Hashirama", "SS", 'https://media1.tenor.com/m/sd97xiiyvtkAAAAC/hashirama-jutsu-naruto.gif', 0, 0, 0),
            ("Tobirama", "SS", 'https://media1.tenor.com/m/4CQxkScISFkAAAAC/tobirama-senju-tobirama.gif', 0, 0, 0),
            ("Toneri", "SS", 'https://media1.tenor.com/m/3iys2Q_ijIsAAAAC/chakra-tenseigan-tenseigan.gif', 0, 0, 0),
            ("Pain", "SS", "https://s12.gifyu.com/images/SZkqx.gif", 0, 0, 0),
            ("Itachi", "SS", 'https://media1.tenor.com/m/9T4QZFujmdcAAAAd/itachi-itachi-uchiha.gif', 0, 0, 0),
            ("Minato", "SS", 'https://media1.tenor.com/m/RvlB8akbQKMAAAAC/minenexos33.gif', 0, 0, 0), # TOREVIEW
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

            # """ PERSONNAGE ONE PIECE"""

            # Personnages X
            ("Kaido", "X", "https://i.imgur.com/BMDbkl8.gif", 0, 0, 0),
            ("Luffy", "X", "https://i.imgur.com/EmzijMq.gif", 0, 0, 0), # TOREVIEW
            ("Big Mom", "X", "https://i.imgur.com/tPjCbUc.gif", 0, 0, 0),
            ("Barbe Noire", "X", "https://i.pinimg.com/originals/08/74/d1/0874d121307b3cc5c123cbea31146127.gif", 0, 0, 0),
            ("Barbe Blanche", "X", "https://i.imgur.com/BdnDfQj.gif", 0, 0, 0),
            ("Shanks", "X", "https://i.imgur.com/IwGDEdb.gif", 0, 0, 0),
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
            ("Cobra", "C", "https://lh6.googleusercontent.com/Jnz9DOxO_5Cw_kDPNjLOw1xDHP2LnY5RlPSwGSG9nO5DZ1vsYtGjeFmSOYHDxq2T3xY5uYH3OUPk6KldqzfBK6c0TLfiUmRa-bVivtaNqg8uRpiDHy8LTSBnRCJDLv8nZEh2i6rs1XU4XtdMBYpy1uI", 0, 0, 0),
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

            # """ PERSONNAGE BLEACH"""

            # Personnages X
            ("Yhwach", "X", "https://i.pinimg.com/originals/61/64/7c/61647c2b43c3aece4d2f4e0f51fd98f8.gif", 0, 0, 0), # TOREVIEW
            ("Ichigo Final", "X", image_temporaire, 0, 0, 0),
            ("Aizen", "X", 'https://i.imgur.com/8xq9dtV.png', 0, 0, 0),
            ("Yamamoto", "X", 'https://i.imgur.com/EGYHcBd.gif', 0, 0, 0),
            ("Kenpachi", "X", "https://i.imgur.com/DCS6I2N.gif", 0, 0, 0),
            ("Ichibe", "X", 'image_temporaire', 0, 0, 0), #TO DO

            # Personnages SS
            ("Jugram", "SS", "https://64.media.tumblr.com/68c0c258665d8e6aa675f50a0190d1b4/e45f851320545784-81/s540x810/f7fb36d19986346588d36c429b2139390f9512b9.gifv", 0, 0, 0),
            ("Uryu", "SS", "https://64.media.tumblr.com/6c3767dab4c696f88d5cd5e311c7d55b/95d88f6156d0ed70-ef/s640x960/8e6f5edeb0fb9be1f2a1ad9b0ff25880bdac660f.gif", 0, 0, 0),
            ("Kyoraku", "SS", "https://i.imgur.com/7DGfP2z.gif", 0, 0, 0),
            ("Byakuya", "SS", "https://i0.wp.com/giffiles.alphacoders.com/134/13477.gif?fit=960%2C960&ssl=1", 0, 0, 0),
            ("Toshiro", "SS", "https://i.imgur.com/R9S0Qa4.gif", 0, 0, 0),
            ("Urahara", "SS", "https://i.gifer.com/53FX.gif", 0, 0, 0),
            ("Yoruichi", "SS", "https://i.gifer.com/3flV.gif", 0, 0, 0),
            ("Unohana", "SS", "https://static.wikia.nocookie.net/bleach/images/2/29/Unohana-1000ans.gif/revision/latest/scale-to-width-down/640?cb=20230821211554&path-prefix=fr", 0, 0, 0),
            ("Ulquiorra", "SS", "https://i.imgur.com/OaYNXCg.gif", 0, 0, 0),
            ("Gin", "SS", "https://i.imgur.com/kveTtpS.gif", 0, 0, 0),
            ("Stark", "SS", "https://64.media.tumblr.com/d098d4d0dcc9411718b795db7cd09ee1/33ae4a4514128801-1c/s500x750/83239f37db8b0611e5b6db959e157c71ff876915.gif", 0, 0, 0),
            ("Renji", "SS", "https://i.pinimg.com/originals/a9/bc/7e/a9bc7e81b852d5487a6136c71fe6fb37.gif", 0, 0, 0), #TOREVIEW
            ("Senjumaru", "SS", "https://64.media.tumblr.com/03802a81c9691aa4d222ebffb95725b1/f8e12cf39120d6fa-8d/s640x960/f1a4333133480be0b08c54e60cc83921023833e7.gif", 0, 0, 0),

            # Personnages S
            ("Mayuri", "S", "https://gifs.eco.br/wp-content/uploads/2022/07/gifs-do-mayuri-kurotsuchi-1.gif", 0, 0, 0),
            ("Sajin", "S", "https://64.media.tumblr.com/9feeb9306aaa5209099b7dfe883e90c0/tumblr_naoc4a1gdh1sv0f5ao1_500.gif", 0, 0, 0),
            ("Isshin", "S", "https://64.media.tumblr.com/f482a92079273624a2ba3594d7e60710/9ffabbab708a4da9-22/s640x960/d0bd1f5d4e745cf6f3dfa7546bbeea55fbaf3f83.gif", 0, 0, 0),
            ("Rukia", "S", "https://i.pinimg.com/originals/27/79/da/2779da8d545e74ef108bbd115df8bc15.gif", 0, 0, 0),
            ("Shinji", "S", 'https://i.imgur.com/xeM1NLz.png', 0, 0, 0), #TOREVIEW
            ("Soi Fon", "S", 'https://i.imgur.com/EVH34qM.png', 0, 0, 0),
            ("Tosen", "S", 'https://i.imgur.com/4GA76X1.png', 0, 0, 0),
            ("Baraggan", "S", 'https://i.imgur.com/k89CHqN.png', 0, 0, 0),
            ("Grimmjow", "S", 'https://i.imgur.com/nj464jc.png', 0, 0, 0),

            # Personnages A

            ("Ukitake", "A", 'https://i.imgur.com/djpHY0S.png', 0, 0, 0), #TOREVIEW
            ("Nnoitra", "A", 'https://i.imgur.com/z5SAM9h.png', 0, 0, 0),
            ("Shuhei", "A", 'https://i.imgur.com/rkQNMQX.png', 0, 0, 0),
            ("Ryuken", "A", 'https://i.imgur.com/turdL6j.png', 0, 0, 0),
            ("Orihime", "A", 'https://i.imgur.com/xGhy8ky.png', 0, 0, 0),
            ("Ginjo", "A", 'https://i.imgur.com/xLPLs5Q.png', 0, 0, 0),
            
            
            # Personnages B

            ("Kira", "B", 'https://i.imgur.com/H5EQmb0.png', 0, 0, 0),
            ("Ikkaku", "B", 'https://i.imgur.com/wWd1Z4z.png', 0, 0, 0),
            ("Kensei", "B", 'https://i.imgur.com/fHD5IZV.png', 0, 0, 0),
            ("Chad", "B", 'image_temporaire', 0, 0, 0),
            ("Yumichika", "B", 'image_temporaire', 0, 0, 0),

            # Personnages C
            ("Ganju", "C", 'https://i.imgur.com/4HYU47B.png', 0, 0, 0),
            ("Marechiyo", "C", 'https://i.imgur.com/QdU2qIp.png', 0, 0, 0),
            ("Love", "C", 'https://i.imgur.com/LJzVWIY.png', 0, 0, 0),

            # Personnages D
            ("Tessai", "D", 'https://i.imgur.com/VwYCDSH.png', 0, 0, 0),
            ("Hanataro", "D", 'https://i.imgur.com/MPaOL4G.png', 0, 0, 0),
            ("Yachiru", "D", 'https://i.imgur.com/CbYKjNb.png', 0, 0, 0),

            # Personnages E
            ("Jinta", "E", 'https://i.imgur.com/pAuQhV7.png', 0, 0, 0),
            ("Ururu", "E", 'https://i.imgur.com/DoiSB83.png', 0, 0, 0),
            ("Keigo", "E", 'https://i.imgur.com/D8dqhs2.png', 0, 0, 0),

            # Personnages F
            ("Kon", "F", 'https://i.imgur.com/t1az2SQ.png', 0, 0, 0),
            ("Karin Kurosaki", "F", 'https://i.imgur.com/Spca2oo.png', 0, 0, 0),
            ("Yuzu", "F", 'https://i.imgur.com/plnofeu.png', 0, 0, 0),
            ("Tatsuki", "F", 'https://i.imgur.com/mSvWp2O.png', 0, 0, 0),
            ("Mizuiro", "F", 'https://i.imgur.com/b4sfzoT.png', 0, 0, 0),
            # """ PERSONNAGE MY HERO ACADEMIA"""
            # Personnages X
            ("All Might", "X", "https://qph.cf2.quoracdn.net/main-qimg-7d4d4918652a643f9b6801606035fe66", 0, 0, 0),
            ("Shigaraki", "X", "https://www.icegif.com/wp-content/uploads/2022/01/icegif-830.gif", 0, 0, 0),
            ("All For One", "X", "https://www.serieously.com/app/uploads/2023/04/tumblr_ouxiale3pz1v1hotuo2_640.gif", 0, 0, 0),
            ("Star And Stripe", "X", "https://64.media.tumblr.com/e7fe132058464fcc7b6e45489836aa12/799bb7ae5d0c1a2d-0b/s640x960/5245e55efb31adf90e196ca6a92b9b64df808ced.gif", 0, 0, 0),
            # Personnages SS
            ("Izuku Midoriya", "SS", "https://i.pinimg.com/originals/49/41/43/4941430a113739775b3fafbe8d1a81b2.gif", 0, 0, 0),
            ("Endeavor", "SS", "https://i.pinimg.com/originals/49/56/12/495612a35e36440b1607270e8bf1ca3e.gif", 0, 0, 0),
            ("Overhaul", "SS", "https://64.media.tumblr.com/17d512a46dd582dd24e0bb36b48dbdcd/d50adf26237562cb-51/s540x810/df6c2dfb27f13cf0538979584d97630140a34283.gif", 0, 0, 0),
            ("Beast Jeanist", "SS", "https://64.media.tumblr.com/521598d908ab9b8d7cb38b09b77b0d9c/tumblr_osxxvly6ms1wqyomso1_540.gif", 0, 0, 0),
            ("Nana Shimura", "SS", "https://i.imgur.com/ct2j0jN.gif", 0, 0, 0),
            ("Dabi", "SS", "https://static.animecorner.me/2022/12/my-hero-academia-season-6-episode-11-1.jpg", 0, 0, 0),
            ("Mirio", "SS", "https://64.media.tumblr.com/bc3415aed521b623970871cf1c332d25/tumblr_pftup2rGRy1ru8plxo1_540.gif", 0, 0, 0),
            ("Re Destro", "SS", "https://i.redd.it/t3m1gtvs9awb1.gif", 0, 0, 0),
            # Personnages S
            ("Hawks", "S", "https://i.pinimg.com/originals/8d/19/c4/8d19c45317f7e38e372ddeba342cf165.gif", 0, 0, 0),
            ("Twice", "S", "https://i.imgur.com/aTXRvNJ.gif", 0, 0, 0),
            ("Shoto", "S", "https://i.redd.it/quy3b0pf16d31.gif", 0, 0, 0),
            ("Bakugo", "S", "https://img.wattpad.com/dc246422070809bd086ac97693bc04a560634155/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4d46367848686d62785448726a773d3d2d313133373837333639312e3136616165316163303134653732633536363335323739353730312e676966", 0, 0, 0),
            ("Eraserhead", "S", "https://i.pinimg.com/originals/e2/58/6b/e2586b5f78e89ecc597293e35a03faad.gif", 0, 0, 0),
            ("Tamaki", "S", "https://i.pinimg.com/originals/ac/a9/02/aca902c662ebf2c39cea2732f352effe.gif", 0, 0, 0),
            ("Stain", "S", "https://78.media.tumblr.com/6960a5a0b1f0f0f665c7f6bfd88f10d5/tumblr_otunqgSVmE1vb2040o2_500.gif", 0, 0, 0),
            ("Fumikage", "S", "https://img.wattpad.com/4283ecbd858dfc3890407125bb15c01719a5b32b/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f455856757964466f4c51314b70673d3d2d313132312e313666643666616233633339363064653137333733353434393032382e676966", 0, 0, 0),
            ("Mirko", "S", "https://i.pinimg.com/originals/d7/fd/6d/d7fd6d2551098794e172a13355a80291.gif", 0, 0, 0),
            ("Lady Nagant", "S", "https://i.pinimg.com/originals/39/59/1c/39591c97f9e6b9a5f47a2b7f0ab7d963.gif", 0, 0, 0),
            # Personnages A
            ("Tenya", "A", "https://static.wikia.nocookie.net/heros/images/f/f6/Tenya_Infobox.gif/revision/latest?cb=20200324130143&path-prefix=fr", 0, 0, 0),
            ("Mt Lady", "A", "https://i.pinimg.com/originals/c5/e7/d0/c5e7d0827bceace163672dd309c33574.gif", 0, 0, 0),
            ("Nighteye", "A", "https://64.media.tumblr.com/efc6870d8848e1ce03cb34c40af6e711/d88e8f356b2e4ba8-39/s540x810/3a7c1a045ed596a30576ff47cfe310f1f9685fe3.gif", 0, 0, 0),
            ("Ryuku", "A", "https://64.media.tumblr.com/2dfb44a3544b3d118168b28fd79e83f4/25d5e489df925e26-49/s540x810/26df1ec3c8eb8d25abb27668924c495ff685e879.gif", 0, 0, 0),
            ("Gran Torino", "A", "https://i.pinimg.com/originals/f4/6d/46/f46d46e7d08b90465475211d87304cdf.gif", 0, 0, 0),
            # Personnages B
            ("Ochaco", "B", image_temporaire, 0, 0, 0),
            ("Midnight", "B", image_temporaire, 0, 0, 0),
            ("Denki", "B", image_temporaire, 0, 0, 0),
            ("Crimson Riot", "B", image_temporaire, 0, 0, 0),
            ("Nezu", "B", image_temporaire, 0, 0, 0),
            ("Momo Yaoyorozu", "B", image_temporaire, 0, 0, 0),
            ("Gang Orca", "B", image_temporaire, 0, 0, 0),
            # Personnages C
            ("Shindo", "C", image_temporaire, 0, 0, 0),
            ("Rock Lock", "C", image_temporaire, 0, 0, 0),
            ("Vlad King", "C", image_temporaire, 0, 0, 0),
            ("Testutetsu", "C", image_temporaire, 0, 0, 0),
            ("Snipe", "C", image_temporaire, 0, 0, 0),
            
            # Personnages D
            ("Spinner", "D", image_temporaire, 0, 0, 0),
            ("Shihai", "D", image_temporaire, 0, 0, 0),
            ("Nomu", "D", image_temporaire, 0, 0, 0),
            # Personnages E
            ("Mineta", "E", image_temporaire, 0, 0, 0),
            ("Shoji", "E", image_temporaire, 0, 0, 0),
            # Personnages F
            ("Eri", "F", image_temporaire, 0, 0, 0),
            ("Kenji", "F", image_temporaire, 0, 0, 0),
            ("Sansa", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE HUNTER X HUNTER"""
            # Personnages X
            ("Meruem", "X", "https://i.imgur.com/c2CR7Hs.gif", 0, 0, 0),
            ("Gon Freecss", "X", "https://64.media.tumblr.com/704dfb6cff638b74862be478cd16f0ee/tumblr_p20mqwIbSZ1w0ii2ho1_1280.gifv", 0, 0, 0),
            ("Netero", "X", image_temporaire, 0, 0, 0),
            ("Ging", "X", "https://i.imgur.com/VOtkd0O.gif", 0, 0, 0),
            # Personnages SS
            ("Kuroro", "SS", 'https://i.imgur.com/eWUEITZ.png', 0, 0, 0),
            ("Hisoka", "SS", 'https://i.imgur.com/l69c0NZ.png', 0, 0, 0),
            ("Killua", "SS", 'https://i.imgur.com/2sLrUqa.png', 0, 0, 0),
            ("Zeno", "SS", "https://i.imgur.com/inIqhEg.gif", 0, 0, 0),
            ("Silva", "SS", "https://i.imgur.com/K8TUsWM.png", 0, 0, 0),
            ("Illumi", "SS", 'https://i.imgur.com/tFOQgXs.gif', 0, 0, 0),
            ("Neferopito", "SS", "https://i.imgur.com/5PkF2QA.gif", 0, 0, 0),
            ("Yupi", "SS", "https://i.imgur.com/tWZDibP.png", 0, 0, 0),
            ("Aruka", "SS", "https://i.imgur.com/DHIbvOx.gif", 0, 0, 0),
            # Personnages S
            ("Kurapika", "S", 'https://i.imgur.com/ltImMBx.png', 0, 0, 0),
            ("Morel", "S", 'https://i.imgur.com/1J0JLeS.png', 0, 0, 0),
            ("Kaito", "S", "https://i.imgur.com/RehnXP7.gif", 0, 0, 0),
            ("Feitan", "S", "https://i.imgur.com/X3AVK76.gif", 0, 0, 0),
            ("Uvogin", "S", 'https://i.imgur.com/iqzrrW8.png', 0, 0, 0),
            ("Phinks", "S", "https://i.imgur.com/k5BLUMw.png", 0, 0, 0),
            ("Knuckle", "S", 'https://i.imgur.com/sMDxcKR.png', 0, 0, 0), #TOREVIEW
            ("Pufu", "S", "https://i.imgur.com/CfoSEeD.gif", 0, 0, 0),
            ("Nabunaga", "S", 'https://i.imgur.com/1UMIlo3.png', 0, 0, 0),
            # Personnages A
            ("Machi", "A", "https://i.imgur.com/HCAKZfB.gif", 0, 0, 0),
            ("Shoot", "A", 'https://i.imgur.com/tU2Fwq6.png', 0, 0, 0),
            ("Genthru", "A", 'https://i.imgur.com/WtnOU7k.png', 0, 0, 0),
            ("Sharnak", "A", 'https://i.imgur.com/EwSJxbs.png', 0, 0, 0),
            ("Biscuit", "A", 'https://i.imgur.com/3WUyIRV.png', 0, 0, 0),
            ("Razor", "A", 'https://i.imgur.com/0quOdEi.png', 0, 0, 0), #TOREVIEW
            ("Pariston", "A", 'https://i.imgur.com/71ouSTW.png', 0, 0, 0),
            # Personnages B
            ("Pakunoda", "B", "https://i.imgur.com/IxWVTzo.gif", 0, 0, 0),
            ("Shizuku", "B", "https://i.imgur.com/IbkxhGl.png", 0, 0, 0),
            ("Franklin", "B", "https://i.imgur.com/xoln4Ly.gif", 0, 0, 0),
            ("Cheetu", "B", "https://i.imgur.com/ZqFKcDD.png", 0, 0, 0),
            ("Korutopi", "B", "https://i.imgur.com/QwL2k3G.png", 0, 0, 0),
            ("Leorio", "B", 'https://i.imgur.com/NBFxlLS.gif', 0, 0, 0),
            ("Kalluto", "B", "https://i.imgur.com/vCDM9hC.png", 0, 0, 0),
            # Personnages C
            ("Zushi", "C", "https://i.imgur.com/zFDjx8z.png", 0, 0, 0),
            ("Wing", "C", 'https://i.imgur.com/h8Btyhj.png', 0, 0, 0),
            ("Ponzu", "C", 'https://i.imgur.com/f4vOKAP.png', 0, 0, 0),
            ("Pokkle", "C", "https://i.imgur.com/7A9UCci.png", 0, 0, 0),
            # Personnages D
            ("Kikyo", "D", "https://i.imgur.com/dR5KneW.png", 0, 0, 0),
            # Personnages E
            ("Tompa", "E", "https://i.imgur.com/ms2R2ki.png", 0, 0, 0),
            ("Neon", "E", 'https://i.imgur.com/Rz5HGeZ.png', 0, 0, 0),
            # Personnages F
            ("Komugi", "F", 'https://i.imgur.com/4VchruE.png', 0, 0, 0),
            ("Mito", "F", 'https://i.imgur.com/Yy7iG5d.png', 0, 0, 0),

            # """ PERSONNAGE AVATAR"""
            # Personnages X
            ("Aang", "X", image_temporaire, 0, 0, 0),
            ("Ozai", "X", image_temporaire, 0, 0, 0),
            ("Kyoshi", "X", image_temporaire, 0, 0, 0),
            ("Roku", "X", image_temporaire, 0, 0, 0),
            ("Iroh", "X", image_temporaire, 0, 0, 0),

            # Personnages SS
            ("Katara", "SS", image_temporaire, 0, 0, 0),
            ("Zuko", "SS", image_temporaire, 0, 0, 0),
            ("Toph", "SS", image_temporaire, 0, 0, 0),
            ("Azula", "SS", image_temporaire, 0, 0, 0),

            # Personnages S
            ("Amiral Zhao", "S", image_temporaire, 0, 0, 0),
            ("Hama", "S", image_temporaire, 0, 0, 0),

            # Personnages A
            ("Sokka", "A", image_temporaire, 0, 0, 0),
            ("Suki", "A", image_temporaire, 0, 0, 0),
            ("Ty Lee", "A", image_temporaire, 0, 0, 0),
            ("Mai", "A", image_temporaire, 0, 0, 0),

            # Personnages B
            ("Jet", "B", image_temporaire, 0, 0, 0),
            ("Haru", "B", image_temporaire, 0, 0, 0),
            ("June", "B", image_temporaire, 0, 0, 0),

            # Personnages C
            
            # Personnages D
            ("Demi-Portion", "D", image_temporaire, 0, 0, 0),
            ("La Flèche", "D", image_temporaire, 0, 0, 0),
            
            # Personnages E
            ("Le Duc", "E", image_temporaire, 0, 0, 0),

            # Personnages F
            ("Meng", "F", image_temporaire, 0, 0, 0),
            ("Pesticide", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE JUJUTSU KAISEN"""
            # Personnages X
            ("Sukuna", "X", "https://i.imgur.com/7l6cBTL.gif", 0, 0, 0),
            ("Gojo", "X", "https://www.gifcen.com/wp-content/uploads/2022/04/gojo-gif-9.gif", 0, 0, 0),
            ("Kenjaku", "X", "https://steamuserimages-a.akamaihd.net/ugc/2278324186548756253/24401D0DEA0E6D00A35B208CEF250966F3C920D0/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true", 0, 0, 0),

            # Personnages SS
            ("Yuta", "SS", "https://64.media.tumblr.com/88eea7db2e1aeff7957867a11eb579dc/8b0c83155df8b2d5-a9/s540x810/d4fd780899e1f38e3b97fcae86bdb41453691535.gifv", 0, 0, 0),
            ("Mahoraga", "SS", "https://www.breakflip.com/uploads/65573b2ad99c7-makora-ou-mahoraga-jujutsu-kaisen.jpg", 0, 0, 0),
            ("Toji", "SS", 'https://i.imgur.com/W479ima.png', 0, 0, 0),
            ("Aoi Todo", "SS", 'https://i.imgur.com/SpLV3Qv.png', 0, 0, 0),
            ("Geto", "SS", 'https://64.media.tumblr.com/19e09d940c695b8d9e47af07ae8826b9/f07192eb66cf933d-73/s640x960/82552430b812572b330eb6c89879b73594ef7474.gif', 0, 0, 0),
            ("Choso", "SS", 'https://i.pinimg.com/originals/65/2f/25/652f253995b84d6156dc4865be48837b.gif', 0, 0, 0),
            ("Mahito", "SS", 'https://i.imgur.com/nx6CAkr.png', 0, 0, 0),
            ("Jogo", "SS", 'https://64.media.tumblr.com/6fda876b0fee0316b1b2808e0b26e8cd/8cdd4038836dcaca-2c/s1280x1920/44fa45b447f79aaa38a691210c1231f041c87bf9.gifv', 0, 0, 0),
            ("Kinji Hakari", "SS", 'https://i.imgur.com/OSTYTVF.png', 0, 0, 0),
            ("Yuki Tsukumo", "SS", 'https://i.imgur.com/WlIBwGu.png', 0, 0, 0),
            ("Hanami","SS","https://i.pinimg.com/originals/e7/17/c6/e717c677e76c4e0df9a22ec53418367f.gif", 0, 0, 0),
            ("Dagon", "SS", 'https://64.media.tumblr.com/97ffcdfbd6a9ea8cffef764d86fe5b11/f98a9cffd59221b8-ab/s640x960/a29d32f3a037b09966e361ebbb26d56a4aafa464.gif', 0, 0, 0),

            # Personnages S
            ("Megumi", "S", "https://i.imgur.com/ZrNNA55.gif", 0, 0, 0),
            ("Maki", "S", 'https://i.imgur.com/zGKPJI9.png', 0, 0, 0),
            ("Nanami", "S", 'https://i.imgur.com/phtWBmN.png', 0, 0, 0),
            ("Higuruma", "S", 'https://media1.tenor.com/m/vt4qMArBGP4AAAAC/hiromi-higuruma-higuruma-hiromi.gif', 0, 0, 0),
            ("Naobito", "S", 'https://i.imgur.com/FTRAhNn.png', 0, 0, 0),
            ("Miguel", "S", 'https://i.imgur.com/a8zQRsZ.png', 0, 0, 0), #TOREVIEW
            ("Mei mei", "S", 'https://i.imgur.com/KoWiulR.png', 0, 0, 0),
            ("Naoya", "S", 'https://i.imgur.com/LiKy4we.png', 0, 0, 0),
            
            
            #Personnages A
            ("Inumaki", "A", 'https://i.imgur.com/OkbjhWZ.png', 0, 0, 0), #VIDEO
            ("Kamo", "A", 'https://i.imgur.com/8N9AYpE.png', 0, 0, 0),
            ("Mechamaru", "A", 'https://i.imgur.com/HIQY96Q.png', 0, 0, 0), #VIDEO

            # Personnages B
            ("Panda", "B", 'https://i0.wp.com/quotetheanime.com/wp-content/uploads/2021/09/p1.jpg', 0, 0, 0),
            ("Nobara", "B", "https://static.wikia.nocookie.net/jujutsu-kaisen/images/1/1c/Nobara_Kugisaki_EP3.png/revision/latest?cb=20210119101146&path-prefix=fr", 0, 0, 0),
            ("Yuji Itadori", "B", "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/11/itadori-yuji.jpg", 0, 0, 0),
            ("Kusakabe", "B", 'https://i.imgur.com/6rujX3t.png', 0, 0, 0),
            ("Takuma Ino", "B", 'https://i.imgur.com/W3diIlg.png', 0, 0, 0),
            ("Yaga", "B", 'https://i.imgur.com/R8Rq12y.png', 0, 0, 0),
            ("Gakuganji", "B", 'https://i.imgur.com/uAnAEms.png', 0, 0, 0),
            

            # Personnages C
            ("Junpei", "C", 'https://i.imgur.com/7sVsWn3.png', 0, 0, 0),
            ("Momo", "C", "https://i.imgur.com/q0viuTx.png", 0, 0, 0),
            ("Utahime", "C", 'https://i.imgur.com/IPp6E9q.png', 0, 0, 0),
            ("Juzo", "C", "https://i.imgur.com/lkcQCxs.png", 0, 0, 0),
            ("Haruta Shigemo", "C", "https://staticg.sportskeeda.com/editor/2023/10/9dbce-16972933761276-1920.jpg", 0, 0, 0),
            

            # Personnages D
            ("Miwa", "D", "https://i.imgur.com/M0twNwm.png", 0, 0, 0),

            # Personnages E
            ("Ijichi", "E", "https://i.imgur.com/6EKKkX3.jpeg", 0, 0, 0),
            ("Kechizu", "E", "https://i.imgur.com/fwEMmNC.png", 0, 0, 0),


            # Personnages F
            ("Riko Amanai", "F", "https://static1.dualshockersimages.com/wordpress/wp-content/uploads/2023/07/whi-is-riko-amanai-important-in-jujutsu-kaisen.jpg", 0, 0, 0),
            ("Tsumiki Fushiguro", "F", "https://thicc-af.mywaifulist.moe/waifus/tsumiki-fushiguro-sorcery-fight/pEdHC9PdLGod6CXdmkwM0Bj7zjHftDfqhXy9ba3B.jpg?class=thumbnail", 0, 0, 0),

            # """ PERSONNAGE MOB PSYCHO """

            # Personnages X
            ("Mob", "X", image_temporaire , 0, 0, 0),

            # Personnages SS
            ("Teruki", "SS", image_temporaire , 0, 0, 0),
            ("Sho Suzuki", "SS", image_temporaire , 0, 0, 0),

            # Personnages A
            ("Ritsu", "A", image_temporaire , 0, 0, 0),

            # Personnages B
            ("Dimple", "B", image_temporaire , 0, 0, 0),
            ("Tome Kurata", "B", image_temporaire , 0, 0, 0),

            # Personnages C
            ("Tenga Onigawara", "C", image_temporaire , 0, 0, 0),

            # Personnages D
            ("Musashi Goda", "D", image_temporaire , 0, 0, 0),
            # Personnages F
            ("Reigen", "F", image_temporaire , 0, 0, 0),
            ("Ichi Mezato", "F", image_temporaire , 0, 0, 0),
            ("Momozo Takenaka", "F", image_temporaire , 0, 0, 0),

            # """ PERSONNAGE JOJO'S BIZARRE ADVENTURE """

            # Personnages X
            ("Giorno", "X", 'https://steamuserimages-a.akamaihd.net/ugc/828010176607459436/A1557FBD095E14949A16EF073E6B166C1A218917/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false', 0, 0, 0),
            ("Pucci", "X", 'https://i.imgur.com/RTdkTrH.png', 0, 0, 0),
            ("Funny Valentine", "X", image_temporaire, 0, 0, 0),
            ("Gyro", "X", image_temporaire, 0, 0, 0),
            ("Johnny", "X", image_temporaire, 0, 0, 0),
            
            # Personnages SS

            ("Kars", "SS", 'https://i.imgur.com/4xhIuVK.png', 0, 0, 0),
            ("Diavolo", "SS", 'https://i.imgur.com/90RxqGR.png', 0, 0, 0),
            ("Jotaro", "SS", 'https://i.imgur.com/XzBAKKf.gif', 0, 0, 0),
            ("Diego", "SS", image_temporaire, 0, 0, 0),
            ("Dio", "SS", 'https://i.imgur.com/xngzKOg.png', 0, 0, 0),
            ("Kira", "SS", 'https://i.imgur.com/ZQPBO3Q.png', 0, 0, 0),

            # Personnages S
            ("Josuke", "S", 'https://i.imgur.com/AcnhlnJ.png', 0, 0, 0), #TOREVIEW
            ("Fugo", "S", 'https://i.imgur.com/gBcvGNj.png', 0, 0, 0), #TOREVIEW
            ("Vanilla Ice", "S", image_temporaire, 0, 0, 0),
            ("Jolyne", "S", 'https://i.imgur.com/T2yg742.png', 0, 0, 0),
            ("Weather Report", "S", image_temporaire, 0, 0, 0),
            
            # Personnages A
            ("Anasui", "A", image_temporaire, 0, 0, 0),
            ("Bucciarati", "A", 'https://i.imgur.com/zaBAVFx.png', 0, 0, 0),
            ("Risotto", "A", 'https://i.imgur.com/hQxmpqR.png', 0, 0, 0),
            ("Rohan", "A", 'https://i.imgur.com/UJgfmGg.png', 0, 0, 0),
            ("Kakyoin", "A", 'https://i.imgur.com/ZsxN3PG.png', 0, 0, 0),
            ("Polnareff", "A", 'https://i.imgur.com/eZjHHa9.png', 0, 0, 0),
            ("Okuyasu", "A", 'https://i.imgur.com/BiveNFJ.png', 0, 0, 0),
            ("Ghiaccio", "A", 'https://i.imgur.com/LNoxXyi.png', 0, 0, 0),
            ("Prosciutto", "A", 'https://i.imgur.com/CsSR05A.png', 0, 0, 0),
            ("Mohamed Abdul", "A", image_temporaire, 0, 0, 0),
            ("Illuso", "A", image_temporaire, 0, 0, 0),
            ("Cioccolata", "A", 'https://i.imgur.com/XAu2MDR.png', 0, 0, 0),

            
            # Personnages B
            ("Koichi", "B", 'https://i.imgur.com/HZ9vn1d.png', 0, 0, 0),
            ("Emporio", "B", 'https://i.imgur.com/KBZCTy6.png', 0, 0, 0),
            ("Akira", "B", 'https://i.imgur.com/xn6pX9Z.png', 0, 0, 0), #TOREVIEW
            ("Narancia", "B", 'https://i.imgur.com/ndZcfok.png', 0, 0, 0),
            ("Yukako", "B", 'https://i.imgur.com/JZKQ2KS.png', 0, 0, 0),
            ("Miyamoto", "B", 'https://i.imgur.com/lZLlEhu.png', 0, 0, 0),
            ("Wamuu", "B", 'https://i.imgur.com/2Jc0FTu.png', 0, 0, 0),
            ("Esidisi", "B", 'https://i.imgur.com/mdsI4Ir.png', 0, 0, 0),
            ("Pesci", "B", 'https://i.imgur.com/RiqetYG.png', 0, 0, 0),
            ("Melone ", "B", 'https://i.imgur.com/EMitGnp.png', 0, 0, 0),
            ("Squalo", "B", 'https://i.imgur.com/1DP3U16.png', 0, 0, 0),
            ("Joseph", "B", 'https://i.imgur.com/YiGGszt.png', 0, 0, 0),
            ("Mista", "B", 'https://i.imgur.com/ab9sgfg.png', 0, 0, 0),


            # Personnages C
            ("Caesar", "C", 'https://i.imgur.com/3nzbH8Y.png', 0, 0, 0),
            ("Lisa Lisa", "C", 'https://i.pinimg.com/736x/8e/81/74/8e817463c33ba3039e93c253f00bbacb.jpg', 0, 0, 0),
            ("Shigechi", "C", 'https://i.imgur.com/6JKniYe.png', 0, 0, 0),
            ("Mikitaka", "C", 'https://i.imgur.com/mMs5O78.png', 0, 0, 0),
            ("Iggy", "C", 'https://i.imgur.com/HTb59id.png', 0, 0, 0),
            ("Formaggio", "C", 'https://i.imgur.com/WCQtqwq.png', 0, 0, 0),
            ("Stroheim", "C", 'https://i.imgur.com/OvyOZy3.png', 0, 0, 0),
            ("Foo Fighters", "C", 'https://i.imgur.com/ZlCOCPn.png', 0, 0, 0),
            ("Trish", "C", 'https://i.imgur.com/I4nMHqt.png', 0, 0, 0),
            ("Hermes", "C", 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/09/Ermes-Costello-and-her-Stand-Smack.jpg', 0, 0, 0),

            # Personnages D
            ("Abbacchio", "D", 'https://i.imgur.com/5FahNJl.png', 0, 0, 0),
            ("Daniel Darby", "D", 'https://i.pinimg.com/736x/5e/8c/15/5e8c15dbafc2d01662eab438bcd32e9d.jpg', 0, 0, 0), #TOREVIEW
            ("Jonathan", "D", 'https://i.imgur.com/dqGKC1P.png', 0, 0, 0),

            # Personnages E
            ("Straizo", "E", 'https://i.imgur.com/D4muQp5.png', 0, 0, 0),
            ("Will Zeppeli", "E", 'https://i.imgur.com/SVm9I2K.png', 0, 0, 0),
            ("Boingo", "E", 'https://jojocomparisons.github.io/images/SC27/bd-02270-1090px.jpg', 0, 0, 0),
            ("Oingo","E", 'https://64.media.tumblr.com/d8034453f7e998104a35e83911d067ec/3cfe647de86da704-47/s1280x1920/d18891e4e45818d59b3d87e7d60ae16e97a09ccb.jpg', 0, 0, 0),

            # Personnages F
            ("Tonio", "F", 'https://i.imgur.com/PIXbcZb.png', 0, 0, 0),
            ("Luca", "F", 'https://i.imgur.com/3HamVjM.png', 0, 0, 0),
            ("Anne", "F", 'https://i.pinimg.com/736x/6e/26/d7/6e26d7d149f72e207059a9c53623bbfc.jpg', 0, 0, 0),
            ("Speedwagon", "F", 'https://i.imgur.com/Q4pR4ws.png', 0, 0, 0),
            ("Poco", "F", 'https://i.imgur.com/qeYo0He.png', 0, 0, 0),
            ("Mario Zucchero", "F", 'https://i.imgur.com/dBDj9C5.png', 0, 0, 0),
            ("Dario Brando", "F", "https://cdn.anisearch.fr/images/character/screen/31/31596/full/479344.webp", 0, 0, 0),

            # """ PERSONNAGE ONE PUNCH MAN ""

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

            # """ PERSONNAGE DEMON SLAYER """
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
            ("Rengoku", "A", image_temporaire, 0, 0, 0),
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
            ("Fille Araignée", "C", image_temporaire, 0, 0, 0),
            ("Mère Araignée", "C", image_temporaire, 0, 0, 0),
            ("Susamaru", "C", image_temporaire, 0, 0, 0),
            ("Jigoro", "C", image_temporaire, 0, 0, 0),


            # Personnages D
            ("Tanjuro", "D", image_temporaire, 0, 0, 0),

            # Personnages E
            ("Shinzu", "E", image_temporaire, 0, 0, 0),
            ("Murata", "E", image_temporaire, 0, 0, 0),
            ("Kyogai", "E", image_temporaire, 0, 0, 0),
            ("Kanamue", "E", image_temporaire, 0, 0, 0),
            ("Kagaya", "E", image_temporaire, 0, 0, 0),


            # Personnages F
            ("Kiriya", "F", image_temporaire, 0, 0, 0),
            ("Nichika", "F", image_temporaire, 0, 0, 0),
            ("Chachamaru", "F", image_temporaire, 0, 0, 0),
            ("Aoi Kanzaki", "F", image_temporaire, 0, 0, 0),
            ("Sumi", "F", image_temporaire, 0, 0, 0),
            ("Kiyo", "F", image_temporaire, 0, 0, 0),
            ("Naho", "F", image_temporaire, 0, 0, 0),
            ("Goto", "F", image_temporaire, 0, 0, 0),
            ("Kaburamaru", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE FMAB """
            # Personnages X
            ("Père", "X", image_temporaire, 0, 0, 0),
            # Personnages SS
            ("Hohenheim", "SS", image_temporaire, 0, 0, 0),
            ("King Bradley", "SS", image_temporaire, 0, 0, 0),
            # Personnages S
            ("Edward", "S", image_temporaire, 0, 0, 0),
            ("Izumi Curtis", "S", image_temporaire, 0, 0, 0),
            ("Alphonse", "S", image_temporaire, 0, 0, 0),
            ("Roy Mustang", "S", image_temporaire, 0, 0, 0),
            ("Scar", "S", image_temporaire, 0, 0, 0),
            ("Kimbley", "S", image_temporaire, 0, 0, 0),
            ("Selim", "S", image_temporaire, 0, 0, 0),
            # Personnages A
            ("Ling Yao", "A", image_temporaire, 0, 0, 0),
            ("Envy", "A", image_temporaire, 0, 0, 0),
            ("Sloth", "A", image_temporaire, 0, 0, 0),
            ("Glutonny", "A", image_temporaire, 0, 0, 0),
            ("Lust", "A", image_temporaire, 0, 0, 0),
            ("Olivia Mira Armstrong", "A", image_temporaire, 0, 0, 0),
            ("Alex Louis Armstrong", "A", image_temporaire, 0, 0, 0),
            # Personnages B
            ("Maes Hughes", "B", image_temporaire, 0, 0, 0),
            ("Mei Chang", "B", image_temporaire, 0, 0, 0),
            ("Riza Hawkeye", "B", image_temporaire, 0, 0, 0),
            ("Lan Fan", "B", image_temporaire, 0, 0, 0),
            ("Fu", "B", image_temporaire, 0, 0, 0),
            ("Alex Louis Armstrong", "B", image_temporaire, 0, 0, 0),
            # Personnages C
            ("Heinkel", "C", image_temporaire, 0, 0, 0),
            ("Marcoh", "C", image_temporaire, 0, 0, 0),
            ("Darius", "C", image_temporaire, 0, 0, 0),
            # Personnages D
            ("Maria Ross", "E", image_temporaire, 0, 0, 0),
            ("Miles", "E", image_temporaire, 0, 0, 0),
            ("Falman", "E", image_temporaire, 0, 0, 0),
            # Personnages E
            ("Paninya", "E", image_temporaire, 0, 0, 0),
            ("Havoc", "E", image_temporaire, 0, 0, 0),
            ("Heymans", "E", image_temporaire, 0, 0, 0),
            ("Fuery", "E", image_temporaire, 0, 0, 0),
            # Personnages F
            ("Yoki", "F", image_temporaire, 0, 0, 0),
            ("Nina Tucker", "F", image_temporaire, 0, 0, 0),
            ("Trisha", "F", image_temporaire, 0, 0, 0),
            ("Xiao Mei", "F", image_temporaire, 0, 0, 0),
            ("Winry", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGES SNK """
            # Personnages X
            ("Eren", "X", image_temporaire, 0, 0, 0),
            # Personnages SS
            ("Armin", "SS", image_temporaire, 0, 0, 0),
            ("Bertholdt", "SS", image_temporaire, 0, 0, 0),
            ("Livai", "SS", image_temporaire, 0, 0, 0),
            ("Reiner", "SS", image_temporaire, 0, 0, 0),
            # Personnages S
            ("Annie", "S", image_temporaire, 0, 0, 0),
            ("Sieg", "S", image_temporaire, 0, 0, 0),
            ("Mikasa", "S", image_temporaire, 0, 0, 0),
            ("Pieck", "S", image_temporaire, 0, 0, 0),
            # Personnages A
            ("Xaver", "A", image_temporaire, 0, 0, 0),
            ("Grisha", "A", image_temporaire, 0, 0, 0),
            ("Ymir", "A", image_temporaire, 0, 0, 0),
            ("Falco", "A", image_temporaire, 0, 0, 0),
            ("Kenny", "A", image_temporaire, 0, 0, 0),
            ("Porco", "A", image_temporaire, 0, 0, 0),
            ("Erwin", "A", image_temporaire, 0, 0, 0),
            # Personnages B
            ("Mike", "B", "https://d2y6mqrpjbqoe6.cloudfront.net/image/upload/f_auto,q_auto/cdn1/movies-pictures/AOTS02_01.jpg", 0, 0, 0),
            ("Frieda", "B", "https://pbs.twimg.com/media/FKbV-8FaUAAn4zI?format=jpg&name=large", 0, 0, 0),
            ("Jean", "B", "https://static.wikia.nocookie.net/shingekinokyojin/images/2/22/Jean_pas_content.jpg/revision/latest/scale-to-width-down/1280?cb=20140629165849&path-prefix=fr", 0, 0, 0),
            ("Hange", "B", "https://45secondes.fr/wp-content/uploads/2023/02/1677204130_Hange-de-Shingeki-no-Kyojin-faits-curieux-que-vous.jpg", 0, 0, 0),
            ("Rhodes", "B", "https://static.wikia.nocookie.net/shingekinokyojin/images/7/78/Rhodes_Reiss_Anime_-_850_%282%29.png/revision/latest/scale-to-width/360?cb=20180826231656&path-prefix=fr", 0, 0, 0),
            # Personnages C
            ("Yelena", "C", "https://static1.srcdn.com/wordpress/wp-content/uploads/2022/03/Yelena-in-Attack-on-Titan-and-Cart.jpg", 0, 0, 0),
            ("Hannes", "C", "https://boutique-manga.fr/wp-content/uploads/2021/03/Hannes.jpg", 0, 0, 0),
            ("Historia", "C", "https://i.pinimg.com/originals/f4/27/13/f427139c83b864284bad663309cc3d7d.jpg", 0, 0, 0),
            ("Floch", "C", "https://static.wikia.nocookie.net/shingekinokyojin/images/a/a5/Floch_acknowledges_his_survival.png/revision/latest?cb=20220215031016", 0, 0, 0),
            ("Pixis", "C", "https://i.pinimg.com/originals/38/4a/bc/384abcf51d55f6272bf047b93e84cfba.jpg", 0, 0, 0),
            ("Sacha", "C", "https://static.wikia.nocookie.net/shingekinokyojin/images/b/bc/Sasha_mange_une_patate_lors_du_rite_d%27initiation.jpg/revision/latest/scale-to-width-down/1334?cb=20230701145817&path-prefix=fr", 0, 0, 0),
            ("Kony", "C", "https://i.pinimg.com/736x/14/e9/0e/14e90e06e144f3279d3cd8b692450bb8.jpg", 0, 0, 0),
            ("Théo Magath", "C", "https://cdn.anisearch.fr/images/character/screen/105/105263/full/541797.webp", 0, 0, 0),
            # Personnages D
            ("Gabi", "D", "https://static.wikia.nocookie.net/shingekinokyojin/images/5/53/Gaby_demandant_%C3%A0_Falco_pourquoi_il_l%27a_suivit_%C3%A0_Paradis.png/revision/latest/scale-to-width-down/1240?cb=20221015230732&path-prefix=fr", 0, 0, 0),
            ("Udo", "D", "https://wisecineman.ru/kartinki/heroes/attack-on-titan/1034.webp", 0, 0, 0),
            ("Zofia", "D", "https://sm.ign.com/t/ign_latam/screenshot/default/zofia-shingeki_bxe5.1280.jpg", 0, 0, 0),
            ("Willy", "D", "https://i0.wp.com/codigoespagueti.com/wp-content/uploads/2020/12/willy-tybur-shingeki-no-kyojin.jpg", 0, 0, 0),
            # Personnages E
            ("Onyankopon", "E", "https://static.wikia.nocookie.net/shingekinokyojin/images/5/52/Onyankopon_protests_the_treatment_of_the_volunteers.png/revision/latest?cb=20210301055248", 0, 0, 0),
            ("Nicolo", "E", "https://static.wikia.nocookie.net/shingekinokyojin/images/1/1e/%C3%89pisode_68.png/revision/latest/scale-to-width-down/1280?cb=20210215025407&path-prefix=fr", 0, 0, 0),
            # Personnages F
]

all_synergies = [
    (1, "Akatsuki", "ATK", 0.15,"L'akkatsuki est une organisation criminelle de ninjas déserteurs.", image_temporaire, "#FF0000"),
    (2, "Saiyan", "ATK", 0.15, "Les Saiyans sont connus pour leur force et leur capacité à se transformer en Super Saiyan.", image_temporaire, "#FFA500"),
    (3, "Hollow", "ATK", 0.15, "Les Hollows sont des âmes corrompues qui ont perdu leur coeur et leur raison.", image_temporaire, "#0000FF"),
    (4, "Mugiwara", "ATK", 0.15, "Les Mugiwara sont l'équipage de Luffy, un pirate qui cherche le One Piece.", image_temporaire, "#800080"),
    (5, "Uchiha", "ATK", 0.15, "Le clan Uchiha est connu pour ses capacités de combat et son Sharingan.", image_temporaire, "#FF0000"),
    (6, "Quincy", "ATK", 0.15, "Les Quincy sont des chasseurs de Hollows qui utilisent des arcs pour combattre.", image_temporaire, "#FFA500"),
    (7, "Amiraux", "ATK", 0.15, "Les Amiraux sont les trois plus puissants marins de la Marine.", image_temporaire, "#0000FF"),
    (8, "Espada", "ATK", 0.15, "Les Espadas sont les dix plus puissants Hollows sous les ordres d'Aizen.", image_temporaire, "#800080"),
    (9, "Vongola", "ATK", 0.15, "La famille Vongola est une organisation mafieuse italienne qui utilise des anneaux pour combattre.", image_temporaire, "#FF0000"),
    (10, "Yonko", "ATK", 0.3, "Les Yonkos sont les quatre plus puissants pirates du Nouveau Monde.", image_temporaire, "#FFA500"),
    (11, "Akimichi", "ATK", 0.15, "Le clan Akimichi est connu pour sa technique de transformation en géant.", image_temporaire, "#0000FF"),
    (12, "Vizard", "ATK", 0.15, "Les Vizards sont des Shinigamis qui ont acquis des pouvoirs de Hollows.", image_temporaire, "#800080"),
    (13, "Varia", "ATK", 0.15, "La Varia est un groupe d'assassins de la famille Vongola.", image_temporaire, "#FF0000"),
    (14, "Gotei 13", "ATK", 0.15, "Le Gotei 13 est une organisation de Shinigamis qui protège le monde des âmes.", image_temporaire, "#FFA500"),
    (15, "Kage", "ATK", 0.15, "Les Kages sont les plus puissants ninjas de leur village.", image_temporaire, "#0000FF"),
    (16, "Shichibukai", "ATK", 0.15, "Les Shichibukai sont des pirates qui ont accepté de servir la Marine.", image_temporaire, "#800080"),
    (17, "Sannin", "ATK", 0.50, "Les Sannins sont les trois ninjas légendaires de Konoha.", image_temporaire, "#FF0000"),
    (18, "Révolutionnaires", "ATK", 0.15, "Les Révolutionnaires sont un groupe qui lutte contre le Gouvernement Mondial.", image_temporaire, "#FFA500"),
    (19, "Volonté du D", "ATK", 0.15, "La Volonté du D est une mystérieuse lignée de pirates qui défient le Gouvernement Mondial.", image_temporaire, "#0000FF"),
    (20, "Animal", "ATK", 0.15, "Les Animaux sont des créatures qui possèdent des pouvoirs spéciaux.", image_temporaire, "#800080"),
    (21, "Taka", "ATK", 0.15, "La Taka est un groupe de ninjas qui a été formé par Sasuke Uchiha.", image_temporaire, "#FF0000"),
    (22, "Rinnegan", "ATK", 0.15, "Le Rinnegan est le dōjutsu le plus puissant de l'univers Naruto.", image_temporaire, "#FFA500"),
    (23, "Konoha", "ATK", 0.15, "Konoha est le village caché de la Feuille, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (24, "Suna", "ATK", 0.15, "Suna est le village caché du Sable, l'un des cinq grands villages ninjas.", image_temporaire, "#800080"),
    (25, "Kiri", "ATK", 0.15, "Kiri est le village caché de la Brume, l'un des cinq grands villages ninjas.", image_temporaire, "#FF0000"),
    (26, "Kumo", "ATK", 0.15, "Kumo est le village caché des Nuages, l'un des cinq grands villages ninjas.", image_temporaire, "#FFA500"),
    (27, "Iwa", "ATK", 0.15, "Iwa est le village caché de la Roche, l'un des cinq grands villages ninjas.", image_temporaire, "#0000FF"),
    (28, "Réceptacle", "ATK", 0.15, "Les Réceptacles sont des personnes qui ont un Monstre scellé en eux.", image_temporaire, "#800080"),
    (29, "Maître du Feu", "ATK", 0.15, "Les Maîtres du Feu sont des personnages qui maîtrisent le feu.", image_temporaire, "#FFA500"),
    (30, "Maître de l'Eau", "ATK", 0.15, "Les Maîtres de l'Eau sont des personnages qui maîtrisent l'eau.", image_temporaire, "#0000FF"),
    (31, "Maître de la Terre", "ATK", 0.15, "Les Maîtres de la Terre sont des personnages qui maîtrisent la terre.", image_temporaire, "#800080"),
    (32, "Maître de l'Air", "ATK", 0.15, "Les Maîtres de l'Air sont des personnages qui maîtrisent l'air.", image_temporaire, "#FF0000"),
    (33, "Maître de l'Éclair", "ATK", 0.15, "Les Maîtres de l'Éclair sont des personnages qui maîtrisent l'éclair.", image_temporaire, "#FFA500"),
    (34, "Maître de la Glace", "ATK", 0.15, "Les Maîtres de la Glace sont des personnages qui maîtrisent la glace.", image_temporaire, "#0000FF"),
    (35, "Maître de la Foudre", "ATK", 0.15, "Les Maîtres de la Foudre sont des personnages qui maîtrisent la foudre.", image_temporaire, "#800080"),
    (36, "Maître de la Lave", "ATK", 0.15, "Les Maîtres de la Lave sont des personnages qui maîtrisent la lave.", image_temporaire, "#FF0000"),
    (37, "Maître du Bois", "ATK", 0.15, "Les Maîtres du Bois sont des personnages qui maîtrisent le bois.", image_temporaire, "#FFA500"),
    (38, "Maître du Vent", "ATK", 0.15, "Les Maîtres du Vent sont des personnages qui maîtrisent le vent.", image_temporaire, "#0000FF"),
    (39, "Maître du Sable", "ATK", 0.15, "Les Maîtres du Sable sont des personnages qui maîtrisent le sable.", image_temporaire, "#800080"),
    (40, "Épéiste", "ATK", 0.15, "Les Épéistes sont des combattants qui utilisent une épée pour se battre.", image_temporaire, "#FF0000"),
    (41, "Télékinésiste", "ATK", 0.15, "Les Télékinésistes sont des personnes qui peuvent déplacer des objets par la pensée ou ont des pouvoirs psychiques.", image_temporaire, "#FFA500"),
    (42, "Equipage de Barbe Noire", "ATK", 0.15, "L'équipage de Barbe Noire est un groupe de pirates dirigé par Barbe Noire.", image_temporaire, "#0000FF"),
    (43, "Equipage de Barbe Blanche", "ATK", 0.15, "L'équipage de Barbe Blanche est un groupe de pirates dirigé par Barbe Blanche.", image_temporaire, "#800080"),
    (44, "Uzumaki", "ATK", 0.15, "Le clan Uzumaki est connu pour sa longévité et ses capacités de guérison.", image_temporaire, "#FF0000"),
    (45, "Hyuga", "ATK", 0.15, "Le clan Hyuga est connu pour son Byakugan et ses techniques de combat douces.", image_temporaire, "#FFA500"),
    (46, "Senju", "ATK", 0.15, "Le clan Senju est connu pour son Mokuton et sa capacité à maîtriser les Bijuus.", image_temporaire, "#0000FF"),
    (47, "Otsutsuki", "ATK", 0.15, "Le clan Otsutsuki est une famille de ninjas extraterrestres qui cherchent à absorber des planètes pour obtenir du chakra.", image_temporaire, "#800080"),
    (48, "Insecte", "ATK", 0.15, "Les Insectes sont des créatures qui possèdent des pouvoirs spéciaux.", image_temporaire, "#FF0000"),
    (49, "Garde Royale", "ATK", 0.15, "La Garde Royale est un groupe qui s'assure de la sécurité du roi.", image_temporaire, "#FFA500"),
    (50, "Zeppeli", "ATK", 0.15, "Les Zeppelis sont une famille de maîtres de l'Onde qui combattent les vampires.", image_temporaire, "#0000FF"),
    (52, "Homme du pillar", "ATK", 0.15, "Les Pillars sont des guerriers qui servent les vampires et protègent la pierre rouge de l'Aja.", image_temporaire, "#FF0000"),
    (53, "Maître du Temps", "ATK", 0.15, "Les Maîtres du Temps sont des personnages qui peuvent contrôler le temps.", image_temporaire, "#FFA500"),
    (54, "Maître de l'Explosion", "ATK", 0.15, "Les Maîtres de l'Explosion sont des personnages qui peuvent créer des explosions.", image_temporaire, "#0000FF"),
    (55, "Squadra Esecuzioni", "ATK", 0.15, "La Squadra Esecuzioni est un groupe de tueurs à gages qui travaillent pour la Passione.", image_temporaire, "#0000FF"),
    (56, "Hamon", "ATK", 0.15, "Le Hamon est une technique de combat qui utilise l'énergie du soleil pour attaquer les vampires.", image_temporaire, "#800080"),
    (57, "Passione", "ATK", 0.15, "La Passione est une organisation criminelle italienne qui contrôle le trafic de drogue.", image_temporaire, "#FF0000"),
    (58, "Team Bucciarati", "ATK", 0.15, "La Team Bucciarati est un groupe de gangsters qui travaillent pour la Passione.", image_temporaire, "#FFA500"),
    (59, "JoBros", "ATK", 0.15, "Les JoBros sont les amis et alliés des Joestars qui les aident dans leur combat contre le mal.", image_temporaire, "#0000FF"),
    (60, "Île de Sirop", "ATK", 0.15, "L'Île de Sirop est une île paradisiaque où les habitants vivent en paix et en harmonie.", image_temporaire, "#800080"),
    (61, "Équipage de Shanks", "ATK", 0.15, "L'équipage de Shanks est un groupe de pirates dirigé par Shanks le Roux.", image_temporaire, "#0000FF"),
    (62, "Équipage de Kaido", "ATK", 0.15, "L'équipage de Kaido est un groupe de pirates dirigé par Kaido le Cent bêtes.", image_temporaire, "#800080"),
    (63, "Équipage de Big Mom", "ATK", 0.15, "L'équipage de Big Mom est un groupe de pirates dirigé par Big Mom.", image_temporaire, "#FF0000"),
    (64, "Draconique", "ATK", 0.15, "Les Dragons sont des créatures mythiques qui possèdent des pouvoirs magiques.", image_temporaire, "#FFA500"),
    (65, "Speedster", "ATK", 0.15, "Les Speedsters sont des personnages qui peuvent se déplacer à une vitesse supersonique.", image_temporaire, "#0000FF"),
    (66, "Aveugle", "ATK", 0.4 , "Les Aveugles sont des personnages qui ont perdu la vue mais qui ont développé d'autres sens pour compenser.", image_temporaire, "#800080"),
    (67, "Dojo de Bang", "ATK", 0.15, "Le Dojo de Bang est un lieu d'entraînement où les disciples apprennent les techniques de combat de Bang.", image_temporaire, "#FF0000"),
    (68, "Cyborg", "ATK", 0.15, "Les Cyborgs sont des êtres humains qui ont été améliorés avec des technologies cybernétiques.", image_temporaire, "#FFA500"),
    (69, "JoJo", "ATK", 0.15, "Les JoJos sont les membres de la famille Joestar qui luttent contre les forces du mal.", image_temporaire, "#0000FF"),
    (70, "Fléaux", "ATK", 0.15, "Les Fléaux sont des créatures maléfiques qui apportent la destruction et la mort partout où ils passent.", image_temporaire, "#800080"),
    (71, "École de Tokyo", "ATK", 0.15, "L'École de Tokyo est un établissement scolaire où les élèves apprennent à maîtriser leurs pouvoirs surnaturels.", image_temporaire, "#FF0000"),
    (72, "École de Kyoto", "ATK", 0.15, "L'École de Kyoto est un établissement scolaire rival de l'École de Tokyo.", image_temporaire, "#FFA500"),
    (73, "Zenin", "ATK", 0.15, "Le clan Zenin est une famille de sorciers qui possède des pouvoirs magiques.", image_temporaire, "#0000FF"),
    (74, "Kamo", "ATK", 0.15, "Le clan Kamo est une famille de sorciers qui possède des pouvoirs magiques.", image_temporaire, "#800080"),
    (75, "Fushiguro", "ATK", 0.15, "La lignée Fushiguro est une lignée d'originaire humaine.", image_temporaire, "#FF0000"),
    (76, "Ubuyashiki", "ATK", 0.15, "La famille Ubuyashiki est une famille de démons qui dirige le clan des pourfendeurs de démons.", image_temporaire, "#FFA500"),
    (77, "Hashira", "ATK", 0.15, "Les Hashiras sont les piliers de l'organisation des pourfendeurs de démons.", image_temporaire, "#0000FF"),
    (78, "Pourfendeurs de démons", "ATK", 0.15, "Les Pourfendeurs de démons sont une organisation secrète qui lutte contre les démons.", image_temporaire, "#800080"),
    (79, "Domaine des Papillons", "ATK", 0.15, "Le Domaine des Papillons est un lieu mystérieux où les démons se rassemblent pour se nourrir.", image_temporaire, "#FF0000"),
    (80, "Démons", "ATK", 0.15, "Les Démons sont des créatures maléfiques qui se nourrissent de la chair humaine.", image_temporaire, "#FFA500"),
    (81, "Kamado", "ATK", 0.15, "La famille Kamado est une famille de pourfendeurs de démons qui a été décimée par les démons.", image_temporaire, "#0000FF"),
    (82, "Souffle du Soleil", "ATK", 0.15, "Le Souffle du Soleil est une technique de combat utilisée par les pourfendeurs de démons.", image_temporaire, "#800080"),
    (83, "Souffle de la Foudre", "ATK", 0.15, "Le Souffle de la Foudre est une technique de combat utilisée par les pourfendeurs de démons.", image_temporaire, "#FF0000"),
    (84, "Souffle de l'Eau", "ATK", 0.15, "Le Souffle de l'Eau est une technique de combat utilisée par les pourfendeurs de démons.", image_temporaire, "#FFA500"),
    (85, "Souffle de la Fleur", "ATK", 0.15, "Le Souffle de la Fleur est une technique de combat utilisée par les pourfendeurs de démons.", image_temporaire, "#0000FF"),
    (86, "Lune", "ATK", 0.15, "Les Lunes sont des démons puissants qui servent Muzan.", image_temporaire, "#800080"),
    (87, "Brando", "ATK", 0.15, "Les Brando sont une famille de vampires qui cherchent à dominer le monde.", image_temporaire, "#FF0000"),
    (88, "Maître de la Gravité", "ATK", 0.15, "Les Maîtres de la Gravité sont des personnages qui peuvent contrôler la gravité.", image_temporaire, "#FFA500"),
    (89, "Armstrong", "ATK", 0.15, "La famille Armstrog est une famille illustre et noble qui a servi Amestris pendant des générations.", image_temporaire, "#0000FF"),
    (90, "Homonculus", "ATK", 0.15, "Les Homonculus sont des êtres artificiels créés par le Père pour servir ses desseins.", image_temporaire, "#800080"),
    (91, "Alchimist d'Etat", "ATK", 0.15, "Les Alchimistes d'Etat sont des alchimistes qui servent le gouvernement d'Amestris.", image_temporaire, "#FF0000"),
    (92, "Xing", "ATK", 0.15, "Le pays de Xing est un pays voisin d'Amestris qui pratique l'alchimie de l'est.", image_temporaire, "#FFA500"),
    (93, "Elric", "ATK", 0.15, "La famille Elric est une famille d'alchilmistes (sauf la mère).", image_temporaire, "#0000FF"),
    (94, "Automail", "ATK", 0.15, "L'Automail est une prothèse mécanique qui remplace un membre perdu.", image_temporaire, "#800080"),
    (95, "Ishval", "ATK", 0.15, "Les Ishvals sont un peuple pacifique qui a été décimé par les alchimistes d'Amestris.", image_temporaire, "#FF0000"),
    (96, "Bradley", "ATK", 0.15, "La famille Bradley comporte deux Homonculus et est au pouvoir du pays.", image_temporaire, "#FFA500"),
    (97, "Unité Mustang", "ATK", 0.15, "L'Unité Mustang est une unité de l'armée d'Amestris dirigée par Roy Mustang.", image_temporaire, "#0000FF"),
]

all_link_synergies = {
    97 : ["Roy Mustang", "Havoc", "Riza Hawkeye","Heymans","Fuery","Falman"],
    96 : ["King Bradley","Selim"],
    95 : ["Scar","Frère de Scar","Miles"], # Ishval
    94 : ["Edward","Paninya","Lan Fan"], # Automail
    93 : ["Hohenheim","Edward","Alphonse","Trisha"], # Elric
    92 : ["Ling Yao","Mei Chang","Lan Fan","Fu","Xiao Mei"], # Xing
    91 : ["Edward Elric","Alphonse Elric","Roy Mustang","Kimbley","Olivia Mira Armstrong","Alex Louis Armstrong"], # Alchimist d'Etat
    90 : ["Lust","Glutonny","Envy","Sloth","Greed","Wrath","Pride","Father"], # Homonculus
    89 : ["Mira","Alex"],
    88 : ["Kenjaku","Okuyasu","Yuki","Fujitora","Pain"], # Maître de la Gravité
    87 : ["Dio","Diego","Giorno","Dario Brando"], # Brando
    86 : ["Kyogai","Kanamue","Rui","Mukago","Wakuraba","Hairo","Rokuro","Enmu","Daki","Gyutaro","Kaigaku","Gyokko","Akaza","Doma","Kokushibo"], # Lune
    85 : ["Kanae","Kanao"], # Souffle de la Fleur
    84 : ["Sakonji","Giyu","Sabito","Makomo","Tanjiro","Murata"], # Souffle de l'Eau
    83 : ["Zenitsu","Kaigaku","Jigoro"], # Souffle de la Foudre
    82 : ["Tanjiro", "Yoriichi","Sumiyoshi","Tanjuro"], #Kamado
    81 : ["Tanjiro","Nezuko","Kanao","Sumiyoshi","Tanjuro"], #Kamado
    80 : ["Muzan","Nezuko","Tamayo","Yushiro","Susamaru","Yahaba","Fille Araignée","Mère Araignée","Shinzu"], # Démons
    79 : ["Aoi Kanzaki","Sumi","Kiyo","Naho","Goto"], # Domaine des Papillons
    78 : ["Kanao","Tanjiro","Zenitsu","Inosuke","Nezuko","Genya","Murata","Ozaki","Yoriichi"], # Pourfendeurs de démons
    77 : ["Giyu","Mitsuri","Obanai","Sanemi","Gyomei","Muichiro","Shinobu Kocho","Rengoku","Kanae Kocho","Uzui"], # Hashira
    76 : ["Kagaya","Amane","Hinaki","Nichika","Kiriya","Kanata"], # Ubuyashiki
    75 : ["Toji","Megumi","Tsumiki Fushiguro"], # Fushiguro
    74 : ["Noritoshi","Kenjaku"], # Kamo
    73 : ["Toji", "Naobito","Mai","Maki","Megumi"], # Zenin
    72 : ["Gakukanji","Utahime","Arata Nitta","Mai","Miwa","Mechamaru","Aoi Todo","Noritoshi","Momo","Akari Nitta"], # École de Kyoto
    71 : ["Yaga","Ijichi","Gojo","Kusakabe","Sheko Ieri","Akari Nitta","Megumi","Yuji","Nobara","Maki","Toge Inumaki","Panda","Yuta","Hakari","Nanami","Geto","Yu Haibara"], # École de Tokyo
    70 : ["Sukuna", "Mahito", "Jogo", "Dagon", "Hanami", "Choso","Eso","Kechizu"], # Fléaux
    69 : ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne", "Johnny"], # JoJo
    68 : ["Genos","Cyborgorilla","C-17","C-18","C-16"], # Cyborg
    67 : ["Grimasse","Garou","Charanko","Bang"], # Dojo de Bang
    66 : ["Fujitora","Toph","Tosen","Komugi","Shaka","N'Doul","Yomi"], # Aveugle 
    65 : ["Minato", "Tobirama", "Yoruichi", "Gran Torino","Sonic"], # Speedster TODO
    64 : ["Kaido","Ryukyu","Toshiro","Acnologia","Igneel","Shenron","Porungan"], # Draconique TODO
    63 : ["Big Mom", "Katakuri"], # Équipage de Big Mom
    62 : ["Kaido", "King", "Queen", "Jack"], # Équipage de Kaido
    61 : ["Shanks","Yasopp","Lucky Roo","Benn Beckman","Rockstar"], # Équipage de Shanks
    60 : ["Ussop","Kaya","Kuro","Merry","Yassop"],
    59 : ["Speedwagon","Caesar","Kakyoin","Polnareff","Mohamed Abdul","Stroheim","Okuyasu","Rohan","Koichi","Gyro","Bucciarati","Yasuho","Foo Fighter"], # JoBros
    1 : ["Itachi", "Kisame", "Deidara", "Sasori", "Hidan", "Kakuzu", "Pain", "Konan", "Zetsu", "Tobi"], # Akatsuki
    2 : ["Goku", "Vegeta", "Gohan", "Trunks", "Goten","Gotenks", "Bardock", "Raditz", "Nappa", "Broly", "Cabba","Caulifla","Kale","Kefla"], # Saiyan
    4 : ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"], # Mugiwara
    5 : ["Itachi", "Sasuke", "Madara", "Obito", "Shisui", "Fugaku", "Indra", "Izuna", "Sarada"], # Uchiha
    7 : ["Akainu", "Aokiji", "Kizaru", "Sengoku", "Garp", "Fujitora", "Ryokugyu", "Kong"], # Amiraux
    10 : ["Barbe Blanche", "Kaido", "Big Mom", "Shanks", "Barbe Noire","Luffy","Mihawk","Crocodile"], # Yonko
    14 : ["Yamamoto", "Unohana", "Byakuya", "Kenpachi", "Ukitake", "Kyoraku", "Sajin", "Mayuri", "Toshiro", "Rukia"], # Gotei 13
    15 : ["Hashirama", "Tobirama", "Hiruzen", "Minato", "Tsunade", "Kakashi", "Naruto","Mei Terumi", "Onoki", "Gaara"], # Kage
    16 : ["Crocodile", "Doflamingo", "Mihawk", "Kuma", "Boa Hancock", "Jinbe", "Buggy", "Law", "Barbe Noire"], # Shichibukai,
    17 : ["Jiraya","Orochimaru","Tsunade"], # Sannin
    18 : ["Dragon", "Ivankov", "Kuma", "Sabo", "Koala", "Hack", "Inazuma", "Belo Betty", "Lindbergh", "Karasu"], # Révolutionnaires
    19 : ["Luffy", "Garp", "Roger", "Ace", "Dragon", "Sabo", "Law", "Barbe Noire","Portgas D. Rouge","Vivi","Cobra"], # Volonté du D
    20 : ["Kiba", "Akamaru", "Karin", "Rob Lucci", "Chopper", "Kaido", "Marco", "Jabra", "Kaku","Cyborgorilla","Crablante", "Tonton","Pakkun", "Laboon","Sajin","Chachamaru","Kaburamaru"], # Animal TODO
    21 : ["Sasuke", "Suigetsu", "Karin (naruto)", "Jugo"], # Taka
    22 : ["Nagato", "Pain", "Obito", "Madara", "Sasuke", "Momoshiki", "Kaguya"], # Rinnegan
    23 : ["Naruto", "Sakura", "Sasuke", "Kakashi", "Shikamaru", "Choji", "Ino", "Hinata", "Kiba", "Shino", "Neji", "Rock Lee", "Tenten"], # Konoha TODO
    24 : ["Gaara", "Temari", "Kankuro", "Rasa", "Yashamaru"], # Suna TODO
    25 : ["Kisame", "Zabuza", "Haku", "Mei Terumi", "Ao", "Chojuro", "Yagura", "Mangetsu", "Suigetsu"], # Kiri TODO
    26 : ["Darui", "C", "Omoi", "Killer Bee", "Samui", "Atsui", "Akatsuchi", "Onoki"], # Kumo TODO
    27 : ["Akatsuchi", "Kurotsuchi", "Onoki", "Deidara", "Kurotsuchi", "Akatsuchi", "Onoki", "Deidara"], # Iwa TODO
    28 : ["Naruto", "Bee", "Yugito", "Yagura", "Roshi", "Han", "Utakata", "Fu", "Ginkaku", "Kinkaku", "Itadori"], # Réceptacle TODO
    29 : ["Aang","Roku","Kyoshi", "Ace","Shoto", "Sabo", "Iroh", "Zuko", "Ozai", "Azula", "Itachi", "Madara", "Sasuke","Kakuzu","Jogo","Mohamed Abdul"],# Maître du Feu TODO
    30 : ["Aang","Roku","Kyoshi", "Katara", "Korra", "Unalaq", "Ming-Hua", "Ghazan", "Kya", "Tenzin", "Suigetsu", "Mei Terumi","Kakuzu","Tobirama","Kisame","Haku"], # Maître de l'Eau TODO
    31 : ["Aang","Roku","Kyoshi", "Toph", "Bumi", "Kuvira", "Suyin", "Lin", "Yamato (ANBU)", "Hashirama","Kakuzu"], # Maître de la Terre TODO
    32 : ["Aang","Roku","Kyoshi", "Tenzin", "Gyatso", "Zaheer", "Jinora", "Ikki", "Meelo", "Kai"], # Maître de l'Air TODO
    33 : ["Zuko", "Iroh", "Azula", "Ozai", "Kakashi","Sasuke", "Killer Bee", "Darui", "A", "Kakuzu", "Ener"], # Maître de l'Éclair TODO
    34 : ["Shoto","Aokiji", "Gray", "Toshiro", "Rukia"], # Maître de la Glace TODO

    36 : ["Akainu", "Jogo","Mei Terumi","Kurotsuchi"], # Maître de la Lave TODO

    40 : ["Zoro", "Mihawk","Toji","Maki", "Killer Bee", "Kuina", "Tashigi", "Kaku", "Sasuke","Kisame", "Suigetsu", "Zabuza","Shanks", "Gol D. Roger", "Stain", "Ichigo", "Aizen", "Kenpachi", "Unohana", "Gin", "Erza", "Dabi", "Darui", "Guts", "Yamamoto", "Trunks", "Tapion", "Gohan", "Rukia", "Byakuya", "Oden", "Law", "Brook","Cavendish","Fujitora","Shiryu", "Yhwach","Haruta Shigemo"], # Épéiste
    41 : ["Mob", "Ritsu", "Teruki", "Sho Suzuki", "Tome Kurata", "Dimple","Tatsumaki"], # Télékinésiste
    42 : ["Barbe Noire", "Shiryu", "Lafitte", "Van Augur", "Doc Q", "Avalo Pizarro", "Catarina Devon", "Vasco Shot"], # Equipage de Barbe Noire
    43 : ["Barbe Blanche", "Marco", "Joz", "Vista", "Blamenco", "Rakuyo", "Namur", "Ace", "Haruta", "Fossa", "Izo", "Atmos"], # Equipage de Barbe Blanche
    44 : ["Naruto", "Kushina", "Nagato", "Karin", "Mito", "Boruto", "Himawari"], # Uzumaki
    45 : ["Neji", "Hinata", "Hiashi", "Hanabi","Himawari", "Boruto"], # Hyuga
    46 : ["Hashirama", "Tobirama", "Tsunade", "Nawaki"], # Senju
    47 : ["Kaguya", "Rikudo", "Hamura", "Urashiki", "Momoshiki", "Kinshiki", "Toneri", "Isshiki"], # Ototsuki
    48 : ["Shino", "Meruem", "Pufu", "Youpi", "Neferopito"], # Insecte
    49 : ["Meruem", "Neferopito", "Youpi", "Pufu"], # Garde Royale
    # 50 Zeppeli
    50 : ["Will Zeppeli", "Caesar", "Gyro","Mario"], # Zeppeli

    53 : ["Dio","Diavolo", "Jotaro","Nighteye"], # Maître du Temps
    54 : ["Kira Yoshikage", "Bakugo"], # Maître de l'Explosion
    55 : ["Ghiaccio", "Prosciutto", "Pesci", "Melone", "Illuso", "Formaggio", "Gelato", "Sorbet", "Cioccolata", "Secco"], # Squadra Esecuzioni
    56 : ["Jonathan", "William Zeppeli", "Joseph", "Caesar", "Lisa Lisa", "Poco"], # Hamon
    57 : ["Bucciarati","Giorno", "Mista", "Narancia","Fugo", "Abbacchio","Diavolo","Fugo","Luca","Polpo"], # Passione
    58 : ["Bucciarati","Giorno", "Mista", "Narancia","Fugo", "Abbacchio"], # Team Bucciarati
    
}

"""import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(maison)
plt.figure(figsize=(10, 10))
for edge in maison:
    G.add_edges_from(([(edge, to) for to in maison[edge]]))
nx.draw(G, with_labels=True, node_size=5000, node_color='skyblue', font_size=15, font_weight='bold')
plt.show()
"""