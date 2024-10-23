from discord.ext import commands
from discord import Embed

def setup(bot):
    @bot.command(name='menu')
    async def menu_command(ctx):
        embed = Embed(
            title="Menú de Preguntas Frecuentes",
            description="Selecciona una opción:",
            color=0x0099ff
        )
        embed.add_field(name='📚 Carreras', value='Información sobre carreras', inline=False)
        embed.add_field(name='👨‍🏫 Maestros', value='Información sobre maestros', inline=False)
        embed.add_field(name='🏫 Instalaciones', value='Información sobre las instalaciones', inline=False)
        embed.add_field(name='🕒 Horarios', value='Información sobre horarios', inline=False)
        embed.add_field(name='📞 Contacto', value='Información de contacto', inline=False)
        embed.set_footer(text="Reacciona con el emoji correspondiente para obtener más información.")

        message = await ctx.send(embed=embed)
        await message.add_reaction('📚')
        await message.add_reaction('👨‍🏫')
        await message.add_reaction('🏫')
        await message.add_reaction('🕒')
        await message.add_reaction('📞')

    @bot.event
    async def on_reaction_add(reaction, user):
        if user.bot:
            return
        
        if reaction.emoji == '📚':
            await reaction.message.channel.send("Las carreras ofrecidas son: Ingeniería en Sistemas, Mecatrónica, etc.")
        elif reaction.emoji == '👨‍🏫':
            await reaction.message.channel.send("Información sobre los maestros: Prof. Juan Pérez, etc.")
        elif reaction.emoji == '🏫':
            await reaction.message.channel.send("Las instalaciones incluyen: Biblioteca, Laboratorios, etc.")
        elif reaction.emoji == '🕒':
            await reaction.message.channel.send("Los horarios de atención son de 8:00 AM a 4:00 PM.")
        elif reaction.emoji == '📞':
            await reaction.message.channel.send("Contacto: 123-456-7890 o email@instituto.com")
