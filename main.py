import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    status = os.getenv('STATUS')
    await bot.change_presence(activity=discord.Game(name=status))

bot.run(os.getenv('TOKEN'))
