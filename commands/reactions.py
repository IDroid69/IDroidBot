import discord
from discord import role
from discord.ext import commands
from discord.ext.commands.core import command


class Reactions(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #Esse comando só foi um teste...
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        
        if reaction.emoji == '👍':
            role = user.guild.get_role(921632821196492810)
            await user.add_roles(role)
        elif reaction.emoji == '👎':
            role = user.guild.get_role(921632866297872404)
            await user.add_roles(role)
        

def setup(bot):
    bot.add_cog(Reactions(bot))