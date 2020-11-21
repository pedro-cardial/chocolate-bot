import discord
from discord.ext import commands
import os
import json

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..")


class AddChocolate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addchocolate(self, ctx, *toAdd):
        # open(f"{os.getcwd()}\\config.json", "w+" || "r+") didn't work
        with open(f"{os.getcwd()}\\config.json", "r") as f:
            config = json.loads(f.read())
        if " ".join(toAdd) not in config["chocolates"]:
            with open(f"{os.getcwd()}\\config.json", "w") as f:
                config["chocolates"].append(' '.join(toAdd))
                f.write(json.dumps(config))
            await ctx.send(f"{' '.join(toAdd)} was added to the list of chocolates")
        else:
            await ctx.send(f"{' '.join(toAdd)} is already on the list of chocolates")


def setup(bot):
    bot.add_cog(AddChocolate(bot))
