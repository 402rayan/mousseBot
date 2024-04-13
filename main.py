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
    commande = {
        "!tickets": "Permet de voir le nombre de tickets que vous avez.",
        "!daily": "Permet de réclamer votre ticket journalier.",
        "!invo": "Permet d'invoquer un personnage.",
        "!inv": "Permet de voir votre inventaire.",
        "!givetickets *{joueur}* *{nombre}*": "Permet de donner des tickets à un autre joueur.",
        "!info *{personnage}*": "Permet de voir les informations d'un personnage.",
        "!team": "Permet de voir votre team.",
        "!ajouterteam *{position}* *{personnage}*": "Permet d'ajouter un personnage à votre team.",
        "!sell *{personnage}*": "Permet de vendre un personnage."
    }
    
    embed = discord.Embed(
        title="Liste des commandes disponibles:",
        description="Voici la liste des commandes disponibles:",
        color=discord.Color.blurple()
    )
    for key, value in commande.items():
        embed.add_field(name=key, value=value, inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await message.channel.send(embed=embed)

@bot.command()
async def getTickets(message):
    logger.info(f"Commande !tickets appelée par {message.author.name} ({message.author.id}).")
    user = await fetch_user_from_message(message, 2)
    if not user:
        await send_embed_info(message, "Utilisateur invalide", "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!", discord.Color.red())
        return
    if user == "ERROR_SYNTAX":
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!tickets** ou **!tickets <joueur>**!", discord.Color.red())
        return
    print(user)
    tickets = database.get_tickets(user.id)
    await send_embed_info(message=message, title=f"{user.name} a {tickets} tickets.",description="", color=discord.Color.blue())

@bot.command()
async def claimDaily(message):
    user = message.author
    claim = database.claim_daily(user.id, user.name)
    if claim[0]:
        
        titre = f"Récompense journalière réclamée avec succès!"
        response = f"Vous avez maintenant {claim[1]} tickets."
        await send_embed_info(message, titre, response, discord.Color.green())
    elif not(claim[0]):
        temps_restant = claim[1]
        temps_restant_heures = temps_restant.seconds//3600
        temps_restant_minutes = (temps_restant.seconds//60)%60
        titre = "Vous avez déjà réclamé votre récompense journalière!"
        response = f"Vous pouvez réclamer une nouvelle récompense dans **{temps_restant_heures} heures et {temps_restant_minutes} minutes**."
        await send_embed_info(message, titre , response, discord.Color.red())
    
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
        await send_embed_info(message, "Inventaire vide", "Votre inventaire est vide!", discord.Color.red())
        return
    
    embed = discord.Embed(
        title=f"Inventaire de {message.author.name}:",
        color=discord.Color.blue()
    )
    for character in characters:
        embed.add_field(name=f"{character[6]} [{character[7]}]", value=f"{character[9]} HP {character[10]} ATK {character[11]} DEF - Niveau {character[3]}\n", inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await message.channel.send(embed=embed)

@bot.command()
async def giveTicket(message):
    # Fonction qui permet à un joueur A de donner x tickets à un joueur B
    contenu = message.content
    if len(contenu.split(' ')) != 3:
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!givetickets <joueur> <nombre>**!", discord.Color.red())
        return
    auteur = message.author
    montant = contenu.split(' ')[2]
    destinataire = contenu.split(' ')[1]
    destinataire = idDiscordToInt(destinataire)
    if destinataire == None:
        await send_embed_info(message, "Erreur de syntaxe", "Le joueur n'est pas valide!", discord.Color.red())
        return
    if not montant.isdigit():
        await send_embed_info(message, "Erreur de syntaxe", "Le montant doit être un **nombre**!", discord.Color.red())
        return
    montant = int(montant)
    if montant < 0:
        await send_embed_info(message, "Erreur de syntaxe", "Le montant doit être **positif**!", discord.Color.red())
        return
    tickets = database.get_tickets(auteur.id)
    if tickets < montant:
        await send_embed_info(message, "Pas assez de tickets", "Vous n'avez **pas assez** de tickets pour donner autant!", discord.Color.red())
        return
    if destinataire == auteur.id:
        await send_embed_info(message, "Erreur", "Vous ne pouvez pas vous donner des tickets à **vous-même**!", discord.Color.red())
        return
    # Vérfication de l'existence du destinataire
    if not database.check_user(destinataire):
        await send_embed_info(message, "Erreur", "Le joueur n'a pas encore joué au jeu.", discord.Color.red())
        return
    database.update_tickets(auteur.id, tickets - montant)
    tickets = database.get_tickets(destinataire)
    database.update_tickets(destinataire, tickets + montant)
    logger.info(f"L'utilisateur {auteur.name} ({auteur.id}) a donné {montant} tickets à {destinataire}.")
    await send_embed_info(message, "Transaction effectuée", f"Vous avez donné **{montant} tickets** à <@{destinataire}>!", discord.Color.green(), f"Tickets restants : {database.get_tickets(auteur.id)}.")
    
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
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!info <nom personnage>**!", discord.Color.red())
        return
    nom = contenu.split(' ')[1]
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        await send_embed_info(message, "Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red())
        return
    response = f"Voici les informations sur {nom}:\n"
    response += f"Nom: {character[1]}\nType: {character[2]}\nHP: {character[4]}\nATK: {character[5]}\nDEF: {character[6]}\nIMAGE: {character[3]}\n"
    await message.channel.send(response)

@bot.command()
async def voirTeam(message): 
    # Permet de voir ses personnages équipés en teams, ou la team d'un autre joueur
    user = await fetch_user_from_message(message, 2)
    if not user:
        await send_embed_info(message, "Utilisateur invalide", "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!", discord.Color.red())
        return
    if user == "ERROR_SYNTAX":
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!team** ou **!team <joueur>**!", discord.Color.red())
        return
    personnages = database.get_team(user.id, user.name)
    embed = discord.Embed(title="Team de " + user.name, color=discord.Color.blue())  
    for index, personnage in enumerate(personnages[:3], start=1):  # Ajoute un compteur commençant par 1
        if personnage is None:
            embed.add_field(name=f"{index}. Emplacement vide", value="", inline=False)
        else:
            # Affiche les détails du personnage avec l'index
            embed.add_field(
                name=f"{index}. {personnage[6]} [{personnage[7]}]",  # Index et nom du personnage
                value=f"{personnage[9]} HP {personnage[10]} ATK {personnage[11]} DEF - Niveau {personnage[3]}\n",  # Détails du personnage
                inline=False
            )
            

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=f"Remplacer des unités avec !ajouterteam")
    await message.channel.send(embed=embed)
    return

@bot.command()
async def ajouterTeam(message):
    # Permet d'ajouter un personnage à son équipe
    contenu = message.content
    if len(contenu.split(' ')) != 3:
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!ajouterteam <position> <nom personnage>**!", discord.Color.red())
        return
    nom = contenu.split(' ')[2]
    position = contenu.split(' ')[1]
    if not position.isdigit():
        await send_embed_info(message, "Erreur de syntaxe", "La position doit être un **nombre**!", discord.Color.red())
        return
    position = int(position)
    if position < 1 or position > 3:
        await send_embed_info(message, "Erreur de syntaxe", "La position doit être **comprise entre 1 et 3**!", discord.Color.red())
        return
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)
    if character == None:
        await send_embed_info(message, "Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red())
        return
    if database.check_character_in_team(message.author.id, character[0]):
        await send_embed_info(message, "Personnage déjà équipé", "Ce personnage est déjà dans votre équipe!", discord.Color.red())
        return
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a ajouté {nom} à sa team en position {str(position)}.")
    database.set_team(message.author.id, message.author.name, character[0], position)
    await send_embed_info(message, "Personnage ajouté", f"Vous avez ajouté {nom} à votre team en position {str(position)}!", discord.Color.green(), f"Pour voir votre team, utilisez !team.")

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
        await send_embed_info(message, "Erreur de syntaxe", "La commande doit être de la forme **!sell <nom personnage>**!", discord.Color.red())
        return
    nom = contenu.split(' ')[1]
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)
    if character == None:
        await send_embed_info(message, "Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red())
        return
    nom = character[6]
    rarity = str(character[7])
    tickets_obtenus = CONSTANTS['RARITY_PRICE'][rarity]
    # Demandez confirmation
    response = f"Voulez-vous vraiment vendre {nom} pour {tickets_obtenus} tickets? (réagissez)"
    msg = await send_embed_info(message, "Confirmation", response, discord.Color.gold())
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    # On met une réaction pour confirmer et on attend 30 secondes que l'utilisateur réagisse
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❌'])
    except:
        await send_embed_info(message, "Temps écoulé", "Vous avez mis trop de temps à répondre!", discord.Color.red())
        return
    if str(reaction.emoji):
        print("Réaction reçue")
    if str(reaction.emoji) != '✅':
        await send_embed_info(message, "Vente annulée", "Vous avez annulé la vente!", discord.Color.red())
        return
    database.sell_character(message.author.id,message.author.name, character[0])
    database.update_tickets(message.author.id, database.get_tickets(message.author.id) + tickets_obtenus)
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a vendu {nom} pour {rarity} tickets.")
    await send_embed_info(message, "Vente effectuée", f"Vous avez vendu **{nom}** pour **{tickets_obtenus} tickets**!", discord.Color.green(), f"Vos tickets : {database.get_tickets(message.author.id)}.")

# Fonction qui envoie un message d'information style embed d'information
async def send_embed_info(message, title, description, color=discord.Color.blue(),footer=None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
    )
    if footer:
        embed.set_footer(text=footer)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    return await message.channel.send(embed=embed)

# Run the bot with the token
bot.run(getToken.getToken())