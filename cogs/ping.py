import discord
import os
import time
from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client

   
    @commands.command()
    async def ping(self,ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")   


def setup(client):
     client.add_cog(Ping(client))      