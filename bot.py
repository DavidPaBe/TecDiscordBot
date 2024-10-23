import os
import discord
from discord.ext import commands
import asyncio
import subprocess
import sys
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}!')
    
    await shutdown_after_time()

async def shutdown_after_time():
    # Cambiado a 3 horas
    await asyncio.sleep(15)  # 3 horas en segundos
    print("Cerrando el bot después de 3 horas.")
    
    await trigger_workflow()
    
    await bot.close()

async def trigger_workflow():
    url = f"https://api.github.com/repos/DavidPaBe/TecDiscordBot/actions/workflows/124212019/dispatches"
    headers = {
        "Authorization": f"token {os.getenv('TOKEN_GITHUB')}",  # Asegúrate de que TOKEN_GITHUB esté configurado
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "ref": "main"  # Rama que deseas usar para activar el workflow
    }
    
    # Realiza la solicitud POST
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 204:
        print("Workflow triggered successfully!")
    else:
        print(f"Failed to trigger workflow: {response.status_code} - {response.text}")

if __name__ == "__main__":
    while True:
        try:
            bot.run(os.getenv('DISCORD_TOKEN'))
        except Exception as e:
            print(f"Error al ejecutar el bot: {e}. Reiniciando...")
            subprocess.Popen([sys.executable, 'bot.py'])  # Reinicia el bot
            break
