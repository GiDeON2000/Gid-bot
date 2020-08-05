import discord #Импорт основной библиотеки дискорда
from discord.ext import commands #Импорт модуля commands

bot = commands.Bot(command_prefix = "!") #Создание переменной bot и установка префикса i

@bot.event #Ивент
async def on_ready():
    """Функция которая срабатывает, при запуске бота.
    В данном слечае она просто выведет в консоль I am ready"""
    print("I am ready")

bot.run() #Сюда через кавычки записываем токен нашего бота



#Запуск бота через бат-файл start.bat
