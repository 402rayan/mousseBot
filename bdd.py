import sqlite3
from loguru import logger
from datetime import datetime, timedelta

from constantes import CONSTANTS

# Configurer Loguru pour écrire les logs dans un fichier
logger.add("mon_fichier_log.log", rotation="100 MB")  # Rotation du fichier après 100 MB

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
            last_claim DATETIME
        )
        ''')
        self.conn.commit()

    def create_character_template_table(self):
        # Create table for character templates
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS character_templates (
            template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            base_rank TEXT,
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
            user_id INTEGER,
            template_id INTEGER,
            level INTEGER DEFAULT 1,
            experience INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (template_id) REFERENCES character_templates (template_id)
        )
        ''')
        self.conn.commit()

    def create_tables(self):
        self.create_user_table()
        self.create_character_template_table()
        self.create_character_table()
        self.conn.commit()
        logger.info("Les tables ont été créées.")
        
    def insert_user(self, user_discord_id, user_name):
        #On vérifie si l'utilisateur existe déjà
        logger.info(f"Vérification de l'utilisateur {user_name} dans la base de données.")
        self.cur.execute(f"SELECT * FROM users WHERE user_discord_id = {user_discord_id}")
        user = self.cur.fetchone()
        if user is None:
            self.cur.execute(f"INSERT INTO users (user_discord_id, user_name) VALUES ({user_discord_id}, '{user_name}')")
            self.conn.commit()
            logger.info(f"L'utilisateur {user_name} a été inscrit dans la base de données.")
        else:
            logger.info(f"L'utilisateur {user_name} existe déjà dans la base de données.")

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
                logger.info(f"L'utilisateur {user_name} a déjà réclamé son daily.")
                remaining_time = last_claim + timedelta(days=1) - datetime.now()
                return [False, remaining_time]
        # On ajoute les tickets
        tickets = self.get_tickets(user_discord_id)
        tickets += CONSTANTS['DAILY_TICKETS']
        self.update_tickets(user_discord_id, tickets)
        # On met à jour la date de réclamation
        self.cur.execute(f"UPDATE users SET last_claim = '{datetime.now()}' WHERE user_discord_id = {user_discord_id}")
        self.conn.commit()
        logger.info(f"L'utilisateur {user_name} a réclamé son daily. Il a maintenant {tickets} tickets.")
        return [True, tickets]
        
        