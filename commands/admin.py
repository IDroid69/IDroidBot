import discord
import asyncio
import datetime
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.utils import get


class Administrativo(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help = "Expulsa um membro do servidor.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, *, user: discord.Member=None, razao=None):
        
        try:
            if user is None:
                embed1 = discord.Embed(title="Mencione o Usuário que será expulso!", description="Ex.: !kick @user [motivo]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
                embed1.set_footer(text=f'Solicitado Por {ctx.author}')
                await ctx.send(embed=embed1)
                return
            
            else:
                await user.kick(reason=razao)
                await ctx.send(f'{ctx.author.name} comeu o caneco do {user}')
                embed = discord.Embed(title=f"Usuário(a) {user} Foi expulso", description=f"Expulso Por {ctx.author.mention}", timestamp=datetime.datetime.utcnow(), color=0xff0000)
                await ctx.send(embed=embed)
                return
        except discord.errors.errors.Forbidden:
            await ctx.send("Não tenho permissão para kickar esse usuário")
        
        
    @commands.command(help= "Bani um membro do servidor.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, *, member: discord.Member=None, razao=''):

        if member is None:
            embed1 = discord.Embed(title="Mencione o Usuário que será banido!", description="Ex.: !ban @user [motivo]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
            return
        
        else:
            await member.ban(reason=razao)
            await ctx.send(f'{ctx.author.mention} comeu o caneco do {member.mention}')
            embed2 = discord.Embed(title=f"Usuário(a) {member} foi banido!", description=f"Banido Por {ctx.author.mention}", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            await ctx.send(embed=embed2)


    @commands.command(help = "Desbani um membro do servidor.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member=None):
        if member is None:
            embed1 = discord.Embed(title="Mencione o Usuário que será desbanido!", description="Ex.: !unban @user", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
            return

        banned_users = await ctx.guild.bans()
        discord_Member, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (discord_Member, member_discriminator):
                await ctx.guild.unban(user)
                embed2 = discord.Embed(title=f"Usuário(a) {member} Foi desbanido", description=f"Desbanido Por {ctx.author.mention}", timestamp=datetime.datetime.utcnow(), color=0xff0000)
                await ctx.send(embed=embed2)
                return


    @commands.command(name='entrar', help='O bot entra na call')
    @commands.has_permissions(administrator = True)
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('Voçê não está em nenhuma call seu animal🙄')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            voice_channel.move_to(voice_channel)

    @commands.command(name='sair', help='O bot sai da call')
    @commands.has_permissions(administrator = True)
    async def leave(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("O bot não está em nenhuma call...")
        else:
            await ctx.voice_client.disconnect()

    @commands.command(help = "Move um membro de call. [O comando ainda não está completo.]")
    async def vmove(self, ctx, member : discord.Member=None,  channel: VoiceChannel=None):
        
        if member is None:
            embed = discord.Embed(title="Mencione o Usuário que será movido!", description="Ex.: !vmove **@user** [canal de voz]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed)
            return
        
        if channel is None:
            embed = discord.Embed(title="Diga para que canal o usuário será movido!", description="Ex.: !vmove @user **[canal de voz]**", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed)
            return
        
        else:
            await member.move_to(channel)
            return
        
    @commands.command(help = "[Este comando não está completo ainda...]")
    async def vkick(self, ctx, member: discord.Member=None):
        await member.disconnect()
        
    @commands.command(pass_context = True, help = "Muta um usuário do chat.")
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, mute_time:int=None):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        
        if member is None:
            embed1 = discord.Embed(title="Mencione o Usuário que será mutado!", description="Ex.: !mute @user [tempo]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
            return
        
        elif mute_time is None:
            await member.add_roles(role)
            embed=discord.Embed(title="O usuário foi mutado do chat!", 
                description=f"**{member}**  foi mutado por **{ctx.message.author}**!", 
                color=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            await member.add_roles(role)
            embed=discord.Embed(title="O usuário foi mutado do chat!", 
                description=f"**{member}**  foi mutado por **{ctx.message.author}**!", 
                color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(mute_time)
            await member.remove_roles(role)
            return
        
    @commands.command(pass_context = True, help = "Desmuta um usuário do chat.")
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if member is None:
            embed1 = discord.Embed(title="Mencione o Usuário que será desmutado!", description="Ex.: !unmute @user", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
            return
        else:
            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.remove_roles(role)
            
            embed=discord.Embed(title="O usuário foi desmutado do chat!", 
                description=f"**{member}**  foi desmutado por **{ctx.message.author}**!", 
                color=0xff0000)
            await ctx.send(embed=embed)
        

    @commands.command(help = "Apaga mensagens do chat.")
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, amount:int=None):
        if amount is None:
            embed1 = discord.Embed(title="Diga quantas mensagens será apagadas!", description="Ex.: !clear [número]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
        
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{ctx.author.mention} {amount} Mensagens foram apagadas!")
        
    @commands.command(pass_context = True, help = "Altera o nick de um membro.")
    @commands.has_permissions(administrator=True)
    async def setnick(self, ctx, member: discord.Member=None, nick=None):
        if member is None:
            embed1 = discord.Embed(title="Mencione o Usuário que terá o apelido mudado!", description="Ex.: !setnick @user [apelido]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
            
        elif nick is None:
            embed1 = discord.Embed(title="Diga o apelido", description="Ex.: !mute @user [`apelido`]", timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed1.set_footer(text=f'Solicitado Por {ctx.author}')
            await ctx.send(embed=embed1)
        
        else:
            await member.edit(nick = nick)
            await ctx.send(f'O apelido do {member.mention} foi alterado por {ctx.author.mention}')
        
    @commands.command(name="vedit")
    @commands.has_permissions(administrator=True)
    async def edit_channel(self, ctx, channel, new_name):
        
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel)
        
        if existing_channel is not None:
            await existing_channel.edit(name=new_name)
            
        else:
            await ctx.send(f'Nenhum canal chamado, "{channel}", foi encontrado.')
        
    @commands.command(name='vdelete')
    @commands.has_permissions(administrator=True)
    async def delete_channel(self, ctx, channel_name):
        
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        
        if existing_channel is not None:
            await existing_channel.delete()
        
        else:
            await ctx.send(f'Nenhum canal chamado, "{channel_name}", foi encontrado.')

    @commands.command(name="alldelete")
    @commands.has_permissions(administrator=True)
    async def delete_channels(self, ctx):
        [await channel.delete()
    for channel in ctx.guild.text_channels]

        [await VoiceChannel.delete()
    for VoiceChannel in ctx.guild.voice_channels]
        
    @commands.command(name="vcriar")
    async def create_channel(self, ctx, canal=None):

        if canal == None:
            embed = discord.Embed(
                title = "Voçê deve digitar o nome do canal que vai ser criado",
                description = "Ex: >vcriar [nome]",
                color = 0xff0000
            )

            await ctx.send(embed=embed)
            
        else:
            guild = ctx.guild
            member = ctx.author
            admin_role = get(guild.roles, name="parcerias")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await guild.create_voice_channel(canal, overwrites=overwrites)
            

def setup(bot):
    bot.add_cog(Administrativo(bot))