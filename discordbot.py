import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Ge!", "ge!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
    case_insensitive=True
)


token = os.environ["token"]

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

bot.load_extension("jishaku")

bot.load_extension("Cogs.event")
bot.load_extension("Cogs.bot")

bot.run(token)
