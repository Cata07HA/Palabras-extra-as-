import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=commands.when_mentioned, description="Nothing to see here!", intents=intents)

@bot.group(hidden=True)
async def secret(ctx: commands.Context):
    """What is this "secret" you speak of?"""
    if ctx.invoked_subcommand is None:
        await ctx.send('Shh!', delete_after=5)

bot.run('TOKEN')
