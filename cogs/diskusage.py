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

#DiskUsage 
dtotal = (psutil.disk_usage('/')[0])
dused = (psutil.disk_usage('/')[1])
dfree = (psutil.disk_usage('/')[2])
dper = (psutil.disk_usage('/')[3])

class Disk_Usage(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def disg(self, ctx):
        await ctx.send(f'//.....Disk-Usage.....//')
        await ctx.send(f'TotalDisk: {("{1}".format(dtotal,humanbytes(dtotal)))}')                                       
        await ctx.send(f'UsedDisk: {("{1}".format(dused,humanbytes(dused)))}')
        await ctx.send(f'FreeDisk: {("{1}".format(dfree,humanbytes(dfree)))}')
        await ctx.send(f'DiskPercentage: {dper}%')     


def setup(client):
     client.add_cog(Disk_Usage(client))      