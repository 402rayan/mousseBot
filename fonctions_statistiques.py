from datas import all_characters_templates
from bdd import Database
import loguru

# Créer un classement des meilleurs teams en fonction de la puissance totale avec les bonus

# 1 - Créer une liste de toutes les teams possibles
# 2 - Calculer la puissance de chaque team
# 3 - Ranger les teams par puissance

database = Database('mousse.db')


# 1 - Créer une liste de toutes les teams possibles
all_characters = database.get_character_templates()

all_chatres_x_ss = []
for character in all_characters:
    if character[2] in ['X']:
        all_chatres_x_ss.append(character)

all_characters = all_chatres_x_ss

all_teams = []
for character1 in all_characters:
    for character2 in all_characters:
        for character3 in all_characters:
            if character1 == character2 or character1 == character3 or character2 == character3:
                continue
            team = [character1, character2, character3]
            all_teams.append(team)

print("Nombre de teams possibles : ", len(all_teams))

# Etape où l'on supprime les doublons (Par exemple : [A, B, C] et [C, B, A] sont les mêmes teams)
teams = []
for team in all_teams:
    team.sort(key=lambda x: x[1])
    if team not in teams:
        teams.append(team)
print("Nombre de teams possibles sans doublons : ", len(teams))

all_teams = teams


all_stats = []

for team in all_teams:
    stats = database.simulation_stats_team(team)
    all_stats.append((stats, (stats['stats']['ATK'] + stats['stats']['DEF'] + stats['stats']['HP'])))

print("Les stats de teams sont calculées !")

all_stats.sort(key=lambda x: x[1], reverse=True)

      
print("Les teams sont écrites dans le fichier teams.txt !")

# On ecrit avec loguru

# On supprime le fichier teams.log si existant
import os
if os.path.exists('teams.log'):
    os.remove('teams.log')
    
with loguru.logger.catch():
    loguru.logger.add('teams.log')
    for team, power in all_stats:
        team_to_write = [character[1] for character in team['team']]
        synergies_to_write = [synergie for synergie in team['synergies']]
        loguru.logger.info(f'{team_to_write} : {power}' + ' ' + str(synergies_to_write) + '\n')