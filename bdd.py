import random
import shutil
import sqlite3
from loguru import logger
from datetime import datetime, timedelta

import requests

from constantes import CONSTANTS
from datas import all_characters_templates, all_synergies, all_link_synergies
import Levenshtein

# Configurer Loguru pour écrire les logs dans un fichier
logger.add("logs.log", rotation="100 MB")  # Rotation du fichier après 100 MB

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
            lvl1feu BOOLEAN DEFAULT NULL,
            FOREIGN KEY (user_discord_id) REFERENCES users (user_discord_id)
        )
        ''')

    def create_tables(self):
        self.create_user_table()
        self.create_character_template_table()
        self.create_character_table()
        self.create_synergy_table()
        self.create_character_template_synergy_table()
        self.crate_user_choices()
        self.conn.commit()
        logger.info("Les tables ont été créées.")
        
    def insert_user(self, user_discord_id, user_name):
        #On vérifie si l'utilisateur existe déjà
        logger.info(f"Vérification de l'utilisateur {user_name} ({user_discord_id}) dans la base de données.")
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        user = self.cur.fetchone()
        if user is None:
            self.cur.execute(f"INSERT INTO users (user_discord_id, user_name, tickets) VALUES ({user_discord_id}, '{user_name}', 10)")
            # On l'insère aussi dans la table des choix
            self.cur.execute(f"INSERT INTO user_choices (user_discord_id) VALUES ({user_discord_id})")
            self.conn.commit()
            logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a été inscrit dans la base de données.")
        else:
            logger.info(f"L'utilisateur {user_name} ({user_discord_id}) existe déjà dans la base de données.")

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
    
    def claim_daily(self, user_discord_id, user_name):
        # On vérifie si l'utilisateur a déjà réclamé son daily
        last_claim = self.get_last_claim(user_discord_id)
        if last_claim is not None:
            last_claim = datetime.strptime(last_claim, '%Y-%m-%d %H:%M:%S.%f')
            if last_claim.date() == datetime.now().date():
                logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a déjà réclamé son daily.")
                remaining_time = last_claim + timedelta(days=1) - datetime.now()
                return [False, remaining_time]
        # On ajoute les tickets
        tickets = self.get_tickets(user_discord_id)
        tickets += CONSTANTS['DAILY_TICKETS']
        self.update_tickets(user_discord_id, tickets)
        # On met à jour la date de réclamation
        self.cur.execute(f"UPDATE users SET last_claim = '{datetime.now()}' WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        logger.info(f"L'utilisateur {user_name} ({user_discord_id}) a réclamé son daily. Il a maintenant {tickets} tickets.")
        return [True, tickets]
        
    def get_character_templates(self):
        self.cur.execute("SELECT * FROM character_templates")
        return self.cur.fetchall()
    
    def get_character_template(self, template_id):
        self.cur.execute(f"SELECT * FROM character_templates WHERE template_id = {template_id}")
        return self.cur.fetchone()
    
    def get_characters(self, user_discord_id):
        self.cur.execute(f"SELECT * FROM characters c LEFT JOIN character_templates t ON c.template_id = t.template_id LEFT JOIN character_template_synergies s ON t.template_id = s.template_id LEFT JOIN synergies sy ON s.synergy_id = sy.synergy_id WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchall()
    
    def get_character(self, char_id):
        self.cur.execute(f"SELECT * FROM characters c LEFT JOIN character_templates t ON c.template_id = t.template_id LEFT JOIN character_template_synergies s ON t.template_id = s.template_id LEFT JOIN synergies sy ON s.synergy_id = sy.synergy_id WHERE char_id = {char_id}")
        return self.cur.fetchone()
    
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
            print(template[1].lower(), template_name.lower(), Levenshtein.distance(template[1].lower(), template_name.lower()))
            if Levenshtein.distance(template[1].lower(), template_name.lower()) <= 1:
                return template
        # Troisième étape : On vérifie si le nom est dans le nom du template
        for template in all_templates:
            if template_name.lower() in template[1].lower():
                return template
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
        logger.info(f"Un nouveau personnage a été créé pour l'utilisateur {user_name} ({user_discord_id}).")
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
    
    def summon_character(self, user_discord_id, user_name):
        # On réduit le nombre de tickets
        tickets = self.get_tickets(user_discord_id)
        if tickets < CONSTANTS['INVOCATION_COST']:
            return None
        tickets -= CONSTANTS['INVOCATION_COST']
        # On choisit la rareté du personnage invoqué
        rarity = random.choices(list(CONSTANTS['RARITY_CHANCE'].keys()), list(CONSTANTS['RARITY_CHANCE'].values()))[0]
        # On invoque un personnage aléatoire
        character_templates = self.get_character_templates()
        character_templates = [char for char in character_templates if char[2] == rarity]
        liste_personnages = self.get_characters(user_discord_id)
        if len(liste_personnages) >= CONSTANTS['MAX_CHARACTERS']:
            return "ERROR_MAX_CHARACTERS"
        iteration = 0
        while True and iteration < 100:
            template = random.choice(character_templates)
            template_id = template[0]
            if not any(char[2] == template_id for char in liste_personnages):
                break
            iteration += 1
        if iteration == 100:
            return "ERROR_NO_CHARACTER"
        template_id = template[0]
        template_name = template[1]
        new_character = self.create_character(user_discord_id,user_name, template_id)
        logger.info(f"Le joueur {user_name} ({user_discord_id}) a invoqué {template_name}. Il reste {tickets} tickets. Le personnage invoqué a pour id {new_character}. La rareté est {rarity}.")
        self.update_tickets(user_discord_id, tickets)
        return [template, self.get_character(new_character)]
    
    def inventaire(self, user_discord_id, user_name):
        logger.info(f"Récupération de l'inventaire de {user_name} ({user_discord_id}).")
        inventaire = self.get_characters(user_discord_id)
        return inventaire
    
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
    
    def get_character_by_name_and_user(self, user_discord_id, user_name, char_name):
        logger.info(f"Récupération du personnage {char_name} pour l'utilisateur {user_name} ({user_discord_id}).")
        self.cur.execute(f"SELECT * FROM characters c JOIN character_templates t ON c.template_id = t.template_id WHERE user_discord_id = {user_discord_id} AND t.name LIKE('{char_name}')") # TODO : Ajout surnom
        return self.cur.fetchone()
    
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
        self.delete_character(char_id)
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
        self.cur.executemany('''
        INSERT INTO character_templates (name, rarity, image_url, base_hp, base_attack, base_defense) VALUES (?, ?, ?, ?, ?, ?) 
        ''', all_characters_templates)
        self.conn.commit()
        logger.info("Les templates de personnages ont été ajoutés à la base de données.")

    def create_synergies(self):
        self.cur.executemany('''
        INSERT INTO synergies (synergy_id, name, type_of_boost, force_of_boost, description, image_url, color) VALUES (?, ?, ?, ?, ?, ?, ?) 
        ''', all_synergies)
        self.conn.commit()
        logger.info("Les synergies ont été ajoutées à la base de données.")
    
    def create_link_synergies(self):
        for synergy_id, characters in all_link_synergies.items():
            for character in characters:
                char = self.get_character_template_by_name(0, "Bot", character)
                if char is None:
                    continue
                char_id = char[0]
                print(char_id, synergy_id)
                self.cur.execute(f"INSERT INTO character_template_synergies (template_id, synergy_id) VALUES ({char_id}, {synergy_id})")
        self.conn.commit()
        logger.info("Les liens de synergies ont été ajoutés à la base de données.")

    def createAllDatas(self):
        self.create_character_templates()
        self.create_synergies()
        self.create_link_synergies()
        self.conn.commit()
        logger.info("Toutes les données ont été ajoutées à la base de données.")

    def reset(self):
        self.cur.execute("DROP TABLE IF EXISTS users")
        self.cur.execute("DROP TABLE IF EXISTS characters")
        self.cur.execute("DROP TABLE IF EXISTS character_templates")
        self.cur.execute("DROP TABLE IF EXISTS synergies")
        self.cur.execute("DROP TABLE IF EXISTS character_template_synergies")
        self.conn.commit()
        self.create_tables()
        self.createAllDatas()
        logger.info("Les tables ont été supprimées.")

    def createGifsFromDatabase(self):
        self.cur.execute("SELECT * FROM character_templates")
        characters = self.cur.fetchall()
        for character in characters:
            self.save_gif_from_url(character[3], f"assets/gifs/{character[0]}.gif")
        logger.info("Les GIFs ont été enregistrés.")
    
    def getIdFromName(self,name):
        # Retourne l'id du personnage à partir de son nom si il existe, sinon None
        template = self.get_character_template_by_name(0, "Bot", name)
        logger.info(f"Récupération de l'id du personnage {name}.")
        logger.info(template)
        if template is None:
            return None
        return template[0]
        

    # Mode histoire

    def getChoices(self, user_discord_id):
        self.cur.execute(f"SELECT * FROM user_choices WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone()
    
    def getUser(self, user_discord_id):
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        return self.cur.fetchone()

    def updateNiveauHistoire(self, user_discord_id, niveau):
        self.cur.execute(f"UPDATE users SET histoireLevel = {niveau} WHERE user_discord_id = {user_discord_id}")
        logger.info(f"Le niveau d'histoire de l'utilisateur {user_discord_id} a été mis à jour à {niveau}.")
        self.conn.commit()