import discord
import os
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands
os.system('clear')
os.system('cls')


dotenv_path = Path('config.env')
load_dotenv(dotenv_path=dotenv_path)



client = commands.Bot(command_prefix = "/",help_command=None)

@client.event
async def on_ready():
    await client.get_channel(882567701174833155).send("Iam Online")
    print("Iam Online")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('BOT_TOKEN'))