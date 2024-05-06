# mousseBot
MousseBot est un bot discord permettant de jouer textuellement à un jeu. Le but est simple! Il faut invoquer des personnages! Cela coûte des tickets que l'on peut obtenir toutes les heures!
Avec ces personnages plusieurs choix s'offrent à nous :
- Essayer de former la meilleure équipe possible grâce aux synergies entre personnages!
- Affronter ses amis la commande `!pvp`
- Découvrire une histoire créée spécialement pour le jeu avec `!histoire`
- Compléter la collection de tous les personnages! Visible avec `!statisttique`

# Lancer le Bot

Pour lancer le bot il faut cloner ce dossier, créer un fichier getToken.py, et dedans créer une fonction getToken() qui retourne le token de votre Bot.

# Arborescence

- `main.py` Fichier principale contenant les fonctionnalités. *(Front)*
- `bdd.py` Fichier contenant les fonctions concernant la base de donnée *(Back)*
- `mousse.db` Base de donnée en SQLITE3
- `logs.log` Fichier des logs
- `constantes.py` Fichier des constantes
- `datas.py` Fichier avec tous les datas des personnages, des synergies, des techniques. ùPeut-être push dans la BDD grâce à la fonction bdd.reset()ù
- `assets/` Dossier des fichiers multimédias
- `assets/histoire` Dossier qui contient les fichiers utiles pour l'histoire (gif, png)
- `assets/gifs` Dossier qui contient des GIFS sous la nommenclature `id.gif`  qui se téléchargent automatiquement grâce à la commande bdd.downloadGif() à partir des URL des personnages (PAS FONCTIONNEL)
- `statistiques/` Dossier qui contient des fichers .log de statistiques générés grâce aux commandes ci-dessous
- `fonctions_statistiques.py` Fichier à lancer contenant des fonctions de statistiques.
