# Import the required modules
import discord
from discord.ext import commands 
from constantes import CONSTANTS
import getToken
import bdd
from loguru import logger

# Connect to database
database = bdd.Database('./mousse.db')

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    logger.info(f'{bot.user} est bien connecté!')
    database.create_tables()
    

@bot.event
async def on_message(message):
    contenu = message.content
    auteur = message.author
    if auteur == bot.user: # Check if the message is from the bot
        return
    if not(contenu.startswith('!')) :
        return
    database.insert_user(auteur.id, auteur.name)
    if contenu.startswith('!tickets'):
        await getTickets(message)
    elif contenu.startswith('!daily'):
        await claimDaily(message)
    elif contenu.startswith('!admin'):
        await admin(message)
    elif contenu.startswith('!list_command') or contenu.startswith('!help'):
        await list_command(message)
    elif contenu.startswith('!invo') or contenu.startswith('!sum'):
        await invocation(message)
    elif contenu.startswith('!inv') or contenu.startswith('!pers') or contenu.startswith('!bag'):
        await inventaire(message)
    elif contenu.startswith('!givetickets') or contenu.startswith('!donnertickets') or contenu.startswith('!donnerticket') or contenu.startswith('!giveticket') or contenu.startswith('!give_tickets') or contenu.startswith('!donner_tickets') or contenu.startswith('!donner_ticket') or contenu.startswith('!give_ticket'):
        await giveTicket(message)
    elif contenu.startswith('!info '):
        await info(message)
    elif contenu.startswith('!team') or contenu.startswith('!voirteam') or contenu.startswith('!voir_team') or contenu.startswith('!voir_team'):
        await voirTeam(message)
    elif contenu.startswith('!ajouterteam') or contenu.startswith('!addteam') or contenu.startswith('!add_team') or contenu.startswith('!ajouter_team'):
        await ajouterTeam(message)
    elif contenu.startswith('!sell') or contenu.startswith('!vendre'):
        await sell(message)


# Fonctions

@bot.command()
async def list_command(message):
    logger.info(f"Commande !list_command appelée par {message.author.name} ({message.author.id}).")
    commandes = ['!tickets', '!daily', '!admin', '!invocation', '!inventaire', '!givetickets', '!info','!team', '!addteam', '!sell']
    response = "Liste des commandes disponibles:\n"
    for commande in commandes:
        response += f"{commande}\n"
    await message.channel.send(response)

@bot.command()
async def getTickets(message):
    logger.info(f"Commande !tickets appelée par {message.author.name} ({message.author.id}).")
    user = await fetch_user_from_message(message, 2)
    if not user:
        response = "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!"
        await message.channel.send(response)
        return
    if user == "ERROR_SYNTAX":
        response = "La commande doit être de la forme !tickets ou !tickets <joueur>!"
        await message.channel.send(response)
        return
    print(user)
    tickets = database.get_tickets(user.id)
    response = f"{user.name} a {tickets} tickets!"
    await message.channel.send(response)

@bot.command()
async def claimDaily(message):
    user = message.author
    claim = database.claim_daily(user.id, user.name)
    if claim[0]:
        response = f"Récompense journalière réclamée avec succès!, vous avez maintenant {claim[1]} tickets!"
    elif not(claim[0]):
        temps_restant = claim[1]
        temps_restant_heures = temps_restant.seconds//3600
        temps_restant_minutes = (temps_restant.seconds//60)%60
        response = f"Vous avez déjà réclamé votre récompense journalière!\n Vous pouvez réclamer une nouvelle récompense dans {temps_restant_heures} heures et {temps_restant_minutes} minutes."
    await message.channel.send(response)

@bot.command()
async def admin(message):
    liste_templates = database.get_character_templates()
    response = "Liste des templates de personnages:\n"
    for template in liste_templates:
        response += f"{template[0]} - {template[1]}\n"
    await message.channel.send(response)

@bot.command()
async def invocation(message):
    # On vérifie si l'utilisateur a assez de tickets
    tickets = database.get_tickets(message.author.id)
    if tickets < CONSTANTS['INVOCATION_COST']:
        response = "Vous n'avez pas assez de tickets pour invoquer un personnage!"
        await message.channel.send(response)
        return
    donnees = database.summon_character(message.author.id, message.author.name)
    # SI la données est de type String, c'est une erreur
    if type(donnees) == str:
        if donnees == "ERROR_NO_CHARACTER":
            response = "Aucun personnage n'a été trouvé pour l'invocation!"
            await message.channel.send(response)
        if donnees == "ERROR_MAX_CHARACTERS":
            response = "Vous avez atteint le nombre maximum de personnages!\nVeuillez enlever un personnage de votre inventaire!"
            await message.channel.send(response)
        return
    template = donnees[0]
    character = donnees[1]
    response = f"Vous avez invoqué {template[1]} de type {template[2]}!{template[3]}\ntickets restants : {tickets-CONSTANTS['INVOCATION_COST']}\nSTATS: HP: {str(template[4])} ATK: {str(template[5])} DEF: {str(template[6])} LEVEL: {str(character[3])} XP: {str(character[4])}\n"
    await message.channel.send(response)

@bot.command()
async def inventaire(message):
    logger.info(f"Commande !inventaire appelée par {message.author.name} ({message.author.id}).")
    characters = database.inventaire(message.author.id, message.author.name)
    if characters == None or len(characters) == 0:
        response = "Votre inventaire est vide!"
        await message.channel.send(response)
        return
    
    response = f"Voici votre inventaire, {message.author.name}:\n"
    for character in characters:
        response += f"{character[6]} [{character[7]}] - Lv{character[3]}\n"
    await message.channel.send(response)

@bot.command()
async def giveTicket(message):
    # Fonction qui permet à un joueur A de donner x tickets à un joueur B
    contenu = message.content
    if len(contenu.split(' ')) != 3:
        response = "La commande doit être de la forme !givetickets <destinataire> <montant>!"
        await message.channel.send(response)
        return
    auteur = message.author
    montant = contenu.split(' ')[2]
    destinataire = contenu.split(' ')[1]
    destinataire = idDiscordToInt(destinataire)
    if destinataire == None:
        response = "Le destinataire n'est pas valide!"
        await message.channel.send(response)
        return
    if not montant.isdigit():
        response = "Le nombre de ticket doit être un nombre!"
        await message.channel.send(response)
        return
    montant = int(montant)
    if montant < 0:
        response = "Le nombre de ticket doit être positif!"
        await message.channel.send(response)
        return
    tickets = database.get_tickets(auteur.id)
    if tickets < montant:
        response = "Vous n'avez pas assez de tickets!"
        await message.channel.send(response)
        return
    if destinataire == auteur.id:
        response = "Vous ne pouvez pas vous donner des tickets à vous-même!"
        await message.channel.send(response)
        return
    # Vérfication de l'existence du destinataire
    if not database.check_user(destinataire):
        response = "Le destinataire n'a pas encore joué au jeu!"
        await message.channel.send(response)
        return
    database.update_tickets(auteur.id, tickets - montant)
    tickets = database.get_tickets(destinataire)
    database.update_tickets(destinataire, tickets + montant)
    logger.info(f"L'utilisateur {auteur.name} ({auteur.id}) a donné {montant} tickets à {destinataire}.")
    response = f"Vous avez donné {montant} tickets à <@{destinataire}>!"
    await message.channel.send(response)
    
def idDiscordToInt(idDiscord):
    try:
        return int(idDiscord.replace('<@', '').replace('>', ''))
    except ValueError:
        logger.error(f"Impossible de convertir {idDiscord} en entier.")
        return None

@bot.command()
async def info(message):
    # Permet d'obtenir les informations d'un personnage
    contenu = message.content
    if len(contenu.split(' ')) != 2:
        response = "La commande doit être de la forme !info <nom personnage>!"
        await message.channel.send(response)
        return
    nom = contenu.split(' ')[1]
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        response = "Ce personnage n'existe pas!"
        await message.channel.send(response)
        return
    response = f"Voici les informations sur {nom}:\n"
    response += f"Nom: {character[1]}\nType: {character[2]}\nHP: {character[4]}\nATK: {character[5]}\nDEF: {character[6]}\nIMAGE: {character[3]}\n"
    await message.channel.send(response)

@bot.command()
async def voirTeam(message):
    # Permet de voir ses personnages équipés en teams, ou la team d'un autre joueur
    user = await fetch_user_from_message(message, 2)
    if not user:
        response = "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!"
        await message.channel.send(response)
        return
    if user == "ERROR_SYNTAX":
        response = "La commande doit être de la forme !voirteam ou !voirteam <joueur>!"
        await message.channel.send(response)
        return
    personnages = database.get_team(user.id, user.name)
    response = "Voici la team de " + user.name + ":\n"
    for personnage in personnages:
        if personnage == None:
            response += "Emplacement vide\n"
            continue
        response += f"{personnage[6]} [{personnage[7]}] - Lv{personnage[3]}\n"
    await message.channel.send(response)

@bot.command()
async def ajouterTeam(message):
    # Permet d'ajouter un personnage à son équipe
    contenu = message.content
    if len(contenu.split(' ')) != 3:
        response = "La commande doit être de la forme !ajouterteam <1 | 2 | 3> <nom personnage>!"
        await message.channel.send(response)
        return
    nom = contenu.split(' ')[2]
    position = contenu.split(' ')[1]
    if not position.isdigit():
        response = "La position doit être un nombre!"
        await message.channel.send(response)
        return
    position = int(position)
    if position < 1 or position > 3:
        response = "La position doit être 1, 2 ou 3!"
        await message.channel.send(response)
        return
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)
    if character == None:
        response = "Ce personnage n'existe pas!"
        await message.channel.send(response)
        return
    if database.check_character_in_team(message.author.id, character[0]):
        response = "Ce personnage est déjà dans votre équipe!"
        await message.channel.send(response)
        return
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a ajouté {nom} à sa team en position {str(position)}.")

    database.set_team(message.author.id, message.author.name, character[0], position)
    response = f"Vous avez ajouté {nom} à votre équipe dans l'emplacement {position}! Vous pouvez voir votre équipe avec la commande !team."
    await message.channel.send(response)

async def fetch_user_from_message(message, nombre_arguments_max=2):
    # Permet de récupérer un utilisateur à partir d'un message
    try:
        parts = message.content.split(' ')
        print(parts, len(parts))
        if len(parts) > nombre_arguments_max:
            logger.error(f"Erreur de syntaxe dans fetch_user_from_message appelée par {message.author.name} ({message.author.id}).")
            return "ERROR_SYNTAX"
        if len(parts) > 1:
            id_discord = parts[1].replace('<@', '').replace('>', '')  # Nettoie la mention
            user = await message.guild.fetch_member(int(id_discord))
            if not database.check_user(user.id):
                return False
            return user
    except ValueError:
        return False
    return message.author

@bot.command()
async def sell(message):
    # Permet de vendre un personnage
    contenu = message.content
    if len(contenu.split(' ')) != 2:
        response = "La commande doit être de la forme !sell <nom personnage>!"
        await message.channel.send(response)
        return
    nom = contenu.split(' ')[1]
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)
    if character == None:
        response = "Ce personnage n'existe pas!"
        await message.channel.send(response)
        return
    nom = character[6]
    rarity = str(character[7])
    tickets_obtenus = CONSTANTS['RARITY_PRICE'][rarity]
    # Demandez confirmation
    response = f"Êtes vous sûr de vouloir vendre {nom} [{rarity}] pour {tickets_obtenus} tickets? (Oui/Non)"
    await message.channel.send(response)
    def check(m):
        return m.author == message.author and m.channel == message.channel
    try:
        msg = await bot.wait_for('message', check=check, timeout=20)
    except:
        response = "Temps écoulé, vente annulée!"
        await message.channel.send(response)
        return
    if msg.content.lower() != "oui":
        response = "Vente annulée!"
        await message.channel.send(response)
        return

    database.sell_character(message.author.id,message.author.name, character[0])
    database.update_tickets(message.author.id, database.get_tickets(message.author.id) + tickets_obtenus)
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a vendu {nom} pour {rarity} tickets.")
    response = f"Vous avez vendu {nom} pour {tickets_obtenus} tickets!"
    await message.channel.send(response)



# Run the bot with the token
bot.run(getToken.getToken())