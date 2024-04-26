from datas import all_characters_templates
from bdd import Database
import loguru

database = Database('mousse.db')

from itertools import combinations

# 1. Créer une liste de toutes les teams possibles
all_characters = database.get_character_templates()
all_characters = [character for character in all_characters if character[2] in ['X','SS']]  # Filtrer les personnages de rareté X
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

# 3. Écrire les équipes dans le fichier teams.txt
with open('teams.log', 'w') as file:
    for team, power in all_stats:
        team_to_write = [character[1] for character in team['team']]
        synergies_to_write = [synergie for synergie in team['synergies']]
        file.write(f"{team_to_write} : {power} {synergies_to_write}\n")

print("Les teams sont écrites dans le fichier teams.log !")
