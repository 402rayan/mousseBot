# Import the required modules
import discord
from discord.ext import commands 
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


# Fonctions

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
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

# Run the bot with the token
bot.run(getToken.getToken())