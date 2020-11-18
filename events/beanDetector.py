import discord
from discord.ext import commands

class BeanDetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if "bean" in message.content.lower() and not message.author.bot:
            await message.channel.send("did someone say... BEAN?!?!??")

def setup(bot):
    bot.add_cog(BeanDetector(bot))