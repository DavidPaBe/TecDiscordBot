import os
import discord
from discord.ext import commands
import asyncio
import aiohttp  # Para hacer solicitudes HTTP de forma asíncrona
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
    
    # Llamar a la función de conteo de tiempo para apagar el bot después de 3 horas
    await shutdown_after_time()

async def shutdown_after_time():
    # Esperar 3 horas (10800 segundos)
    await asyncio.sleep(15)  # Espera de 3 horas
    print("Cerrando el bot después de 3 horas.")
    
    # Realiza alguna acción antes de cerrar, si lo necesitas
    await trigger_workflow()

    # Cerrar el bot
    await bot.close()

async def trigger_workflow():
    url = "https://api.github.com/repos/DavidPaBe/TecDiscordBot/actions/workflows/124212019/dispatches"
    headers = {
        "Authorization": "token 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",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "ref": "main"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 204:
                print("Workflow triggered successfully!")
            else:
                print(f"Failed to trigger workflow: {response.status} - {await response.text()}")

bot_commands.setup(bot)

# Iniciar el bot con el token de las variables de entorno
bot.run(os.getenv('DISCORD_TOKEN'))
