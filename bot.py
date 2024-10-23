import os
import discord
from discord.ext import commands
import asyncio
import subprocess
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}!')
    
    await shutdown_after_time()

async def shutdown_after_time():
    await asyncio.sleep(60)
    print("Cerrando el bot después de 3 horas.")
    
    await bot.close()

if __name__ == "__main__":
    while True:
        try:
            bot.run(os.getenv('DISCORD_TOKEN'))
        except Exception as e:
            print(f"Error al ejecutar el bot: {e}. Reiniciando...")
            
            subprocess.Popen([sys.executable, 'bot.py'])
            break
