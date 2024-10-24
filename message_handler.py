# message_handler.py

async def process_message_without_prefix(message):
    content = message.content.lower()

    # Lógica de respuestas basadas en palabras clave
    if "carreras" in content or "📚" in content:
        await message.channel.send("Las carreras ofrecidas son: Ingeniería en Sistemas, Mecatrónica, etc.")
    elif "maestros" in content or "👨‍🏫" in content:
        await message.channel.send("Información sobre los maestros: Prof. Marco Antonio, Prof. Maria Eugenia, etc.")
    elif "instalaciones" in content or "🏫" in content:
        await message.channel.send("Las instalaciones incluyen: Biblioteca, Laboratorios de Informática, Cafetería, etc.")
    elif "horarios" in content or "🕒" in content:
        await message.channel.send("Los horarios de atención son de 8:00 AM a 4:00 PM.")
    elif "contacto" in content or "📞" in content:
        await message.channel.send("Contacto: +52 (664) 607 8400 o webmaster@tijuana.tecnm.mx")
    elif content == "hola":
        await message.channel.send(f"Hola, {message.author.mention}!")
    elif content == "ping":
        await message.channel.send("Pong!")
    elif message.content.
    else:
        # Respuesta genérica si no se encuentra palabra clave
        await message.channel.send(f"No entiendo tu mensaje, {message.author.mention}. ¿Puedes preguntar algo sobre carreras, maestros, instalaciones, horarios o contacto?")
