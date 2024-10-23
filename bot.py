import discord
import os
from discord.ext import commands
import commands as bot_commands  # Importamos los comandos desde otro archivo

# Inicializamos el bot con los intents necesarios
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Registramos los eventos y comandos en el archivo commands.py
bot_commands.setup(bot)

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Inicia el bot usando el token
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
