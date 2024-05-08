import os
import random
import time
from datas import all_characters_templates
from bdd import Database
import loguru
from itertools import combinations
from constantes import CONSTANTS

from matplotlib import pyplot as plt
import concurrent.futures
from itertools import combinations

database = Database('mousse.db')
if not os.path.exists('statistiques'):
    os.makedirs('statistiques')
        
def generer_team_stats():

    """Génère toutes les combinaisons possibles de 3 personnages et calcule les stats de chaque team."""
    """Écrit les teams dans le fichier teams.log."""
    database = Database('mousse.db')

    temps_depart = time.time()
    print("Début du programme...", time.strftime('%H:%M:%S', time.localtime(temps_depart)))
    # 1. Créer une liste de toutes les teams possibles
    all_characters = database.get_character_templates()
    all_characters = [character for character in all_characters if character[2] in ['S','A']]  # Filtrer les personnages de rareté X
    all_teams = []

    # Générer toutes les combinaisons possibles de 3 personnages
    for team_characters in combinations(all_characters, 3):
        team = sorted(team_characters, key=lambda x: x[1])  # Tri des personnages par nom
        all_teams.append(team)

    print("Nombre de teams possibles :", len(all_teams))

    # 2. Éliminer les doublons en utilisant un ensemble
    teams_set = {tuple(team) for team in all_teams}
    all_teams = [list(team) for team in teams_set]
    print("Nombre de teams possibles sans doublons :", len(all_teams))

    all_stats = []
    i = 0
    for team in all_teams:
        i += 1
        stats = database.simulation_stats_team(team)
        total_power = stats['stats']['ATK'] + stats['stats']['DEF'] + stats['stats']['HP']
        all_stats.append((stats, total_power))
        temps_ecoule = time.time() - temps_depart
        temps_restant_estime = temps_ecoule / i * (len(all_teams) - i)
        if i % 5000 == 0:
            print(f"Nombre de teams traitées : {i} / {len(all_teams)} - Temps restant estimé : {int(temps_restant_estime // 60)}m{int(temps_restant_estime % 60)}s")

    print("Les stats de teams sont calculées !")

    all_stats.sort(key=lambda x: x[1], reverse=True)
    # Créer un fichier log
    # 3. Écrire les équipes dans le fichier teams.txt
    with open('statistiques/teams.log', 'w') as file:
        for team, power in all_stats:
            team_to_write = [character[1] for character in team['team']]
            synergies_to_write = [synergie for synergie in team['synergies']]
            file.write(f"{team_to_write} : {power} {synergies_to_write}\n")

    print("Les teams sont écrites dans le fichier teams.log !")

    with open("statistiques/teams3000.log","w") as file:
        for team, power in all_stats[:3000]:
            team_to_write = [character[1] for character in team['team']]
            synergies_to_write = [synergie for synergie in team['synergies']]
            file.write(f"{team_to_write} : {power} {synergies_to_write}\n")

    temps_fin = time.time()
    print("Fin du programme...", time.strftime('%H:%M:%S', time.localtime(temps_fin)))

def somme_proba_invocation():
    def somme_liste(liste):
        somme = 0
        for element in liste:
            somme += element
        return somme
    return somme_liste(CONSTANTS['RARITY_CHANCE'].values()), somme_liste(CONSTANTS['RARITY_CHANCE_HIGH'].values())

def classement_personnages():
    database = Database('mousse.db')
    all_characters = database.get_character_templates()
    # on calcule la somme des stats de chaque personnage
    all_characters = [(character[1], character[4] + character[5] + character[6]) for character in all_characters]
    all_characters.sort(key=lambda x: x[1], reverse=True)
    with open('statistiques/classement_personnage.log', 'w') as file:
        for character in all_characters:
            file.write(f"{character[0]} : {character[1]}\n")

def classement_nombre_synergies(verbose=False):
    database = Database('mousse.db')
    all_characters = database.get_character_templates()
    all_characters_synergies = {}
    for character in all_characters:
        all_characters_synergies[character] = database.get_synergies_by_character_template(character[0])
    print(all_characters_synergies) if verbose else None
    for character, synergies in all_characters_synergies.items():
        if synergies is None:
            all_characters_synergies[character] = []
    all_characters_synergies = [(character, len(synergies)) for character, synergies in all_characters_synergies.items()]
    all_characters_synergies.sort(key=lambda x: x[1], reverse=True)
    with open('statistiques/classement_nombre_synergies.log', 'w') as file:
        for character in all_characters_synergies:
            file.write(f"{character[0][1]} [{character[0][2]}] : {character[1]}\n")

def max_puissance_en_invocation(nombre_invocations, Verbose=False):
    liste_perso_puissance = {}
    """ Retourne le nombre maximum de puissance que l'on peut obtenir en invoquant un certain nombre de fois """
    database = Database('mousse.db')
    character_templates = database.get_character_templates()
    liste_personnage_invoques = []
    for i in range(nombre_invocations):
        # On choisit une rareté au hasard
        rarity = random.choices(list(CONSTANTS['RARITY_CHANCE'].keys()), list(CONSTANTS['RARITY_CHANCE'].values()))[0]
        # On choisit un univers au hasard TODO
        # On invoque un personnage aléatoire
        character_templates_new = [char for char in character_templates if char[2] == rarity]
        character = random.choice(character_templates_new)
        liste_personnage_invoques.append(character)
    # On trie les personnages par puissance
    liste_personnage_invoques.sort(key=lambda x: x[4] + x[5] + x[6], reverse=True)
    liste_personnage_invoques = liste_personnage_invoques[0:16] if len(liste_personnage_invoques) > 15 else liste_personnage_invoques
    print(liste_personnage_invoques) if Verbose else None
    all_teams = []
    # Générer toutes les combinaisons possibles de 3 personnages
    for team_characters in combinations(liste_personnage_invoques, 3):
        team = sorted(team_characters, key=lambda x: x[1])  # Tri des personnages par nom
        all_teams.append(team)
    teams_set = {tuple(team) for team in all_teams}
    all_teams = [list(team) for team in teams_set]
    all_stats = []
    for team in all_teams:
        stats = database.simulation_stats_team(team)
        total_power = stats['stats']['ATK'] + stats['stats']['DEF'] + stats['stats']['HP']
        all_stats.append((stats, total_power))
    all_stats.sort(key=lambda x: x[1], reverse=True)
    # On affiche la meilleure équipe
    print(all_stats[0][0]['team']) if Verbose else None
    return all_stats[0][1]

def moyenne_max_puissance_en_invocation(nombre_invocations, nombre_simulations=30):
    """ Retourne la moyenne de la puissance obtenue en invoquant un certain nombre de fois """
    puissances = []
    print(f"Calcul de la moyenne de la puissance en invoquant {nombre_invocations} fois. Temps départ : {time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    for i in range(nombre_simulations):
        puissances.append(max_puissance_en_invocation(nombre_invocations))
    print(f"Calcul terminé. Temps fin : {time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    return sum(puissances) / len(puissances)


def graphique_puissance_invocation():
    """ Crée un graphique de la puissance des personnages en fonction du nombre d'invocations """
    x = [i for i in range(3, 200)]
    y = [moyenne_max_puissance_en_invocation(i) for i in x]
    # On peut faire un modèle de prédiction pour voir la tendance
    import numpy as np
    z = np.polyfit(x, y, 3)
    p = np.poly1d(z)
    print(z,p)
    plt.plot(x, p(x), "r--")

    plt.plot(x, y)
    plt.xlabel("Nombre d'invocations")
    plt.ylabel("Puissance des 3 plus puissants personnages")
    plt.title("Puissance des personnages en fonction du nombre d'invocations")
    plt.show()

def analyse_stats_aberrantes():
    # On va chercher les stats des personnages
    # On va calculer la moyenne et l'écart-type
    # On va chercher les personnages qui ont des stats aberrantes
    database = Database('mousse.db')
    all_characters = database.get_character_templates()
    moyennes = getMoyennes(all_characters)
    seuil = input("Entrez le seuil de détection d'aberration (1.3 par défaut) : ")
    seuil = float(seuil) if seuil else 1.3
    for character in all_characters:
        if character[4] > moyennes[character[2]][0] * seuil or character[4] < moyennes[character[2]][0] * (2-seuil):
            print(f"{character[1]} a une attaque de {character[4]} contre une moyenne de {moyennes[character[2]][0]}")
        if character[5] > moyennes[character[2]][1] * seuil or character[5] < moyennes[character[2]][1] * (2-seuil):
            print(f"{character[1]} a une défense de {character[5]} contre une moyenne de {moyennes[character[2]][1]}")
        if character[6] > moyennes[character[2]][2] * seuil or character[6] < moyennes[character[2]][2] * (2-seuil):
            print(f"{character[1]} a une vie de {character[6]} contre une moyenne de {moyennes[character[2]][2]}")

def getMoyennes(all_characters):
    #Retourne un dictionnaire avec les stats moyennes des personnages par rang
    moyennes = {}
    nombres_persos = {}
    for character in all_characters:
        rang = character[2]
        if rang not in moyennes:
            moyennes[rang] = [0,0,0]
            nombres_persos[rang] = 0
        moyennes[rang][0] += character[4]
        moyennes[rang][1] += character[5]
        moyennes[rang][2] += character[6]
        nombres_persos[rang] += 1
    for rang in moyennes:
        moyennes[rang][0] //= nombres_persos[rang]
        moyennes[rang][1] //= nombres_persos[rang]
        moyennes[rang][2] //= nombres_persos[rang]
    return moyennes

def check_double_synergie():
    # Vérifie si un personnage a deux fois la même synergie
    database = Database('mousse.db')
    all_characters = database.get_character_templates()
    for character in all_characters:
        synergies = database.get_synergies_by_character_template(character[0])
        if len(synergies) != len(set(synergies)):
            print(f"{character[1]} a des doublons dans ses synergies")

def classement_synergies_les_plus_donnes():
    # Ecris dans un fichier texte le nombre de personnages qui ont une synergie donnée
    database = Database('mousse.db')
    all_synergies = database.get_synergies()
    all_characters = database.get_character_templates()
    all_synergies_count = {}
    for synergy in all_synergies:
        all_synergies_count[synergy[1]] = 0
    for character in all_characters:
        synergies = database.get_synergies_by_character_template(character[0])
        for synergy in synergies:
            all_synergies_count[synergy[3]] += 1
    all_synergies_count = sorted(all_synergies_count.items(), key=lambda x: x[1], reverse=True)
    with open('statistiques/classement_synergies.log', 'w') as file:
        for synergy in all_synergies_count:
            file.write(f"{synergy[0]} : {synergy[1]}\n")



def demandes():
    if input("Voulez vous reset la BDD ? (o/n) ") == 'o':
        Database('mousse.db').reset()
    if input("Voulez vous reset toutes les URL ? (o/n) ") == 'o':
        Database('mousse.db').remplacer_toutes_les_urls()
    if input("Voulez-vous vérifier les doublons dans les synergies ? (o/n) ") == 'o':
        check_double_synergie()
    if input("Voulez voir les stats aberrantes ? (o/n) ") == 'o':
        analyse_stats_aberrantes()
    if input("Voulez-vous générer un graphique de la puissance des personnages en fonction du nombre d'invocations (GOURMAND EN RESSOURCE) ? (o/n) ") == 'o':
        graphique_puissance_invocation()
    somme_invocation = input("Voulez-vous calculer la somme des probabilités d'invocation ? (o/n) ")
    if somme_invocation == 'o':
        print(somme_proba_invocation())
    generer_stats = input("Voulez-vous générer les stats des teams (GOURMAND EN RESSOURCE)? (o/n) ")
    if generer_stats == 'o':
        generer_team_stats()
    classement = input("Voulez-vous générer le classement des statistiques personnages ? (o/n) ")
    if classement == 'o':
        classement_personnages()
    top_synergie = input("Voulez-vous générer le nombre de synergies par personnage ? (o/n) ")
    if top_synergie == 'o':
        classement_nombre_synergies()
    if input("Voulez-vous générer le classement des synergies les plus données ? (o/n) ") == 'o':
        classement_synergies_les_plus_donnes()
    if input("Souhaitez vous clear le dossier logs? (o/n) ") == 'o':
        for file in os.listdir('./logs'):
            try:
                os.remove(f'./logs/{file}')
            except Exception as e:
                print(f"Impossible de supprimer {file} : {e}")
    print("Fin des demandes.")
    return


if input("Voulez-vous accéder au menu des demandes ? (o/n) ") == 'o':
    demandes()


