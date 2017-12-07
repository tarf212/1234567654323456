import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()  
client = commands.Bot(command_prefix = "i")


@client.event 
async def on_ready():
    print("-----------BotInfo_est_connecté------------")

@client.event
async def on_message(message):
    if message.content == ",owner":
        await client.send_message(message.channel, "Que dire sur le Fondateur à part qu'il tiens un serveur discord et une chaine YouTube : Capitaine Stunt")
    if message.content == ",gemu":
        await client.send_message(message.channel, "Gemu est un serveur gaming sur lequel vous pouvez discuter avec vos amis /ou les membres [en_developpement] , invitation : https://discord.gg/TbmkMGW , partager !") 
    if message.content == ",crack":
        await client.send_message(message.channel, "Ah ah voilà un petit malin qui veut cracké des comptes Spotify , Netflix , EA origin ...Bref voilà mon site : http://freekeys.craym.eu/ ne change pas les mots de passes")
    if message.content == ",moibi":
        await client.send_message(message.channel, "Mon créateur est : @!Mowgli.#7835 et j'en suis fière ! :)")
    if message.content == "bimaj":
        await client.send_message(message.channel, "Les messages ont bien été supprimés !!")
    if message.content == "biciao":
        await client.send_message(message.channel, "Oh , non ! Mon créateur me dit qui faut que j'ailles me couché ! A bientôt ! ")
    if message.content ==  ",membre":
        await client.send_message(message.channel, "Pour devenir un membre officiel du serveur il faut : parler régulièrement , faire des choses qui aide le serveur à avancer !")
    if message.content == ",staff":
        await client.send_message(message.channel, "Pour devenir un Staff mp un administrateur ou le fondateur")
    if message.content == ",helpstaff":
        await client.send_message(message.channel, "Vous avez un problème , besoin d'aide , mp un membre du Staff")
    if message.content == ",suggestion":
        await client.send_message(message.channel, "Si vous avez une suggestion pour le bot allez dans le channel suggestion puis mettez votre suggestion (exemple : Botinfo suggestion : blablabla)")
    if message.content == ",help":
        await client.send_message(message.channel, "Commande bot BotInfo :  ,suggestion  ,helpstaff  ,staff  ,owner  ,gemu  ,crack  ,moibi  ,membre  ,help           En développement")
    if message.content == "bimaint":
        await client.send_message(message.channel, "Maintenance du bot !")

client.run("Mzg3NjkwMTQ1MDA2MDkyMjg4.DQiIwA.FhK7XOEfk9wc2JmPW9dfJk1h_AU")
