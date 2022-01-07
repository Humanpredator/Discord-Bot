import os
import psutil
import discord
from discord.ext import commands

 #Cpu Usage
cpufrq = (psutil.cpu_freq()[0])
cpuper = (psutil.cpu_percent(1))
corecoun = (psutil.cpu_count())

class CPU_Usage(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def cpsg(self, ctx):
        await ctx.send(f'//.....CPU-Usage.....//')
        await ctx.send(f'CpuFreq: {cpufrq}Hz')
        await ctx.send(f'CpuPercentage: {cpuper}%')
        await ctx.send(f'CoreCount: {corecoun}')     


def setup(client):
     client.add_cog(CPU_Usage(client))      