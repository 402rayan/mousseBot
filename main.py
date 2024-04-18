# Import the required modules
import asyncio
import random
import discord
from discord.ext import commands 
from constantes import CONSTANTS
import getToken
import bdd
from loguru import logger
from constantes import phrases_invocation
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
    userFromDb = database.getUser(auteur.id)
    if not userFromDb:
        logger.error(f"Erreur lors de la récupération de l'utilisateur {message.author.name} ({message.author.id}).")
        return
    if contenu.startswith('!tickets'):
        await getTickets(message, userFromDb)
    elif contenu.startswith('!daily'):
        await claimDaily(message, userFromDb)
    elif contenu.startswith('!admin'):
        await admin(message, userFromDb)
    elif contenu.startswith('!list_command') or contenu.startswith('!help'):
        await list_command(message, userFromDb)
    elif contenu.startswith('!invo') or contenu.startswith('!sum'):
        await invocation(message, userFromDb)
    elif contenu.startswith('!inv') or contenu.startswith('!pers') or contenu.startswith('!bag'):
        await inventaire(message, userFromDb)
    elif contenu.startswith('!givetickets') or contenu.startswith('!donnertickets') or contenu.startswith('!donnerticket') or contenu.startswith('!giveticket') or contenu.startswith('!give_tickets') or contenu.startswith('!donner_tickets') or contenu.startswith('!donner_ticket') or contenu.startswith('!give_ticket'):
        await giveTicket(message, userFromDb)
    elif contenu.startswith('!info '):
        await info(message, userFromDb)
    elif contenu.startswith('!infos'):
        await infoSynergie(message, userFromDb)
    elif contenu.startswith('!team') or contenu.startswith('!voirteam') or contenu.startswith('!voir_team') or contenu.startswith('!voir_team'):
        await voirTeam(message, userFromDb)
    elif contenu.startswith('!ajouterteam') or contenu.startswith('!addteam') or contenu.startswith('!add_team') or contenu.startswith('!ajouter_team'):
        await ajouterTeam(message, userFromDb)
    elif contenu.startswith('!sell') or contenu.startswith('!vendre'):
        await sell(message, userFromDb)
    elif contenu.startswith('!create'):
        await createTemplates(message, userFromDb)
    elif contenu.startswith('!his'):
        await histoire(message, userFromDb)
    # A supp
    elif contenu.startswith('!purple'):
        await purple(message, userFromDb)
    elif contenu.startswith('!cookWithSanji'):
        await cookWithSanji(message, userFromDb)
    elif contenu.startswith('!labyrinthe'):
        await labyrinthe(message, userFromDb)
    elif contenu.startswith('!reset'):
        await reset(message, userFromDb)
    elif contenu.startswith('!couleur'):
        await couleur(message, userFromDb)
    elif contenu.startswith('!liste '):
        await liste(message, userFromDb)
# Fonctions

# Partie Histoire
async def histoire(message, userFromDb):
    if not userFromDb:
        logger.error(f"Erreur lors de la récupération de l'utilisateur {message.author.name} ({message.author.id}).")
        return
    niveau = getNiveauFromUser(userFromDb)
    if niveau == 1:
        await niveau1(message, userFromDb)
    elif niveau == 2:
        await niveau2(message, userFromDb)

async def niveau1(message, userFromDb):
    await message.channel.send(embed=embed_naratteur("Niveau 1 - Introduction", ""))
    await asyncio.sleep(2)
    await finDeNiveau(message, userFromDb, 2)

async def niveau2(message, userFromDb):
    await message.channel.send(embed=embed_naratteur("Niveau 2 - La forêt", ""))
    await asyncio.sleep(2)
    await finDeNiveau(message, userFromDb, 3)


def embed_naratteur(titre, description, color=CONSTANTS['COLORS']['HISTOIRE'], niveau=None):
    embed = discord.Embed(
        title=titre,
        description=description,
        color=color
    )
    nom = "Histoire" if not niveau else f"Histoire - Niv.{niveau}"
    embed.set_author(name=nom, icon_url=bot.user.avatar_url)
    return embed

async def finDeNiveau(message, userFromDb, level):
    database.updateNiveauHistoire(userFromDb[1], level)
    await message.channel.send(embed=embed_naratteur(f"Vous avez terminé le niveau {str(level-1)}!", f"Vous êtes maintenant au niveau {str(level)}!"))

def getNiveauFromUser(user):
    return user[8]

async def cookWithSanji(message, userFromDb):
    await embed_histoire_character(message, "Sanji", "cookWithSanji", "sanji", "","Sanji a besoin de votre aide pour cuisiner!", discord.Color.gold())
    # Le but est que sanji vous donne un nom d'ingrédient ou d'aliment et que vous cliquiez sur la bonne réaction
    # Il faut cliquer sur la bonne dans les 3 secondes sinon on perd!
    # Il y a 4 réactions différentes dont une seule bonne
    ingredientReussis = 0; totalIngredients = 2; temps = 3
    while ingredientReussis <= totalIngredients:
        await asyncio.sleep(2)
        retour = get_ingredient() 
        ingredient = retour[0]
        liste_reactions = retour[1]
        msg = await embed_histoire_character(message, "Sanji", None ,"sanji", f"Cliquez sur la bonne réaction!",f"Sanji a besoin de {ingredient[0]} pour cuisiner!", discord.Color.gold())
        # On veut que dans la liste des réactions il y a ait 3 réactions aléatoires et une bonne
        for reaction in liste_reactions:
            await msg.add_reaction(reaction)
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=temps, check=lambda reaction, user: user == message.author and str(reaction.emoji) in liste_reactions)
        except:
            await message.channel.send(embed=embed_info("Vous n'avez pas donné l'ingrédient à temps. ", "Le plat est un total désastre.", discord.Color.red()))
            return
        if str(reaction.emoji) == ingredient[1]:
            await embed_histoire_character(message, "Sanji", None, "sanji", f"Plus que {totalIngredients - ingredientReussis} ingrédients.", "Bravo! Vous avez réussi!", discord.Color.gold())
            ingredientReussis += 1; temps -= 0.4
        else:
            await message.channel.send(embed=embed_info("Vous avez donné le mauvais ingrédient..", "Le plat est un total désastre.", discord.Color.red()))
            return
    await embed_histoire_character(message, "Sanji", "sanjiTaste", "sanji", "Grâce à vous, Sanji a pu préparer un plat exquis!", "Félicitations!", discord.Color.gold())

def get_ingredient():
    # Fonction qui retourne un ingrédient, et une liste de 3 ingrédients aléatoires + le bon ingrédient
    ingredient = random.choice(list(CONSTANTS['INGREDIENTS'].keys()))
    ingredient = (ingredient, CONSTANTS['INGREDIENTS'][ingredient])
    liste_reactions = list(CONSTANTS['INGREDIENTS'].values())
    liste_reactions.remove(ingredient[1])
    liste_reactions = random.sample(liste_reactions, 3)
    liste_reactions.append(ingredient[1])
    random.shuffle(liste_reactions)
    return ingredient, liste_reactions

async def purple(message, userFromDb):
    await embed_histoire_character(message, "Purple Haze", "purpleHaze", "purpleHaze", "Fuyez aussi vite que vous pouvez!","Purple Haze a déclenché son virus!", discord.Color.purple())
    alive = True
    ticketsGagnes = 0
    await asyncio.sleep(3)
    while alive:
        # le taux de mort est entre 0 et 0.3
        tauxDeMort = random.random() * 0.3
        # On lui demande s'il souhaite s'enfuir ou s'il veut risquer sa chance pour gagner des tickets
        phrase = "Vous avez vu un autre " if ticketsGagnes > 0 else "Vous avez vu un "
        notice = "\n🏃 : Fuir  💰 : Prendre le ticket"
        msg = await embed_histoire_character(message, "Purple Haze", None, "purpleHaze","Avez-vous vraiment le temps.. ?" + notice, phrase + "ticket, souhaitez vous le prendre?", discord.Color.purple())
        await msg.add_reaction('🏃')
        await msg.add_reaction('💰')
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🏃', '💰'])
        except:
            await embed_histoire_character(message, "Purple Haze", None, "purpleHaze", "Le poison de Purple Haze vous a rattrapé et avez perdu tous vos tickets!","Vous avez pris trop de temps!", discord.Color.dark_red())
            return
        if str(reaction.emoji) == '🏃':
            alive = False
            await message.channel.send(embed=embed_info("PURPLE HAZE", f"Vous avez fui le sous-terrain avec {ticketsGagnes}!", discord.Color.green()))

        elif str(reaction.emoji) == '💰':
            if random.random() < tauxDeMort:
                await embed_histoire_character(message, "Purple Haze", None, "purpleHaze","Le poison de Purple Haze vous a rattrapé et avez perdu tous vos tickets!","Vous avez été touché.", discord.Color.dark_red())
                return
            ticketsGagnes += 1
            await message.channel.send(embed=embed_info("PURPLE HAZE", "Vous avez récupéré un ticket!", discord.Color.green(), f"Tickets sur vous : {ticketsGagnes}."))
            await asyncio.sleep(2.5)
    return

async def labyrinthe(message, userFromDb):
    maison = {
    'Entrée': ['Salon', 'Écurie'],
    'Chambre 1': ['Salle de bain', 'Chambre 2'],
    'Cuisine': ['Salon', 'Cellier','Bureau'],
    'Salon': ['Entrée', 'Cuisine', 'Bureau', 'Chambre 1'],
    'Salle de bain': ['Chambre 1'],
    'Bureau': ['Salon', 'Bibliothèque','Cuisine'],
    'Cave': [], 
    'Grenier': ['Chambre 3'],
    'Cellier': ['Cuisine'],
    'Chambre 3': ['Grenier', 'Chambre 2','Écurie'],
    'Chambre 2': ['Chambre 1', 'Chambre 3'],
    'Forge': ['Écurie','Cellier'],
    'Écurie': ['Forge', 'Entrée'],
    'Bibliothèque': ['Bureau', 'Cave']  
}
    pieceActuelle = 'Entrée'
    pieceFinale = 'Cave'
    ticketsRamasses = 0
    hasDiscoveredSdb = False; hasDiscoveredGrenier = False; hasDiscoveredForge = False
    listeEmojis = ['1️⃣', '2️⃣', '3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
    while pieceActuelle != pieceFinale:
        if pieceActuelle == 'Salle de bain' and not hasDiscoveredSdb:
            hasDiscoveredSdb = True
            await message.channel.send(embed=embed_info(f"Vous avez découvert un ticket dans la salle de bain!", "", discord.Color.gold()))
            await asyncio.sleep(2)
            ticketsRamasses += 1
        if pieceActuelle == 'Grenier' and not hasDiscoveredGrenier:
            hasDiscoveredGrenier = True
            await message.channel.send(embed=embed_info(f"Vous avez découvert un ticket dans le grenier!", "", discord.Color.gold()))
            await asyncio.sleep(2)
            ticketsRamasses += 1
        if pieceActuelle == 'Forge' and not hasDiscoveredForge:
            hasDiscoveredForge = True
            await message.channel.send(embed=embed_info(f"Vous sentez une présence...", "", discord.Color.dark_gray()))
            await asyncio.sleep(2)
            await message.channel.send(embed=embed_info(f"La présence se rapproche!!!", "", discord.Color.dark_gray()))
            await asyncio.sleep(2)
            await message.channel.send(embed=embed_info(f"Ce n'était qu'un petit chat mignon!", "", discord.Color.dark_orange()))
            await asyncio.sleep(2)
            await message.channel.send(embed=embed_info(f"Le chat se transforme..", "Combat contre Yoruichi", discord.Color.gold()))
            await message.channel.send(embed=embed_info(f"Après avoir battu Yoruichi, vous trouvez 6 tickets dans sa poche!", "", discord.Color.gold()))
            await asyncio.sleep(2)
            ticketsRamasses += 6
        if ticketsRamasses <= 0:
            await message.channel.send(embed=embed_info(f"Vous êtes actuellement dans la pièce {pieceActuelle}.", f"", discord.Color.blue()))
        else:
            await message.channel.send(embed=embed_info(f"Vous êtes actuellement dans la pièce {pieceActuelle}.", f"Tickets trouvés : {ticketsRamasses}", discord.Color.blue()))
        await asyncio.sleep(2)
        listePiecesAvailables = maison[pieceActuelle]
        listePiecesAvailables = random.sample(listePiecesAvailables, len(listePiecesAvailables))
        description = ""
        for i in range(len(listePiecesAvailables)):
            description += f"{listeEmojis[i]} : {listePiecesAvailables[i]}\n"
        msg = await message.channel.send(embed=embed_info("Choisissez une pièce à explorer :", description, discord.Color.blue()))
        for i in range(len(listePiecesAvailables)):
            await msg.add_reaction(listeEmojis[i])
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in listeEmojis)
        except:
            await message.channel.send(embed=embed_info("Labyrinthe", "Vous avez mis trop de temps à répondre!", discord.Color.red()))
            return
        pieceActuelle = listePiecesAvailables[listeEmojis.index(str(reaction.emoji))]
    await message.channel.send(embed=embed_info("Labyrinthe", "Vous avez trouvé la sortie de la cave!", discord.Color.green()))
        
def embed_histoire_character(message, nom, nomGif, nomPfp, description,titre, color=discord.Color.gold()):
    files = []
    embed = discord.Embed(
        title=titre,
        description=description,
        color=color
    )
    if nomGif:
        gif = discord.File("./assets/histoire/" + nomGif + ".gif", filename=nomGif + ".gif")
        embed.set_image(url="attachment://" + nomGif + ".gif")
        files.append(gif)
    if nomPfp:
        pfp = discord.File("./assets/histoire/" + nomPfp + ".png", filename=nomPfp + ".png")
        embed.set_author(name=nom, icon_url="attachment://" + nomPfp + ".png")
        files.append(pfp)
    return message.channel.send(files=files, embed=embed)
        
# Fin Partie Histoire
@bot.command()
async def liste(message, userFromDb):
    # Retourne la liste de tous les persos de rang
    rang = message.content.split(' ')[1]
    if rang not in CONSTANTS['RARITY']:
        await message.channel.send(embed=embed_info("Erreur", "Le rang n'est pas valide!", discord.Color.red()))
        return
    liste = database.get_character_templates()
    response = "Liste des personnages:\n"
    for character in liste:
        if character[2] == rang:
            response += f"{character[1]},"
    await message.channel.send(response[:2000])

@bot.command()
async def couleur(message, userFromDb):
    # Récupère un personnage de chaque rang et les affiche avec embed_invocation
    for rang in ["F", "E", "D", "C", "B", "A", "S", "SS", "X"]:
        template = database.get_character_template_by_rarity(rang)
        await asyncio.sleep(0.5)
        await message.channel.send(embed=embed_invocation(template))
@bot.command()
async def list_command(message, userFromDb):
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
async def getTickets(message, userFromDb):
    logger.info(f"Commande !tickets appelée par {message.author.name} ({message.author.id}).")
    user = await fetch_user_from_message(message, 2)
    if not user:
        await message.channel.send(embed=embed_info("Utilisateur invalide", "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!", discord.Color.red()))
        return
    if user == "ERROR_SYNTAX":
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!tickets** ou **!tickets <joueur>**!", discord.Color.red()))
        return
    print(user)
    tickets = database.get_tickets(user.id)
    await message.channel.send(embed=embed_info(title=f"{user.name} a {tickets} tickets.",description="", color=discord.Color.blue()))

@bot.command()
async def claimDaily(message, userFromDb):
    user = message.author
    claim = database.claim_daily(user.id, user.name)
    if claim[0]:
        titre = f"Récompense journalière réclamée avec succès!"
        response = f"Tickets : {claim[1]}."
        await message.channel.send(embed=embed_info(titre, response, discord.Color.green()))
    elif not(claim[0]):
        temps_restant = claim[1]
        temps_restant_heures = temps_restant.seconds//3600
        temps_restant_minutes = (temps_restant.seconds//60)%60
        titre = "Récompense journalière déjà récupérée!"
        response = f"Prochaine récompense dans **{temps_restant_heures} heures et {temps_restant_minutes} minutes**."
        await message.channel.send(embed=embed_info(titre , response, discord.Color.red()))
    
@bot.command()
async def admin(message, userFromDb):
    liste_templates = database.get_character_templates()
    response = "Liste des templates de personnages:\n"
    for template in liste_templates:
        response += f"{template[0]} - {template[1]}\n"
    await message.channel.send(response[:2000])

@bot.command()
async def invocation(message, userFromDb):
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
            await message.channel.send(embed=embed_info("Erreur", "Aucun personnage n'a été trouvé!", discord.Color.red(), footer="Ticket remboursé."))
        elif donnees == "ERROR_MAX_CHARACTERS":
            await message.channel.send(embed=embed_info("Erreur", f"Vous avez atteint le nombre maximum de personnages {CONSTANTS['MAX_CHARACTERS']} !", discord.Color.red(),footer="Vendez des personnages avec !sell"))
        return
    template = donnees[0]
    msg = await message.channel.send(embed=embed_info("Invocation...", "Veuillez patienter...", discord.Color.gold()))
    rarityOfCharacter = template[2]
    if rarityOfCharacter in ["F", "E", "D", "C"]:
        await asyncio.sleep(3)
        await msg.edit(embed=embed_invocation(template))
        return
    else:
        random.shuffle(phrases_invocation) # On mélange les phrases d'invocation
        nombreRotation = {"B" : 1, "A" : 2, "S" : 3, "SS" : 4, "X" : 6}
        couleurs = [discord.Color.green(), discord.Color.blue(), discord.Color.purple(), discord.Color.orange(), discord.Color.red(), discord.Color.gold(), discord.Color.teal(), discord.Color.dark_gold(), discord.Color.dark_teal()]
        random.shuffle(couleurs) # On mélange les couleurs
        for i in range(nombreRotation[rarityOfCharacter]):
            await asyncio.sleep(3.5)
            await msg.edit(embed=embed_info("Invocation...", phrases_invocation[i] if i < 2 else phrases_invocation[i].upper(), couleurs[i]))
        await asyncio.sleep(random.randint(1, 3))
        await msg.channel.send(embed=embed_invocation(template))
    return


@bot.command()
async def inventaire(message, userFromDb):
    logger.info(f"Commande !inventaire appelée par {message.author.name} ({message.author.id}).")
    characters = database.inventaire(message.author.id, message.author.name)
    if characters == None or len(characters) == 0:
        await message.channel.send(embed=embed_info("Inventaire vide", "Votre inventaire est vide!", discord.Color.red()))
        return
    
    embed = discord.Embed(
        title=f"Inventaire de {message.author.name}:",
        color=discord.Color.blue()
    )
    for character in characters:
        identifiant = character[2]
        synergies = database.get_synergies_by_character_template(identifiant)
        value = f"Synergies : " + " ~ ".join([synergie[3] for synergie in synergies])
        if len(synergies) == 0:
            value = ""
        value = f"HP: {character[4]} ATK: {character[5]} DEF: {character[6]} - Niveau {character[3]}\n" + value
        embed.add_field(name=f"{character[6]} [{character[7]}]", value=value, inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await message.channel.send(embed=embed)

@bot.command()
async def giveTicket(message, userFromDb):
    # Fonction qui permet à un joueur A de donner x tickets à un joueur B
    contenu = message.content
    if len(contenu.split(' ')) != 3:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!givetickets <joueur> <nombre>**!", discord.Color.red()))
        return
    auteur = message.author
    montant = contenu.split(' ')[2]
    destinataire = contenu.split(' ')[1]
    destinataire = idDiscordToInt(destinataire)
    if destinataire == None:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "Le joueur n'est pas valide!", discord.Color.red()))
        return
    if not montant.isdigit():
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "Le montant doit être un **nombre**!", discord.Color.red()))
        return
    montant = int(montant)
    if montant < 0:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "Le montant doit être **positif**!", discord.Color.red()))
        return
    tickets = database.get_tickets(auteur.id)
    if tickets < montant:
        await message.channel.send(embed=embed_info("Pas assez de tickets", "Vous n'avez **pas assez** de tickets pour donner autant!", discord.Color.red()))
        return
    if destinataire == auteur.id:
        await message.channel.send(embed=embed_info("Erreur", "Vous ne pouvez pas vous donner des tickets à **vous-même**!", discord.Color.red()))
        return
    # Vérfication de l'existence du destinataire
    if not database.check_user(destinataire):
        await message.channel.send(embed=embed_info("Erreur", "Le joueur n'a pas encore joué au jeu.", discord.Color.red()))
        return
    database.update_tickets(auteur.id, tickets - montant)
    tickets = database.get_tickets(destinataire)
    database.update_tickets(destinataire, tickets + montant)
    logger.info(f"L'utilisateur {auteur.name} ({auteur.id}) a donné {montant} tickets à {destinataire}.")
    await message.channel.send(embed=embed_info("Transaction effectuée", f"Vous avez donné **{montant} tickets** à <@{destinataire}>!", discord.Color.green(), f"Tickets restants : {database.get_tickets(auteur.id)}."))
    
def idDiscordToInt(idDiscord):
    try:
        return int(idDiscord.replace('<@', '').replace('>', ''))
    except ValueError:
        logger.error(f"Impossible de convertir {idDiscord} en entier.")
        return None

@bot.command()
async def info(message, userFromDb):
    # Permet d'obtenir les informations d'un personnage
    contenu = message.content
    if len(contenu.split(' ')) < 2:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!info <nom personnage>**!", discord.Color.red()))
        return
    # On récupère le nom (tout ce qui suit le !info)
    nom = " ".join(contenu.split(' ')[1:])
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        await message.channel.send(embed=embed_info("Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red()))
        return
    
    synergies = database.get_synergies_by_character_template(character[0])
    hp = character[4]; atk = character[5]; defense = character[6]; image = character[3]; nom = character[1]; rarity = character[2]
    embed = discord.Embed(
        title=f"{nom} **[{rarity}]**",
        color=CONSTANTS['RARITY_COLOR'][rarity],
    )
    embed.set_image(url=image)
    embed.add_field(name="", value=f"HP: {hp} ATK: {atk} DEF: {defense}", inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    print(synergies)
    if len(synergies) > 0:
        embed.set_footer(text="Synergies : " + " ~ ".join([synergie[3] for synergie in synergies]))
    await message.channel.send(embed=embed)

@bot.command()
async def infoSynergie(message, userFromDb):
    # Permet d'obtenir les informations d'une synergie
    contenu = message.content
    if len(contenu.split(' ')) < 2:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!infosynergie <nom synergie>**!", discord.Color.red()))
        return
    # On récupère le nom (tout ce qui suit le !info)
    nom = " ".join(contenu.split(' ')[1:])
    synergie = database.get_synergie_by_name(userFromDb[0], userFromDb[1], nom)
    if synergie == None:
        await message.channel.send(embed=embed_info("Synergie introuvable", "Cette synergie **n'existe pas**!", discord.Color.red()))
        return
    
    # Création de l'embed
    nom = synergie[1]; typeOfBoost = synergie[2]; forceOfBoost = synergie[3];
    description = synergie[4]; image = synergie[5]; color = int(synergie[6][1:], 16)
    charactersFromSynergy = database.get_character_template_who_has_synergy(synergie[0])
    if not charactersFromSynergy or len(charactersFromSynergy) == 0:
        liste_personnages = "Aucun personnage n'a cette synergie."
    else:
        liste_personnages = " ~ ".join([character[1] for character in charactersFromSynergy])
    embed = discord.Embed(
        title=nom,
        description=description,
        color=color
    )
    embed.set_footer(text=f"Boost : {typeOfBoost} {forceOfBoost}")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="Personnages", value=liste_personnages[:1999], inline=False)
    embed.set_image(url=image)
    
    await message.channel.send(embed=embed)

@bot.command()
async def voirTeam(message, userFromDb): 
    # Permet de voir ses personnages équipés en teams, ou la team d'un autre joueur
    user = await fetch_user_from_message(message, 2)
    if not user:
        await message.channel.send(embed=embed_info("Utilisateur invalide", "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!", discord.Color.red()))
        return
    if user == "ERROR_SYNTAX":
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!team** ou **!team <joueur>**!", discord.Color.red()))
        return
    team = database.get_team(user.id, user.name)
    embed = discord.Embed(title="Team de " + user.name, color=discord.Color.blue()) 

    nom_synergies_actives = team['synergies']; personnages = team['team']; stats = team['stats']; bonus = team['bonus']

    for index, personnage in enumerate(personnages[:3], start=1):  # Ajoute un compteur commençant par 1
        if personnage is None:
            embed.add_field(name=f"{index}. Emplacement vide", value="", inline=False)
        else:
            # Affiche les détails du personnage avec l'index
            identifiant = personnage[2]
            synergies = database.get_synergies_by_character_template(identifiant)
            value = f"*Synergies : " + " ~ ".join([synergie[3] for synergie in synergies])  + "*"
            if len(synergies) == 0:
                value = ""
            value = f"{personnage[9]} HP {personnage[10]} ATK {personnage[11]} DEF - Niveau {personnage[3]}\n" + value
            embed.add_field(
                name=f"{index}. {personnage[6]} [{personnage[7]}]",  # Index et nom du personnage
                value=value,  # Détails du personnage
                inline=False
            )
            
    embed.add_field(name=f"Statistiques\n{stats['HP']}HP   {stats['ATK']}ATK   {stats['DEF']}DEF", value=f"", inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    # On met les synergies en footer et le bonus
    footer = "Synergies actives : " + " ~ ".join(nom_synergies_actives)
    if bonus:
        footer += f"\nBonus : {bonus['HP']}HP {bonus['ATK']}ATK {bonus['DEF']}DEF "
    embed.set_footer(text=footer)
    await message.channel.send(embed=embed)
    return

@bot.command()
async def ajouterTeam(message, userFromDb):
    # Permet d'ajouter un personnage à son équipe
    contenu = message.content
    if len(contenu.split(' ')) < 3:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!ajouterteam <position> <nom personnage>**!", discord.Color.red()))
        return

    nom = " ".join(contenu.split(' ')[2:])
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        await message.channel.send(embed=embed_info("Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red()))
        return
    nom = character[1]
    position = contenu.split(' ')[1]
    if not position.isdigit():
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La position doit être un **nombre**!", discord.Color.red()))
        return
    position = int(position)

    if position < 1 or position > 3:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La position doit être **comprise entre 1 et 3**!", discord.Color.red()))
        return
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)

    if character == None:
        await message.channel.send(embed=embed_info("Vous ne possèdez pas ce personnage!", f"Vous ne possèdez pas **{nom}**", discord.Color.red()))
        return
    
    if database.check_character_in_team(message.author.id, character[0]):
        await message.channel.send(embed=embed_info("Personnage déjà équipé", f"**{nom}** est déjà dans votre équipe!", discord.Color.red()))
        return
    
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a ajouté {nom} à sa team en position {str(position)}.")
    database.set_team(message.author.id, message.author.name, character[0], position)

    # Génération de l'embem
    image = character[8]
    embed = discord.Embed(
        title=f"{ nom } occupe désormais la position { position }.",
        color=discord.Color.green()
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text="Pour voir votre team, tapez !team.")
 
    embed.set_image(url=image)

    await message.channel.send(embed=embed)
    return

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
async def sell(message, userFromDb):
    logger.info(f"Commande !sell appelée par {message.author.name} ({message.author.id}).")
    # Permet de vendre un personnage
       # Permet d'ajouter un personnage à son équipe
    contenu = message.content
    if len(contenu.split(' ')) < 2:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!ajouterteam <position> <nom personnage>**!", discord.Color.red()))
        return
    nom = " ".join(contenu.split(' ')[1:])
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        await message.channel.send(embed=embed_info("Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red()))
        return
    nom = character[1]
    character = database.get_character_by_name_and_user(message.author.id, message.author.name, nom)
    if character == None:
        await message.channel.send(embed=embed_info("Vous ne possèdez pas ce personnage!", f"Vous ne possèdez pas **{nom}**", discord.Color.red()))
        return
    nom = character[6]
    rarity = str(character[7])
    tickets_obtenus = CONSTANTS['RARITY_PRICE'][rarity]
    # Demandez confirmation
    if rarity in ["X", "SS", "S", "A"]:
        response = f"Voulez-vous vraiment vendre {nom} pour {tickets_obtenus} tickets? (réagissez)"
        msg = await message.channel.send(embed=embed_info("Confirmation", response, discord.Color.gold()))
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        # On met une réaction pour confirmer et on attend 30 secondes que l'utilisateur réagisse
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❌'])
        except:
            await message.channel.send(embed=embed_info("Temps écoulé", "Vous avez mis trop de temps à répondre!", discord.Color.red()))
            return
        if str(reaction.emoji):
            print("Réaction reçue")
        if str(reaction.emoji) != '✅':
            await message.channel.send(embed=embed_info("Vente annulée", "Vous avez annulé la vente!", discord.Color.red()))
            return
    database.sell_character(message.author.id,message.author.name, character[0])
    database.update_tickets(message.author.id, database.get_tickets(message.author.id) + tickets_obtenus)
    logger.info(f"L'utilisateur {message.author.name} ({message.author.id}) a vendu {nom} pour {rarity} tickets.")
    await message.channel.send(embed=embed_info("Vente effectuée", f"Vous avez vendu **{nom}** pour **{tickets_obtenus} tickets**!", discord.Color.green(), f"Vos tickets : {database.get_tickets(message.author.id)}."))

@bot.command()
async def createTemplates(message, userFromDb):
    if message.author.id != 724383641752436757:
        await message.channel.send(embed=embed_info("Erreur", "Vous n'avez pas la permission de faire cela!", discord.Color.red()))
        return
    database.createAllDatas()
    await message.channel.send(embed=embed_info("Templates créés", "Les templates de personnages ont été créés!", discord.Color.green()))

@bot.command()
async def reset(message, userFromDb):
    if message.author.id != 724383641752436757:
        await message.channel.send(embed=embed_info("Erreur", "Vous n'avez pas la permission de faire cela!", discord.Color.red()))
        return
    database.reset(False)
    await message.channel.send(embed=embed_info("Base de données réinitialisée", "La base de données a été réinitialisée!", discord.Color.green()))

# Fonction qui envoie un message d'information style embed d'information
def embed_info(title, description, color=discord.Color.blue(),footer=None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
    )
    if footer:
        embed.set_footer(text=footer)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    return embed

def embed_invocation(character_template):
    """ Fonction qui retourne un embed pour l'invocation d'un personnage """
    character = character_template # Pour plus de lisibilité
    print(character)
    synergies = database.get_synergies_by_character_template(character[0])
    hp = character[4]; atk = character[5]; defense = character[6]; image = character[3]; nom = character[1]; rarity = character[2]
    embed = discord.Embed(
        title=f"{nom} **[{rarity}]**",
        description="Félicitations! Vous avez invoqué un nouveau personnage!",
        color=CONSTANTS['RARITY_COLOR'][rarity],
    )
    embed.set_image(url=image)
    embed.add_field(name="", value=f"HP: {hp} ATK: {atk} DEF: {defense}", inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    if len(synergies) > 0:
        embed.set_footer(text="Synergies : " + " ~ ".join([synergie[3] for synergie in synergies]))
    return embed

# Run the bot with the token
bot.run(getToken.getToken())