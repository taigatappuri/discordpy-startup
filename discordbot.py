from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_voice_state_update(before, after):
  print("ボイスチャンネルで変化がありました")

client.run(token)

@bot.command()
async def ping(ctx):
    await ctx.send('うるさい')

@bot.command()
async def test(ctx):
    await ctx.send('testr')
    
bot.run(token)
