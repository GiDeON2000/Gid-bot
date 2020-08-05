import discord #Импорт основной библиотеки дискорда
from discord.ext import commands #Импорт модуля commands
import config #Импорт нашего config.py
import pymongo #Импорт библиотеки pymongo

token = config.worker["TOKEN"]
prefix = config.worker["prefix"]
bot = commands.Bot(command_prefix = "!") #Создание переменной bot и установка префикса i

cluster = MongoClient("mongodb+srv://gideon:upitob32@cluster0.gy3lr.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["discord-bot"]
collection = db["main"]


@bot.event
async def on_ready():
	for guild in bot.guilds:
  		for member in guild.members:
  			if collection.count_documents({"_id": member.id}) == 0:
  				collection.insert_one({
  				"_id": member.id,
  				"name": member.name,
  				"rep": 0,
                "lvl": 0,
                "xp": 0,
                "cash": 0,
                "msg": 0
  				})
	print('ok')

@bot.event
async def on_member_join(member):
	if collection.count_documents({"_id": member.id}) == 0:
		collection.insert_one({"_id": member.id, "name": member.name, "rep": 0})

@bot.command()
async def load(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}')
    await ctx.send('loaded')

@bot.command()
async def reload(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}')
    Bot.unload_extensions(f'cogs.{extensions}')
    await ctx.send('reloaded')

@bot.command()
async def unload(ctx, extensions):
    Bot.unload_extension(f'cogs.{extensions}')
    await ctx.send('unloaded')



bot.run(token) #Сюда через кавычки записываем токен нашего бота





#Запуск бота через бат-файл start.bat
