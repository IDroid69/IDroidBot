import discord
import requests
from discord.ext import commands


class Smarts(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name=('calcular'), help='Calcula uma expresão para voçê!')
    async def calcular_expressão(self, ctx, *expression):
        expression = ''.join(expression)
    
        resposta = eval(expression)
    
        await ctx.send(f'A resposta é: {resposta}')
        
    @commands.command(name="temperatura")
    async def on_weather(self, ctx, *, city: str):
        
        api_key = "14b26f842f6702547ab6a9273e30360a"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel
        
        if x["cod"] != "404":
            async with channel.typing():
                
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                
                weather_description = z[0]["description"]
                embed = discord.Embed(title=f"Weather in {city_name}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                embed.add_field(name="Descrição", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="Temperatura(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                embed.add_field(name="Umidade(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(name="Pressão atmosférica(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                
                await channel.send(embed=embed)
        else:
            await channel.send("Cidade não encontrada.")

def setup(bot):
    bot.add_cog(Smarts(bot))