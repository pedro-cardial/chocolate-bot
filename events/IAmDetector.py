import discord
from discord.ext import commands

class IAmDetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        split = message.content.lower().split()
        if "i am" in message.content.lower():
            index = split.index("am")
            name = ' '.join(split[index + 1:])
            await message.channel.send(f"Hi {name}, I'm Chocolate Bot")
            await message.author.edit(nick=name)
        elif "i'm" in message.content.lower():
            index = split.index("i'm")
            name = ' '.join(split[index + 1:])
            await message.channel.send(f"Hi {name}, I'm Chocolate Bot")
            await message.author.edit(nick=name)
        elif "im" in message.content.lower():
            index = split.index("im")
            name = ' '.join(split[index + 1:])
            await message.channel.send(f"Hi {name}, I'm Chocolate Bot")
            await message.author.edit(nick=name)

def setup(bot):
    bot.add_cog(IAmDetector(bot))