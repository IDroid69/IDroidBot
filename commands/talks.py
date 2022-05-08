from discord.ext import commands
import discord

class Talks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name=('oi'), help='Manda um oi!')
    async def mandar_oi(self, ctx):
        nome = ctx.author.mention
        resposta = (f'Olá, {nome}')
    
        await ctx.send(resposta)
        
    @commands.command(name='segredo', help='Envia um segredo no seu privado!')
    async def segredo(self, ctx):
        try:
            await ctx.author.send('Esse foi alguns comandos que eu fiz! :)')
            await ctx.author.send('Bot feito por !Felipe#8945')
        except discord.errors.Forbidden:
            await ctx.send('''Não posso te contar o segredo, habilide receber 
    mensagem de qualquer pessoa do servidor (Configuraçôes > Privacidade) ''')

def setup(bot):
    bot.add_cog(Talks(bot))