import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="VSCode?", type=3)
        await self.bot.change_presence(activity=activity)
        print(f'Estou pronto!✅ Estou conectado como {self.bot.user}')
        
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} Por favor enviar todos os argumentos.')
        elif isinstance(error, CommandNotFound):
            await ctx.send(f'{ctx.author.mention} O comando não existe.')
        elif isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.author.mention} Voçê não tem permissão para usar esse comando!')
        else:
            raise error

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(
            color=0x00FFF7,
        )

        embed.set_author(name='Menu de Ajuda!', icon_url=self.bot.user.avatar_url)
        embed.set_footer(text='feito por ' + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.add_field(
            name='Comandos para Administrador:',
            value='''**!kick:** `Expulsa um membro do servidor.`
**!ban:** `Bani um membro do servidor.`
**!unban:** `Desbani um membro do servidor.`
**!entrar:** `O bot entra na call.`
**!sair:** `O bot sai da call.`
**!mute:** `Muta um usuário do chat.`
**!unmute:** `Desmuta um usuário do chat.`
**!clear:** `Apaga mensagens do chat.`
**!setnick:** `Altera o nick de um membro.`''')


        embed.add_field(
            name='Outros:',
            value='''**!calcular:** `Calcula uma expresão para voçê!`
**!beijar:** `Dar um beijo em alguem!`
**!tapa:** `Dar um tapa em alguem!`
**!abracar:** `Dar um abraço em alguem!`
**!idroid:** `Dar uma mamada no Felipe!`
**!oi:** `Manda um oi!`
**!segredo:** `Envia um segredo no seu privado!`''')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Manager(bot))