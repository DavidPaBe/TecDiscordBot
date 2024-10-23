import os
import discord
from discord.ext import commands
import commands as bot_commands  # Importamos los comandos desde otro archivo

# Inicializar el bot con los intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}!')

# Cargar los comandos desde commands.py
bot_commands.setup(bot)

# Iniciar el bot con el token de las variables de entorno
bot.run(os.getenv('DISCORD_TOKEN'))
