import os
import random
import time
from datas import all_characters_templates
from bdd import Database
import loguru
from itertools import combinations
from constantes import CONSTANTS

from matplotlib import pyplot as plt

def generer_team_stats():
    if not os.path.exists('statistiques'):
        os.makedirs('statistiques')
    """Génère toutes les combinaisons possibles de 3 personnages et calcule les stats de chaque team."""
    """Écrit les teams dans le fichier teams.log."""
    database = Database('mousse.db')

    temps_depart = time.time()
    print("Début du programme...", time.strftime('%H:%M:%S', time.localtime(temps_depart)))
    # 1. Créer une liste de toutes les teams possibles
    all_characters = database.get_character_templates()
    all_characters = [character for character in all_characters if character[2] in ['X','SS','S']]  # Filtrer les personnages de rareté X
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

    for team in all_teams:
        stats = database.simulation_stats_team(team)
        total_power = stats['stats']['ATK'] + stats['stats']['DEF'] + stats['stats']['HP']
        all_stats.append((stats, total_power))

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
        all_characters_synergies[character[1]] = database.get_synergies_by_character_template(character[0])
    print(all_characters_synergies) if verbose else None
    for character, synergies in all_characters_synergies.items():
        if synergies is None:
            all_characters_synergies[character] = []
    all_characters_synergies = [(character, len(synergies)) for character, synergies in all_characters_synergies.items()]
    all_characters_synergies.sort(key=lambda x: x[1], reverse=True)
    with open('statistiques/classement_nombre_synergies.log', 'w') as file:
        for character in all_characters_synergies:
            file.write(f"{character[0]} : {character[1]}\n")

def max_puissance_en_invocation(nombre_invocations, Verbose=False):
    liste_perso_puissance = {}
    """ Retourne le nombre maximum de puissance que l'on peut obtenir en invoquant un certain nombre de fois """
    database = Database('mousse.db')
    character_templates = database.get_character_templates()
    for i in range(nombre_invocations):
        # On choisit une rareté au hasard
        rarity = random.choices(list(CONSTANTS['RARITY_CHANCE'].keys()), list(CONSTANTS['RARITY_CHANCE'].values()))[0]
        # On choisit un univers au hasard TODO
        # On invoque un personnage aléatoire
        character_templates_new = [char for char in character_templates if char[2] == rarity]
        character = random.choice(character_templates_new)
        power = character[4] + character[5] + character[6]
        liste_perso_puissance[character[1]] = power
    liste_perso_puissance = sorted(liste_perso_puissance.items(), key=lambda x: x[1], reverse=True)
    # On retourne la somme des 3 plus puissants
    print(liste_perso_puissance[:3]) if Verbose else None
    return sum([puissance for perso, puissance in liste_perso_puissance[:3]])


def graphique_puissance_invocation():
    """ Crée un graphique de la puissance des personnages en fonction du nombre d'invocations """
    x = [i for i in range(1, 400)]
    y = [max_puissance_en_invocation(i) for i in x]
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


def demandes():
    if input("Voulez vous reset la BDD ? (o/n) ") == 'o':
        Database('mousse.db').reset()
    if input("Voulez-vous générer un graphique de la puissance des personnages en fonction du nombre d'invocations ? (o/n) ") == 'o':
        graphique_puissance_invocation()
    somme_invocation = input("Voulez-vous calculer la somme des probabilités d'invocation ? (o/n) ")
    if somme_invocation == 'o':
        print(somme_proba_invocation())
    generer_stats = input("Voulez-vous générer les stats des teams (GOURMAND EN RESSOURCE)? (o/n) ")
    if generer_stats == 'o':
        generer_team_stats()
    classement = input("Voulez-vous générer le classement des personnages ? (o/n) ")
    if classement == 'o':
        classement_personnages()
    top_synergie = input("Voulez-vous générer le top des synergies ? (o/n) ")
    if top_synergie == 'o':
        classement_nombre_synergies()



if input("Voulez-vous accéder au menu des demandes ? (o/n) ") == 'o':
    demandes()


