from operator import truediv
from pickle import FALSE
from pydoc import describe
from sqlite3 import Timestamp
from unicodedata import name
import discord 
from discord.ext import commands 
import random
import os
import io
import aiohttp
import time 
from pip._vendor import requests
import asyncio






## prefix bota

client =  commands.Bot(command_prefix= ";")
client.remove_command("help")





## to gówno co się pokazuje w konsoli jak się bot odpali 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Netflix"
        )
    )






## wyświetlenie embeda że coś się zjebało z komendą

@client.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Error', value=f'Nie masz permisji {error.missing_perms}.')
        await ctx.send(embed=embed)

    else:
        embed.add_field(name = f':x: Error', value = f"``{error}``")
        await ctx.send(embed = embed)
        raise error


## pokazuje ping bota przy okazji możesz z nim zagrać w ping ponga

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency * 1000)}ms`")

## dołączanie bota do voice channelu 

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()



## banowanie debili

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} został zbanowany pomyślnie")


## dołączanie bota do kanału vc

@client.command()
async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='muka')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()






# nakładka 'triggered' na profilowe oznaczonego członka

@client.command()
async def triggered(ctx, member: discord.Member = None):
    if not member:  # if no member is mentioned
        member = ctx.author  # the user who ran the command will be the member

    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(
                f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage:  # get users avatar as png with 1024 size
            imageData = io.BytesIO(await wastedImage.read())  # read the image/bytes

            await wastedSession.close()  # closing the session and;

            await ctx.reply(file=discord.File(imageData, 'triggered.gif'))  # sending the file




## nakładka tęczowej flagi na profilowe oznczonego członka

@client.command()
async def gay(ctx, member: discord.Member = None):
    if not member:  # if no member is mentioned
        member = ctx.author  # the user who ran the command will be the member

    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(
                f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage:  # get users avatar as png with 1024 size
            imageData = io.BytesIO(await wastedImage.read())  # read the image/bytes

            await wastedSession.close()  # closing the session and;

            await ctx.reply(file=discord.File(imageData, 'gay.gif'))  # sending the file




## wysyłanie gifa jebnięcia oponenta którego oznaczyłeś

@client.command(pass_context=True)
async def uderz(ctx, member: discord.Member):
    
    await ctx.send("jeb")
    embed = discord.Embed(title="Uderz!", description="**{1}** uderzyl **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/yUWGLXWLPMd44/source.gif")
    await ctx.send(embed=embed)



## wysyła ci zdjęcie słodkiego piseka UwU

@client.command()
async def pies(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    data = response.json()
    embed = discord.Embed(
        title = 'pies!',
        description = '',
        colour = discord.Colour.purple()
          )
    embed.set_image(url=data['link'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)




## wysyła ci zdjęcie słodziutkiej pandy OwO

@client.command()
async def panda(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    data = response.json()
    embed = discord.Embed(
        title = 'Panda!',
        description = '',
        colour = discord.Colour.purple()
          )
    embed.set_image(url=data['link'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)


## wysyła ci zdjęcie kotka Baka....

@client.command()
async def kot(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    data = response.json()
    embed = discord.Embed(
        title = 'Kot!',
        description = '',
        colour = discord.Colour.purple()
          )
    embed.set_image(url=data['link'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)

## jebać sergille 

@client.command()
async def serek(ctx):
    embed = discord.Embed(title="", description="jebać sergille")
    await ctx.send(embed=embed)

## wysyła ci potężnego memeska

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Polska_wpz/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


 
## pokazuje aktualną godzinę

@client.command()
async def godzina(ctx):
    strings = time.strftime("**godzina %H**,**minuta %M**,**sekunda %S**")
    t = strings.split(',')
    await ctx.send(strings)


## never gonna give you up 

@client.command()
async def trol(ctx):
    embed=discord.Embed()
    embed.set_thumbnail(url="https://media0.giphy.com/media/10kABVanhwykJW/giphy.gif?cid=790b7611e7d60e8d6e375ab47e280a482e4973a3f70af0a7&rid=giphy.gif&ct=g")
    embed.add_field(name="zostałeś", value="zrickrollowany", inline=False)
    await ctx.send(embed=embed)


## wysyła informację na temat serwera 

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="Informacje serwera {} ".format(ctx.message.guild.name), color=0x176cd5)
    embed.add_field(name="Nazwa:", value=ctx.message.guild.name, inline=True)
    embed.add_field(name="Role:", value=len(ctx.message.guild.roles), inline=True)
    embed.add_field(name="Uzytkownicy:", value=len(ctx.message.guild.members))
    embed.add_field(name="Kanaly:", value=len(ctx.message.guild.channels))
    embed.add_field(name="Region:", value=ctx.message.guild.region)
    embed.add_field(name="Level weryfikacji", value=ctx.message.guild.verification_level)
    embed.add_field(name="Emotikony serwerowe:", value=len(ctx.message.guild.emojis))
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    embed.set_author(name=ctx.message.guild.name, icon_url=ctx.message.guild.icon_url)
    await ctx.send(embed=embed)


## spamuje na priv do wybranego oponenta (potrzeba admina)

@client.command()
@commands.has_permissions(administrator=True)
async def dmSpam(ctx, user_id=None, *, args=None):

    if ctx.message.author.id == 404354878035722240:
        await ctx.send("spierdalaj")
    else:
        if user_id != None and args != None:
            try:
                while True:
                    target = await client.fetch_user(user_id)
                    await target.send(args)
                    await ctx.channel.send("'" + args + "' wyslano do: " + target.name)
            except:
                await ctx.channel.send("Nie mozna wyslac wiadomosci")
    await ctx.send("spam zakończony!")




## no jebać a co ?

@client.command()
async def jebaćokle(ctx):
        await ctx.send('jebać i się nie bać')



## wysyła link do najlepszego kanału na yt

@client.command()
async def yt(ctx):
    embed = discord.Embed(title = "Youtube", description = "", color = discord.Colour.purple())
    embed.set_thumbnail(url="https://i.pinimg.com/474x/a9/6a/c0/a96ac0dd32817abe31f78a7a3c465a1e.jpg")
    embed.add_field(name = "Najlepsze filmy i streamy na polskim youtube", value = "https://www.youtube.com/channel/UCTzE4vNqpfR97EzvuBI1bmA", inline = False)
    await ctx.send(embed=embed)
    






## wyświelta changelog

@client.command()
async def changelog(ctx):
    embed = discord.Embed(title="Changelog", description="     ", color= discord.Colour.purple())
    embed.add_field(name="Wersja 0.1", value="Dodano podstawowe komendy", inline=False)
    embed.add_field(name="Wersja 0.1.1", value="Naprawiono Bugi", inline=False)
    embed.add_field(name="Wersja 0.2", value="Dodano więcej komend administratorskich ", inline=False)
    embed.add_field(name="Wersja 0.2.1", value="Więcej komend administratorskich", inline=False)
    embed.add_field(name="Wersja 0.2.2", value="Poprawki komend ", inline=False)
    embed.add_field(name="Wersja 0.3", value="Dodano sekretną komendę", inline=False)
    embed.add_field(name="Wersja 0.3.1", value="Wyczyszczenie kodu dla deweloperów ", inline=False)
    embed.add_field(name="Wersja 0.3.2", value="Dodano więcej komend dla użytkowników ", inline=False)
    embed.add_field(name="Wersja 0.3.3", value="Naprawa Buga związanego z sekretną komendą", inline=False)
    embed.add_field(name="Wersja 0.4", value="WAŻNA ZMIANA, zmieniono hosting bota", inline=False)
    embed.add_field(name="Wersja 0.4.1", value="Poprawki błędów oraz dodano kilka funkcji bota", inline=False)
    embed.add_field(name="Wersja 0.4.2", value="Kilka drobnych zmian niezauważalnych dla użytwkonika ", inline=False)
    
    embed.set_footer(text="Aktualna wersja = 0.4.2, Wielkie podziękowania do Grawether oraz czlonków serwera DuinoCoin <3")
    await ctx.send(embed=embed)


        
## komenda wyświetla embed z komendami 

@client.command(aliases=["h"])
async def help(ctx):
   embed = discord.Embed(title = "Pomoc", description = "", color = discord.Colour.purple())
   embed.add_field(name = "Lista komend", value = "Tutaj są wszystkie komendy", inline = False)
   embed.add_field(name = ";jebaćokle", value = "pisze jebać okle", inline = False)
   embed.add_field(name = ";godzina", value = "mówi ci aktualną godzinę", inline = False)
   embed.add_field(name = ";gay", value = "sam sie przekonaj", inline = False)
   embed.add_field(name = ";triggered", value = "triggeruje oznaczoną osobę", inline = False)
   embed.add_field(name = ";uderz", value = "uderza oznaczoną osobę", inline = False)
   embed.add_field(name = ";pies", value = "wysyła ci zdjęcie pieska :3", inline = False)
   embed.add_field(name = ";panda", value = "wysyła ci zdjęcie pandy :3", inline = False)
   embed.add_field(name = ";yt", value = "wysyła link do najlepszego kanału yt", inline = False)
   embed.add_field(name = ";trol", value = "wysyła rickrolla", inline = False)
   embed.add_field(name = ";changelog", value = "wysyła changelog", inline = False)
   embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    



   await ctx.send(embed=embed)










client.run("OTQzNDg0MDgwMzY2OTQ0MjY2.YgzuBQ._XkoeGbHka9NOEnaiHJANdgOSkw")