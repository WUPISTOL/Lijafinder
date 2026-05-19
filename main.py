import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore other bots

    if message.content.startswith("MAMASAY"):
        echo = message.content[len("MAMASAY"):].strip()
        if echo:
            await message.channel.send(echo)

    await bot.process_commands(message)  # Still lets ! commands work

async def main():
    async with bot:
        await bot.load_extension("cogs.combat")
        await bot.load_extension("cogs.dice")
        await bot.load_extension("cogs.sheets")
        await bot.start(os.getenv("DISCORD_TOKEN"))

import asyncio
asyncio.run(main())