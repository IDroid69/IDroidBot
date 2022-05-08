from turtle import title
from discord.ext import commands
import discord
import datetime
import random


class Images(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='testeembed', help='Apenas um teste de embed.')
    async def get_random_image(self, ctx):
        url_image = '''https://picsum.photos/1928/1080'''
        
        embed = discord.Embed(
            title='Feliz ou Triste?',
            description='endo endo endo comi o cu de quem tá lendo',
            color=0x0000FF,
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text='feito por ' + self.bot.user.name, icon_url=self.bot.user.avatar_url)
    
        embed.add_field(name='API', value='usamos a api do https://picsum.photos')
        embed.add_field(name='Parâmetros', value='{largura}/{altura}')
        embed.add_field(name='Exemplo', value=url_image, inline=False)

        embed.set_image(url=url_image)
    
        await ctx.send(embed=embed)
        
        
    @commands.command(name='beijar', help='Dar um beijo em alguem')
    async def get_kiss_image(self, ctx, member: discord.Member= None):
        if member is None:
            
            embed = discord.Embed(
                title="Mencione o Usuário!",
                description="Ex.: !beijar @user",
                timestamp=datetime.datetime.utcnow(),
                color=0xff0000)
            await ctx.send(embed = embed)
            return
        else:
            
            image1 = "https://i.pinimg.com/originals/11/8a/c9/118ac94d9f00f9b668223113a5944af4.gif"
            image2 = "http://67.media.tumblr.com/756c52d84caf10e177777d6ee8504581/tumblr_ngyt1mvACH1qg78wpo1_500.gif"
            image3 = "https://i.imgur.com/Rtu2JyU.gif"
            image4 = "https://acegif.com/wp-content/uploads/anime-kiss-30.gif"
            image5 = "https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-49.gif"
            image6 = "https://i.pinimg.com/originals/68/a3/7a/68a37a5a1b86f227b8e1169f33a6a6bb.gif"
            image7 = "https://c.tenor.com/9IHLn02sU7MAAAAC/anime-beijo.gif"
            
            url_image = random.choice([image1, image2, image3, image4, image5, image6,  image7])
            
            embed = discord.Embed(
                title = '❤', description=f'{ctx.author.mention} beijou {member.mention}'
            )
            embed.set_image(url=url_image)
            
            await ctx.send(embed = embed)
            return
        

    @commands.command(name="tapa")
    async def send_slap(self, ctx, member: discord.Member=None):
        if member is None:
            
            
            embed = discord.Embed(
                title="Mencione o Usuário!",
                description="Ex.: !tapa @user",
                timestamp=datetime.datetime.utcnow(),
                color=0xff0000)
            await ctx.send(embed = embed)
            return
        else:
            
            image1 = "https://uploads.spiritfanfiction.com/fanfics/capitulos/201401/fanfiction-one-direction-a-different-love-1565268,250120142249.gif"
            image2 = "https://c.tenor.com/G615xUCziBoAAAAC/globo-tapa.gif"
            image3 = "https://thumbs.gfycat.com/ExcellentSoreChameleon-size_restricted.gif"
            image4 = "https://c.tenor.com/ra17G61QRQQAAAAC/tapa-slap.gif"
            image5 = "https://i.pinimg.com/originals/2f/0f/82/2f0f82e4fb0dee8efd75bee975496eab.gif"
            image6 = "https://www.intoxianime.com/wp-content/uploads/2017/04/tumblr_ooub8fIHkT1qz64n4o2_400.gif"
            image7 = "https://i.pinimg.com/originals/bc/ee/bf/bceebfa72d3a5933cb0e9cf319bb67ae.gif"
            
            url_image = random.choice([image1, image2, image3, image4, image5, image6, image7])
            
            embed = discord.Embed(
                title = '😡', description=f'{ctx.author.mention} Deu um tapa em {member.mention}'
            )
            embed.set_image(url=url_image)
            
            await ctx.send(embed = embed)
            return
        
    @commands.command(name='abracar', help='Dar um abaraço em alguem!')
    async def get_kiss_image(self, ctx, member: discord.Member= None):
        if member is None:
            
            embed = discord.Embed(
                title="Mencione o Usuário!",
                description="Ex.: !abracar @user",
                timestamp=datetime.datetime.utcnow(),
                color=0xff0000)
            await ctx.send(embed = embed)
            return
        else:
            
            image1 = "https://acegif.com/wp-content/gif/anime-hug-38.gif"
            image2 = "https://c.tenor.com/NIVvWLRYWJcAAAAC/abra%C3%A7o.gif"
            image3 = "https://acegif.com/wp-content/gif/anime-hug-59.gif"
            image4 = "https://i.pinimg.com/originals/91/9e/ac/919eacc6c73786fed53606b325c62e40.gif"
            image5 = "https://acegif.com/wp-content/gif/anime-hug-25.gif"
            image6 = "http://30.media.tumblr.com/tumblr_m2emecM0bQ1r5zfj8o1_500.gif"
            image7 = "https://i.gifer.com/27tM.gif"
            
            url_image = random.choice([image1, image2, image3, image4, image5, image6,  image7])
            
            embed = discord.Embed(
                title = '❤', description=f'{ctx.author.mention} Deu um abraço em {member.mention}'
            )
            embed.set_image(url=url_image)
            
            await ctx.send(embed = embed)
            return
        
    
    @commands.command(name="ship") #Esse comando está em fase de teste ainda... kkkk
    async def send_ship(self, ctx, member: discord.Member=None):
        
        image1 = "https://i.pinimg.com/originals/11/8a/c9/118ac94d9f00f9b668223113a5944af4.gif"
        image2 = "http://67.media.tumblr.com/756c52d84caf10e177777d6ee8504581/tumblr_ngyt1mvACH1qg78wpo1_500.gif"
        image3 = "https://i.imgur.com/Rtu2JyU.gif"
        image4 = "https://acegif.com/wp-content/uploads/anime-kiss-30.gif"
        image5 = "https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-49.gif"
        image6 = "https://i.pinimg.com/originals/68/a3/7a/68a37a5a1b86f227b8e1169f33a6a6bb.gif"
        image7 = "https://c.tenor.com/9IHLn02sU7MAAAAC/anime-beijo.gif"
            
        ship1 = "`31%[████.......]`"
        ship2 = "`45%[██████.......]`"
        ship3 = "`60%[██████████.....]`"
        ship4 = "`72%[████████████....]`"
        ship5 = "`85%[███████████████..]`"
        ship6 = "`96%[██████████████████.]`"
        
        ship = random.choice([ship1, ship2, ship3, ship4, ship5, ship6])
            
        url_image = random.choice([image1, image2, image3, image4, image5, image6, image7])
            
        name1 = ctx.author.name
        name2 = member.name
        name3 = name1[:4]+name2[3:]
        
        if member is None:
            embed = discord.Embed(
                title="Mencione o Usuário!",
                description="Ex.: !ship @user",
                timestamp=datetime.datetime.utcnow(),
                color=0xff0000)
            await ctx.send(embed = embed)
            return
        
        elif ship == ship1:
            
            embed = discord.Embed(
                title = "💖 Hmmm, será que nós temos um novo casal aqui? 💖",
                description = f"💗{ctx.author.mention}\n{member.mention}\n{name3}\n😶{ship} Parece que só são conhecidos... 😶",
                color = 0xff00cc
            )
            embed.set_image(url=url_image)
            await ctx.send(embed=embed)
            return
        
        else:
            
            embed = discord.Embed(
                title = '💖 Hmmm, será que nós temos um novo casal aqui? 💖',
                description=f'💗{ctx.author.mention}\n{member.mention}\n{name3}\n{ship}',
                color = 0xff00cc
            )
            embed.set_image(url=url_image)
            
            await ctx.send(embed = embed)
            return
            
def setup(bot):
    bot.add_cog(Images(bot))