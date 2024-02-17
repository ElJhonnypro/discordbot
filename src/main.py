import json
import discord
from discord.ext import commands
import base64
import random
import asyncio
import os
import sqlite3

def connect_db():
    return sqlite3.connect("database/secretos.db")
    
conn = connect_db()

cursor = conn.cursor()

with open("../data.json", 'r+') as datafile:
    data = json.load(datafile)


token = base64.b64decode(data['token']).decode('utf-8')
description = "bot del JhP-Y"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} Ha despertado')


@bot.event
async def on_member_join(member):
    frases = ['Bienvenido Trajiste pizza? Tenemos hambre','Bienvenido pareces cool!','Bienvenido Como estas!']
    
    general_channel = discord.utils.get(member.guild.channels, name="general")
    if general_channel:
        await general_channel.send(f'Hola {member.mention} {random.choice(frases)}')


@bot.command()
async def secreto(ctx, *secreto):
    secreto = " ".join(secreto)
    cursor.execute('INSERT INTO secrets (member, secret, server) VALUES (?,?,?)', (ctx.author.global_name, secreto, ctx.guild.name))
    conn.commit()
    await ctx.send(f'ya escuche tu secreto {ctx.author.mention} lo guardare')
    await asyncio.sleep(1.5)
    await ctx.message.delete()
    
    async for message in ctx.channel.history(limit=10):
        if message.author == bot.user:
            await message.delete()
            break


memes = [archivo for archivo in os.listdir('images/memes') if os.path.isfile(os.path.join('images/memes', archivo))]

@bot.command()
async def dameunmeme(ctx):
    meme = random.choice(memes)
    meme_archivo = f'images/memes/{meme}'
    with open(meme_archivo, "rb") as Meme:
        memeenviar = discord.File(Meme)
    
    if meme == 'meme8.jpeg':
        await ctx.send("Aqui esta tu meme **random** :", file=memeenviar)
        await ctx.send('(Si soy :pensive:)')
    elif meme == 'meme3.jpeg':
        await ctx.send("Aqui esta tu meme **random** :")
    else:
        await ctx.send("Aqui esta tu meme **random** :", file=memeenviar)

bot.run(token)