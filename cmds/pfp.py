import discord
from discord.ext import commands

class Pfp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pfp(self, ctx, member:discord.Member=None):
        if member:
            await ctx.send(member.avatar_url)
        else:
            await ctx.send(ctx.author.avatar_url)

def setup(bot):
    bot.add_cog(Pfp(bot))