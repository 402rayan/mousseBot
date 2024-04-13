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
    elif contenu.startswith('!invoc') or contenu.startswith('!invoq') :
        await invocation(message)
    elif contenu.startswith('!inv') or contenu.startswith('!pers'):
        await inventaire(message)
    elif contenu.startswith('!givetickets') or contenu.startswith('!donnertickets') or contenu.startswith('!donnerticket') or contenu.startswith('!giveticket') or contenu.startswith('!give_tickets') or contenu.startswith('!donner_tickets') or contenu.startswith('!donner_ticket') or contenu.startswith('!give_ticket'):
        await giveTicket(message)
    elif contenu.startswith('!info '):
        await info(message)

# Fonctions

@bot.command()
async def list_command(message):
    logger.info(f"Commande !list_command appelée par {message.author.name} ({message.author.id}).")
    commandes = ['!tickets', '!daily', '!admin', '!invocation', '!inventaire', '!givetickets', '!info']
    response = "Liste des commandes disponibles:\n"
    for commande in commandes:
        response += f"{commande}\n"
    await message.channel.send(response)

@bot.command()
async def getTickets(message):
    logger.info(f"Commande !tickets appelée par {message.author.name} ({message.author.id}).")
    user = message.author
    # S'il y a un argument, on vérifie si c'est un utilisateur
    if len(message.content.split(' ')) > 1:
        idDiscord = message.content.split(' ')[1]
        idDiscord = idDiscordToInt(idDiscord)
        if idDiscord == None:
            response = "L'utilisateur n'est pas valide!"
            await message.channel.send(response)
            return
        user = await bot.fetch_user(idDiscord)
    tickets = database.get_tickets(user.id)
    response = f'{user} has {tickets} tickets!'
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
    template = donnees[0]
    character = donnees[1]
    response = f"Vous avez invoqué {template[1]} de type {template[2]}!{template[3]}\ntickets restants : {tickets-CONSTANTS['INVOCATION_COST']}\nSTATS: HP: {str(template[4])} ATK: {str(template[5])} DEF: {str(template[6])} LEVEL: {str(character[3])} XP: {str(character[4])}\n"
    await message.channel.send(response)

@bot.command()
async def inventaire(message):
    logger.info(f"Commande !inventaire appelée par {message.author.name} ({message.author.id}).")
    characters = database.inventaire(message.author.id, message.author.name)
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


# Run the bot with the token
bot.run(getToken.getToken())