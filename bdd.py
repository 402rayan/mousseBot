from itertools import combinations
import random
import shutil
import sqlite3
from loguru import logger
from datetime import datetime, timedelta

import requests

from constantes import CONSTANTS
from datas import all_characters_templates, all_synergies, all_link_synergies, all_techniques
import Levenshtein

# SI le dossiers logs n'existe pas, on le crée
from os import path, makedirs

if not path.exists("logs"):
    makedirs("logs")
# Configurer Loguru pour écrire les logs dans un fichier

logger.add("./logs/logs_{time}.log", rotation="1 day")

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        self.cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def select(self, table_name, columns, condition):
        self.cur.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cur.fetchall()

    def update(self, table_name, columns, values, condition):
        self.cur.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, condition):
        self.cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def create_user_table(self):
        # Create table for users
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            user_discord_id TEXT,
            user_name TEXT,
            tickets INTEGER DEFAULT 0,
            last_claim DATETIME,
            character_slot_one INTEGER,
            character_slot_two INTEGER,
            character_slot_three INTEGER,
            histoireLevel INTEGER DEFAULT 1,
            next_invocation INTEGER DEFAULT 0,
            last_time_auto_team DATETIME DEFAULT NULL,
            FOREIGN KEY (character_slot_one) REFERENCES characters (char_id),
            FOREIGN KEY (character_slot_two) REFERENCES characters (char_id),
            FOREIGN KEY (character_slot_three) REFERENCES characters (char_id)
        )
        ''')
        self.conn.commit()

    def create_character_template_table(self):
        # Create table for character templates
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS character_templates (
            template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rarity TEXT,
            image_url TEXT,
            base_hp INTEGER,
            base_attack INTEGER,
            base_defense INTEGER
        )
        ''')
        self.conn.commit()

    def create_character_table(self):
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            char_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_discord_id INTEGER,
            template_id INTEGER,
            level INTEGER DEFAULT 1,
            experience INTEGER DEFAULT 0,
            FOREIGN KEY (user_discord_id) REFERENCES users (user_discord_id),
            FOREIGN KEY (template_id) REFERENCES character_templates (template_id)
        )
        ''')
        self.conn.commit()

    def create_synergy_table(self):
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS synergies (
            synergy_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type_of_boost TEXT,
            force_of_boost FLOAT,
            description TEXT,
            image_url TEXT,
            color INTEGER
        )
        ''')
        self.conn.commit()
    
    def create_character_template_synergy_table(self):
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS character_template_synergies (
            template_id INTEGER,
            synergy_id INTEGER,
            FOREIGN KEY (template_id) REFERENCES character_templates (template_id),
            FOREIGN KEY (synergy_id) REFERENCES synergies (synergy_id)
        )
        ''')
        self.conn.commit()
    
    def crate_user_choices(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS user_choices (
            user_discord_id TEXT,
            lvl1fumee BOOLEAN DEFAULT NULL,
            lvl4zukoLie BOOLEAN DEFAULT NULL,
            lvl6pucci BOOLEAN DEFAULT NULL,
            lvl10run BOOLEAN DEFAULT NULL,
            lvl13chatMaisonHantee BOOLEAN DEFAULT NULL,
            lvl18skipDialogue BOOLEAN DEFAULT NULL,
            FOREIGN KEY (user_discord_id) REFERENCES users (user_discord_id)
        )
        ''')
    
    def create_character_template_technique_table(self):
        # technique ID, character_template_ID, nom, descriptionn, image_url, color
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS character_template_techniques (
            technique_id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_id INTEGER,
            name TEXT,
            phrase TEXT,
            image_url TEXT,
            color INTEGER,
            FOREIGN KEY (template_id) REFERENCES character_templates (template_id)
        )
        ''')
        self.conn.commit()
        
    def getChoice(self, user_discord_id, choice):
        self.cur.execute(f"SELECT {choice} FROM user_choices WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone()[0]
    
    def autoTeam(self, user_discord_id,ignoreTime = False,max_character_auto_team = 25):
        # Vérifie que l'utilisateur a moins de 50 personnages
        self.cur.execute(f"SELECT COUNT(*) FROM characters WHERE user_discord_id = {user_discord_id}")
        count = self.cur.fetchone()[0]
        print(count)
        if count < 3:
            return "ERROR_MIN_CHARACTERS"
        # Récupère les personnages de l'utilisateur
        # Verifie qu'il n'a pas utilisé la commande il y a 2 minutes
        self.cur.execute(f"SELECT last_time_auto_team FROM users WHERE user_discord_id = {user_discord_id}")
        last_time = self.cur.fetchone()[0]
        last_time = datetime.strptime(last_time, '%Y-%m-%d %H:%M:%S.%f') if last_time is not None else None
        if last_time is not None and last_time + timedelta(minutes=2) > datetime.now() and not ignoreTime:
            return "ERROR_AUTO_TEAM_TOO_FAST"
        self.cur.execute(f"UPDATE users SET last_time_auto_team = '{datetime.now()}' WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        characters = self.get_characters(user_discord_id)
        if count >= max_character_auto_team:
            logger.info(f"L'utilisateur {user_discord_id} a trop de personnages pour utiliser la commande auto_team.")
            # On trie les characters pour ne prendre que les 35 plus puissants
            characters.sort(key=lambda x: x[3] + x[4] + x[5], reverse=True)
            characters = characters[:max_character_auto_team]
        all_teams = []
        # Générer toutes les combinaisons possibles de 3 personnages
        for team_characters in combinations(characters, 3):
            team = sorted(team_characters, key=lambda x: x[1])  # Tri des personnages par nom
            all_teams.append(team)

        # 2. Éliminer les doublons en utilisant un ensemble
        teams_set = {tuple(team) for team in all_teams}
        all_teams = [list(team) for team in teams_set]

        all_stats = []

        for team in all_teams:
            stats = self.simulation_stats_team(team,True)
            total_power = stats['stats']['ATK'] + stats['stats']['DEF'] + stats['stats']['HP']
            all_stats.append((stats, total_power))
        
        all_stats.sort(key=lambda x: x[1], reverse=True)
        return all_stats[:3]
        

    def get_stats(self):
        # Retourne des statistiques tel que le nombre de personnages par rareté
        self.cur.execute("SELECT rarity, COUNT(*) FROM character_templates GROUP BY rarity")
        nombre_par_rarete = self.cur.fetchall()
        dic = {}
        for i in nombre_par_rarete:
            dic[i[0]] = i[1]
        return {'NOMBRE_PAR_RARETE': dic}
    
    def get_stats_joueur(self, user_discord_id):
        # Retourne des statistiques sur le joueur tel que le nombre de personnages qu'il possède
        self.cur.execute(f"SELECT COUNT(*) FROM characters WHERE user_discord_id = {user_discord_id}")
        nombre_personnages = self.cur.fetchone()[0]
        self.cur.execute(f"SELECT rarity, COUNT(*) FROM characters c JOIN character_templates t ON c.template_id = t.template_id WHERE user_discord_id = {user_discord_id} GROUP BY rarity")
        nombre_par_rarete = self.cur.fetchall()
        self.cur.execute(f"SELECT tickets FROM users WHERE user_discord_id = {user_discord_id}")
        nombre_tickets = self.cur.fetchone()[0]
        puissance = self.getPower(user_discord_id)
        return {'NOMBRE_PERSONNAGES': nombre_personnages, 'NOMBRE_PAR_RARETE': nombre_par_rarete, 'NOMBRE_TICKETS': nombre_tickets, 'PUISSANCE': puissance}
        

    def updateChoice(self, user_discord_id, choice, value):
        self.cur.execute(f"UPDATE user_choices SET {choice} = {value} WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
    
    def create_tables(self):
        self.create_user_table()
        self.create_character_template_table()
        self.create_character_table()
        self.create_synergy_table()
        self.create_character_template_synergy_table()
        self.crate_user_choices()
        self.create_character_template_technique_table()
        self.conn.commit()
        logger.info("Fin de la création des tables.")
        
    def insert_user(self, user_discord_id, user_name):
        #On vérifie si l'utilisateur existe déjà
        #logger.info(f"Vérification de l'utilisateur {user_name} ({user_discord_id}) dans la base de données.")
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        user = self.cur.fetchone()
        if user is None:
            self.cur.execute(f"INSERT INTO users (user_discord_id, user_name, tickets) VALUES ({user_discord_id}, '{user_name}', 10)")
            # On l'insère aussi dans la table des choix
            self.cur.execute(f"INSERT INTO user_choices (user_discord_id) VALUES ({user_discord_id})")
            self.conn.commit()
            logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a été inscrit dans la base de données.")
            return True

    def get_tickets(self, user_discord_id):
        self.cur.execute(f"SELECT tickets FROM users WHERE user_discord_id = {user_discord_id}")
        tickets = self.cur.fetchone()
        return tickets[0]
    
    def get_last_claim(self, user_discord_id):
        self.cur.execute(f"SELECT last_claim FROM users WHERE user_discord_id = {user_discord_id}")
        last_claim = self.cur.fetchone()
        return last_claim[0]
    
    def update_tickets(self, user_discord_id, tickets):
        self.cur.execute(f"UPDATE users SET tickets = {tickets} WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
    
    def xp_for_next_level(self, current_level):
        # Base XP required for the first level
        base_xp = 100
        # Growth rate
        growth_rate = 1.15
        # Calculate XP for the next level
        return int(base_xp * (growth_rate ** current_level))

    def get_current_xp_and_level(self, character_id):
        self.cur.execute(f"SELECT experience, level FROM characters WHERE char_id = {character_id}")
        current_xp, current_level = self.cur.fetchone()
        return current_xp, current_level
    
    def update_level_and_xp(self,character_id, xp_to_add):
        # Récupère l'XP actuel et le niveau de l'utilisateur
        current_xp, current_level = self.get_current_xp_and_level(character_id)
        
        # Mise à jour de l'XP
        new_xp = current_xp + xp_to_add
        while (new_xp >= self.xp_for_next_level(current_level)) and (current_level < 100):
            new_xp -= self.xp_for_next_level(current_level)
            current_level += 1
        
        # Mettre à jour l'XP et le niveau dans la base de données
        self.cur.execute(f"UPDATE characters SET experience = {new_xp}, level = {current_level} WHERE char_id = {character_id}")
        logger.info(f"Le personnage {character_id} a gagné {xp_to_add} XP. Il est maintenant niveau {current_level} avec {new_xp} XP.")
        self.conn.commit()
        
    def claim_hourly(self, user_discord_id, user_name):
        # On vérifie si l'utilisateur a déjà réclamé son hourly
        last_claim = self.get_last_claim(user_discord_id)
        if last_claim is not None:
            last_claim = datetime.strptime(last_claim, '%Y-%m-%d %H:%M:%S.%f')
            if last_claim + timedelta(hours=1) > datetime.now():
                logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a déjà réclamé son hourly.")
                remaining_time = last_claim + timedelta(days=1) - datetime.now()
                return [False, remaining_time]
        # On ajoute les tickets
        tickets = self.get_tickets(user_discord_id)
        tickets += CONSTANTS['HOURLY_TICKETS']
        self.update_tickets(user_discord_id, tickets)
        # On met à jour la date de réclamation
        self.cur.execute(f"UPDATE users SET last_claim = '{datetime.now()}' WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        # On rajoute un niveau à toute sa team
        xp = random.choice(CONSTANTS['HOURLY_XP'])
        self.ajouter_niveau_team(user_discord_id,xp)
        logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a réclamé son daily. Il a maintenant {tickets} tickets.")
        return [True, tickets,xp]
        
    def ajouter_niveau_team(self, user_discord_id, amount):
        # On récupère la team de l'utilisateur
        team = self.get_characters(user_discord_id)
        # On ajoute un niveau à chaque personnage
        for character in team:
            self.update_level_and_xp(character[0], amount)
        logger.info(f"L'utilisateur {user_discord_id} a ajouté {amount} niveaux à sa team.")
        return

    def get_character_templates(self):
        self.cur.execute("SELECT * FROM character_templates")
        return self.cur.fetchall()
    
    def get_character_template(self, template_id):
        self.cur.execute(f"SELECT * FROM character_templates WHERE template_id = {template_id}")
        return self.cur.fetchone()
    
    def get_characters(self, user_discord_id,rarity=None):
        if rarity is not None:
            self.cur.execute(f"SELECT * FROM characters c LEFT JOIN character_templates t ON c.template_id = t.template_id WHERE user_discord_id = {user_discord_id} AND t.rarity = '{rarity}'")
        else:
            self.cur.execute(f"SELECT * FROM characters c LEFT JOIN character_templates t ON c.template_id = t.template_id WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchall()
    
    def get_character_with_stats(self,character):
        level = character[3]
        newCharacter = (character[0],character[1],character[2],character[3],character[4],character[5],character[6],character[7],character[8],character[9] + level,character[10] + level,character[11] + level)
        return newCharacter
    
    def get_character(self, char_id):
        # Retourne un character avec ses stats à jour en fonction du niveau
        self.cur.execute(f"SELECT * FROM characters c LEFT JOIN character_templates t ON c.template_id = t.template_id WHERE char_id = {char_id}")
        character = self.cur.fetchone()
        return self.get_character_with_stats(character)
    
    def get_character_template_by_name(self, user_discord_id, user_name, template_name):
        # Exécuter la requête SQL pour obtenir tous les templates
        self.cur.execute(f"SELECT * FROM character_templates")
        all_templates = self.cur.fetchall()
        # Premiere étape : on vérifie si le nom est exact
        for template in all_templates:
            if template[1].lower() == template_name.lower():
                return template
        # Deuxième étape : on vérifie si le nom est proche
        for template in all_templates:
            # print(template[1].lower(), template_name.lower(), Levenshtein.distance(template[1].lower(), template_name.lower()))
            if Levenshtein.distance(template[1].lower(), template_name.lower()) <= 1:
                if user_name == "Bot":
                    logger.warning(f"Levenshtein : {template[1].lower()} - {template_name.lower()}")
                return template
        # Troisième étape : On vérifie si le nom est dans le nom du template
        for template in all_templates:
            if template_name.lower() in template[1].lower():
                if user_name == "Bot":
                    logger.warning(template_name, " a été trouvé dans le nom.")
                return template
        logger.error(f"Le template {template_name} n'a pas été trouvé.")
        return None
    
    def get_synergie_by_name(self, user_discord_id, user_name, synergy_name):
        # Exécuter la requête SQL pour obtenir toutes les synergies
        self.cur.execute(f"SELECT * FROM synergies")
        all_synergies = self.cur.fetchall()
        # Premiere étape : on vérifie si le nom est exact
        for synergy in all_synergies:
            if synergy[1].lower() == synergy_name.lower():
                return synergy
        # Deuxième étape : on vérifie si le nom est proche
        for synergy in all_synergies:
            if Levenshtein.distance(synergy[1].lower(), synergy_name.lower()) <= 1:
                return synergy
        # Troisième étape : On vérifie si le nom est dans le nom de la synergie
        for synergy in all_synergies:
            if synergy_name.lower() in synergy[1].lower():
                return synergy
        return None
    
    def get_character_template_who_has_synergy(self, synergy_id):
        logger.info(f"Récupération des personnages ayant la synergie {synergy_id}.")
        self.cur.execute(f"SELECT * FROM character_templates c JOIN character_template_synergies s ON c.template_id = s.template_id WHERE synergy_id = {synergy_id}")
        return self.cur.fetchall()
        
    def create_character(self, user_discord_id,user_name, template_id):
        self.cur.execute(f"INSERT INTO characters (user_discord_id, template_id) VALUES ({user_discord_id}, {template_id})")
        self.conn.commit()
        return self.cur.lastrowid
    
    def delete_character(self, char_id):
        self.cur.execute(f"DELETE FROM characters WHERE char_id = {char_id}")
        self.cur.execute(f"UPDATE users SET character_slot_one = NULL WHERE character_slot_one = {char_id}")
        self.cur.execute(f"UPDATE users SET character_slot_two = NULL WHERE character_slot_two = {char_id}")
        self.cur.execute(f"UPDATE users SET character_slot_three = NULL WHERE character_slot_three = {char_id}")
        self.conn.commit()
        logger.info(f"Le personnage {char_id} a été supprimé.")
    
    def update_character(self, char_id, level, experience):
        self.cur.execute(f"UPDATE characters SET level = {level}, experience = {experience} WHERE char_id = {char_id}")
        self.conn.commit()
        logger.info(f"Le personnage {char_id} a été mis à jour.")
    
    def update_special_invocation(self, user_discord_id, value):
        self.cur.execute(f"UPDATE users SET next_invocation = {value} WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()

    def summon_character(self, user_discord_id, user_name, special=False):
        # On réduit le nombre de tickets
        tickets = self.get_tickets(user_discord_id)
        if tickets < CONSTANTS['INVOCATION_COST']:
            return None
        tickets -= CONSTANTS['INVOCATION_COST']
        # On choisit la rareté du personnage invoqué
        if special:
            rarity = random.choices(list(CONSTANTS['RARITY_CHANCE_HIGH'].keys()), list(CONSTANTS['RARITY_CHANCE_HIGH'].values()))[0]
        else:
            rarity = random.choices(list(CONSTANTS['RARITY_CHANCE'].keys()), list(CONSTANTS['RARITY_CHANCE'].values()))[0]
        # On choisit un univers au hasard TODO
        # On invoque un personnage aléatoire
        character_templates = self.get_character_templates()
        character_templates = [char for char in character_templates if char[2] == rarity]
        liste_personnages = self.get_characters(user_discord_id)
        if len(liste_personnages) >= CONSTANTS['MAX_CHARACTERS']:
            return "ERROR_MAX_CHARACTERS"
        iteration = 0
        while True and iteration < 50:
            template = random.choice(character_templates)
            template_id = template[0]
            if not any(char[2] == template_id for char in liste_personnages):
                break
            iteration += 1
        if iteration > 49:
            logger.error(f"Le joueur {user_name} ({user_discord_id}) n'a pas pu invoquer de personnage de rareté {rarity}.")
            return "ERROR_NO_CHARACTER"
        template_id = template[0]
        template_name = template[1]
        new_character = self.create_character(user_discord_id,user_name, template_id)
        logger.info(f"Le joueur {user_name} ({user_discord_id}) a invoqué {template_name} [{rarity}] (id : {template_id}) (character Id : {new_character}) . Tickets restants : {tickets}. " + ("Invocation spéciale." if special else ""))
        self.update_tickets(user_discord_id, tickets)
        if special:
            self.update_special_invocation(user_discord_id, False)
        return [template, self.get_character(new_character)]
    
    def fakeTeam(self, user_discord_id):
        # Donne Gojo, Sasuke et All Might
        goku = self.get_character_template_by_name(user_discord_id, "Bot", "Goku")
        sasuke = self.get_character_template_by_name(user_discord_id, "Bot", "Sasuke")
        allmight = self.get_character_template_by_name(user_discord_id, "Bot", "All Might")
        self.create_character(user_discord_id, "Bot", goku[0])
        self.create_character(user_discord_id, "Bot", sasuke[0])
        self.create_character(user_discord_id, "Bot", allmight[0])

        
    def inventaire(self, user_discord_id, user_name):
        # Retourne l'inventaire de l'utilisateur avec les statistiques des personnages en fonction du niveau
        logger.info(f"Récupération de l'inventaire de {user_name} ({user_discord_id}).")
        rarity_order = {'Z': 0,'X': 0.5, 'SS': 1, 'S': 2, 'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7, 'F': 8}

        # Utiliser une clause CASE pour attribuer un poids à chaque rareté
        case_statement = "CASE"
        for rarity, weight in rarity_order.items():
            case_statement += f" WHEN t.rarity = '{rarity}' THEN {weight}"
        case_statement += " END AS rarity_weight"

        # Utiliser la clause ORDER BY avec la colonne de poids nouvellement créée
        query = f"""
            SELECT *, {case_statement}
            FROM characters c 
            JOIN character_templates t ON c.template_id = t.template_id 
            WHERE user_discord_id = {user_discord_id} 
            ORDER BY rarity_weight
        """

        self.cur.execute(query)

        characters = self.cur.fetchall()
        # Ajout des stats 
        characters = [self.get_character_with_stats(character) for character in characters]
        return characters
    
    def check_user(self, user_discord_id):
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone() is not None
    
    def get_team(self, user_discord_id, user_name):
        logger.info(f"Récupération de l'équipe de {user_name} ({user_discord_id}).")
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        user = self.cur.fetchone()
        team = [user[5], user[6], user[7]]
        for i in range(len(team)):
            if team[i] is not None:
                team[i] = self.get_character(team[i])

        # Calcul des statistiques de l'équipe
        stats = {'HP': 0, 'ATK': 0, 'DEF': 0}
        for char in team:
            if char is not None:
                stats['HP'] += int(char[9])
                stats['ATK'] += int(char[10])
                stats['DEF'] += int(char[11])

        # Calcul des synergies et leurs nombres
        synergies = {}
        for char in team:
            if char is not None:
                for synergy in self.get_synergies_by_character_template(char[2]):
                    if synergy[1] not in synergies:
                        synergies[synergy[1]] = 1
                    else:
                        synergies[synergy[1]] += 1
        
        # Calcul des boosts des synergies et application sur les statistiques
        bonus = {'HP': 0, 'ATK': 0, 'DEF': 0}
        noms_synergies = []
        for synergy_id, synergy_nb in synergies.items(): # On parcourt les synergies et leur nombre
            if synergy_nb < 2: # On ne prend pas en compte les synergies où il n'y a pas au moins 2 personnages
                continue
            noms_synergies.append(self.get_synergy(synergy_id)[1]) # On ajoute le nom de la synergie
            synergy = self.get_synergy(synergy_id) # On récupère la synergie
            if synergy[2] == 'HP':
                bonus['HP'] += int(synergy[3] * synergy_nb * stats['HP'])
            elif synergy[2] == 'ATK':
                bonus['ATK'] += int(synergy[3] * synergy_nb * stats['ATK'])
            elif synergy[2] == 'DEF':
                bonus['DEF'] += int(synergy[3] * synergy_nb * stats['DEF'])
        stats['HP'] += bonus['HP']; stats['ATK'] += bonus['ATK']; stats['DEF'] += bonus['DEF']
        
        team = {'team': team, 'stats': stats, 'synergies': noms_synergies, 'bonus': bonus}
        return team
    
    def simulation_stats_team(self,team, isRealData = False):
        stats = {'HP': 0, 'ATK': 0, 'DEF': 0}
        if isRealData:
            for char in team:
                if char is not None:
                    stats['HP'] += int(char[9]) + self.get_current_xp_and_level(char[0])[1]
                    stats['ATK'] += int(char[10]) + self.get_current_xp_and_level(char[0])[1]
                    stats['DEF'] += int(char[11]) + self.get_current_xp_and_level(char[0])[1]
        else:
            for char in team:
                if char is not None:
                    stats['HP'] += int(char[4]) 
                    stats['ATK'] += int(char[5])
                    stats['DEF'] += int(char[6])

        # Calcul des synergies et leurs nombres
        synergies = {}
        for char in team:
            if char is not None:
                if isRealData:
                    for synergy in self.get_synergies_by_character_template(char[5]):
                        if synergy[1] not in synergies:
                            synergies[synergy[1]] = 1
                        else:
                            synergies[synergy[1]] += 1
                else:
                    for synergy in self.get_synergies_by_character_template(char[0]):
                        if synergy[1] not in synergies:
                            synergies[synergy[1]] = 1
                        else:
                            synergies[synergy[1]] += 1
        
        # Calcul des boosts des synergies et application sur les statistiques
        bonus = {'HP': 0, 'ATK': 0, 'DEF': 0}
        noms_synergies = []
        for synergy_id, synergy_nb in synergies.items(): # On parcourt les synergies et leur nombre
            if synergy_nb < 2:
                continue
            noms_synergies.append(self.get_synergy(synergy_id)[1]) # On ajoute le nom de la synergie
            synergy = self.get_synergy(synergy_id)
            if synergy[2] == 'HP':
                bonus['HP'] += int(synergy[3] * synergy_nb * stats['HP'])
            elif synergy[2] == 'ATK':
                bonus['ATK'] += int(synergy[3] * synergy_nb * stats['ATK'])
            elif synergy[2] == 'DEF':
                bonus['DEF'] += int(synergy[3] * synergy_nb * stats['DEF'])
        stats['HP'] += bonus['HP']; stats['ATK'] += bonus['ATK']; stats['DEF'] += bonus['DEF']
        
        team = {'team': team, 'stats': stats, 'synergies': noms_synergies, 'bonus': bonus}
        return team
    
    
    def get_character_by_name_and_user(self, user_discord_id, user_name, char_name):
        logger.info(f"Récupération du personnage {char_name} pour l'utilisateur {user_name} ({user_discord_id}).")
        self.cur.execute(f"SELECT * FROM characters c JOIN character_templates t ON c.template_id = t.template_id WHERE user_discord_id = {user_discord_id} AND t.name LIKE('{char_name}')") # TODO : Ajout surnom
        return self.cur.fetchone()
    
    def get_technique_by_name_and_character(self,name,nom_personnage):
        # On fait une requete croisé entre les techniques et les personnages
        # On retourne la technique qui a le nom et le nom personnage
        self.cur.execute(f"SELECT * FROM character_template_techniques t JOIN character_templates c ON t.template_id = c.template_id WHERE t.name = '{name}' AND c.name = '{nom_personnage}'")
        return self.cur.fetchone()
    
    def get_technique_by_name(self, name):
        self.cur.execute(f"SELECT * FROM character_template_techniques")
        techniques = self.cur.fetchall()
        # On cherche d'abord le nom exact
        for technique in techniques:
            if technique[2].lower() == name.lower():
                return technique
            # On cherche ensuite si le nom est proche
            if Levenshtein.distance(technique[2].lower(), name.lower()) <= 1:
                return technique
            # On cherche ensuite si le nom est dans le nom de la technique
            if name.lower() in technique[2].lower():
                return technique
        return None
    
    def set_team(self, user_discord_id, user_name, char_id, slot):
        logger.info(f"Modification de l'équipe de {user_name} ({user_discord_id}), slot {slot}, character id {char_id}.")
        slot = ['character_slot_one', 'character_slot_two', 'character_slot_three'][slot-1]
        self.cur.execute(f"UPDATE users SET {slot} = {char_id} WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        return True
    
    def check_character_in_team(self, user_discord_id, char_id):
        
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        user = self.cur.fetchone()
        if char_id in user[5:8]:
            return True
        return False
    
    def sell_character(self, user_discord_id, user_name, char_id):
        logger.info(f"Vente du personnage {char_id} pour l'utilisateur {user_name} ({user_discord_id}).")
        rarity = self.get_character(char_id)[7]
        xp = CONSTANTS['RARITY_XP'][rarity]
        self.ajouter_niveau_team(user_discord_id, xp)
        self.delete_character(char_id)
        # On ajoute de l'xp grâce à la constantes RARITY_XP


        return True
    
    def get_synergies(self):
        self.cur.execute("SELECT * FROM synergies")
        return self.cur.fetchall()
    
    def get_synergy(self, synergy_id):
        self.cur.execute(f"SELECT * FROM synergies WHERE synergy_id = {synergy_id}")
        return self.cur.fetchone()
    
    def nameFinder(self, name):
        self.cur.execute(f"SELECT * FROM character_templates WHERE name LIKE '%{name}%'")
        return self.cur.fetchall()

    def get_synergies_by_character_template(self, template_id):
        self.cur.execute(f"SELECT * FROM character_template_synergies s JOIN synergies sy ON s.synergy_id = sy.synergy_id WHERE template_id = {template_id}")
        return self.cur.fetchall()
        
    def save_gif_from_url(self,url, output_file):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
                print("GIF enregistré avec succès sous:", output_file)
            else:
                print("La requête a échoué avec le code:", response.status_code)
        except Exception as e:
            print("Une erreur s'est produite lors de l'enregistrement du GIF:", str(e))

    def create_character_templates(self):
        for univers in all_characters_templates:
            self.cur.executemany(''' 
            INSERT INTO character_templates (name, rarity, image_url, base_hp, base_attack, base_defense) VALUES (?, ?, ?, ?, ?, ?)
            ''', all_characters_templates[univers])
        self.conn.commit()
        logger.success("Les templates de personnages ont été ajoutés à la base de données.")

    def create_synergies(self):
        self.cur.executemany('''
        INSERT INTO synergies (synergy_id, name, type_of_boost, force_of_boost, description, image_url, color) VALUES (?, ?, ?, ?, ?, ?, ?) 
        ''', all_synergies)
        self.conn.commit()
        logger.success("Les synergies ont été ajoutées à la base de données.")
    
    def create_link_synergies(self):
        for synergy_id, characters in all_link_synergies.items():
            for character in characters:
                char = self.get_character_template_by_name(0, "Bot", character)
                if char is None:
                    continue
                char_id = char[0]
                # print(char_id, synergy_id)
                self.cur.execute(f"INSERT INTO character_template_synergies (template_id, synergy_id) VALUES ({char_id}, {synergy_id})")
        self.conn.commit()
        logger.success("Les liens de synergies ont été ajoutés à la base de données.")
        
    def create_techniques(self, verbose=False):
        for character, techniques in all_techniques.items():
            if verbose:
                logger.info(f"Ajout des techniques pour le personnage {character}.")
                logger.info(techniques)
            for technique in techniques:
                self.cur.execute(f"INSERT INTO character_template_techniques (template_id, name, phrase, image_url, color) VALUES ({self.getIdFromName(character)}, '{technique[0]}', '{technique[1]}', '{technique[2]}', '{technique[3]}')")
                if verbose:
                    logger.info(f"La technique {technique[0]} a été ajoutée pour le personnage {character}.")
        self.conn.commit()
        logger.success("Les techniques ont été ajoutées à la base de données.")

    def createAllDatas(self):
        self.create_character_templates()
        self.create_synergies()
        self.create_link_synergies()
        self.create_techniques(True)
        self.conn.commit()
        logger.success("Toutes les données ont été ajoutées à la base de données.")

    def reset(self,verbose=False):
        self.cur.execute("DROP TABLE IF EXISTS users")
        self.cur.execute("DROP TABLE IF EXISTS characters")
        self.cur.execute("DROP TABLE IF EXISTS character_templates")
        self.cur.execute("DROP TABLE IF EXISTS synergies")
        self.cur.execute("DROP TABLE IF EXISTS character_template_synergies")
        self.cur.execute("DROP TABLE IF EXISTS user_choices")
        self.cur.execute("DROP TABLE IF EXISTS character_template_techniques")
        self.conn.commit()
        self.create_tables()

        self.createAllDatas()
        self.equilibrer_synergies()
        if verbose:
            logger.info("Les tables ont été supprimées.")

    def resetCharactersTemplatesAndSynergies(self):
        self.cur.execute("DROP TABLE IF EXISTS character_templates")
        self.cur.execute("DROP TABLE IF EXISTS synergies")
        self.cur.execute("DROP TABLE IF EXISTS character_template_synergies")
        self.cur.execute("DROP TABLE IF EXISTS character_template_techniques")
        self.conn.commit()
        self.create_character_template_table()
        self.create_synergy_table()
        self.create_character_template_synergy_table()
        self.create_character_template_technique_table()
        self.createAllDatas()
        logger.success("Les tables des personnages et des synergies ont été réinitialisées.")
        
    def createGifsFromDatabase(self):
        self.cur.execute("SELECT * FROM character_templates")
        characters = self.cur.fetchall()
        for character in characters:
            self.save_gif_from_url(character[3], f"assets/gifs/{character[0]}.gif")
        logger.info("Les GIFs ont été enregistrés.")
    
    def getIdFromName(self,name):
        # Retourne l'id du personnage à partir de son nom si il existe, sinon None
        template = self.get_character_template_by_name(0, "Bot", name)
        # logger.info(f"Récupération de l'id du personnage {name}.")
        # logger.info(template)
        if template is None:
            return None
        return template[0]
        
    def getPower(self, user_discord_id):
        # On récupère les personnages de l'utilisateur
        characters = self.get_characters(user_discord_id)
        power = 0
        for character in characters:
            rarity = character[7]
            level = character[3]
            power += (CONSTANTS['RARITY_POWER'][rarity] + level)
        return power
    
    def getClassement(self, guildMembers):
        # On sélectionne les joueurs qui sont sur le serveur Discord de l'utilisateur
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id IN ({','.join(str(member.id) for member in guildMembers)})")
        users = self.cur.fetchall()
        classement = []
        for users in users:
            classement.append([users[1],self.getPower(users[1])])
        classement.sort(key=lambda x: x[1], reverse=True)
        return classement

    # Mode histoire
    
    def getUser(self, user_discord_id):
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone()

    def updateNiveauHistoire(self, user_discord_id, niveau):
        self.cur.execute(f"UPDATE users SET histoireLevel = {niveau} WHERE user_discord_id = {user_discord_id}")
        logger.info(f"Le niveau d'histoire de l'utilisateur {user_discord_id} a été mis à jour à {niveau}.")
        self.conn.commit()

    def get_character_template_by_rarity(self, rarity):
        self.cur.execute(f"SELECT * FROM character_templates WHERE rarity = '{rarity}'")
        return self.cur.fetchone()
    
    def setLevel(self, user_discord_id, level):
        self.cur.execute(f"UPDATE users SET histoireLevel = {level} WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        logger.info(f"Le niveau d'histoire de l'utilisateur {user_discord_id} a été mis à jour à {level}.")
        
    def getAllCharactersFromUniversName(self, univers_name):
        for univers in all_characters_templates:
            if univers_name.lower() in univers.lower():
                return all_characters_templates[univers]
            
    def get_attaques_by_character_name(self, name):
        identifiant = self.getIdFromName(name)
        if identifiant is None:
            return None
        self.cur.execute(f"SELECT * FROM character_template_techniques WHERE template_id = {identifiant}")
        return self.cur.fetchall()
    
    def get_synergie_equilibrage(self, id, verbose=False):
        self.cur.execute(f"SELECT * FROM character_template_synergies c LEFT JOIN character_templates ct ON c.template_id = ct.template_id WHERE synergy_id = {id}")
        base_rate = 120 # De base, le multiplicateur d'une synergie est de 1
        characters = self.cur.fetchall()
        taux_de_baisse = {'Z' : 8,'X' : 8, 'SS' : 6.75, 'S' : 6, 'A' : 5.5, 'B' : 5, 'C' : 4, 'D' : 3.5, 'E' : 2, 'F' : 1}
        synergie = self.get_synergy(id)
        if synergie is None:
            return None
        for character in characters:
            rarete = character[4]
            base_rate -= taux_de_baisse[rarete]
            if verbose:
                print(f"Le personnage {character[3]}[{rarete}] et fait passer le taux de {base_rate + taux_de_baisse[rarete]} à {base_rate}.")
        final_base_rate = max(20, base_rate) / 100
        print(f"La synergie {synergie[1]} a un taux de {final_base_rate}.") if verbose else None
        return final_base_rate

    def set_equilibre_synergy(self, id, rate,verbose=False):
        self.cur.execute(f"UPDATE synergies SET force_of_boost = {rate} WHERE synergy_id = {id}")
        self.conn.commit()
        logger.info(f"La synergie {self.get_synergy(id)[1]} a été mise à jour avec un taux de {rate}.") if verbose else None

    def equilibrer_synergies(self):
        # on recupere toutes les synergies
        self.cur.execute(f"SELECT * FROM synergies")
        synergies = self.cur.fetchall()
        for synergy in synergies:
            equilibrage = self.get_synergie_equilibrage(synergy[0],False)
            if equilibrage is not None:
                self.set_equilibre_synergy(synergy[0],equilibrage, True)
        logger.success("Toutes les synergies ont été équilibrées.")

    def get_all_techniques(self):
        self.cur.execute("SELECT * FROM character_template_techniques")
        return self.cur.fetchall()
    
    def get_techniques(self, template_id):
        self.cur.execute(f"SELECT * FROM character_template_techniques WHERE template_id = {template_id}")
        return self.cur.fetchall()
    
    def remplacer_url_image_character_templates(self):
        self.cur.execute("SELECT * FROM character_templates")
        characters = self.cur.fetchall()
        liste_fixe = all_characters_templates
        for univers in liste_fixe:
            for character in liste_fixe[univers]:
                character_in_database = self.get_character_template_by_name(0, "Bot", character[0])
                if character_in_database is not None:
                    if character_in_database[3] != character[2]:    
                        self.cur.execute(f"UPDATE character_templates SET image_url = '{character[2]}' WHERE template_id = {character_in_database[0]}")
                        logger.info(f"L'image du personnage {character[0]} a été mise à jour.")
        self.conn.commit()
        logger.success("Les URLs des images des personnages ont été mises à jour.")
    
    def remplacer_url_image_synergies(self):
        self.cur.execute("SELECT * FROM synergies")
        synergies = self.cur.fetchall()
        for synergy in synergies:
            for synergie in all_synergies:
                if synergy[1] == synergie[1]:
                    if synergy[5] != synergie[5] and synergie[5] not in ['https://i.imgur.com/I5FU4lB.png','https://i.imgur.com/H9CetGc.png','https://i.imgur.com/wqFQ0by.png','https://i.imgur.com/BOcSeri.png']:
                        self.cur.execute(f"UPDATE synergies SET image_url = '{synergie[5]}' WHERE synergy_id = {synergy[0]}")
                        logger.info(f"L'image de la synergie {synergy[1]} a été mise à jour.")
        self.conn.commit()
        logger.success("Les URLs des images des synergies ont été mises à jour.")

    def remplacer_url_image_techniques(self):
        self.cur.execute("SELECT * FROM character_template_techniques")
        techniques = self.cur.fetchall()
        for technique in techniques:
            for technique_data in all_techniques:
                if technique[2] == technique_data[0]:
                    if technique[4] != technique_data[2]:
                        self.cur.execute(f"UPDATE character_template_techniques SET image_url = '{technique_data[2]}' WHERE technique_id = {technique[0]}")
                        logger.info(f"L'image de la technique {technique[2]} a été mise à jour.")
        self.conn.commit()
        logger.success("Les URLs des images des techniques ont été mises à jour.")

    def remplacer_toutes_les_urls(self):
        self.remplacer_url_image_character_templates()
        self.remplacer_url_image_synergies()
        self.remplacer_url_image_techniques()

    def get_last_auto_team_time(self, user_discord_id):
        self.cur.execute(f"SELECT last_time_auto_team FROM users WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone()[0]
    
    def get_nb_techniques(self, template_id):
        self.cur.execute(f"SELECT COUNT(*) FROM character_template_techniques WHERE template_id = {template_id}")
        return self.cur.fetchone()[0]
    
    def insert_technique(self, technique,nom):
        identifiant = self.get_character_template_by_name(0, "Bot", nom)[0]
        self.cur.execute(f"INSERT INTO character_template_techniques (template_id, name, phrase, image_url, color) VALUES ({identifiant}, '{technique[0]}', '{technique[1]}', '{technique[2]}', '{technique[3]}')")
        self.conn.commit()
        logger.success(f"La technique {technique[1]} a été ajoutée pour le personnage {technique[0]}.")
    
    def remake_techniques(self):
        self.cur.execute("DROP TABLE IF EXISTS character_template_techniques")
        self.create_character_template_technique_table()
        self.create_techniques()
        logger.success("Les techniques ont été réinitialisées.")