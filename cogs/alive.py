import discord
import os
from discord.ext import commands



class Alive(commands.Cog):

    def __init__(self,client):
        self.client = client

    #@commands.Cog.listener()
    #async def on_ready(self):
        #print('Iam Online')
          
    @commands.command()
    async def alive(self, ctx):
        await ctx.send('Iam Living For you')      


def setup(client):
     client.add_cog(Alive(client))      