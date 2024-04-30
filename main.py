# Import the required modules
import asyncio
import os
import random
import discord
from discord import File
from discord.ext import commands 
from constantes import CONSTANTS
import getToken
import bdd
from loguru import logger
from constantes import phrases_invocation, ennemis
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
    # Sauf si c'est la commande inventaire
    if command != inventaire:
        user_locks[userFromDb[0]] = asyncio.Lock()
        try:
            # Attendre l'acquisition du verrou
            async with user_locks[userFromDb[0]]:
                await command(message, userFromDb)
        finally:
            # Assurez-vous de libérer le verrou après l'exécution de la commande
            del user_locks[userFromDb[0]]
    else:
        await command(message, userFromDb)

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
        7: niveau7, 8: niveau8, 9: niveau9,
        10: niveau10, 11: niveau11, 12 : niveau12,
        13: niveau13
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

async def niveau13(message, userFromDb, equipe):
    # Début de niveau : maison abandonnée
    await debutDeNiveau(message, userFromDb, 13, "La maison abandonnée", equipe, CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    # On décide de retourner voir le village pour voir comment ça évolue mais sur la route on apercoit une immense maison
    await message.channel.send(embed=embed_naratteur("Vous décidez de partir en route vers le village pour voir si les habitants se remettent de l'attaque.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5.5)
    await message.channel.send(embed=embed_naratteur("Sur la route, vous apercevez une immense maison semblant abandonnée.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4.5)
    # On décide d'aller voir ce qu'il se passe
    await message.channel.send(embed=embed_naratteur("Vous décidez d'aller visiter la maison.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    ticket_ramasses = await labyrinthe(message, userFromDb, equipe)
    if ticket_ramasses < 0:
        return await echecNiveau(message, userFromDb, 13)
    await asyncio.sleep(1)
    # Vous descendez dans la cave
    await message.channel.send(embed=embed_naratteur("Vous descendez dans la cave..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("En descendant dans la cave, vous sentez une présence derrière vous..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_naratteur("...", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(3)
    await finDeNiveau(message, userFromDb, 14)
    

async def niveau12(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 12, "Ticket de Diamant", equipe, CONSTANTS['COLORS']['TICKET_DIAMANT'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("En sortant de la montagne, vous croisez Zuko..", "", CONSTANTS['COLORS']['MONTAGNE']))
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous félicite :", "", "zuko", "", "Félicitations, tu as réussi la tâche que je t'ai confié.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko est étonné par nos explications :", "", "zuko", "", "Vraiment ?.. J'ignorais qu'il y avait deux membres ici.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous raconte :", "", "zuko", "", "De mon côté, j'ai affronté un membre redoutable nommé Feitan. C'était très éprouvant mais j'ai réussi à le battre.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous informe :", "", "zuko", "", "J'ai obtenu des réponses. Le prêtre s'appelle en réalité Enrico Pucci.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous informe :", "", "zuko", "", "Il est en train de former un culte et a bâti un château sur la plaine principale.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous propose un plan :", "", "zuko", "", "Occupons nous d'abord de la brigade, puis nous nous occuperons de Pucci.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko vous félicite à nouveau :", "", "zuko", "", "Tiens un objet qui pourrait t'être utile.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_info("Vous avez reçu un Ticket de Diamant!", "", CONSTANTS['COLORS']['TICKET_DIAMANT'] ,"Votre prochaine invocation sera garantie de qualité supérieure!"))
    database.update_special_invocation(userFromDb[1], 1)
    await asyncio.sleep(5)
    await message.channel.send(embed=embed_naratteur("Zuko s'en va.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 13)

async def niveau11(message, userFromDb, equipe):
    # libération
    hasRun = database.getChoice(userFromDb[1], "lvl10run")
    if hasRun:
        await debutDeNiveau(message, userFromDb, 11, "La seule rescapée", equipe, CONSTANTS['COLORS']['C18'])
        await asyncio.sleep(4)
        # On revient vers la grotte, mais Uvoguin avait détruit une grosse partie avant de nous rattraper
        await message.channel.send(embed=embed_naratteur("Vous revenez vers la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Mais vous ne constatez que des horreurs, Uvoguine a détruit une majeure partie de la grotte lorsque vous avez fui.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous entendez cependant quelqu'un au fond..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous vous précipitez vers la personne..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "La personne vous rassure : ", "c18recoiffe", "c18", "", "Ne t'inquiète pas, mon corp peut résister à ça.", CONSTANTS['COLORS']['C18'])
        # Surpris, on lui demande comment ça se fait
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Surpris, vous lui demandez comment c'est possible.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "C18 :", "", "c18", "", "Je suis un cyborg et je m'appelle C-18, je peux résister à des dégâts que vous ne pouvez pas imaginer.", CONSTANTS['COLORS']['C18'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "C-18 :", "", "c18", "", "Grâce à vous on peut dire que je suis libérée.", CONSTANTS['COLORS']['C18'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "C-18 :", "", "c18", "", "Je vous en suis reconnaissante. Permettez moi de joindre votre équipe.", CONSTANTS['COLORS']['C18'])
        await asyncio.sleep(5)
        await giveCharacterHistory(message, userFromDb, "c18")
        await asyncio.sleep(4.5)
    else:
        await debutDeNiveau(message, userFromDb, 11, "Un nouvel allié!", equipe, CONSTANTS['COLORS']['LEORIO'])
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous revenez vers la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Votre combat a fait beaucoup de dégâts..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        # La grotte est entrain de s'écrouler, la plus part des gens sont morts
        await message.channel.send(embed=embed_naratteur("La grotte s'écroule..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("La plupart des prisonniers sont morts mais il semble rester quatre personnes.", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        # Il semblerait que vous n'ayez le temps que pour un seul prisonnier
        await message.channel.send(embed=embed_naratteur("Vous n'avez le temps de libérer qu'un seul prisonnier..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        description = "🤡 : Un homme ressemblant à un clown\n🧒 : Un adolescent aux cheveux ébouriffés\n👔 : Un jeune homme en costume\n👱‍♂️ : Un grand homme blond et charismatique"
        msg = await message.channel.send(embed=embed_naratteur("Qui choisissez-vous de libérer?", description, CONSTANTS['COLORS']['BRUIT']))
        for reaction in ['🤡', '🧒', '👔', '👱‍♂️']:
            await msg.add_reaction(reaction)
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🤡', '🧒', '👔', '👱‍♂️'])
        except:
            await message.channel.send(embed=embed_info("Vous avez mis trop de temps et la grotte s'est écroulée.", "", discord.Color.red()))
            return await echecNiveau(message, userFromDb, 11)
        if str(reaction.emoji) == '🤡':
            await message.channel.send(embed=embed_raw("Vous avez libéré l'homme ressemblant à un clown.", "", CONSTANTS['COLORS']['BAGGY']))
            await asyncio.sleep(3)
            await embed_histoire_character(message, "L'homme vous remercie :", "", "baggy", "", "Merci BEAUCOUP, partons d'ici RAPIDEMENTT.", CONSTANTS['COLORS']['BAGGY'])
            await asyncio.sleep(4)
            # vous vous dépechez de sortir de la grotte
            await message.channel.send(embed=embed_naratteur("Vous vous dépêchez de sortir de la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "Baggy vous interpelle :", "", "baggy", "", "Je vous en suis reconnaissant, mon nom est Baggy, permettez-moi de combattre à vos côtés.", CONSTANTS['COLORS']['BAGGY'])
            await asyncio.sleep(5)
            nomPerso = "Baggy"
        elif str(reaction.emoji) == '🧒':
            await message.channel.send(embed=embed_raw("Vous avez libéré l'adolescent aux cheveux ébouriffés.", "", CONSTANTS['COLORS']['DENKI']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "L'adolescent vous remercie :", "", "denki", "", "Merci énormément, partons d'ici rapidement!!!!", CONSTANTS['COLORS']['DENKI'])
            await asyncio.sleep(4)
            # vous vous dépechez de sortir de la grotte
            await message.channel.send(embed=embed_naratteur("Vous vous dépêchez de sortir de la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "Denki vous interpelle :", "", "denki", "", "Je vous en suis reconnaissant, je m'appelle Denki, permettez-moi de combattre à vos côtés.", CONSTANTS['COLORS']['DENKI'])
            await asyncio.sleep(5)
            nomPerso = "Denki Kaminari"
        elif str(reaction.emoji) == '👔':
            await message.channel.send(embed=embed_raw("Vous avez libéré le jeune homme en costume.", "", CONSTANTS['COLORS']['LEORIO']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "Le jeune homme vous remercie :", "", "leorio", "", "Merci beaucoup, partons d'ici rapidement!", CONSTANTS['COLORS']['LEORIO'])
            await asyncio.sleep(4)
            # vous vous dépechez de sortir de la grotte
            await message.channel.send(embed=embed_naratteur("Vous vous dépêchez de sortir de la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "Leorio vous interpelle :", "", "leorio", "", "Je vous en suis reconnaissant, je m'appelle Leorio, permettez-moi de combattre à vos côtés.", CONSTANTS['COLORS']['LEORIO'])
            await asyncio.sleep(5)
            nomPerso = "Leorio"
        else:
            await message.channel.send(embed=embed_raw("Vous avez libéré le grand homme blond.", "", CONSTANTS['COLORS']['ERWIN']))
            await asyncio.sleep(3)
            await embed_histoire_character(message, "Le grand homme vous remercie :", "", "erwin", "", "Merci beaucoup, partons d'ici rapidement!", CONSTANTS['COLORS']['ERWIN'])
            await asyncio.sleep(4)
            # vous vous dépechez de sortir de la grotte
            await message.channel.send(embed=embed_naratteur("Vous vous dépêchez de sortir de la grotte..", "", CONSTANTS['COLORS']['BRUIT']))
            await asyncio.sleep(4)
            await embed_histoire_character(message, "Erwin vous interpelle :", "", "erwin", "", "Je vous en suis reconnaissant, je m'appelle Erwin, permettez-moi de combattre à vos côtés.", CONSTANTS['COLORS']['ERWIN'])
            await asyncio.sleep(5)
            nomPerso = "Erwin Smith"
        await giveCharacterHistory(message, userFromDb, nomPerso)
        await asyncio.sleep(4.5)
    await finDeNiveau(message, userFromDb, 12)

async def niveau10(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 10, "Encore un?", equipe, CONSTANTS['COLORS']['UVOGUINE'])
    await asyncio.sleep(4)
    # Après avoir vaincu Franklin, on continue notre route mais on entend des bruits venant d'une grotte
    await message.channel.send(embed=embed_naratteur("Après avoir vaincu Franklin, vous continuez votre route..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await embed_histoire_character(message, "", "grotte", "", "", "Vous entendez des cris venant d'une grotte..", CONSTANTS['COLORS']['FORET'],True)
    await asyncio.sleep(4)
    # Vous décidez d'aller voir ce qu'il se passe
    await message.channel.send(embed=embed_naratteur("Vous décidez d'aller voir ce qu'il se passe..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Des gens sont enfermés dans des cellules et nous crient de nous en aller le plus vite possible
    await embed_histoire_character(message, "Des gens enfermés dans des cellules vous crient :", "", "inconnu", "", "Partez!! Partez d'ici le plus vite possible!", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Un homme vous interpelle :", "uvoguine", "uvoguine", "", "On dirait bien que mon petit-déjeuner est arrivé!", CONSTANTS['COLORS']['UVOGUINE'])
    await asyncio.sleep(4)
    # QQue faire ? Fuir ou combattre
    description = "🏃 : Fuir avec lâcheté" + "\n⚔️ : Combattre avec honneur"
    msg = await message.channel.send(embed=embed_naratteur("Que faites-vous?", description, CONSTANTS['COLORS']['UVOGUINE']))
    for reaction in ['🏃','⚔️']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🏃', '⚔️'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à prendre une décision, Uvoguine n'a fait qu'une bouchée de vous.", "", discord.Color.red()))
        return await echecNiveau(message, userFromDb, 10)
    database.updateChoice(userFromDb[1], "lvl10run", str(reaction.emoji) != '⚔️')
    if str(reaction.emoji) == '🏃':
        await message.channel.send(embed=embed_info("Vous avez fui la grotte.", "", discord.Color.green()))
        await asyncio.sleep(4)
        # On entend un bruit d'explosion
        await message.channel.send(embed=embed_naratteur("Vous entendez un bruit d'explosion..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(3)
        # Mais uvoguine vous a rattrapé
        await embed_histoire_character(message, "Uvoguine vous interpelle :", "", "uvoguine", "", "Espèce de lâche. Tu ne peux pas m'échapper.", CONSTANTS['COLORS']['UVOGUINE'])
        await asyncio.sleep(4)
    
    # Combat avec Uvoguine
    if not await combatPvm(message, equipe, ennemis['UVOGUINE']):
        return await echecNiveau(message, userFromDb, 10)
    # Vous avez réussi à le battre
    await message.channel.send(embed=embed_naratteur("Vous avez réussi à battre Uvoguine et vous décidez de vous orienter vers les celulles.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 11)

async def niveau9(message, userFromDb, equipe):
    await debutDeNiveau(message, userFromDb, 9, "Synergie et fusillade", equipe, CONSTANTS['COLORS']['FRANKLIN'])
    await asyncio.sleep(3)
    # On vérifie que l'utilisateur à bien une synergie dans son équipe
    team = database.get_team(userFromDb[1], userFromDb[2])
    synergies = team['synergies']
    if not synergies:
        await message.channel.send(embed=embed_info("Votre équipe ne présente pas de synergie.", "Vous feriez mieux d'écouter les conseils de Zuko.", CONSTANTS['COLORS']['ZUKO']))
        await asyncio.sleep(2)
        return await echecNiveau(message, userFromDb, 9)
    await message.channel.send(embed=embed_naratteur("Super! Vous avez une synergie dans votre équipe!", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Vous partez vers l'ouest 
    await message.channel.send(embed=embed_naratteur("Vous partez vers l'ouest suite à la demande de Zuko.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Sur la route, vous croisez petit à petit des groupes
    await message.channel.send(embed=embed_naratteur("Sur la route, vous commencez à croiser de plus en plus de regroupements de personnes.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Les gens commencent à se regrouper
    await message.channel.send(embed=embed_naratteur("Votre voyage se passe bien.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Après 4h de route, vous arrivez devant une montagne et vous êtes attaqués subitement par un membre de la brigade fantôme, c'est Pakunoda
    await message.channel.send(embed=embed_naratteur("Après quatre heures de route, vous arrivez devant la montagne décrite par Zuko..", "", CONSTANTS['COLORS']['MONTAGNE']))
    await asyncio.sleep(4)
    # Franklin nous shoot dessus
    await embed_histoire_character(message, "Quelqu'un vous tire dessus!!", "franklinShoot", "franklin", "", "", CONSTANTS['COLORS']['FRANKLIN'])
    description = "➡️ : Esquiver à droite" + "\n⬅️ : Esquiver à gauche" + "\n🛡️ : Essayer de parer"
    emojis = ['➡️', '⬅️', '🛡️']
    for balle in range(3):
        # Une balle arrive sur vous, que faites vous, esquiver à droite, à gauche, essayer de parer
        addition = "autre " if balle > 0 else ""
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Une " + addition + " balle arrive sur vous..", "", CONSTANTS['COLORS']['FRANKLIN']))
        await asyncio.sleep(3)
        msg = await message.channel.send(embed=embed_naratteur("Que faites-vous?", description, CONSTANTS['COLORS']['FRANKLIN']))
        for reaction in emojis:
            await msg.add_reaction(reaction)
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in emojis)
        except:
            await message.channel.send(embed=embed_info("Vous n'avez pas pris de décision à temps et les balles vous ont tués!", "", discord.Color.red()))
            return await echecNiveau(message, userFromDb, 9)
        reussite = 0.9 > random.random()
        
        if str(reaction.emoji) == '🛡️':
            if reussite:
                await message.channel.send(embed=embed_info("Vous avez réussi à parer la balle!", "", discord.Color.green()))
            else:
                await message.channel.send(embed=embed_info("Vous n'avez pas réussi à parer la balle! Vous succombez à vos blessures.", "", discord.Color.red()))
                return await echecNiveau(message, userFromDb, 9)
        else:
            if reussite:
                await message.channel.send(embed=embed_info("Vous avez réussi à esquiver la balle!", "", discord.Color.green()))
            else:
                await message.channel.send(embed=embed_info("Vous n'avez pas réussi à esquiver la balle! Vous succombez à vos blessures.", "", discord.Color.red()))
                await asyncio.sleep(2)
                return await echecNiveau(message, userFromDb, 9)
            
    await asyncio.sleep(4)
    # On arrive à atteindre son corps à corps
    await message.channel.send(embed=embed_naratteur("Vous parvenez à vous rapprocher de votre adversaire.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Combat avec Franklin
    if not await combatPvm(message, equipe, ennemis['FRANKLIN']):
        return await echecNiveau(message, userFromDb, 9)
    # Vous avez réussi à le battre
    # Ce combat n'était pas de tout repos, vous continuez votre route mais votre instinct vous dit d'aller plus loin
    await message.channel.send(embed=embed_naratteur("Ce combat n'était pas de tout repos, vous avez finis la mission de Zuko mais votre instinct vous dit d'aller plus loin.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5)
    await finDeNiveau(message, userFromDb, 10)

async def niveau8(message, userFromDb, equipe):
    followedPucci = database.getChoice(userFromDb[1], "lvl6pucci")
    # Si followed Pucci Héros du Village, sinon Lâche
    if followedPucci:
        await debutDeNiveau(message, userFromDb, 8, "Paria du village", equipe, CONSTANTS['COLORS']['ZUKO'])
    else:
        await debutDeNiveau(message, userFromDb, 8, "Héros du village", equipe, discord.Color.gold())
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous vous réveillez dans une pièce sombre..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Zuko nous dit ah tu es
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Ah, tu es réveillé.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    if followedPucci:
        # Zuko nous dit qu'il a entendu des combats au loin et quil 'est intervenu
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "J'ai entendu des combats au loin, je suis intervenu aussi vite que j'ai pu.", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # J'ai réussi à terasser le monstre mais..
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "J'ai réussi à vaincre le monstre qui attaquait le village mais..", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # Ton ami aux cheveux blonds n'a pas survécu
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Ton ami aux cheveux blonds n'a pas survécu.", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # Le village t'en veut
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Le village t'en veut, ils te reprochent d'avoir fui le combat.", CONSTANTS['COLORS']['ZUKO'])
    else:
        # Zuko nous dit qu'il a entendu des combats au loin et quil 'est intervenu
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "J'ai entendu des combats au loin, je suis intervenu aussi vite que j'ai pu.", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # J'ai réussi à terasser le monstre mais..
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Ne t'en fais pas, j'ai réussi à vaincre le monstre qui attaquait le village", CONSTANTS['COLORS']['ZUKO'])
        await asyncio.sleep(4)
        # Tout le village t'ait reconnaissant de les avoir sauvé
        await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Tout le village t'est reconnaissant de les avoir sauvés.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Je dois partir rapidement à cause d'un terrible groupe d'individus.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Ils se font appeler la brigade fantome, ils font couler le sang partout.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Puis-je te demander une faveur?", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "J'aimerais que tu t'occupes d'un de leur membre qui se situe vers l'ouest.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "Zuko :", "", "zuko", "", "Tu devrais pouvoir le battre, mais assure toi quand même d'avoir une synergie dans ton équipe.", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Zuko s'en va.", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 9) 

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
        # Du feu jaillis de là bas
        await message.channel.send(embed=embed_naratteur("Des flammes jaillissent de là bas..", "", CONSTANTS['COLORS']['FLAMME']))
        await asyncio.sleep(4)
        await message.channel.send(embed=embed_naratteur("Vous entendez un petit bruit..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(1.5)
        # Le prêtre nous dit de rester concentré
        await embed_histoire_character(message, "Le prêtre mystérieux vous rappelle à l'ordre :", "", "pucci", "", "Reste concentré ici.", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Le prêtre vous attrape par la gorge et vous emporte avec lui", "pucciShot", "pucci", "", "", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(6)
        await message.channel.send(embed=embed_naratteur("Vous êtes projeté au loin, presque inconscient..", "", CONSTANTS['COLORS']['BRUIT']))
        await asyncio.sleep(4)
        await embed_histoire_character(message, "Le Prêtre vous donne un ultime avertissement :", "", "pucci", "", "C'est contre mes intérêts de t'éliminer maintenant.", CONSTANTS['COLORS']['ENRICO_PUCCI'])
        await asyncio.sleep(5)
        await embed_histoire_character(message, "Le Prêtre :", "", "pucci", "", "Donc disparaîs de ma vue, insecte.", CONSTANTS['COLORS']['ENRICO_PUCCI'])
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
    await message.channel.send(embed=embed_naratteur("Un bruit vous réveille alors que vous étiez entrain de vous reposer dans la caverne..", "", CONSTANTS['COLORS']['GROTTE']))
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
    await embed_histoire_character(message,"Shanks vous annonce :", "", "shanks", "", "Eh bien.. je dois faire route à part, je pars retrouver les miens!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    # Shanks part 
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "Je vous souhaite bonne chance!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(3)
    await message.channel.send(embed=embed_naratteur("Shanks s'en va..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(3)
    # On s'en va dans la forêt pour trouver un endroit sûr
    await message.channel.send(embed=embed_raw("Vous partez dans la forêt pour trouver un endroit sûr..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    # On croise quelqu'un 
    await embed_histoire_character(message,"Un inconnu vous interpelle", "", "inconnu", "", "Vous.., là-bas!", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko se présente :", "zuko", "zuko", "", "Je m'appelle Zuko!", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko vous raconte :", "", "zuko", "", "Je viens d'un pays en guerre, je suis arrivé ici il y a peu et rien n'y semble différent..", CONSTANTS['COLORS']['ZUKO'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Zuko :", "", "zuko", "", "Je cherche mon oncle, savez-vous où il se trouve par hasard?", CONSTANTS['COLORS']['ZUKO'])
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
        await embed_histoire_character(message,"Zuko vous remercie :", "", "zuko", "", "Super! Merci pour votre indication.", CONSTANTS['COLORS']['ZUKO'])

    else:
        await embed_histoire_character(message,"Zuko", "", "zuko", "", "Je vois.. Merci quand même.", CONSTANTS['COLORS']['ZUKO'])
    database.updateChoice(userFromDb[1], "lvl4zukoLie", str(reaction.emoji) == '🌍')
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
    await message.channel.send(embed=embed_naratteur("Vous continuez votre route dans la forêt mais vous sentez une présence..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_raw("Un homme perfide vous attaque.", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(3)
    if not await combatPvm(message, equipe, ennemis["Tompa"]):
        return await echecNiveau(message, userFromDb, 4)
    await asyncio.sleep(4)
    # QUelqu'un vous observait pendant votre combat et profite pour vous attaquer..
    await message.channel.send(embed=embed_naratteur("Un monstre vous observait pendant votre combat et profite pour vous attaquer également..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4.5)
    if not await combatPvm(message, equipe, ennemis["Rui"]):
        return await echecNiveau(message, userFromDb, 4)
    # Vous continuez votre route et apercevez une grotte au loin
    await message.channel.send(embed=embed_raw("Ces combats vous ont épuisés..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(3)
    await message.channel.send(embed=embed_naratteur("Vous continuez votre route et apercevez une grotte au loin..", "Vous partez vous reposer au sein de la grotte.", CONSTANTS['COLORS']['GROTTE']))
    await asyncio.sleep(4)
    await finDeNiveau(message, userFromDb, 5)

async def niveau3(message, userFromDb, equipe):
    ticketsGagnes = 0
    await debutDeNiveau(message, userFromDb, 3, "Vêtu de sang", equipe, CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(4)
    # Le bug qui se produit ne vous téléporte pas cette fois, mais la nuit est tombé d'un coup... 
    # Shanks est rassuré, le bug n'est pas si grave
    await embed_histoire_character(message, "Shanks est rassuré :", "", "shanks", "", "L'anomalie n'a pas l'air si grave.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("La nuit est tombée d'un coup suite à l'anomalie..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Vous parcourez la forêt à la recherche d'autres personnes ou de réponses et des murmures se font entendre au loin.
    await message.channel.send(embed=embed_naratteur("Vous partez en direction la forêt à la recherche d'autres personnes ou de réponses..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Alors que vous voyagez, des murmures se font entendre au loin..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Ces murmures sont étranges, comme s'ils étaient les échos du passés. Un évènement sûrement liés aux bugs.
    await message.channel.send(embed=embed_naratteur("Ces murmures sont étranges..", "*Comme s'ils étaient les échos du passé.*", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    # Après quelques temps, vous quittez la forêt, il commence subitement à faire très froid. Vous arrivez nez à nez avec un jeune garçon accompagné d'un homme, ils ont du sang sur eux. Vous n'avez même pas le temps de réfléchir qu'ils vous attaquent.
    await message.channel.send(embed=embed_naratteur("Vous quittez la forêt, il commence à faire très froid..", "", CONSTANTS['COLORS']['FROID']))
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Vous arrivez nez à nez avec un jeune garçon accompagné d'un homme.", "Ils ont du sang sur eux..", CONSTANTS['COLORS']['FROID']))
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Le jeune garçon vous attaque avant même que vous le réalisez.", "", "froid", "", "", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(3.5)
    if not await combatPvm(message, equipe, ennemis["Haku"]):
        return await echecNiveau(message, userFromDb, 3)
    # await embed_histoire_character(message, "Shanks est surpris :", "", "shanks", "", "Je ne vous pensais pas aussi fort.", CONSTANTS['COLORS']['SHANKS'])
    # await asyncio.sleep(4)
    await embed_histoire_character(message, "L'autre homme se jette sur vous :", "", "froid", "", "Tu ne vas pas t'en tirer comme ça!!", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Shanks immobilise l'homme avant qu'il ne vous attaque :", "shanksHaki", "shanks", "", "", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(5)
    await embed_histoire_character(message, "Shanks lui ordonne :", "", "shanks", "", "Reste bien sage et contente toi de répondre à mes questions.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(3)
    await embed_histoire_character(message, "L'inconnu est sous le choc :", "", "froid", "", "Hmpf..... Je suppose que je n'ai pas le choix..", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(4)
    await embed_histoire_character(message, "L'inconnu vous regarde :", "", "froid", "", "Mais ne rêvez pas, je ne répondrai qu'à une seule question.", CONSTANTS['COLORS']['FROID'])
    await asyncio.sleep(3.5)
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
        await asyncio.sleep(3)
        await embed_histoire_character(message, "Inconnu :", "", "froid", "", "Nous ne vous avons pas attaqué pour le plaisir, mais pour nous défendre.", CONSTANTS['COLORS']['FROID'])
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
    await embed_histoire_character(message, "Zabuza :", "", "zabuza", "", "Je reconnais ta puissance. Mon nom est Zabuza, laissez moi vous mettre en garde : nous nous recroiserons.", CONSTANTS['COLORS']['FROID'])
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
        return await echecNiveau(message, userFromDb, 2)
    if str(reaction.emoji) == '🗡️':
        await message.channel.send(embed=embed_raw("Vous attaquez les géants..", "", discord.Color.red()))
        await asyncio.sleep(2)
        if not await combatPvm(message, equipe, ennemis["Dorry et Broggy"]):
            return await echecNiveau(message, userFromDb, 2)
        await embed_histoire_character(message,"Shanks est perplexe :", "", "shanks", "", "Etait-ce vraiment le bon choix?\nLa violence est rarement la meilleure des solutions.", CONSTANTS['COLORS']['SHANKS'])
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
    await message.channel.send(embed=embed_naratteur("Cinématique : Enrico Pucci détruit l'univers...", "", CONSTANTS['COLORS']['ENRICO_PUCCI']))
    await asyncio.sleep(3)
    await debutDeNiveau(message, userFromDb, 1, "Introduction", equipe, CONSTANTS['COLORS']['ENRICO_PUCCI'])
    await asyncio.sleep(4.5)
    await message.channel.send(embed=embed_naratteur("Vous vous réveillez dans un indroit inconnu.. une autre personne semble ne pas être très loin..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4.5)
    await message.channel.send(embed=embed_naratteur("Vous semblez être dans une forêt..", "", CONSTANTS['COLORS']['FORET']))
    await asyncio.sleep(4.5)
    await embed_histoire_character(message,"Un homme inconnu vous demande : ", "", "inconnu", "", "Tout va bien?", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks se présente : ", "", "shanks", "", "Mon nom est Shanks.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks vous raconte :", "", "shanks", "", "J'étais avec mes compagnons sur mon navire lorsque le ciel s'est assombri.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(5)
    await embed_histoire_character(message,"Shanks :", "", "shanks", "", "J'ai alors aperçu une sorte de prêtre... et je me suis réveillé ici.", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Inconu", "", "inconnu", "", "Un bruit surgit..", CONSTANTS['COLORS']['INCONNU'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_naratteur("Un monstre vous attaque!", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(4)
    if not await combatPvm(message, equipe, ennemis["SAIBAMAN"]):
        return await echecNiveau(message, userFromDb, 1)
    await embed_histoire_character(message,"Shanks est étoné :", "", "shanks", "", "Oh mais tu sais te battre!", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await embed_histoire_character(message,"Shanks semble apercevoir quelque chose :", "", "shanks", "", "Serait-ce de la fumée vers là-bas?", CONSTANTS['COLORS']['SHANKS'])
    await asyncio.sleep(4)
    await message.channel.send(embed=embed_raw("Mais du côté opposé de la fumée, un bruit retentit dans la forêt..", "", CONSTANTS['COLORS']['BRUIT']))
    await asyncio.sleep(5)
    description = "🌲 : Aller vers la forêt" + "\n💨 : Aller vers la fumée"
    msg = await embed_histoire_character(message,"Shanks vous questionne :", "", "shanks", description, "Où devrions-nous aller?", CONSTANTS['COLORS']['SHANKS'])
    for reaction in ['🌲','💨']:
        await msg.add_reaction(reaction)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['🌲', '💨'])
    except:
        await message.channel.send(embed=embed_info("Vous avez mis trop de temps à répondre!", "", discord.Color.red()))
        return await echecNiveau(message, userFromDb, 1)
    if str(reaction.emoji) == '🌲':
        await message.channel.send(embed=embed_raw("Vous partez en route vers la forêt.", "", CONSTANTS['COLORS']['FORET']))
    if str(reaction.emoji) == '💨':
        await message.channel.send(embed=embed_raw("Vous partez en route vers la fumée.", "", CONSTANTS['COLORS']['BRUIT']))
    database.updateChoice(userFromDb[1], "lvl1fumee", str(reaction.emoji) == '💨')
    await asyncio.sleep(3)
    await finDeNiveau(message, userFromDb, 2)

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

async def echecNiveau(message, userFromDb, level):
    await message.channel.send(embed=embed_naratteur(f"Vous avez échoué au niveau {str(level)}", "", CONSTANTS['COLORS']['ZUKO'],footer="Réessayez ou renforcez votre équipe."))

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
    alive = True; escaped = False
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

async def labyrinthe(message, userFromDb, equipe):
    maison = {
    'Entrée': ['Salon', 'Écurie'],
    'Chambre Une': ['Salle de bain', 'Chambre Deux'],
    'Cuisine': ['Salon', 'Cellier','Bureau'],
    'Salon': ['Entrée', 'Cuisine', 'Bureau', 'Chambre Une'],
    'Salle de bain': ['Chambre Une'],
    'Bureau': ['Salon', 'Bibliothèque','Cuisine'],
    'Cave': [], 
    'Grenier': ['Chambre Trois'],
    'Cellier': ['Cuisine'],
    'Chambre Trois': ['Grenier', 'Chambre Deux','Écurie'],
    'Chambre Deux': ['Chambre Une', 'Chambre Trois'],
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
            # vous sentez une présence menaçante dans la forge
            await message.channel.send(embed=embed_info(f"Vous sentez une présence menaçante dans la forge..", "", ))
            await asyncio.sleep(3.3)
            # embed character il ne s'agissait uqe d'un petit chat
            await embed_histoire_character(message, "", "chatMaisonHantee", "", "", "Ce n'était qu'un petit chat!", CONSTANTS['COLORS']['GRAY_CAT'])
            await asyncio.sleep(5)
            # Le chat se transforme ..
            await message.channel.send(embed=embed_info(f"Qu-quoi ? Le chat se transforme..", "", discord.Color.darker_gray()))
            await asyncio.sleep(3.5)
            database.updateChoice(userFromDb[1], "lvl13chatMaisonHantee", True)
            if not await combatPvm(message, equipe, ennemis["YORUICHI"]):
                return -1
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
            await message.channel.send(embed=embed_info("Maison abandonnée", "Vous avez mis trop de temps à répondre!", CONSTANTS['COLORS']['ZUKO']))
            return -1
        pieceActuelle = listePiecesAvailables[listeEmojis.index(str(reaction.emoji))]
    return ticketsRamasses
        
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


async def giveCharacterHistory(message, userFromDb, characterName):
    # Donne l'histoire d'un personnage
    character = database.get_character_template_by_name(userFromDb[1], userFromDb[2],characterName)
    if not character:
        await message.channel.send(embed=embed_info("Erreur", "Personnage non trouvé!", discord.Color.red()))
        return
    await message.channel.send(embed=embed_invocation(character,recruter=True))
    # On lui ajoute le personnage
    database.create_character(userFromDb[1], userFromDb[2], character[0])
    return

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
    tickets = database.get_tickets(user.id)
    await message.channel.send(embed=embed_info(title=f"{user.name} a {tickets} tickets.",description="", color=discord.Color.blue()))

@bot.command()
async def claimHourly(message, userFromDb):
    user = message.author
    claim = database.claim_hourly(user.id, user.name)
    if claim[0]:
        titre = f"Vous avez obtenu {str(CONSTANTS['HOURLY_TICKETS'])} tickets et beaucoup d'expérience!"
        await message.channel.send(embed=embed_auteur(message.author,f"Récompense :",titre, "", discord.Color.green(), "Revenez dans une heure!"))
        if random.random() < 0.3:
            await asyncio.sleep(1)
            await message.channel.send(embed=embed_info("Récompense spéciale", "Vous avez obtenu un ticket bonus!", discord.Color.gold()))
            database.update_tickets(user.id, database.get_tickets(user.id) + 1)
        if random.random() < 0.05:
            await asyncio.sleep(1)
            await message.channel.send(embed=embed_info("Récompense spéciale", "Votre prochaine invocation sera chanceuse!", discord.Color.gold()))
            database.update_special_invocation(user.id, True)
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
async def invocation(message, userFromDb, lucky=False):
    # On vérifie si l'utilisateur a assez de tickets
    tickets = database.get_tickets(message.author.id)
    if tickets < CONSTANTS['INVOCATION_COST']:
        await message.channel.send(embed=embed_info("Vous n'avez pas assez de tickets pour invoquer!","", discord.Color.red()))
        return
    specialInvocation = userFromDb[9]
    if lucky:
        specialInvocation = True
    print(f"Invocation spéciale : {specialInvocation}")
    donnees = database.summon_character(message.author.id, message.author.name, specialInvocation)
    # SI la données est de type String, c'est une erreur
    if type(donnees) == str:
        if donnees == "ERROR_NO_CHARACTER":
            await message.channel.send(embed=embed_info("Erreur", "Aucun personnage n'a été trouvé!", discord.Color.red(), footer="Ticket remboursé."))
        elif donnees == "ERROR_MAX_CHARACTERS":
            await message.channel.send(embed=embed_info("Erreur", f"Vous avez atteint le nombre maximum de personnages {CONSTANTS['MAX_CHARACTERS']} !", discord.Color.red(),footer="Vendez des personnages avec !sell"))
        return
    template = donnees[0]
    if specialInvocation:
        await message.channel.send(embed=embed_info("Oh.. Mais c'est un Ticket de Diamant!", "", CONSTANTS['COLORS']['TICKET_DIAMANT']))
        await asyncio.sleep(2)
    msg = await message.channel.send(embed=embed_info("Invocation...", "Veuillez patienter...", discord.Color.gold()))
    rarityOfCharacter = template[2]
    if rarityOfCharacter in ['X','SS']:
        schema = random.choice(CONSTANTS['NOMS_GIF_INVOCATION'])
        nomDuGif = schema[0] ; texteAAfficher = schema[1] ; couleur = schema[2] ; nomPfp = schema[3]
        msg = await embed_histoire_character(message=message, nom=texteAAfficher, nomGif=nomDuGif, nomPfp=nomPfp, color=couleur, description="", titre="")
        # await asyncio.sleep(6)
        await msg.delete()
        await message.channel.send(embed=embed_invocation(template,message.author))
        
    elif rarityOfCharacter in ["F", "E", "D", "C"]:
        # await asyncio.sleep(3)
        await msg.edit(embed=embed_invocation(template,message.author))

    else:
        random.shuffle(phrases_invocation) # On mélange les phrases d'invocation
        nombreRotation = {"B" : 1, "A" : 2, "S" : 3}
        couleurs = [discord.Color.green(), discord.Color.blue(), discord.Color.purple(), discord.Color.orange(), discord.Color.red(), discord.Color.gold(), discord.Color.teal(), discord.Color.dark_gold(), discord.Color.dark_teal()]
        random.shuffle(couleurs) # On mélange les couleurs
        for i in range(nombreRotation[rarityOfCharacter]):
            # await asyncio.sleep(random.uniform(1, 2))
            await msg.edit(embed=embed_info("Invocation...", phrases_invocation[i] if i < 2 else phrases_invocation[i].upper(), couleurs[i]))
        # await asyncio.sleep(3)
        await msg.delete()
        await message.channel.send(embed=embed_invocation(template,message.author))
    return

@bot.command()
async def luckyInvocation(message, userFromDb):
    await invocation(message, userFromDb, True)

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
            reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
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
async def combatPvm(message, team, ennemi):
    logger.info(f"Commande !combatPvm appelée par {message.author.name} ({message.author.id})   contre {ennemi['nom']}.")
    await introductionCombat(message, team, ennemi)
    await asyncio.sleep(2)
    # Calcul des sommes des statistiques pour l'équipe et l'ennemi
    somme_stats_ennemi = ennemi['stats']['ATK'] + ennemi['stats']['DEF'] + ennemi['stats']['HP']
    somme_stats_team = team['stats']['ATK'] + team['stats']['DEF'] + team['stats']['HP']
    chanceVictory, combatType = statistiquesCombat(message,somme_stats_team, somme_stats_ennemi)
    #logger.info(f"Chances de victoire de l'équipe : {chanceVictory} - Type de combat : {combatType}")
    victoire = random.random() < chanceVictory
    logger.info(f"Résultat du combat : {'Victoire' if victoire else 'Défaite'}")
    if combatType == 0:
        # Combat facile, on ne montre qu'une attaque
        if victoire:
            personnageQuiJoue = random.choice(team['team'])[6]
        else:
            personnageQuiJoue = ennemi["nom"]
        await tour(message, personnageQuiJoue, team, onlyAttack=True)
    elif combatType == 1:
        # Combat Low diff
        # On montre 2 tours du gagnats et 1 tour du perdant dans un ordre aléatoire
        if victoire:
            ordre = ["team", "ennemi", "team"]
        else:
            ordre = ["ennemi", "team", "ennemi"]
        logger.info(f"Ordre des tours : {ordre}")
        for i in range(3):
            if ordre[i] == "team":
                personnageQuiJoue = random.choice(team['team'])[6]
            else:
                personnageQuiJoue = ennemi["nom"]
            await tour(message, personnageQuiJoue, team)
            await asyncio.sleep(3)
    elif combatType == 2:
        #Combat mid diff
        ordre = ["team", "ennemi", "team", "ennemi", "team"] 
        random.shuffle(ordre)
        if victoire:
            ordre.append("team")
        else:
            ordre.append("ennemi")
        logger.info(f"Ordre des tours : {ordre}")
        for i in range(6):
            if ordre[i] == "team":
                personnageQuiJoue = random.choice(team['team'])[6]
            else:
                personnageQuiJoue = ennemi["nom"]
            await tour(message, personnageQuiJoue, team)
            await asyncio.sleep(3)
    else:
        # Combat difficile
        ordre = ["team","ennemi","team","ennemi","team","ennemi","team"]
        random.shuffle(ordre)
        if victoire:
            ordre.append("team")
        else:
            ordre.append("ennemi")
        logger.info(f"Ordre des tours : {ordre}")
        for i in range(8):
            if ordre[i] == "team":
                personnageQuiJoue = random.choice(team['team'])[6]
            else:
                personnageQuiJoue = ennemi["nom"]
            await tour(message, personnageQuiJoue, team)
            await asyncio.sleep(3)
    await asyncio.sleep(2)
    await message.channel.send(embed=embed_info("Le combat semble être terminé ...", "", 0x00000))
    await asyncio.sleep(2)
    # Vous avez triomphé si on a gagné sinon on a perdu
    if victoire:
        await message.channel.send(embed=embed_info("Vous avez triomphé de l'adversaire !!", "", discord.Color.gold()))
    else:
        await message.channel.send(embed=embed_info("Vous avez été vaincu par l'ennemi!", "", discord.Color.red()))
    await asyncio.sleep(4)
    return victoire
    


    
async def tour(message, personnage, ennemi,onlyAttack=False):
    # Envoie un message pour le tour d'un personnage
    # On cherche si le personnage a des attaques gifs
    attaques = database.get_attaques_by_character_name(personnage)
    # Si le personnage a une attaque ET qu'il a de la chance
    if random.random() < 0.25: #message de suspens
        liste_messages = ["Le combat fait rage!", "Le combat est intense!", "Les combattants se jaugent!", "Mais qui l'emportera?", "Le combat est acharné!", "Le combat touche-t-il à sa fin?", "Le combat est serré!"]
        await message.channel.send(embed=embed_info(random.choice(liste_messages), "",discord.Color.dark_purple()))
        await asyncio.sleep(2.5)
    if attaques and len(attaques) > 0 and random.random() < 0.9:
        attaque = random.choice(attaques)
        nom = attaque[2]; verbe = attaque[3]; gif = attaque[4]; couleur = int(attaque[5][1:], 16)
        embed = discord.Embed(
            title=f"{personnage} {verbe} {nom}",
            color=couleur
        )
        if gif:
            embed.set_image(url=gif)
        await message.channel.send(embed=embed)
        await asyncio.sleep(1.5)
        return
    # Sinon, on envoie une attaque normale
    rdm = random.random()
    if rdm < 0.6 or onlyAttack:
        liste_attaques = ["attaque", "inflige des dégâts", "frappe fort"]
        await message.channel.send(embed=embed_info(f"{personnage} {random.choice(liste_attaques)}.", "",discord.Color.red()))
    elif rdm < 0.90:
        liste_defenses = ["se protège", "se défend", "se met en garde","est sur la défensive"]
        await message.channel.send(embed=embed_info(f"{personnage} {random.choice(liste_defenses)}.", "",discord.Color.blue()))
    else:
        liste_autres = ["se concentre", "observe l'ennemi", "prend une grande inspiration", "se prépare", "analyse les mouvements de l'ennemi"]
        await message.channel.send(embed=embed_info(f"{personnage} {random.choice(liste_autres)}.", "",discord.Color.brand_green()))
    

def statistiquesCombat(message, somme_stats_team, somme_stats_ennemi):
    # Calcul de la différence relative en pourcentage
    total_stats = somme_stats_ennemi + somme_stats_team
    if total_stats == 0:
        total_stats = 1  # Éviter la division par zéro

    difference_relative = (somme_stats_team - somme_stats_ennemi) / total_stats
    ajustement = min(0.40, abs(difference_relative))
    # Calcul des chances de victoire
    if somme_stats_team > somme_stats_ennemi:
        chance_victory_team = CONSTANTS['BASE_CHANCE_VICTORY'] + ajustement
    else:
        chance_victory_team = 1 - (CONSTANTS['BASE_CHANCE_VICTORY'] + ajustement)
    chance_victory_ennemy = 1 - chance_victory_team
    # Seuils pour la classification des combats basés sur la différence relative
    percentage_difference = abs(difference_relative * 100)  # Convertir en pourcentage
    
    if percentage_difference < 8:
        combat_type = 3 # TRES DIFFICILE
    elif percentage_difference < 15:
        combat_type = 2 # DIFFICILE
    elif percentage_difference < 25:
        combat_type = 1 # LOW DIFF
    else:
        combat_type = 0 # NO DIFF
    logger.info(f"Chances de victoire de l'équipe : {chance_victory_team} - Type de combat : {combat_type}")
    return chance_victory_team, combat_type


@bot.command()
async def introductionCombat(message, team, ennemi):
    # Affiche l'introduction du combat
    await message.channel.send(embed=embed_info("Un combat est sur le point de commencer!", "", discord.Color.red()))
    await asyncio.sleep(0.5)
    team_atk = team['stats']['ATK']; team_def = team['stats']['DEF']; team_hp = team['stats']['HP']
    titre = "Votre équipe est prête à combattre!"; statsTeam = f"HP:{team_hp} ATK:{team_atk} DEF:{team_def}"
    perso1 = team['team'][0]; perso2 = team['team'][1]; perso3 = team['team'][2]
    description1 = f"{perso1[6]} **[{perso1[7]}]**"; description2 = f"{perso2[6]} **[{perso2[7]}]**"; description3 = f"{perso3[6]} **[{perso3[7]}]**"
    embed = embed_character(message,team['team'][0], titre, description1, statsTeam)
    embed2 = embed_character(message,team['team'][1], titre, description1 + " ~ " + description2, statsTeam)
    embed3 = embed_character(message,team['team'][2], titre, description1 + " ~ " + description2 + " ~ " + description3, statsTeam)
    msg = await message.channel.send(embed=embed)
    await asyncio.sleep(2.5)
    await msg.edit(embed=embed2)
    await asyncio.sleep(2.5)
    await msg.edit(embed=embed3)
    await asyncio.sleep(2.5)
    embedVs = discord.Embed(
        title="VS",
        color=0xffcc33
    )
    await message.channel.send(embed=embedVs)
    await asyncio.sleep(2)
    if not ennemi['isNotGif']:
        isNotGif = False
    else:
        isNotGif = True
    await embed_histoire_character(message, ennemi['nom'], ennemi['nomGif'], ennemi['nomPfp'],"", "", ennemi['couleur'], isNotGif)
    


def embed_character(message, character,title="",description="", footer=""):
    # Retourne un embed avec les informations d'un personnage 
    nom = character[6]; hp = character[9]; atk = character[10]; defense = character[11]; rarity = character[7]; nomImage = character[8]
    embed = discord.Embed(
        title=title,
        description=description,
        color=CONSTANTS['RARITY_COLOR'][rarity],
    )
    embed.set_image(url=nomImage)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
    if footer:
        embed.set_footer(text=footer)
    return embed

    
    
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
    def formatteur(nombre):
        # Prend un nombre comme {0.4} et retourne 40%
        return str(int(nombre * 100)) + "%"
    embed.set_footer(text=f"Boost : {typeOfBoost} {formatteur(forceOfBoost)}")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    embed.add_field(name="Personnages", value=liste_personnages[:1999], inline=False)
    embed.set_image(url=image)
    
    await message.channel.send(embed=embed)

@bot.command()
async def infoTechnique(message, userFromDb):
    # Permet d'obtenir les informations d'une technique
    contenu = message.content
    if len(contenu.split(' ')) < 2:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!infotechnique <nom technique>**!", discord.Color.red()))
        return
    # On récupère le nom (tout ce qui suit le !info)
    nom = " ".join(contenu.split(' ')[1:])
    technique = database.get_technique_by_name(nom)
    if technique == None:
        await message.channel.send(embed=embed_info("Technique introuvable", "Cette technique **n'existe pas**!", discord.Color.red()))
        return
    
    # Création de l'embed
    nom = technique[2]; description = technique[3]; image = technique[4]; color = int(technique[5][1:], 16)
    charactersFromTechnique = database.get_character_template(technique[1])
    if not charactersFromTechnique:
        liste_personnages = "Aucun personnage n'a cette technique."
    else:
        liste_personnages = "Cette technique appartient à " + charactersFromTechnique[1]
    embed = discord.Embed(
        title=nom,
        description="",
        color=color
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    embed.set_footer(text=liste_personnages)
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
        footer += f"\nBonus de synergies : {bonus['HP']}HP {bonus['ATK']}ATK {bonus['DEF']}DEF "
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
    nomImage = character[8]
    print(character)
    print(nomImage)
    embed = discord.Embed(
        title=f"{ nom } occupe désormais la position { position }.",
        color=discord.Color.green()
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
    embed.set_footer(text="Pour voir votre team, tapez !team.")
    embed.set_image(url=nomImage)

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
    titre = "Voulez vous reset TOUTES les données ou seulement les personnages?"
    msg = await message.channel.send(embed=embed_info("Confirmation", titre, discord.Color.gold()))
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❌'])
    except:
        await message.channel.send(embed=embed_info("Temps écoulé", "Vous avez mis trop de temps à répondre!", discord.Color.red()))
        return
    if str(reaction.emoji) != '✅':
        database.resetCharactersTemplatesAndSynergies()
    else:
        database.reset()
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
async def fakeTeam(message, userFromDb):
    # Fonction pour tester la team
    # On créer les characters All Might, Sasuke et Gojo
    database.fakeTeam(message.author.id)
    await message.channel.send(embed=embed_info("Team ajoutée", "Votre team a été ajoutée!", discord.Color.green()))

@bot.command()
async def fakeCharacter(message, userFromDb):
    # Donne un personnage
    contenu = message.content
    if len(contenu.split(' ')) < 2:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!fakecharacter <nom personnage>**!", discord.Color.red()))
        return
    nom = " ".join(contenu.split(' ')[1:])
    character = database.get_character_template_by_name(message.author.id, message.author.name, nom)
    if character == None:
        await message.channel.send(embed=embed_info("Personnage introuvable", "Ce personnage **n'existe pas**!", discord.Color.red()))
        return
    database.create_character(message.author.id, message.author.name, character[0])
    await message.channel.send(embed=embed_info("Personnage ajouté", f"Vous avez obtenu **{nom}**!", discord.Color.green()))

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
async def afficherUnivers(message, userFromDb):
    univers = message.content.split(' ')[1]
    persos = database.getAllCharactersFromUniversName(univers)
    if persos == None or len(persos) == 0:
        await message.channel.send(embed=embed_info("Univers introuvable", "Cet univers n'existe pas!", discord.Color.red()))
        return
    prevention = "Etre vous sur dafficher " + str(len(persos)) + " personnages ?"
    if len(persos) > 10:
        msg = await message.channel.send(embed=embed_info("Attention", prevention, discord.Color.red()))
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❌'])
        except:
            await message.channel.send(embed=embed_info("Temps écoulé", "Vous avez mis trop de temps à répondre!", discord.Color.red()))
            return
        if str(reaction.emoji) != '✅':
            await message.channel.send(embed=embed_info("Affichage annulé", "Vous avez annulé l'affichage!", discord.Color.red()))
            return
    for perso in persos:
        nom = perso[0]; rarity = perso[1]; image = perso[2]; hp = perso[3]; atk = perso[4]; defense = perso[5]
        embed = discord.Embed(
            title=f"{nom} **[{rarity}]**",
            description=f"HP: {hp} ATK: {atk} DEF: {defense}",
            color=CONSTANTS['RARITY_COLOR'][rarity],
        )
        embed.set_image(url=image)
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)
        await message.channel.send(embed=embed)

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

def embed_invocation(character_template, user=None,recruter=False):
    """ Fonction qui retourne un embed pour l'invocation d'un personnage """
    character = character_template # Pour plus de lisibilité
    synergies = database.get_synergies_by_character_template(character[0])
    verbe = "recruté" if recruter else "invoqué"
    hp = character[4]; atk = character[5]; defense = character[6]; image = character[3]; nom = character[1]; rarity = character[2]
    embed = discord.Embed(
        title=f"{nom} **[{rarity}]**",
        description="Félicitations! Vous avez " + verbe + " un nouveau personnage!",
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
async def fakeStatistiquesCombat(message, userFromDb):
    # Fonction pour tester les statistiques de combat, sous forme !stat <nbTeam> <nbAllie>
    somme_stats_team = 0
    somme_stats_ennemi = 0
    if len(message.content.split(' ')) < 3:
        await message.channel.send(embed=embed_info("Erreur de syntaxe", "La commande doit être de la forme **!stat <nbTeam> <nbAllie>**!", discord.Color.red()))
        return
    somme_stats_team = int(message.content.split(' ')[1])
    somme_stats_ennemi = int(message.content.split(' ')[2])
    a = statistiquesCombat(message, somme_stats_team, somme_stats_ennemi)
    print(a)

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
    "add": ajouterTeam,        # "addteam", "add_team"
    "admi": admin,             # "admin"
    "aff": afficherUnivers,    # "affi"
    "bag": inventaire,         # "inv", "inventaire", "pers", "bag"
    "cla": classement,         # "cla", "ran"
    "cou": couleur,            # "coul"
    "cre": createTemplates,    # "create"
    "don": giveTicket,         # "donnertickets", "donnerticket", "donner_tickets", "donner_ticket"
    "fakeC": fakeCharacter,    # "fakeCh"
    "fakeS": fakeStatistiquesCombat,  # "stat"
    "fakeT": fakeTeam,         # "fakeT"
    "giv": giveTicket,         # "givetickets", "giveticket", "give_tickets", "give_ticket"
    "his": histoire,           # "his"
    "inf": info,               # "info"
    "infoT": infoTechnique,    # "infot"
    "infoS": infoSynergie,     # "infos"
    "lis": list_command,       # "list", "help"
    "luc": luckyInvocation,    # "luckyInv"
    "pur": purple,             # "pur"
    "pow": getPower,           # "pow", "pui"
    "res": reset,              # "reset"
    "sel": sell,               # "sell", "vendre"
    "set": setLevel,           # "setlevel"
    "su": invocation,          # "summon"
    "tic": getTickets,         # "tic"
    "te": voirTeam,            # "te", "voi"
}





# Run the bot with the token
bot.run(getToken.getToken())
