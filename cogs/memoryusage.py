import os
import psutil
import discord
from discord.ext import commands

#BitConversion
def humanbytes(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)

#memory Usage
mtotal = (psutil.virtual_memory()[0])
mused = (psutil.virtual_memory()[3])
mfree = (psutil.virtual_memory()[4])
mper = (psutil.virtual_memory()[2])

class Memory_Usage(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def memsg(self, ctx):
        await ctx.send(f'//.....RAM-Usage.....//')
        await ctx.send(f'TotalMemory: {("{1}".format(mtotal,humanbytes(mtotal)))}')                                       
        await ctx.send(f'UsedMemory: {("{1}".format(mused,humanbytes(mused)))}')
        await ctx.send(f'FreeMemory: {("{1}".format(mfree,humanbytes(mfree)))}')
        await ctx.send(f'MemoryPercentage: {mper}%')     


def setup(client):
     client.add_cog(Memory_Usage(client))      