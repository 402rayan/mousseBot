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
    if contenu.startswith('!daily'):
        await claimDaily(message)
    if contenu.startswith('!admin'):
        await admin(message)
    if contenu.startswith('!list_command') or contenu.startswith('!help'):
        await list_command(message)
    if contenu.startswith('!invoc') or contenu.startswith('!invoq') :
        await invocation(message)
    if contenu.startswith('!inv') or contenu.startswith('!pers'):
        await inventaire(message)

# Fonctions

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !tickets \n !daily \n '
    await ctx.send(response)

@bot.command()
async def getTickets(message):
    user = message.author
    tickets = database.get_tickets(user.id)
    response = f'You have {tickets} tickets!'
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
    characters = database.inventaire(message.author.id, message.author.name)
    response = f"Voici votre inventaire, {message.author.name}:\n"
    for character in characters:
        response += f"{character[6]} [{character[7]}] - Lv{character[3]}\n"
    await message.channel.send(response)

# Run the bot with the token
bot.run(getToken.getToken())