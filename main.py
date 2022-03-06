# importation des bibliotheque utile pour le programe

import discord
import random
from discord_slash import SlashCommand
from discord.ext import commands
from fonction.fonction_hero.Api_fonction import get_api
from fonction.fonction_hero.search_data import *
from fonction.fonction_hero.image_rec import image_recup
from fonction.fonction_tournois.tirage_au_sort import creation_tableau

# création du bot
bot = commands.Bot(command_prefix="l!")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
# quand le bot est pret ecrire prêt dans la console
async def on_ready():
    print('prêt')


@bot.command()
async def hero(ctx, *perso):
    perso_join = " ".join(perso)  # si le nom du personne est composé on en fait une seul chaine de caractère
    data = get_api(
        perso_join)  # utilise la fonction get_api qui nous permet d'avoir les donné sur le personage que l'on a demandé

    stat = stat_hero(data)  # utilise la fonction stat_hero pour recuperer un dictionnaire avec les stats du perso

    imprint = imprint_hero(data)

    # création d'un embed
    embed = discord.Embed(title="**" + perso_join + "**", description=perso_join + ": ", color=0x990066)

    # recuperation dans les donnée du personnage d'une image
    image = image_recup(data)

    embed.set_thumbnail(url=image)  # ajout de l'image a l'embed

    # ajout de l'imprint et du self imprint a l'embed
    try:
        value_imprint = str(imprint["grades"]["D"]) + " (D), " + str(imprint["grades"]["C"]) + " (C), " \
                        + str(imprint["grades"]["B"]) + " (B), " + str(imprint["grades"]["A"]) + " (A), " \
                        + str(imprint["grades"]["S"]) + " (S), " \
                        + str(imprint["grades"]["SS"]) + " (SS), " + str(imprint["grades"]["SSS"]) + " (SSS), "
    except KeyError:
        try:
            value_imprint = str(imprint["grades"]["C"]) + " (C), " \
                            + str(imprint["grades"]["B"]) + " (B), " + str(imprint["grades"]["A"]) + " (A), " \
                            + str(imprint["grades"]["S"]) + " (S), " \
                            + str(imprint["grades"]["SS"]) + " (SS), " + str(imprint["grades"]["SSS"]) + " (SSS), "
        except KeyError:
            value_imprint = str(imprint["grades"]["B"]) + " (B), " + str(imprint["grades"]["A"]) + " (A), " \
                            + str(imprint["grades"]["S"]) + " (S), " \
                            + str(imprint["grades"]["SS"]) + " (SS), " + str(imprint["grades"]["SSS"]) + " (SSS), "




    embed.add_field(name="imprint" + " - " + imprint["type"], value=value_imprint)

    # ajout des stat a l'embed
    embed.add_field(name="Attack :", value=stat['atk'], inline=True)
    embed.add_field(name="Health :", value=stat['hp'], inline=True)
    embed.add_field(name="Speed :", value=stat['spd'], inline=True)
    embed.add_field(name="Defense :", value=stat['def'], inline=True)
    embed.add_field(name="Critical Hit Chance :", value=str(int(stat['chc'] * 100)) + "%", inline=True)
    embed.add_field(name="Critical Hit Damage :", value=str(int(stat['chd'] * 100)) + "%", inline=True)
    embed.add_field(name="Effectiveness :", value=str(int(stat['eff'] * 300)) + "%", inline=True)
    embed.add_field(name="Effect Resistance :", value=str(int(stat['efr'] * 100)) + "%", inline=True)
    embed.add_field(name="Dual Attack Chance :", value=str(int(stat['dac'] * 100)) + "%", inline=True)

    # envoit de l'embed au complet
    await ctx.send(embed=embed)


@slash.slash(name='défi', description='description')
async def rta(ctx):
    # création de la liste des defi
    liste_defi = ['Que des 3* et 4* rgb', 'Un ban en plus', 'Interdit au ml', 'Que des waifus',
                  'Seulement 1 unité par classe', 'Pas de héros limités', 'Pas de chevaliers',
                  'pas de dps pur(perso à moins 12k hp et qui fait des dega)',
                  'Seulement 1 héros meta', 'Limited de speed < 260''pas de AOL']

    # choix d'un défi parmis la liste
    defi = random.choice(liste_defi)

    # création d'un embed
    embed = discord.Embed(title="La contrainte Est", description=defi, color=0xA22200)

    # envoit de l'embed au complet
    await ctx.send(embed=embed)


@bot.command()
async def skills(ctx, *perso):
    perso_join = " ".join(perso)  # si le nom du personne est composé on en fait une seul chaine de caractère
    data = get_api(
        perso_join)  # utilise la fonction get_api qui nous permet d'avoir les donné sur le personage que l'on a demandé

    skill = skills(data)  # utilise la fonction skills pour recuperer un dictionnaire avec les stats du perso

    skill_name = skill["0"]["name"]
    embed = discord.Embed(title="**" + "**", description=perso_join + ": ", color=0x990066)


@slash.slash(name='tirage_tournois',description='prend une liste de joueur et creer un arbre de tournois')
async def tirage_tournois(ctx, *joueur):
    # création de la liste de joueur
    joueur_liste = " ".join(joueur)
    joueur_liste = joueur_liste.split()
    print(joueur_liste)
    # creéation des match par tirage aléatoire
    Matchs = creation_tableau(joueur_liste)

    # création d'un embed
    embed = discord.Embed(title="Les matchs sont :", color=0xA22200)
    # boucle pour mettre les diférent match dans l'embed
    for i in range(len(Matchs)):
        embed.add_field(name="Match" + str(i+1), value=Matchs[i][0] + " contre " + Matchs[i][1])

    # envoit de l'embed au complet
    await ctx.send(embed=embed)


bot.run(key)
