image_temporaire = "https://picsum.photos/900/500"
all_characters_templates = [
            # """ PERSONNAGE DRAGON BALL"""
            # Personnages X
            ("Vegeta Ultra Ego", "X", "https://i.imgur.com/sSjFzsz.jpeg", 0, 0, 0),
            ("Goku Ultra Instinct", "X", "https://i.imgur.com/k2T0SKd.gif", 0, 0, 0),
            ("Zeno", "X", "https://i.imgur.com/W579wtw.gif", 0, 0, 0),
            # Personnages SS
            ("Broly", "SS", "https://i.imgur.com/flUOeQK.gif", 0, 0, 0), #TODO
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
            # Personnages D
            ("Chiaotzu", "D", 'https://static.wikia.nocookie.net/dragonball/images/7/70/381px-Chiaotzu23WMAT.png/revision/latest?cb=20130717190215&path-prefix=fr', 0, 0, 0),
            ("Raditz", "D", 'https://static.wikia.nocookie.net/dragonball/images/f/fa/Raditz_with_tail.jpg/revision/latest/scale-to-width-down/1000?cb=20130224144129&path-prefix=fr', 0, 0, 0),
            ("Nappa", "D", 'https://static.wikia.nocookie.net/dragonball/images/a/a0/Nappa2.jpg/revision/latest?cb=20121011190756&path-prefix=fr', 0, 0, 0),
            ("Saibaman", "D", 'https://static.wikia.nocookie.net/dragonball/images/9/99/SaiabamenInfoBox-1-.jpg/revision/latest?cb=20141016164645&path-prefix=fr', 0, 0, 0),
            # Personnages E
            ("Yamcha", "E", 'https://www.superherodb.com/pictures2/portraits/10/050/1211.jpg?v=1645322906', 0, 0, 0),
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
            ("Shisui", "SS", 'https://media1.tenor.com/m/_To3NtVgZv0AAAAC/shisui-uchiha-shisui.gif', 0, 0, 0),
            ("Minato", "SS", 'https://media1.tenor.com/m/RvlB8akbQKMAAAAC/minenexos33.gif', 0, 0, 0), # TOREVIEW
            ("Kabuto", "SS", 'https://media1.tenor.com/m/-nxrWjUdXRYAAAAC/anime-kabuto-yakushi.gif', 0, 0, 0),
            ("Guy (8 portes)", "SS", 'https://media1.tenor.com/m/xa87Jinyrc0AAAAC/naruto-shippuden-might-guy.gif', 0, 0, 0),
            ("Momoshiki", "SS", 'https://media1.tenor.com/m/74cmic57CwoAAAAC/momoshiki.gif', 0, 0, 0),
            # Personnages S
            ("Hidan", "S", 'https://i.imgur.com/Nz7dGAU.png', 0, 0, 0),
            ("Kakuzu", "S", 'https://i.imgur.com/BKf04A1.gif', 0, 0, 0),
            ("Hiruzen", "S", 'https://media1.tenor.com/m/j6hgBpYSrL4AAAAC/hiruzen-sarutobi.gif', 0, 0, 0),
            ("Orochimaru", "S", 'https://media1.tenor.com/m/5lzbp1JeaGoAAAAd/anime-naruto-shippuden.gif', 0, 0, 0),
            ("Mei Terumi", "S", "https://i.imgur.com/JTaGhQQ.gif", 0, 0, 0),
            ("Onoki", "S", image_temporaire, 0, 0, 0),
            ("Gaara", "S", 'https://i.imgur.com/39HCNme.png', 0, 0, 0),
            ("Tsunade", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808357678472232960/Tsunade.gif', 0, 0, 0),
            ("Kakashi", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808401405283008593/KAKASHI.gif', 0, 0, 0),
            ("Kisame", "S", 'https://i.imgur.com/50KuDl3.gif', 0, 0, 0),
            ("Darui", "S", 'https://i.imgur.com/4agHAoM.gif', 0, 0, 0),
            ("Asuma", "S", 'https://i.imgur.com/lGIqLP3.gif', 0, 0, 0),
            ("Neji", "S", 'https://i.imgur.com/acFMgGN.gif', 0, 0, 0),
            ("Kimimaro", "S", 'https://i.imgur.com/OEKnkD4.png', 0, 0, 0),
            ("Shikamaru", "S", 'https://i.imgur.com/KySPqGV.gif', 0, 0, 0),
            ("Rock Lee", "S", 'https://i.imgur.com/1V4WwG9.png', 0, 0, 0),
            ("Sasori", "S", 'https://i.imgur.com/RlpI6Rd.gif', 0, 0, 0),
            ("Deidara", "S", 'https://i.imgur.com/k83MFjs.gif', 0, 0, 0),
            ("Killer Bee", "S", image_temporaire, 0, 0, 0),
            ("Jiraya", "S", 'https://cdn.discordapp.com/attachments/804401351080542269/808356331022319616/JIRAYA.gif', 0, 0, 0),
            ("Izuna", "S", 'https://i.imgur.com/OxGlzHg.png', 0, 0, 0),
            ("Konan", "S", 'https://i.imgur.com/3mOmZ0v.gif', 0, 0, 0),
            ("Tobi", "S", 'https://64.media.tumblr.com/a6ac04d437e10a8c383c601e9f8421a6/tumblr_n5vm5cCKrX1qk9powo1_500.gif', 0, 0, 0),
            # Personnages A
            ("Neji", "A", "https://imgur.com/acFMgGN", 0, 0, 0),
            ("Yamato (ANBU)", "A", image_temporaire, 0, 0, 0),
            ("Zabuza", "A", image_temporaire, 0, 0, 0),
            ("Kankuro", "A", image_temporaire, 0, 0, 0),
            ("Choji", "A", image_temporaire, 0, 0, 0),
            ("Sai", "A", image_temporaire, 0, 0, 0),
            ("Temari", "A", image_temporaire, 0, 0, 0),
            # Personnages B
            ("Shino", "B", image_temporaire, 0, 0, 0),
            ("Kiba", "B", image_temporaire, 0, 0, 0),
            ("Ino", "B", image_temporaire, 0, 0, 0),
            ("Sakura", "B", image_temporaire, 0, 0, 0),
            ("Hinata", "B", image_temporaire, 0, 0, 0),
            ("Suigetsu", "B", image_temporaire, 0, 0, 0),
            ("Jugo", "B", image_temporaire, 0, 0, 0),
            ("Haku", "B", "https://imgur.com/vqQD56N", 0, 0, 0),
            ("Kurenai", "B", image_temporaire, 0, 0, 0),
            ("Fugaku", "B", image_temporaire, 0, 0, 0),

            # Personnages C
            ("Iruka", "C", "https://i.imgur.com/p0YmijL.png", 0, 0, 0),
            ("Zetsu", "C", image_temporaire, 0, 0, 0),
            ("Shizune", "C", image_temporaire, 0, 0, 0),
            ("Anko", "C", image_temporaire, 0, 0, 0),
            ("Guren", "C", image_temporaire, 0, 0, 0),
            ("Yugao", "C", image_temporaire, 0, 0, 0),
            ("Sarada", "C", image_temporaire, 0, 0, 0),
            ("Tenten", "D", "https://imgur.com/s6MEz46", 0, 0, 0),
            # Personnages D
            ("Ebisu", "D", image_temporaire, 0, 0, 0),
            

            # Personnages E
            ("Tonton", "E", image_temporaire, 0, 0, 0),
            ("Pakkun", "E", image_temporaire, 0, 0, 0),
            ("Gama", "E", image_temporaire, 0, 0, 0),
            ("Konohamaru", "E", image_temporaire, 0, 0, 0),
            ("Karin (naruto)", "E", image_temporaire, 0, 0, 0),

            # Personnages F
            ("Mizuki", "F", image_temporaire, 0, 0, 0),
            ("Inari", "F", image_temporaire, 0, 0, 0),
            ("Gato", "F", image_temporaire, 0, 0, 0),

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
            ("Aokiji", "SS", image_temporaire, 0, 0, 0),
            ("Kizaru", "SS", image_temporaire, 0, 0, 0),
            ("Fujitora", "SS", image_temporaire, 0, 0, 0),
            ("Rayleigh", "SS", image_temporaire, 0, 0, 0),
            ("Kong", "SS", image_temporaire, 0, 0, 0),
            ("Katakuri", "SS", image_temporaire, 0, 0, 0),
            ("Ryokugyu", "SS", image_temporaire, 0, 0, 0),
            ("Garp", "SS", image_temporaire, 0, 0, 0),
            ("Sengoku", "SS", image_temporaire, 0, 0, 0),
            ("Mihawk", "SS", image_temporaire, 0, 0, 0),
            ("Doflamingo", "SS", image_temporaire, 0, 0, 0),
            ("Law", "SS", image_temporaire, 0, 0, 0),
            ("Kid", "SS", image_temporaire, 0, 0, 0),
            ("Zoro", "SS", image_temporaire, 0, 0, 0),
            ("King", "SS", image_temporaire, 0, 0, 0),
            

            # Personnages S
            ("Crocodile", "S", image_temporaire, 0, 0, 0),
            ("Ener", "S", image_temporaire, 0, 0, 0),
            ("Shiryu", "S", image_temporaire, 0, 0, 0),
            ("Smoker", "S", "https://i.imgur.com/3vJPaRx.gif", 0, 0, 0),
            ("Kuma", "S", image_temporaire, 0, 0, 0),
            ("Oden", "S", image_temporaire, 0, 0, 0),
            ("Sabo", "S", "https://i.imgur.com/vjcu8Gg.gif", 0, 0, 0),
            ("Boa Hancock", "S", image_temporaire, 0, 0, 0),
            ("Marco", "S", image_temporaire, 0, 0, 0),
            ("Sanji", "S", image_temporaire, 0, 0, 0),
            ("Yamato", "S", image_temporaire, 0, 0, 0),

            # Personnages A
            ("Ivankov", "A", image_temporaire, 0, 0, 0),
            ("Brook", "A", image_temporaire, 0, 0, 0),
            ("Robin", "A", image_temporaire, 0, 0, 0),
            ("Jinbe", "A", image_temporaire, 0, 0, 0),
            ("Rob Lucci", "A", "https://i.imgur.com/aewCvhP.gif", 0, 0, 0),
            ("Magellan", "A", image_temporaire, 0, 0, 0),
            ("Ace", "A", "https://i.imgur.com/8AGmDrS.gif", 0, 0, 0),
            ("Karasu", "A", image_temporaire, 0, 0, 0),
            
            # Personnages B
            ("Chooper", "B", image_temporaire, 0, 0, 0),
            ("Nami", "B", image_temporaire, 0, 0, 0),
            ("Ussop", "B", "https://i.imgur.com/oJD4qsv.gif", 0, 0, 0),
            ("Hina", "B", image_temporaire, 0, 0, 0),
            ("Buggy", "B", image_temporaire, 0, 0, 0),
            ("Koala", "B", image_temporaire, 0, 0, 0),
            ("Inazuma", "B", image_temporaire, 0, 0, 0),
            ("Belo Betty", "B", image_temporaire, 0, 0, 0),
            ("Franky", "B", image_temporaire, 0, 0, 0),
            

            # Personnages C
            ("Vivi", "C", image_temporaire, 0, 0, 0),
            ("Arlong", "C", image_temporaire, 0, 0, 0),
            ("Don Krieg", "C", image_temporaire, 0, 0, 0),
            ("Tashigi", "C", image_temporaire, 0, 0, 0),
            ("Cobra", "C", image_temporaire, 0, 0, 0),
            ("Hack", "C", image_temporaire, 0, 0, 0),
            ("Chopper", "C", image_temporaire, 0, 0, 0),

            # Personnages D
            ("Koby", "D", image_temporaire, 0, 0, 0),
            ("Helmeppo", "D", image_temporaire, 0, 0, 0),
            ("Dorry", "D", image_temporaire, 0, 0, 0),
            ("Brogy", "D", image_temporaire, 0, 0, 0),
            ("Lindbergh", "D", image_temporaire, 0, 0, 0),
            
            # Personnages E
            ("Hatchan", "E", image_temporaire, 0, 0, 0),
            ("Pell", "E", image_temporaire, 0, 0, 0),
            ("Wapol", "E", image_temporaire, 0, 0, 0),

            # Personnages F
            ("Gaimon", "F", image_temporaire, 0, 0, 0),
            ("Kaya", "F", image_temporaire, 0, 0, 0),
            ("Laboon", "F", image_temporaire, 0, 0, 0),
            ("Portgas D. Rouge", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE BLEACH"""

            # Personnages X
            ("Yhwach", "X", "https://i.pinimg.com/originals/61/64/7c/61647c2b43c3aece4d2f4e0f51fd98f8.gif", 0, 0, 0), # TOREVIEW
            ("Ichigo Final", "X", image_temporaire, 0, 0, 0),
            ("Aizen", "X", image_temporaire, 0, 0, 0),
            ("Yamamoto", "X", 'https://i.imgur.com/EGYHcBd.gif', 0, 0, 0),
            ("Kenpachi", "X", "https://i.imgur.com/DCS6I2N.gif", 0, 0, 0),
            ("Ichibe", "X", image_temporaire, 0, 0, 0),

            # Personnages SS
            ("Jugram", "SS", image_temporaire, 0, 0, 0),
            ("Uryu", "SS", image_temporaire, 0, 0, 0),
            ("Kyoraku", "SS", image_temporaire, 0, 0, 0),
            ("Byakuya", "SS", image_temporaire, 0, 0, 0),
            ("Toshiro", "SS", image_temporaire, 0, 0, 0),
            ("Urahara", "SS", image_temporaire, 0, 0, 0),
            ("Yoruichi", "SS", image_temporaire, 0, 0, 0),
            ("Unohana", "SS", image_temporaire, 0, 0, 0),
            ("Ulquiorra", "SS", image_temporaire, 0, 0, 0),
            ("Gin", "SS", image_temporaire, 0, 0, 0),
            ("Stark", "SS", image_temporaire, 0, 0, 0),
            ("Renji", "SS", image_temporaire, 0, 0, 0),

            # Personnages S
            ("Mayuri", "S", image_temporaire, 0, 0, 0),
            ("Sajin", "S", image_temporaire, 0, 0, 0),
            ("Senjumaru", "S", image_temporaire, 0, 0, 0),
            ("Isshin", "S", image_temporaire, 0, 0, 0),

            ("Rukia", "S", image_temporaire, 0, 0, 0),
            ("Shinji", "S", image_temporaire, 0, 0, 0),
            ("Soi Fon", "S", image_temporaire, 0, 0, 0),
            ("Tosen", "S", image_temporaire, 0, 0, 0),
            ("Baraggan", "S", image_temporaire, 0, 0, 0),
            ("Grimmjow", "S", image_temporaire, 0, 0, 0),

            # Personnages A

            ("Ukitake", "A", image_temporaire, 0, 0, 0),
            ("Nnoitra", "A", image_temporaire, 0, 0, 0),
            ("Shuhei", "A", image_temporaire, 0, 0, 0),
            ("Ryuken", "A", image_temporaire, 0, 0, 0),
            ("Orihime", "A", image_temporaire, 0, 0, 0),
            ("Ginjo", "A", image_temporaire, 0, 0, 0),
            
            
            # Personnages B

            ("Kira", "B", image_temporaire, 0, 0, 0),
            ("Ikkaku", "B", image_temporaire, 0, 0, 0),
            ("Kensei", "B", image_temporaire, 0, 0, 0),
            ("Chad", "B", image_temporaire, 0, 0, 0),
            ("Yumichika", "B", image_temporaire, 0, 0, 0),

            # Personnages C
            ("Ganju", "C", image_temporaire, 0, 0, 0),
            ("Marechiyo", "C", image_temporaire, 0, 0, 0),
            ("Love", "C", image_temporaire, 0, 0, 0),

            # Personnages D
            ("Tessai", "D", image_temporaire, 0, 0, 0),
            ("Hanataro", "D", image_temporaire, 0, 0, 0),
            ("Yachiru", "D", image_temporaire, 0, 0, 0),

            # Personnages E
            ("Jinta", "E", image_temporaire, 0, 0, 0),
            ("Ururu", "E", image_temporaire, 0, 0, 0),
            ("Keigo", "E", image_temporaire, 0, 0, 0),

            # Personnages F
            ("Kon", "F", image_temporaire, 0, 0, 0),
            ("Karin Kurosaki", "F", image_temporaire, 0, 0, 0),
            ("Yuzu", "F", image_temporaire, 0, 0, 0),
            ("Tatsuki", "F", image_temporaire, 0, 0, 0),
            ("Mizuiro", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE MY HERO ACADEMIA"""
            # Personnages X
            ("All Might", "X", image_temporaire, 0, 0, 0),
            ("Endeavor", "X", image_temporaire, 0, 0, 0),
            ("Shigaraki", "X", image_temporaire, 0, 0, 0),
            ("Deku (100%)", "X", image_temporaire, 0, 0, 0),
            ("All For One", "X", image_temporaire, 0, 0, 0),
            ("Star And Stripe", "X", image_temporaire, 0, 0, 0),
            # Personnages SS
            ("Overhaul", "SS", image_temporaire, 0, 0, 0),
            ("Hawks", "SS", image_temporaire, 0, 0, 0),
            ("Beast Jeanist", "SS", image_temporaire, 0, 0, 0),
            ("Dabi", "SS", image_temporaire, 0, 0, 0),
            ("Mirio", "SS", image_temporaire, 0, 0, 0),
            ("Re Destro", "SS", image_temporaire, 0, 0, 0),
            # Personnages S
            ("Twice", "S", image_temporaire, 0, 0, 0),
            ("Shoto", "S", image_temporaire, 0, 0, 0),
            ("Bakugo", "S", image_temporaire, 0, 0, 0),
            ("Eraserhead", "S", image_temporaire, 0, 0, 0),
            ("Tamaki", "S", image_temporaire, 0, 0, 0),
            ("Stain", "S", image_temporaire, 0, 0, 0),
            ("Fumikage", "S", image_temporaire, 0, 0, 0),
            ("Nana Shimura", "S", image_temporaire, 0, 0, 0),
            ("Mirko", "S", image_temporaire, 0, 0, 0),
            ("Lady Nagant", "S", image_temporaire, 0, 0, 0),
            # Personnages A
            ("Tenya", "A", image_temporaire, 0, 0, 0),
            ("Mt Lady", "A", image_temporaire, 0, 0, 0),
            ("Nighteye", "A", image_temporaire, 0, 0, 0),
            ("Sun Eater", "A", image_temporaire, 0, 0, 0),
            ("Ryuku", "A", image_temporaire, 0, 0, 0),
            ("Gran Torino", "A", image_temporaire, 0, 0, 0),
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
            ("Meruem", "X", image_temporaire, 0, 0, 0),
            ("Gon Adulte", "X", image_temporaire, 0, 0, 0),
            ("Netero", "X", image_temporaire, 0, 0, 0),
            ("Ging", "X", image_temporaire, 0, 0, 0),
            # Personnages SS
            ("Kuroro", "SS", image_temporaire, 0, 0, 0),
            ("Hisoka", "SS", image_temporaire, 0, 0, 0),
            ("Killua", "SS", image_temporaire, 0, 0, 0),
            ("Zeno", "SS", image_temporaire, 0, 0, 0),
            ("Silva", "SS", image_temporaire, 0, 0, 0),
            ("Illumi", "SS", image_temporaire, 0, 0, 0),
            ("Neferopito", "SS", image_temporaire, 0, 0, 0),
            ("Yupi", "SS", image_temporaire, 0, 0, 0),
            ("Aruka", "SS", image_temporaire, 0, 0, 0),
            # Personnages S
            ("Kurapika", "S", image_temporaire, 0, 0, 0),
            ("Morel", "S", image_temporaire, 0, 0, 0),
            ("Kaito", "S", image_temporaire, 0, 0, 0),
            ("Feitan", "S", image_temporaire, 0, 0, 0),
            ("Uvogin", "S", image_temporaire, 0, 0, 0),
            ("Phinks", "S", image_temporaire, 0, 0, 0),
            ("Knuckle", "S", image_temporaire, 0, 0, 0),
            ("Pouf", "S", image_temporaire, 0, 0, 0),
            ("Nabunaga", "S", image_temporaire, 0, 0, 0),
            # Personnages A
            ("Machi", "A", image_temporaire, 0, 0, 0),
            ("Shoot", "A", image_temporaire, 0, 0, 0),
            ("Genthru", "A", image_temporaire, 0, 0, 0),
            ("Sharnak", "A", image_temporaire, 0, 0, 0),
            ("Biscuit", "A", image_temporaire, 0, 0, 0),
            ("Razor", "A", image_temporaire, 0, 0, 0),
            ("Gon", "A", image_temporaire, 0, 0, 0),
            ("Pariston", "A", image_temporaire, 0, 0, 0),
            # Personnages B
            ("Pakunoda", "B", image_temporaire, 0, 0, 0),
            ("Shizuku", "B", image_temporaire, 0, 0, 0),
            ("Franklin", "B", image_temporaire, 0, 0, 0),
            ("Cheetu", "B", image_temporaire, 0, 0, 0),
            ("Korutopi", "B", image_temporaire, 0, 0, 0),
            ("Leorio", "B", image_temporaire, 0, 0, 0),
            ("Kalluto", "B", image_temporaire, 0, 0, 0),
            # Personnages C
            ("Zushi", "C", image_temporaire, 0, 0, 0),
            ("Wing", "C", image_temporaire, 0, 0, 0),
            ("Ponzu", "C", image_temporaire, 0, 0, 0),
            ("Pokkle", "C", image_temporaire, 0, 0, 0),
            # Personnages D
            ("Kikyo", "D", image_temporaire, 0, 0, 0),
            # Personnages E
            ("Tompa", "E", image_temporaire, 0, 0, 0),
            ("Neon", "E", image_temporaire, 0, 0, 0),
            # Personnages F
            ("Komugi", "F", image_temporaire, 0, 0, 0),
            ("Mito", "F", image_temporaire, 0, 0, 0),

            # """ PERSONNAGE AVATAR"""
            # Personnages X
            ("Aang (Avatar)", "X", image_temporaire, 0, 0, 0),
            ("Ozai", "X", image_temporaire, 0, 0, 0),
            ("Kyoshi (Avatar)", "X", image_temporaire, 0, 0, 0),
            ("Roku (Avatar)", "X", image_temporaire, 0, 0, 0),
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
            ("Gojo", "X", image_temporaire, 0, 0, 0),
            ("Yuta", "X", image_temporaire, 0, 0, 0),
            ("Kenjaku", "X", image_temporaire, 0, 0, 0),
            ("Mahoraga", "X", image_temporaire, 0, 0, 0),

            # Personnages SS
            ("Toji", "SS", image_temporaire, 0, 0, 0),
            ("Aoi Todo", "SS", image_temporaire, 0, 0, 0),
            ("Geto", "SS", image_temporaire, 0, 0, 0),
            ("Choso", "SS", image_temporaire, 0, 0, 0),
            ("Mahito", "SS", image_temporaire, 0, 0, 0),
            ("Jogo", "SS", image_temporaire, 0, 0, 0),
            ("Kinji Hakari", "SS", image_temporaire, 0, 0, 0),
            ("Yuki Tsukumo", "SS", image_temporaire, 0, 0, 0),
            ("Dagon", "SS", image_temporaire, 0, 0, 0),

            # Personnages S
            ("Megumi", "S", "https://i.imgur.com/ZrNNA55.gif", 0, 0, 0),
            ("Maki", "S", image_temporaire, 0, 0, 0),
            ("Nanami", "S", image_temporaire, 0, 0, 0),
            ("Higuruma", "S", image_temporaire, 0, 0, 0),
            ("Naobito", "S", image_temporaire, 0, 0, 0),
            ("Miguel", "S", image_temporaire, 0, 0, 0),
            ("Mei mei", "S", image_temporaire, 0, 0, 0),
            ("Naoya", "S", image_temporaire, 0, 0, 0),
            
            
            #Personnages A
            ("Panda", "A", image_temporaire, 0, 0, 0),
            ("Inumaki", "A", image_temporaire, 0, 0, 0),
            ("Kamo", "A", image_temporaire, 0, 0, 0),
            ("Nobara", "A", "https://64.media.tumblr.com/71aaf9fe1a8bb90bdb18a12af4a66f0c/baebe1b5c0659d44-38/s540x810/c63e18a1e02b3ddc124a63a57af3d3745ba93cbb.gif", 0, 0, 0),
            ("Toge", "A", image_temporaire, 0, 0, 0),
            ("Mechamaru", "A", image_temporaire, 0, 0, 0),

            # Personnages B
            ("Yuji Itadori", "B", "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/11/itadori-yuji.jpg", 0, 0, 0),
            ("Kusakabe", "B", image_temporaire, 0, 0, 0),
            ("Takuma Ino", "B", image_temporaire, 0, 0, 0),
            ("Yaga", "B", image_temporaire, 0, 0, 0),
            ("Gakuganji", "B", image_temporaire, 0, 0, 0),
            

            # Personnages C
            ("Junpei", "C", image_temporaire, 0, 0, 0),
            ("Momo", "C", "https://i.imgur.com/q0viuTx.png", 0, 0, 0),
            ("Utahime", "C", image_temporaire, 0, 0, 0),
            

            # Personnages D
            
            ("Miwa", "D", "https://i.imgur.com/M0twNwm.png", 0, 0, 0),

            # Personnages E
            ("Juzo", "E", "https://i.imgur.com/lkcQCxs.png", 0, 0, 0),
            ("Ijichi", "E", "https://i.imgur.com/6EKKkX3.jpeg", 0, 0, 0),

            # Personnages F
            ("Kechizu", "F", "https://i.imgur.com/fwEMmNC.png", 0, 0, 0),

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
    (28, "Jinchuriki", "ATK", 0.15, "Les Jinchurikis sont des ninjas qui ont un démon à queue scellé en eux.", image_temporaire, "#FF0000"),
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
    (47, "Ototsuki", "ATK", 0.15, "Le clan Otsutsuki est une famille de ninjas extraterrestres qui cherchent à absorber des planètes pour obtenir du chakra.", image_temporaire, "#800080"),


]

all_link_synergies = {
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
    20 : ["Kiba", "Akamaru", "Karin", "Rob Lucci", "Chopper", "Kaido", "Marco", "Jabra", "Kaku"], # Animal TODO
    21 : ["Sasuke", "Suigetsu", "Karin (naruto)", "Jugo"], # Taka
    22 : ["Nagato", "Pain", "Obito", "Madara", "Sasuke", "Momoshiki", "Kaguya"], # Rinnegan
    23 : ["Naruto", "Sakura", "Sasuke", "Kakashi", "Shikamaru", "Choji", "Ino", "Hinata", "Kiba", "Shino", "Neji", "Rock Lee", "Tenten"], # Konoha TODO
    24 : ["Gaara", "Temari", "Kankuro", "Rasa", "Yashamaru"], # Suna TODO
    25 : ["Kisame", "Zabuza", "Haku", "Mei Terumi", "Ao", "Chojuro", "Yagura", "Mangetsu", "Suigetsu"], # Kiri TODO
    26 : ["Darui", "C", "Omoi", "Killer Bee", "Samui", "Atsui", "Akatsuchi", "Onoki"], # Kumo TODO
    27 : ["Akatsuchi", "Kurotsuchi", "Onoki", "Deidara", "Kurotsuchi", "Akatsuchi", "Onoki", "Deidara"], # Iwa TODO
    28 : ["Naruto", "Bee", "Yugito", "Yagura", "Roshi", "Han", "Utakata", "Fu", "Ginkaku", "Kinkaku"], # Jinchuriki TODO
    29 : ["Aang","Roku","Kyoshi", "Ace", "Sabo", "Iroh", "Zuko", "Ozai", "Azula", "Aang", "Itachi", "Madara", "Sasuke","Kakuzu","Jogo"],# Maître du Feu TODO
    30 : ["Aang","Roku","Kyoshi", "Katara", "Korra", "Unalaq", "Ming-Hua", "Ghazan", "Kya", "Tenzin", "Suigetsu", "Mei Terumi","Kakuzu","Tobirama","Kisame","Haku"], # Maître de l'Eau TODO
    31 : ["Aang","Roku","Kyoshi", "Toph", "Bumi", "Kuvira", "Suyin", "Lin", "Yamato (ANBU)", "Hashirama","Kakuzu"], # Maître de la Terre TODO
    32 : ["Aang","Roku","Kyoshi", "Tenzin", "Gyatso", "Zaheer", "Jinora", "Ikki", "Meelo", "Kai"], # Maître de l'Air TODO
    33 : ["Zuko", "Iroh", "Azula", "Ozai", "Kakashi","Sasuke", "Killer Bee", "Darui", "A", "Kakuzu", "Ener"], # Maître de l'Éclair TODO


    36 : ["Akainu", "Jogo","Mei Terumi","Kurotsuchi"], # Maître de la Lave TODO

    40 : ["Zoro", "Mihawk","Toji", "Killer Bee", "Kuina", "Tashigi", "Kaku", "Sasuke","Kisame", "Suigetsu", "Zabuza","Shanks", "Gol D. Roger", "Stain", "Ichigo", "Aizen", "Kenpachi", "Unohana", "Gin", "Erza", "Dabi", "Darui", "Guts", "Yamamoto", "Trunks", "Tapion", "Gohan", "Rukia", "Byakuya", "Oden", "Law", "Brook","Cavendish","Fujitora","Shiryu", "Yhwach"], # Épéiste
    41 : ["Mob", "Ritsu", "Teruki", "Sho Suzuki", "Tome Kurata", "Dimple"], # Télékinésiste
    42 : ["Barbe Noire", "Shiryu", "Lafitte", "Van Augur", "Doc Q", "Avalo Pizarro", "Catarina Devon", "Vasco Shot"], # Equipage de Barbe Noire
    43 : ["Barbe Blanche", "Marco", "Joz", "Vista", "Blamenco", "Rakuyo", "Namur", "Ace", "Haruta", "Fossa", "Izo", "Atmos"], # Equipage de Barbe Blanche
    44 : ["Naruto", "Kushina", "Nagato", "Karin", "Mito", "Boruto", "Himawari"], # Uzumaki
    45 : ["Neji", "Hinata", "Hiashi", "Hanabi","Himawari", "Boruto"], # Hyuga
    46 : ["Hashirama", "Tobirama", "Tsunade", "Nawaki"], # Senju
    47 : ["Kaguya", "Rikudo", "Hamura", "Urashiki", "Momoshiki", "Kinshiki", "Toneri", "Isshiki"], # Ototsuki
}