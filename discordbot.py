import discord
from discord.ext import commands
from discord.http import Route
import os
import sys

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Yb!", "yb!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
    case_insensitive=True
)


@bot.command('youtube')
async def youtube(ctx):
    voice = ctx.author.voice

    if not voice:
        return await ctx.send('You have to be in a voice channel to use this command.')

    r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)

    payload = {
        'max_age': 0,
        'target_type': 2,
        'target_application_id': 755600276941176913
    }

    try:
        code = (await bot.http.request(r, json=payload))['code']
    except discord.Forbidden:
        return await ctx.send('I Need the `Create Invite` permission.')

    await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))

@bot.command('betrayal')
async def betrayal(ctx):
    voice = ctx.author.voice

    if not voice:
        return await ctx.send('You have to be in a voice channel to use this command.')

    r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)

    payload = {
        'max_age': 0,
        'target_type': 2,
        'target_application_id': 773336526917861400
    }

    try:
        code = (await bot.http.request(r, json=payload))['code']
    except discord.Forbidden:
        return await ctx.send('I Need the `Create Invite` permission.')

    await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))

@bot.command('fishington')
async def fishington(ctx):
    voice = ctx.author.voice

    if not voice:
        return await ctx.send('You have to be in a voice channel to use this command.')

    r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)

    payload = {
        'max_age': 0,
        'target_type': 2,
        'target_application_id': 814288819477020702
    }

    try:
        code = (await bot.http.request(r, json=payload))['code']
    except discord.Forbidden:
        return await ctx.send('I Need the `Create Invite` permission.')

    await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))
    
token = os.environ["token"]

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

bot.load_extension("jishaku")

bot.run(token)
