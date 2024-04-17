# mousseBot
Bot discord permettant de joueur à un jeu où il faut monter son équipe et tenter de finir l'aventure.

# Arborescence

- `main.py` Fichier principale contenant les fonctionnalités.
- `bdd` Fichier contenant les fonctions concernant la base de donnée
- `mousse.db` Base de donnée en SQLITE3
- `logs.log` Fichier des logs
- `constantes.py` Fichier des constantes
- `datas.py` Fichier avec tous les datas des personnages, des synergies et des liaisons. Peut-être push dans la BDD grâce à la fonction bdd.reset()
- `assets/` Dossier des fichiers multimédias
- `assets/histoire` Dossier qui contient les fichiers utiles pour l'histoire (gif, png)
- `assets/gifs` Dossier qui contient des GIFS sous la nommenclature `id.gif`  qui se téléchargent automatiquement grâce à la commande bdd.downloadGif() à partir des URL des personnages
