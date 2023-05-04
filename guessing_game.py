from typing import Self
import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

    answer = random.randint(1, 10)

    try:
        guess = await Self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await discord.Message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')

bot.run("TOKEN")
