import discord
from discord.ext import commands
import random
import json
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..")


class Chocolate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chocolate(self, ctx):
        with open(f"{os.getcwd()}\\config.json", "r") as f:
            config = json.loads(f.read())
        try:
            elise = ctx.guild.get_member(<elise id>)
            nick = f"{random.choice(config['chocolates'])}_Elise"
            await elise.edit(nick=nick)
            await ctx.send(f"Changed Elise's nickname to {nick}")
        except:
            await ctx.send(f"Could not change Elise's nickname")


def setup(bot):
    bot.add_cog(Chocolate(bot))
