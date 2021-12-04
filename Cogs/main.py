from discord.ext import commands
from discord_together import DiscordTogether

class AppCmdMain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        await self.bot.change_presence(
            activity=discord.Activity(name=f"Yb!help | {str(servers)}servers | {str(members)}users", type=3)
        )

    @commands.command()
    async def start(self,ctx):
        link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")

        
def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
