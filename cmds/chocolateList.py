import discord
from discord.ext import commands
import json
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..")

class Chocolates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chocolatelist(self, ctx):
        with open(f"{os.getcwd()}\\config.json", "r") as f:
            config = json.loads(f.read())
        await ctx.send("\n".join(config["chocolates"]))


def setup(bot):
    bot.add_cog(Chocolates(bot))
