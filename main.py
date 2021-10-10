import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_message_delete(message):
    with open('snipe.txt', "w") as myfile:
        myfile.write(message.content)
    with open('snipe2.txt', "w") as myfile:
        myfile.write(str(message.author.id))

@bot.command()
async def snipe(ctx):
    my_file = open("snipe.txt", "r")
    my_file2 = open("snipe2.txt", "r")
    await ctx.reply('<@' + my_file2.read() + '>: ' + my_file.read())

bot.run(process.env.TOKEN)
