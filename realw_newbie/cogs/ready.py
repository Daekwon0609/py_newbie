from discord.ext import commands

class ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.bot.user)
        print(self.bot.user.id)
        print('Newbie BOT has Ready.')

def setup(bot):
    bot.add_cog(ready(bot))