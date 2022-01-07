import discord
import os
import asyncio
import sys
import time
from discord import client
from discord.ext import commands

class Restart(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def restart(self,ctx):
        if commands.has_permissions(administrator=True):
            await ctx.send("Restarting bot...")
            await ctx.send("Bot Restarted.")
            os.execv(sys.executable, ['python'] + sys.argv)
        else: 
            await ctx.send(f'{client.user.id}Need Admin permission')


def setup(client):
     client.add_cog(Restart(client))   