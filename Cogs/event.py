import discord
from discord.ext import commands
import traceback

class AppCmdEvent(commands.Cog):
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

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        orig_error = getattr(error, "original", error)
        error_msg = "".join(traceback.TracebackException.from_exception(orig_error).format())
        if isinstance(error, commands.errors.MissingPermissions):
            embed = discord.Embed(
                title="エラー-不明なコマンド",
                description="不明なコマンドです。`Cu!list`でコマンドを確認してください。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
                colour=0xff0000,
            )
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.errors.MissingPermissions):
            embed = discord.Embed(
                title="エラー-権限不足",
                description="権限が不足しています。権限設定をご確認ください。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
                colour=0xff0000,
            )
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="エラー",
                description="予期せぬエラーが発生しました。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
                colour=0xff0000,
            )
            await ctx.reply(embed=embed, mention_author=False)
            
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        await self.bot.change_presence(
            activity=discord.Activity(name=f"Ga!help | {str(servers)}servers | {str(members)}users", type=3)
        )
        
    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        await self.bot.change_presence(
            activity=discord.Activity(name=f"Ga!help | {str(servers)}servers | {str(members)}users", type=3)
        )

def setup(bot):
    return bot.add_cog(AppCmdEvent(bot))
