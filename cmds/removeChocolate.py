import discord
from discord.ext import commands
import os
import json

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..")


class RemoveChocolate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def removechocolate(self, ctx, *toRemove):
        # open(f"{os.getcwd()}\\config.json", "w+" || "r+") didn't work
        with open(f"{os.getcwd()}\\config.json", "r") as f:
            config = json.loads(f.read())
        if " ".join(toRemove) in config["chocolates"]:
            with open(f"{os.getcwd()}\\config.json", "w") as f:
                config["chocolates"].remove(' '.join(toRemove))
                f.write(json.dumps(config))
            await ctx.send(f"{' '.join(toRemove)} was removed from the list of chocolates")
        else:
            await ctx.send(f"{' '.join(toRemove)} is not on the list of chocolates")


def setup(bot):
    bot.add_cog(RemoveChocolate(bot))
