# shutdown.py

import asyncio
import aiohttp

async def shutdown_after_time(bot):
    # Esperar 3 horas (10800 segundos)
    await asyncio.sleep(10800)  # Espera de 3 horas
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
