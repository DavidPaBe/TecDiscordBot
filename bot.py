import os
import discord
from discord.ext import commands
import asyncio
import subprocess
import sys

# Inicializar el bot con los intents necesarios
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}!')
    
    # Llamar a la función de conteo de tiempo para apagar el bot después de 3 horas
    await shutdown_after_time()

async def shutdown_after_time():
    # Esperar 3 horas (10800 segundos)
    await asyncio.sleep(10800)
    print("Cerrando el bot después de 3 horas.")
    
    # Cerrar el bot
    await bot.close()

# Iniciar el bot con el token de las variables de entorno
if __name__ == "__main__":
    while True:
        try:
            bot.run(os.getenv('DISCORD_TOKEN'))
        except Exception as e:
            print(f"Error al ejecutar el bot: {e}. Reiniciando...")
            # Reiniciar el script
            subprocess.Popen([sys.executable, 'bot.py'])
            break
