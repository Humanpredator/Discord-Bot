import discord
import os
import time
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def help(self,ctx):
        await ctx.send(f'//.....Help-Command.....//')
        await ctx.send(f'use /alive To Check Iam online')
        await ctx.send(f'use /ping To Check Latency')
        await ctx.send(f'use /cpsg To Check Cpu-usage')
        await ctx.send(f'use /memsg To Check RAM-usage')
        await ctx.send(f'use /disk To check DiskUsage')
        await ctx.send(f'use /restart To restart bot')


def setup(client):
     client.add_cog(Help(client))   