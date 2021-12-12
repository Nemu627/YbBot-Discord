import discord
from discord.ext import commands
import asyncio

class AppCmdBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="ヘルプ", description="ちわーっす！\nVoice Channel Activities BOT！Ybっす！", colour=0xff0000)
        embed.add_field(
            name=":robot: 》コマンドリスト",
            value="`help`：ヘルプを表示します。\n"
                  "`ping`：YbBOTのping値を表示します。\n"
                  "`youtube`：YouTubeTogetherを開始します。\n"
                  "`betrayal`：Betrayal.ioを開始します。\n"
                  "`fishington`：Fishington.ioを開始します。",
        )
        await ctx.reply(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="PING", description=f"ただいまのping値は**{round(self.bot.latency * 1000)}**msです！",
                              color=0xff0000)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
