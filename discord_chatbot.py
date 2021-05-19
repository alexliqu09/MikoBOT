import discord
from chat import chat 
llave = "PONER APLICATION ID"# Usted puede verlo aquí : https://discord.com/developers/applications
cliente = discord.Client()
@cliente.event
async def  on_message(mensaje):
    if mensaje.author == cliente.user:
        return
    await mensaje.channel.send(chat(mensaje.content))

cliente.run(llave)