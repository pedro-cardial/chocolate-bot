import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.members = True

with open("config.json", "r") as f:
    config = json.loads(f.read())

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

for file_ in os.listdir("./cmds"):
    if file_.endswith(".py"):
        bot.load_extension(f"cmds.{file_[:-3]}")

for file_ in os.listdir("./events"):
    if file_.endswith(".py"):
        bot.load_extension(f"events.{file_[:-3]}")

bot.run(config["token"])
