# Import the required modules
import discord
from discord.ext import commands 
import getToken

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Je suis connecté sur le bot {bot.user.name}')

@bot.event
async def on_message(message):
    contenu = message.content
    auteur = message.author
    if auteur == bot.user: # Check if the message is from the bot
        return
    if contenu.startswith('!') == False: # Check if the message starts with '!'
        return

    await message.channel.send('Hello!')


# Fonctions

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
    await ctx.send(response)


# Run the bot with the token
bot.run(getToken.getToken())