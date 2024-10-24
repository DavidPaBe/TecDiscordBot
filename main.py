# main.py

import os
import discord
from discord.ext import commands
from botSetup import setup as bot_setup  # Cambiar a botSetup para importar la función setup
import shutdown  # Importamos la lógica de apagado desde shutdown.py

# Inicializar los intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix=None, intents=intents)  # Sin prefijo por defecto aquí

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}!')
    
    # Llamar a la función de conteo de tiempo para apagar el bot después de 3 horas
    await shutdown.shutdown_after_time(bot)

# Cargar los comandos desde botSetup.py
bot_setup(bot)  # Llama a la función setup aquí

# Iniciar el bot con el token de las variables de entorno
bot.run(os.getenv('DISCORD_TOKEN'))
