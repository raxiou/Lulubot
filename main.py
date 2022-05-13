import discord
from discord.ext import commands
from discord_slash import SlashCommand
from cherche_perso import *
import json

# création du bot
bot = commands.Bot(command_prefix="k!")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
# quand le bot est pret ecrire prêt dans la console
async def on_ready():
    print('prêt')



@bot.command()
async def hero(ctx, jeu , *perso):
    perso_join = "-".join(perso)  # si le nom du personne est composé on en fait une seul chaine de caractère
    
    if jeu.upper() == 'E7':       
        data = cherche_persoE7(perso_join) #vas chercher les données du perso dans la base de données
    elif jeu.upper() == 'GENSHIN':
        data = cherche_perso_Genshin(perso_join)
        
    if data == False:
        await ctx.send('le hero qui vous avez envoyer n\'existe pas/n\'est pas encore dans la base de donnée ou a été mal orthographié')
    # création d'un embed
    embed = discord.Embed(title="**" + perso_join.capitalize() + "**", color=0x990066)
    embed.add_field(name="Attack :", value=data["stats"]["stat_general"]["atk"],  inline=True)
    embed.add_field(name="defense :", value=data["stats"]["stat_general"]["def"],  inline=True)
    embed.add_field(name="health :", value=data["stats"]["stat_general"]["hp"],  inline=True)
    if jeu.upper() == 'E7':
        
        embed.add_field(name="Critical Hit Chance :", value=data["stats"]["stat_general"]["chc"], inline=True)
        embed.add_field(name="Critical Hit Damage :", value=data["stats"]["stat_general"]["chd"], inline=True)
        embed.add_field(name="speeeeed :", value=data["stats"]["stat_general"]["spd"],  inline=True)
        embed.add_field(name="Effectiveness :", value=data["stats"]["stat_general"]["eff"], inline=True)
        embed.add_field(name="Effect Resistance :", value=data["stats"]["stat_general"]["efr"], inline=True)
    if jeu.upper() == 'GENSHIN':
        
        embed.add_field(name=f"{data['stats']['stat_general']['stat_elevation']['nom']} :", value=data["stats"]["stat_general"]['stat_elevation']['valeur'],  inline=True)
        
    await ctx.send(embed = embed)
 
        
        
        
@slash.slash(name='hero',
             guild_ids = [951418575351074826],
             description='description')
async def hero(ctx, jeu , perso):
    perso_join = "-".join(perso)  # si le nom du personne est composé on en fait une seul chaine de caractère
    
    if jeu.upper() == 'E7':       
        data = cherche_persoE7(perso_join) #vas chercher les données du perso dans la base de données
    elif jeu.upper() == 'GENSHIN':
        data = cherche_perso_genshin(perso_join)
        
    if data == False:
        await ctx.send('le hero qui vous avez envoyer n\'existe pas/n\'est pas encore dans la base de donnée ou a été mal orthographié')
    # création d'un embed
    embed = discord.Embed(title="**" + perso_join.capitalize() + "**", color=0x990066)
    embed.add_field(name="Attack :", value=data["stats"]["stat_general"]["atk"],  inline=True)
    embed.add_field(name="defense :", value=data["stats"]["stat_general"]["def"],  inline=True)
    embed.add_field(name="health :", value=data["stats"]["stat_general"]["hp"],  inline=True)
    if jeu.upper() == 'E7':
        
        embed.add_field(name="Critical Hit Chance :", value=data["stats"]["stat_general"]["chc"], inline=True)
        embed.add_field(name="Critical Hit Damage :", value=data["stats"]["stat_general"]["chd"], inline=True)
        embed.add_field(name="speeeeed :", value=data["stats"]["stat_general"]["spd"],  inline=True)
        embed.add_field(name="Effectiveness :", value=data["stats"]["stat_general"]["eff"], inline=True)
        embed.add_field(name="Effect Resistance :", value=data["stats"]["stat_general"]["efr"], inline=True)
    if jeu.upper() == 'GENSHIN':
        
        embed.add_field(name=f"{data['stats']['stat_general']['stat_elevation']['nom']} :", value=data["stats"]["stat_general"]['stat_elevation']['valeur'],  inline=True)
        
    await ctx.send(embed = embed)
        
        
        
        
        
        
        
        
        
        
        
        
        
@bot.command()
async def skills(ctx,jeu,nbSkill,*perso):
    perso_join = "-".join(perso)  # si le nom du personne est composé on en fait une seul chaine de caractère
    print('coucou')
    if jeu.upper() == 'E7':
        with open(f'BDD/bddE7/perso/{perso_join}.json','r', encoding='utf-8') as json_data:
            data_dict = json.load(json_data)
        data_dict = data_dict['skills'][nbSkill]
    
    elif jeu.upper() == 'GENSHIN':
        with open(f'BDD/bddGenshin/{perso_join}.json','r', encoding='utf-8') as json_data:
            data_dict = json.load(json_data)
        data_dict = data_dict['skills'][int(nbSkill)-1]

    print(data_dict)
        

    embed=discord.Embed(title="**" + perso_join.capitalize() + "**", color=0x00ff00)
    embed.add_field(name="description", value=data_dict['description'], inline=False)
    
    if jeu.upper() == 'E7':
        embed.add_field(name="cooldown", value=data_dict['cooldown'], inline=False)
        embed.add_field(name="gain d'ame", value=data_dict['gain_ame'], inline=False)
        embed.add_field(name="power", value=data_dict['power'], inline=False)
        embed.add_field(name="atk_rate", value=data_dict['atk_rate'], inline=False)
        
    elif jeu.upper() == 'GENSHIN':
        embed.add_field(name="type",value=data_dict['unlock'],inline=True)
      
    await ctx.send(embed = embed)
    
key = 'OTUxNDIwMjM2NTkzMjM4MDE2.YinNJA.AZ2zKwszog5WOIH1Jbh9vGNLC1M'
bot.run(key)