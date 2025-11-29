import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def meme(ctx):
    # Lista todos los archivos dentro de la carpeta "imagenes"
    files = os.listdir("imagenes")

    # Elige uno al azar
    img_name = random.choice(files)

    # Abre el archivo y lo envía
    with open(f"imagenes/{img_name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run('TOKEN')
