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
    url = f"https://api.github.com/repos/DavidPaBe/TecDiscordBot/actions/jobs/JOB_ID/rerun"
    headers = {
        "Authorization": f"token {os.getenv('TOKEN_GITHUB')}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 201:
        print("Job rerun successfully!")
    else:
        print(f"Failed to rerun job: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    while True:
        try:
            bot.run(os.getenv('DISCORD_TOKEN'))
        except Exception as e:
            print(f"Error al ejecutar el bot: {e}. Reiniciando...")
            subprocess.Popen([sys.executable, 'bot.py'])  # Reinicia el bot
            break
