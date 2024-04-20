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

# Dictionnaire pour suivre les verrous par utilisateur
user_locks = {}

async def execute_command(command, message, userFromDb):
    if userFromDb[0] in user_locks:
        await message.channel.send(embed=embed_info("Vous avez déjà une commande en cours!", "", discord.Color.red()))
        return

    # Créer un verrou pour l'utilisateur
    user_locks[userFromDb[0]] = asyncio.Lock()
    try:
        # Attendre l'acquisition du verrou
        async with user_locks[userFromDb[0]]:
            await command(message, userFromDb)
    finally:
        # Assurez-vous de libérer le verrou après l'exécution de la commande
        del user_locks[userFromDb[0]]

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
    contenu = contenu[1:]
    for cmd, func in commands.items():
        if contenu.startswith(cmd):
            await execute_command(func, message, userFromDb)
            break



# Partie Histoire
async def handle_user_level(message, userFromDb):
    level_to_function = {
        1: niveau1, 2: niveau2, 3: niveau3,
        4: niveau4, 5: niveau5, 6: niveau6,
        7: niveau7
    }
    niveau = getNiveauFromUser(userFromDb)
    equipe = database.get_team(userFromDb[1],userFromDb[2])
    if not equipe:
        logger.error(f"Erreur lors de la récupération de l'équipe de l'utilisateur {message.author.name} ({message.author.id}).")
        return
    if None in equipe['team']:
        await message.channel.send(embed=embed_info("Erreur", "Vous devez avoir une équipe complète pour continuer l'histoire!", discord.Color.red()))
        return
    handler = level_to_function.get(niveau)
    if handler:
        await handler(message, userFromDb, equipe)
    else:
        logger.error(f"Niveau inconnu {niveau} pour l'utilisateur {message.author.name} ({message.author.id}).")
        await message.channel.send(embed=embed_info("Félicitations", "Vous avez terminé l'histoire!", random.choice(list(CONSTANTS['COLORS'].values()))))

async def histoire(message, userFromDb):
    if not userFromDb:
        logger.error(f"Erreur lors de la récupération de l'utilisateur {message.author.name} ({message.author.id}).")
        return
    await handle_user_level(message, userFromDb)

async def niveau7(message, userFromDb, equipe):
    followedPucci = database.getChoice(userFromDb[1], "lvl6pucci")
    if followedPucci:
        await debutDeNiveau(message, userFromDb, 7, "Poursuite du prêtre mystérieux!", equipe, CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous partez à la poursuite du prêtre..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous le perdez de vue..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        # Vous entendez que le combat entre le mosntre et Sanji a commencé et des flammes jaillisent de là bas
        await message.channel.send(embed=embed_naratteur("Vous entendez que le combat entre le monstre et Sanji a commencé..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous entendez un petit bruit..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(1.5)
        await embed_histoire_character(message, "Le prêtre vous attrape par la gorge", "pucciShot", "pucci", "", "Et vous emporte avec lui", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(6)
        await message.channel.send(embed=embed_naratteur("Vous êtes projeté au loin, presque inconscient..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Le Prêtre :", "", "pucci", "", "C'est contre mes intérêts de t'éliminer maintenant.", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Le Prêtre :", "", "pucci", "", "Disparaîs de ma vue, insecte.", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("L'aura du prêtre et sa force vous est insupportable..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
    
    else:
        await debutDeNiveau(message, userFromDb, 7, "Défense du village", equipe, CONSTANTS['COLORS']['MAHITO'])
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous décidez de rester défendre le village.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous vous dépêchez d'aller prêter main forte à Sanji..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Mahito", "", "mahito", "", "C'est parfait, continuez à venir, venez me rendre plus fort!", CONSTANTS['COLORS']['MAHITO'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Sanji est surpris :", "", "sanji", "", "Je ne peux pas le battre! Attaquons le à 2!", discord.Color.gold())
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous vous battez contre Mahito..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Alors que vous pensiez avoir le dessus..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Mahito", "mahitoDomain", "mahito", "", "Extension du-.. Territoire", CONSTANTS['COLORS']['MAHITO'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Zuko intervient :", "", "zuko", "", "Lâche-les.", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Zuko", "zukoThrowFire", "zuko", "", "Je vais m'occuper de lui.", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # Avec le combat et l'intervention de Zuko, nous nous évanouissons
        await message.channel.send(embed=embed_naratteur("L'épuisement du au combat, et la chaleur ardente du feu vous est insupportable..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous vous évanouissez..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 8)

async def niveau6(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 6, "Un repas pris de court", equipe, discord.Color.gold())
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous ressortez de la grotte et il fait jour!", "", CONSTANTS['COLORS']['CIEL']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous apercevez un petit village au loin et décidez d'y aller.", "", CONSTANTS['COLORS']['CIEL']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous êtes accueilis avec hospitalité! Les gens sont souriants et gentils!", "", CONSTANTS['COLORS']['CIEL']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous décidez de manger quelque chose et vous vous dirigez vers le chef cuisinier du village..", "", CONSTANTS['COLORS']['CIEL']))
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Sanji se présente :", "", "sanji", "", "Je suis Sanji, c'est moi qui m'occupe de faire à manger ici.", discord.Color.gold())
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Sanji :", "", "sanji", "", "Et si vous m'aidiez à faire à manger pour ce midi!", discord.Color.gold())
    await asyncio.sleep(4)
    reussis = await cookWithSanji(message, userFromDb)
    await asyncio.sleep(4)
    if not reussis:
        return
    await message.channel.send(embed=embed_naratteur("Le repas est un succès et tout le monde est content!", "", CONSTANTS['COLORS']['CIEL']))
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Sanji est surpris :", "", "sanji", "", "Mai-s... Qu'est-ce que c'est que ça?!", discord.Color.gold())
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Sanji est terrifié :", "sanjiScared", "sanji", "", "De-des gens se transforment en monstres!", discord.Color.gold(),isNotGif=True)
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Un monstre attaque le village", "mahitoAttack", "mahito", "", "", CONSTANTS['COLORS']['MAHITO'])
    await asyncio.sleep(6)
    await embed_histoire_character(message,"Sanji s'adresse à nous:", "", "sanji", "", "Je vais m'occuper de lui, occupez-vous des habitants!", discord.Color.gold())
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous vous occupez de mettre en sécurité les habitants du village, mais quelque chose attire votre attention", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_naratteur("Vous apercevez un homme au loin, un homme qui ressemble fortement au prêtre..", "", CONSTANTS['COLORS']['ENRICO_PUCCI']))
    await asyncio.sleep(4)
    description = "🏃 : Poursuivre le prêtre" + "\n🛡️ : Défendre le village"
    msg = await message.channel.send(embed=embed_naratteur("Que faites-vous?", description, CONSTANTS['COLORS']['ENRICO_PUCCI']))
    for reaction in ['🏃','🛡️']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🏃', '🛡️'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return
    if str(reaction.emoji) == '🏃':
        await message.channel.send(embed=embed_info("Vous partez à la poursuite du prêtre..", "", CONSTANTS['COLORS']['ENRICO_PUCCI']))
    else:
        await message.channel.send(embed=embed_info("Vous décider de rester défendre le village.", "", CONSTANTS['COLORS']['ENRICO_PUCCI']))
    await asyncio.sleep(2.5)
    database.updateChoice(userFromDb[1], "lvl6pucci", str(reaction.emoji) == '🏃')
    await finDeNiveau(message, userFromDb, 7)

async def niveau5(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 5, "Caverne", equipe, CONSTANTS['COLORS']['GROTTE'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Un bruit vous réveille alors que vous étiez entrain de vous reposer..", "", CONSTANTS['COLORS']['GROTTE']))
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_naratteur("Une étrange odeur se fait sentir..", "", CONSTANTS['COLORS']['GROTTE']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous vous levez et apercevez une lumière au fond de la caverne..", "", CONSTANTS['COLORS']['LIGHT']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous vous approchez de la lumière..", "", CONSTANTS['COLORS']['LIGHT']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous apercevez un humain et un monstre violet au loin..", "", CONSTANTS['COLORS']['PURPLE_HAZE']))
    await asyncio.sleep(5)
    # on entend quelqu'un dire "oh encore des visiteurs, purple Haze tu sais quoi faire"
    await embed_histoire_character(message,"Inconnu", "", "inconnu", "", "Encore des visiteurs? Purple Haze tu sais quoi faire.", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(5)
    ticketGagnes, escaped = await purple(message, userFromDb)
    await asyncio.sleep(4)
    if not escaped:
        # On prend le nombre de tickets qu'il a
        tickets = database.get_tickets(userFromDb[1])
        # Vous avez perdu 
        ticketGagnes = -10
        if tickets < 10:
            ticketGagnes = -tickets
        # On affiche la valeur absolu pour le texte
        nombreAffiche = abs(ticketGagnes)
        await message.channel.send(embed=embed_info("Vous avez perdu..", f"Vous avez perdu {nombreAffiche} tickets.", discord.Color.red()))
        # On retire les tickets
        await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 6, ticketGagnes)

async def niveau4(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 4, "Une nouvelle rencontre", equipe, CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    # Shanks nous annonce qu'il va faire route à part, il à ses amis à retrouver 
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "Eh bien.. je dois faire route à part, je pars retrouver les miens!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    # Shanks part 
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "Je vous souhaite bonne chance!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    # On s'en va dans la forêt pour trouver un endroit sûr
    await message.channel.send(embed=embed_raw("Vous partez dans la forêt pour trouver un endroit sûr..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    # On croise quelqu'un 
    await embed_histoire_character(message,"Inconnu", "", "inconnu", "", "Vous.., là-bas!", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko se présente :", "zuko", "zuko", "", "Je m'appelle Zuko!", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko vous raconte :", "", "zuko", "", "Je viens d'un pays en guerre, je suis arrivé ici il y a peu et rien n'y est différent..", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko :", "", "zuko", "", "Je cherche mon oncle, savez-vous où il se trouve?", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    description = "🌍 : Inventer une destination" + "\n❌ : Dire non"
    msg = await embed_histoire_character(message,"Que lui répondez-vous?", "", "zuko", description, "", CONSTANTS['COLORS']['ZUKO'])
    for reaction in ['🌍','❌']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🌍', '❌'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return
    if str(reaction.emoji) == '🌍':
        await embed_histoire_character(message,"Zuko vous remercie :", "", "zuko", "", "Je vois.. Merci pour votre indication.", CONSTANTS['COLORS']['ZUKO'])
    else:
        await embed_histoire_character(message,"Zuko", "", "zuko", "", "Je vois.. Merci quand même.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko", "", "zuko", "", "Tant que nous y sommes, laissez moi vous prévenir.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko", "", "zuko", "", "Les gens commencent à se regrouper, il devient dangereux de voyager seul.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(5)
    await embed_histoire_character(message,"Zuko", "", "zuko", "", "Vous feriez mieux de trouver un endroit sûr rapidement.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko", "", "zuko", "", "Je dois retourner retrouver mon oncle. Nous nous recroiserons sûrement.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_raw("Zuko s'en va..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous continuez votre route dans la forêt..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Quelqu'un vous attaque!", "rui", "rui", "", "", CONSTANTS['COLORS']['RUI'],False)
    await asyncio.sleep(4)
    await message.channel.send("combat avec rui") #TODO
    await asyncio.sleep(4)
    # QUelqu'un vous observait pendant votre combat et profite pour vous attaquer..
    await message.channel.send(embed=embed_naratteur("Quelqu'un vous observait pendant votre combat et profite pour vous attaquer également.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await message.channel.send("combat avec haruto") #TODO
    await asyncio.sleep(4)
    # Vous continuez votre route et apercevez une grotte au loin
    await message.channel.send(embed=embed_naratteur("Vous continuez votre route et apercevez une grotte au loin..", "Vous partez vous reposer au sein de la grotte.", CONSTANTS['COLORS']['GROTTE']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 5)

async def niveau3(message, userFromDb, equipe):
    ticketsGagnes = 0
    await debutDeNiveau(message, userFromDb, 3, "Un nouveau monde impitoyable", equipe, CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(4)
    # Le bug qui se produit ne vous téléporte pas cette fois, mais la nuit est tombé d'un coup... 
    await message.channel.send(embed=embed_naratteur("La nuit est tombée d'un coup suite à l'anomalie..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Vous parcourez la forêt à la recherche d'autres personnes ou de réponses et des murmures se font entendre au loin.
    await message.channel.send(embed=embed_naratteur("Vous parcourez la forêt à la recherche d'autres personnes ou de réponses..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Des murmures se font entendre au loin..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Ces murmures sont étranges, comme s'ils étaient les échos du passés. Un évènement sûrement liés aux bugs.
    await message.channel.send(embed=embed_naratteur("Ces murmures sont étranges..", "Comme s'ils étaient les échos du passé.", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Après quelques temps, vous quittez la forêt, il commence subitement à faire très froid. Vous arrivez nez à nez avec un jeune garçon accompagné d'un homme, ils ont du sang sur eux. Vous n'avez même pas le temps de réfléchir qu'ils vous attaquent.
    await message.channel.send(embed=embed_naratteur("Vous quittez la forêt, il commence à faire très froid..", "", CONSTANTS['COLORS']['FROID']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous arrivez nez à nez avec un jeune garçon accompagné d'un homme.", "Ils ont du sang sur eux..", CONSTANTS['COLORS']['FROID']))
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Jeune garçon", "haku", "froid", "", "Le jeune garçon vous attaque.", CONSTANTS['COLORS']['FROID'],isNotGif=True)
    await asyncio.sleep(4)
    await message.channel.send("combat avec haku") #TODO
    await asyncio.sleep(4)
    # await embed_histoire_character(message, "Shanks est surpris :", "", "shanks", "", "Je ne vous pensais pas aussi fort.", CONSTANTS['COLORS']['SHANKS'])
    # await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Voulant défendre son ami, l'autre homme se jette sur vous avec son épée mais..", "", CONSTANTS['COLORS']['FROID']))
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Shanks immobilise l'homme :", "shanksHaki", "shanks", "", "", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Shanks lui ordonne:", "", "shanks", "", "Reste bien sage et contente toi de répondre à mes questions.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(3)
    await embed_histoire_character(message, "L'inconnu rétorque :", "", "froid", "", "Hmprf.. Je suppose que je n'ai pas le choix. Mais qu'une seule question.", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(4)
    """
    1 - Sais-tu où sommes nous?  -> Je l'ignore, mais j'ai apercu un pretre qui blablabla
    2 - Comment es-tu arrivé là? -> j'ai aperçu un homme mystérieux accélerer les cycles de la jours et la nuit, puis j'ai été téléporté dans divers monde, un monde remplis d'eau, un monde remplis de bâtiments immenses.. puis un groupe de gens m'ont attaqué
    3 - Pourquoi nous-as tu attaqué? -> Quand nous sommes venus ici, divers groupes de personnes nous ont attaqués..
    4 - Aurais-tu trouvé des objets? Oui j'ai trouvé ça en fouillant l'un de nos assaillants, ça ne m'a pas l'air utile vous pouvez le prendre +2 ticket
    """
    description = "1️⃣ : Sais-tu où nous sommes?\n2️⃣ : Comment es-tu arrivé là?\n3️⃣ : Pourquoi nous-as tu attaqué?\n4️⃣ : As-tu trouvé quelque chose?"
    msg = await embed_histoire_character(message, "L'inconnu nous demande :", "", "froid", description, "Alors ?", CONSTANTS['COLORS']['FROID'])
    for reaction in ['1️⃣', '2️⃣', '3️⃣', '4️⃣']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣', '4️⃣'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return
    if str(reaction.emoji) in ['1️⃣', '2️⃣']:
        await embed_histoire_character(message, "Inconnu :", "", "froid", "", "Je l'ignore, tout ce que j'ai aperçu c'est le jour et la nuit qui ne faisaient plus qu'un.", CONSTANTS['COLORS']['FROID'])
    elif str(reaction.emoji) == '3️⃣':
        await embed_histoire_character(message, "Inconnu :", "", "froid", "", "Quand nous sommes venus ici, divers groupes de personnes nous ont attaqués..", CONSTANTS['COLORS']['FROID'])
    else:
        await embed_histoire_character(message, "Inconnu :", "", "froid", "", "Non, rien d'intéressant.", CONSTANTS['COLORS']['FROID'])
        await asyncio.sleep(3)
        await embed_histoire_character(message, "Inconnu :", "", "froid", "", "Ah, peut-être que ce truc pourrait t'intéresser.", CONSTANTS['COLORS']['FROID'])
        await asyncio.sleep(3)
        ticketsGagnes += 2
        await message.channel.send(embed=embed_info("L'homme vous tend 2 tickets d'invocations.", "", discord.Color.gold()))
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Shanks :", "", "shanks", "", "Merci pour ces informations.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    # Zabuza nous dis de ne surtout pas oublier que ce monde est impitoyable, et qu'il faut être en permanence sur ses gardes
    await embed_histoire_character(message, "Zabuza :", "", "zabuza", "", "Je reconnais ta puissance. Mon nom est Zabuza, laissez moi vous dire que ce nouveau monde est impitoyable.", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 4, ticketsGagnes)

async def niveau2(message, userFromDb, equipe):
    isFumee = database.getChoice(userFromDb[1], "lvl1fumee")
    ticketsGagnes = 0
    nom = "Un bruit étrange"
    if isFumee:
        nom = "Une fumée étrange"
    await debutDeNiveau(message, userFromDb, 2, nom, equipe, CONSTANTS['COLORS']['FORET'])
    await asyncio.sleep(4)
    if isFumee:
        await message.channel.send(embed=embed_raw("Votre équipe et Shanks se dirigent vers la fumée.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        # La fumée provient d'un grand feu de camp
        await message.channel.send(embed=embed_raw("La fumée semble provenir d'un grand feu de camp..", "", CONSTANTS['COLORS']['FUMEE']))
    else:
        await message.channel.send(embed=embed_raw("Votre équipe et Shanks se dirigent vers le bruit.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_raw("Vous trouvez un objet brillant!", "", discord.Color.gold(), "Vous avez trouvé un ticket!"))
        ticketsGagnes += 1
        await asyncio.sleep(4)
        await embed_histoire_character(message,"Shanks constate:", "", "shanks", "", "Il n'y a rien ici.", CONSTANTS['COLORS']['SHANKS'])
        await asyncio.sleep(4) 
        await message.channel.send(embed=embed_raw("Le bruit recommence et s'approche..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Une grande voix s'exclame : ", "", "inconnu", "", "Hmrpf.. Broggy regarde, nous avons des visiteurs!", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Inconnu", "dorryBroggy", "inconnu", "", "Deux géants intimidants vous regardent", CONSTANTS['COLORS']['INCONNU'],isNotGif=True)
    await asyncio.sleep(4)
    # Shanks nous demande que faire, Soit les attaquer soit Essayer de leur parler
    description = "🗡️ : Les attaquer" + "\n💬 : Essayer de leur parler"
    msg = await embed_histoire_character(message,"Shanks :", "", "shanks", description, "Que devrions-nous faire?", CONSTANTS['COLORS']['SHANKS'])
    couleursBug = [0xa732f0,0x001aff, CONSTANTS['COLORS']['ENRICO_PUCCI'], 0xa732f0, 0x8B4513, 0x8B0000, 0x000000, 0x8B0000, 0x1C1C1C]
    for reaction in ['🗡️','💬']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🗡️', '💬'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return
    if str(reaction.emoji) == '🗡️':
        await message.channel.send(embed=embed_raw("Vous attaquez les géants..", "", discord.Color.red()))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_info("Combat contre Dorry et Broggy", "Vous avez vaincu les géants!", discord.Color.green()))
        await asyncio.sleep(4)
        await embed_histoire_character(message,"Shanks est perplexe :", "", "shanks", "", "La violence n'est pas toujours la meilleure des solutions.", CONSTANTS['COLORS']['SHANKS'])
        await asyncio.sleep(4)
        embed = discord.Embed(
            title="Mai-.. Mais que se passe-t-il ?",
            description="",
            color=CONSTANTS['COLORS']['SHANKS']
        )
        pfp = discord.File("./assets/histoire/shanks.png", filename="shanks.png")
        embed.set_author(name="Shanks :", icon_url="attachment://shanks.png")
        msg = await message.channel.send(files=[pfp], embed=embed)
        await asyncio.sleep(1)
        # On changer la couleur du message
        for i in range(4):
            embed.color = couleursBug[i]
            await msg.edit(embed=embed)
            await asyncio.sleep(1.2)
    else:
        # On essaye de leur parler
        await message.channel.send(embed=embed_raw("Vous essayez de leur parler..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_raw("Dorry et Broggy vous écoutent attentivement et semblent amicaux..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(5)
        # Ils nous trouvent drôles et nous explique qu'eux aussi étaient sur une île quand des bugs ont commencé à se produire
        embed = discord.Embed(
            title="Nous aussi! Nous étions sur notre île quand la nuit a comm-..",
            description="",
            color=CONSTANTS['COLORS']['BROGGY']
        )
        pfp = discord.File("./assets/histoire/broggy.png", filename="broggy.png")
        embed.set_author(name="Dorry et Broggy :", icon_url="attachment://broggy.png")
        msg = await message.channel.send(files=[pfp], embed=embed)
        await asyncio.sleep(2)
        # On changer la couleur du message
        for i in range(4):
            embed.color = couleursBug[i]
            await msg.edit(embed=embed)
            await asyncio.sleep(1.2)
    await asyncio.sleep(1)
    # Un nouveau bug se produit
    await message.channel.send(embed=embed_raw("Une nouvelle anomalie se produit..", "",CONSTANTS['COLORS']['ENRICO_PUCCI']))
    await asyncio.sleep(3)
    await finDeNiveau(message, userFromDb, 3, ticketsGagnes)

async def niveau1(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 1, "Introduction", equipe, CONSTANTS['COLORS']['ENRICO_PUCCI'])
    await asyncio.sleep(3)
    await message.channel.send(embed=embed_naratteur("Cinématique : Enrico Pucci détruit l'univers...", "", CONSTANTS['COLORS']['ENRICO_PUCCI']))
    await asyncio.sleep(4.5)
    await message.channel.send(embed=embed_naratteur("Vous vous réveillez dans un indroit inconnu.. une autre personne semble ne pas être très loin..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4.5)
    await message.channel.send(embed=embed_naratteur("Vous semblez être dans une forêt..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4.5)
    await embed_histoire_character(message,"Un homme inconnu vous demande : ", "", "inconnu", "", "Tout va bien?", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks se présente : ", "", "shanks", "", "Mon nom est Shanks."[:245], CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "J'étais avec mes compagnons sur mon navire lorsque la lune et le soleil ont commencé à défiler inexorablement.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(5)
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "J'ai alors aperçu un homme vêtu d'une chape noire et puis.. je me suis réveillé ici.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Inconu", "", "inconnu", "", "Un bruit surgit..", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Saibaman", "saibaman", "saibaman", "", "Un monstre vous attaque!", CONSTANTS['COLORS']['SAIBAMAN'],False)
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_info("Combat contre le Saibaman", "Vous avez vaincu le Saibaman!", discord.Color.green()))
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "Impressionant!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "Je crois apercevoir de la fumée vers là-bas.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_raw("Un bruit retentit de l'autre côté de la forêt..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5)
    description = "🌲 : Aller vers la forêt" + "\n💨 : Aller vers la fumée"
    msg = await embed_histoire_character(message,"Shanks :", "", "shanks", description, "Où devrions-nous aller?", CONSTANTS['COLORS']['SHANKS'])
    for reaction in ['🌲','💨']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🌲', '💨'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return
    if str(reaction.emoji) == '🌲':
        await message.channel.send(embed=embed_raw("Vous partez en route vers la forêt.", "", CONSTANTS['COLORS']['FORET']))
    if str(reaction.emoji) == '💨':
        await message.channel.send(embed=embed_raw("Vous partez en route vers la fumée.", "", CONSTANTS['COLORS']['BRUIT']))
    database.updateChoice(userFromDb[1], "lvl1fumee", str(reaction.emoji) == '💨')
    print(str(reaction.emoji) == '💨')
    await asyncio.sleep(3)
    await finDeNiveau(message, userFromDb, 2)

async def test(message, userFromDb):
    await embed_histoire_character(message,"Shanks se présente : ", "", "shanks", "J'étais avec mes compagnons sur mon navire lorsque la lune et le soleil ont commencé à tournoyer inlassablement.\nJ'ai alors aperçu une sorte de prêtre, et je me suis réveiller ici..", "Mon nom est Shanks."[:245], CONSTANTS['COLORS']['SHANKS'])

def embed_raw(titre,description,color, footer=None):
    # Retourne un embed avec un titre, une description, une couleur et un footer
    embed = discord.Embed(
        title=titre,
        description=description,
        color=color
    )
    if footer:
        embed.set_footer(text=footer)
    return embed

def embed_naratteur(titre, description, color=CONSTANTS['COLORS']['HISTOIRE'], niveau=None, footer=None):
    # Retourne un embed avec un titre, une description, une couleur, un niveau et un footer ainsi que MOUSSE en haut
    embed = discord.Embed(
        title=titre,
        description=description,
        color=color
    )
    nom = "Histoire" if not niveau else f"Histoire - Niv.{niveau}"
    if footer:
        embed.set_footer(text=footer)
    embed.set_author(name=nom, icon_url=bot.user.avatar.url)
    return embed

async def finDeNiveau(message, userFromDb, level, ticketsGagnes = 0):
    # Met à jour le niveau de l'utilisateur et lui donne des tickets s'il en a gagné et lui envoie un message de fin de niveau
    database.updateNiveauHistoire(userFromDb[1], level)
    footer = None
    if ticketsGagnes != 0:
        database.update_tickets(userFromDb[1], database.get_tickets(userFromDb[1]) + ticketsGagnes)
        footer = f"Tickets gagnés : {ticketsGagnes}."
    await message.channel.send(embed=embed_naratteur(f"Félicitations! Vous avez terminé le niveau {str(level-1)}!", f"", CONSTANTS['COLORS']['FIN_NIVEAU'], None, footer))

async def debutDeNiveau(message, userFromDb, level,nom, equipe, couleur=discord.Color.gold()):
    description = "Équipe: " + " ~ ".join([f"{equipe['team'][i][6]}" for i in range(len(equipe['team']))])
    await message.channel.send(embed=embed_naratteur(f"Niveau {str(level)} - {nom}", "", couleur,"",description))

def getNiveauFromUser(user):
    return user[8]

async def cookWithSanji(message, userFromDb):
    await embed_histoire_character(message, "Sanji", "cookWithSanji", "sanji", "","Sanji prépare à manger!", discord.Color.gold())
    # Le but est que sanji vous donne un nom d'ingrédient ou d'aliment et que vous cliquiez sur la bonne réaction
    # Il faut cliquer sur la bonne dans les 3 secondes sinon on perd!
    # Il y a 4 réactions différentes dont une seule bonne
    ingredientReussis = 0; totalIngredients = 5; temps = 5
    await asyncio.sleep(4)
    while ingredientReussis <= totalIngredients:
        await asyncio.sleep(2)
        temps -= (0.2* temps)
        retour = get_ingredient() 
        ingredient = retour[0]
        liste_reactions = retour[1]
        msg = await embed_histoire_character(message, "Sanji", None ,"sanji", f"Cliquez sur la bonne réaction!",f"Sanji a besoin de {ingredient[0]} pour son plat!", discord.Color.gold())
        # On veut que dans la liste des réactions il y a ait 3 réactions aléatoires et une bonne
        for reaction in liste_reactions:
            await msg.add_reaction(reaction)
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=temps, check=lambda reaction, user: user == message.author and str(reaction.emoji) in liste_reactions)
        except:
            await message.channel.send(embed=embed_info("Vous n'avez pas donné l'ingrédient à temps. ", "Le plat est un total désastre.", discord.Color.red()))
            return False
        if str(reaction.emoji) == ingredient[1]:
            desc = f"Plus que {totalIngredients - ingredientReussis} ingrédients." if ingredientReussis < totalIngredients else ""
            await embed_histoire_character(message, "Sanji", None, "sanji", desc, "Bravo! Vous avez réussi!", discord.Color.gold())
            ingredientReussis += 1;
        else:
            await message.channel.send(embed=embed_info("Vous avez donné le mauvais ingrédient..", "Le plat est un total désastre.", discord.Color.red()))
            return False
    await asyncio.sleep(3)
    await embed_histoire_character(message, "Sanji", "sanjiTaste", "sanji", "Grâce à vous, Sanji a pu préparer un plat exquis!", "Félicitations!", discord.Color.gold())
    return True

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
    alive = True; escaped = False;
    ticketsGagnes = 0
    await asyncio.sleep(7)
    while alive and not escaped:
        # le taux de mort est entre 0 et 0.3
        tauxDeMort = random.random() * 0.3
        # On lui demande s'il souhaite s'enfuir ou s'il veut risquer sa chance pour gagner des tickets
        phrase = "Vous aperçevait un autre " if ticketsGagnes > 0 else "Vous apercevez un "
        notice = "\n🏃 : Fuir  🎫 : Prendre le ticket"
        msg = await embed_histoire_character(message, "Purple Haze", None, "purpleHaze","Avez-vous vraiment le temps.. ?" + notice, phrase + "ticket, souhaitez vous le prendre?", discord.Color.purple())
        await msg.add_reaction('🏃')
        await msg.add_reaction('🎫')
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🏃', '🎫'])
        except:
            await embed_histoire_character(message, "Purple Haze", None, "purpleHaze", "Le poison de Purple Haze vous a rattrapé et a désagrégé 10 de vos tickets!","Vous avez pris trop de temps!", discord.Color.dark_red())
            return 0, False
        if str(reaction.emoji) == '🏃':
            escaped = True
            await message.channel.send(embed=embed_info("", f"Vous avez réussi à fuire la caverne avec {ticketsGagnes} tickets!", discord.Color.gold()))

        elif str(reaction.emoji) == '🎫':
            if random.random() < tauxDeMort:
                await embed_histoire_character(message, "Purple Haze", None, "purpleHaze","Le poison de Purple Haze vous a rattrapé et a désagrégé tous vos tickets!","Vous avez été touché.", discord.Color.dark_red())
                return 0, False
            ticketsGagnes += 1
            await message.channel.send(embed=embed_raw("Vous avez pris le ticket!", f"Tickets sur vous : {ticketsGagnes}", discord.Color.gold()))
            await asyncio.sleep(2.5)
    return ticketsGagnes, escaped

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
        
def embed_histoire_character(message, nom, nomGif, nomPfp, description,titre, color=discord.Color.gold(), isNotGif=False):
    files = []
    embed = discord.Embed(
        title=titre,
        description=description,
        color=color
    )
    if nomGif:
        if isNotGif:
            gif = discord.File("./assets/histoire/" + nomGif + ".png", filename=nomGif + ".png")
            embed.set_image(url="attachment://" + nomGif + ".png")
        else:
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
async def claimHourly(message, userFromDb):
    user = message.author
    claim = database.claim_hourly(user.id, user.name)
    if claim[0]:
        titre = f"Vous avez obtenu 3 tickets et beaucoup d'expérience!"
        await message.channel.send(embed=embed_auteur(message.author,f"Récompense :",titre, "", discord.Color.green(), "Revenez dans une heure!"))
    elif not(claim[0]):
        temps_restant = claim[1]
        temps_restant_minutes = (temps_restant.seconds//60)%60
        temps_restants_secondes = temps_restant.seconds%60
        titre = "Récompense journalière déjà récupérée!"
        response = f"Prochaine récompense dans **{temps_restant_minutes} minutes et {temps_restants_secondes} secondes**."
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
    if rarityOfCharacter == "X":
        schema = random.choice(CONSTANTS['NOMS_GIF_INVOCATION'])
        nomDuGif = schema[0] ; texteAAfficher = schema[1] ; couleur = schema[2] ; nomPfp = schema[3]
        msg = await embed_histoire_character(message=message, nom=texteAAfficher, nomGif=nomDuGif, nomPfp=nomPfp, color=couleur, description="", titre="")
        await asyncio.sleep(6)
        await msg.delete()
        await message.channel.send(embed=embed_invocation(template,message.author))
        
    elif rarityOfCharacter in ["F", "E", "D", "C"]:
        await asyncio.sleep(3)
        await msg.edit(embed=embed_invocation(template,message.author))

    else:
        random.shuffle(phrases_invocation) # On mélange les phrases d'invocation
        nombreRotation = {"B" : 1, "A" : 2, "S" : 3, "SS" : 4}
        couleurs = [discord.Color.green(), discord.Color.blue(), discord.Color.purple(), discord.Color.orange(), discord.Color.red(), discord.Color.gold(), discord.Color.teal(), discord.Color.dark_gold(), discord.Color.dark_teal()]
        random.shuffle(couleurs) # On mélange les couleurs
        for i in range(nombreRotation[rarityOfCharacter]):
            await asyncio.sleep(random.uniform(0.5, 2))
            await msg.edit(embed=embed_info("Invocation...", phrases_invocation[i] if i < 2 else phrases_invocation[i].upper(), couleurs[i]))
        await asyncio.sleep(3)
        await msg.delete()
        await message.channel.send(embed=embed_invocation(template,message.author))
    return

@bot.command()
async def inventaire(message, userFromDb):
    logger.info(f"Commande !inventaire appelée par {message.author.name} ({message.author.id}).")
    characters = database.inventaire(message.author.id, message.author.name)
    if characters is None or len(characters) == 0:
        await message.channel.send(embed=embed_info("Inventaire vide", "Votre inventaire est vide!", discord.Color.red()))
        return

    # Pagination setup
    items_per_page = 5
    pages = [characters[i:i + items_per_page] for i in range(0, len(characters), items_per_page)]
    page_index = 0

    def create_embed(page_index):
        embed = discord.Embed(
            title="",
        )
        # Initialisation du dictionnaire pour compter les rangs
        rang_comptage = {}
        

        
        embed.set_author(name=f"Inventaire {page_index + 1}/{len(pages)}", icon_url=message.author.avatar.url)
        for character in pages[page_index]:
            identifiant = character[2]
            rang = character[7]  # Assumons que l'indice 7 contient le rang du personnage
            # Mise à jour du compteur pour le rang
            if rang in rang_comptage:
                rang_comptage[rang] += 1
            else:
                rang_comptage[rang] = 1
            synergies = database.get_synergies_by_character_template(identifiant)
            value = f"Synergies : " + " ~ ".join([synergie[3] for synergie in synergies])
            if len(synergies) == 0:
                value = ""
            value = f"HP: {character[9]} ATK: {character[10]} DEF: {character[11]} - Niveau {character[3]}\n" + value
            embed.add_field(name=f"{character[6]} [{rang}]", value=value, inline=False)
        majorite = max(rang_comptage, key=rang_comptage.get)
        embed.color = CONSTANTS['RARITY_COLOR'][majorite]
        return embed


    # Send initial embed
    inventory_msg = await message.channel.send(embed=create_embed(page_index))
    if len(pages) > 1:
        await inventory_msg.add_reaction('◀️')
        await inventory_msg.add_reaction('▶️')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['◀️', '▶️'] and reaction.message.id == inventory_msg.id

    # Reaction-based pagination
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=4.0, check=check)
            if str(reaction.emoji) == '▶️' and page_index + 1 < len(pages):
                page_index += 1
                await inventory_msg.edit(embed=create_embed(page_index))
            elif str(reaction.emoji) == '◀️' and page_index > 0:
                page_index -= 1
                await inventory_msg.edit(embed=create_embed(page_index))
        except asyncio.TimeoutError:
            break

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
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
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
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
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
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
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
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    embed.set_footer(text="Pour voir votre team, tapez !team.")
 
    embed.set_image(url=image)

    await message.channel.send(embed=embed)
    return

async def fetch_user_from_message(message, nombre_arguments_max=2):
    # Permet de récupérer un utilisateur à partir d'un message
    try:
        parts = message.content.split(' ')
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
    if message.author.id not in [724383641752436757,617045747862470803]:
        await message.channel.send(embed=embed_info("Erreur", "Vous n'avez pas la permission de faire cela!", discord.Color.red()))
        return
    database.reset(False)
    await message.channel.send(embed=embed_info("Base de données réinitialisée", "La base de données a été réinitialisée!", discord.Color.green()))

@bot.command()
async def classement(message, userFromDb):
    classement = database.getClassement(message.guild.members)
    max_length = 10
    classement = classement[:max_length]
    titre = "Classement des joueurs de " + message.guild.name + " :"
    response = ""
    for index, joueur in enumerate(classement):
        identifiant = joueur[0]
        user = await message.guild.fetch_member(identifiant)
        response += f"{index + 1}. {user.name} - {joueur[1]} puissance\n"
    await message.channel.send(embed=embed_info(titre, response, discord.Color.blue(),"La puissance est calculée en fonction des niveaux et des personnages de votre inventaire."))


def get_color_based_on_power(power):
    power_ranges = {
        100: CONSTANTS['RARITY_COLOR']['F'],
        200: CONSTANTS['RARITY_COLOR']['E'],
        300: CONSTANTS['RARITY_COLOR']['D'],
        float('inf'): CONSTANTS['RARITY_COLOR']['C']  # Supposons que tout supérieur à 300 est 'C'
    }

    for threshold, color in power_ranges.items():
        if power < threshold:
            return color
    return CONSTANTS['RARIY_COLOR']['C']  # Fallback par sécurité


@bot.command()
async def getPower(message, userFromDb):
    user = await fetch_user_from_message(message, 2)
    if not user:
        await message.channel.send(embed=embed_info("Utilisateur invalide", "L'utilisateur n'est pas valide ou n'a pas encore joué au jeu!", discord.Color.red()))
        return
    if user == "ERROR_SYNTAX":
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!power** ou **!power <joueur>**!", discord.Color.red()))
        return
    power = database.getPower(user.id)
    # On atribue une couleur en fonction de la puissance
    color = get_color_based_on_power(power)
    await message.channel.send(embed=embed_auteur(user, name=f"", description=f"Votre puissance est de **{power}**!", couleur=color))
        

@bot.command()
async def setLevel(message, userFromDb):
    level = message.content.split(' ')[1]
    if not level.isdigit():
        await message.channel.send(embed=embed_info("Erreur", "Le niveau doit être un nombre!", discord.Color.red()))
        return
    level = int(level)
    if level < 1 or level > 100:
        await message.channel.send(embed=embed_info("Erreur", "Le niveau doit être compris entre 1 et 100!", discord.Color.red()))
        return
    database.setLevel(message.author.id, level)
    await message.channel.send(embed=embed_info("Niveau modifié", f"Votre niveau a été modifié à {level}!", discord.Color.green()))
# Fonction qui envoie un message d'information style embed d'information
def embed_info(title, description, color=discord.Color.blue(),footer=None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
    )
    if footer:
        embed.set_footer(text=footer)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    return embed

def embed_invocation(character_template, user=None):
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
    if not user:
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    else:
        embed.set_author(name=f"{user.name} a invoqué :", icon_url=user.avatar.url)
    if len(synergies) > 0:
        embed.set_footer(text="Synergies : " + " ~ ".join([synergie[3] for synergie in synergies]))
    return embed

def embed_auteur(auteur,name=None,titre="",description="",couleur=CONSTANTS['COLORS']['FROID'],footer=None):
    # Retourne un embed avec la photo de l'auteur et son nom en haut à gauche
    embed = discord.Embed(
        title=titre,
        description=description,
        color=couleur
    )
    nom = name if name else auteur.name
    embed.set_author(name=nom, icon_url=auteur.avatar.url)
    if footer:
        embed.set_footer(text=footer)
    return embed


@bot.command()
async def list_command(message, userFromDb):
    logger.info(f"Commande !list_command appelée par {message.author.name} ({message.author.id}).")
    commande = {
        "!tickets": "Permet de voir le nombre de tickets que vous avez.",
        "!hourly": "Permet de réclamer tickets  et expériences!",
        "!invo": "Permet d'invoquer un personnage.",
        "!inv": "Permet de voir votre inventaire.",
        "!givetickets *{joueur}* *{nombre}*": "Permet de donner des tickets à un autre joueur.",
        "!info *{personnage}*": "Permet de voir les informations d'un personnage.",
        "!team": "Permet de voir votre team.",
        "!ajouterteam *{position}* *{personnage}*": "Permet d'ajouter un personnage à votre team.",
        "!sell *{personnage}*": "Permet de vendre un personnage.",
        "!classement": "Permet de voir le classement des joueurs.",
        "!power": "Permet de voir votre puissance basé sur l'inventaire.",
    }
    
    embed = discord.Embed(
        title="Liste des commandes disponibles:",
        description="",
        color=discord.Color.blurple()
    )
    for key, value in commande.items():
        embed.add_field(name=key, value=value, inline=False)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    await message.channel.send(embed=embed)

commands = {
    "pow": getPower,
    "pui" : getPower,
    "tickets": getTickets,
    "hou": claimHourly,
    "dai": claimHourly,
    "admin": admin,
    "list": list_command,
    "help": list_command,
    "invo": invocation,
    "sum": invocation,
    "inv": inventaire,
    "pers": inventaire,
    "bag": inventaire,
    "givetickets": giveTicket,
    "donnertickets": giveTicket,
    "donnerticket": giveTicket,
    "giveticket": giveTicket,
    "give_tickets": giveTicket,
    "donner_tickets": giveTicket,
    "donner_ticket": giveTicket,
    "give_ticket": giveTicket,
    "info": info,
    "infos": infoSynergie,
    "te": voirTeam,
    "voi": voirTeam,
    "ajouterteam": ajouterTeam,
    "addteam": ajouterTeam,
    "add_team": ajouterTeam,
    "ajou": ajouterTeam,
    "sell": sell,
    "vendre": sell,
    "create": createTemplates,
    "his": histoire,
    "pur": purple,
    "cook": cookWithSanji,
    "laby": labyrinthe,
    "reset": reset,
    "coul": couleur,
    "liste": liste,
    "setlevel": setLevel,
    "test": test,
    "cla": classement,
    "ran": classement,
}





# Run the bot with the token
bot.run(getToken.getToken())
