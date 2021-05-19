import discord
from chat import chat 

'''
    Con este archivo podremos realizar la comunicación de con Discord
    en llave se debe poner el ID dado por Discord Developers.
'''
llave = "PONER APLICATION_ID"# Usted puede verlo aquí : https://discord.com/developers/applications
cliente = discord.Client()
@cliente.event
async def  on_message(mensaje):
    if mensaje.author == cliente.user:
        return
    await mensaje.channel.send(chat(mensaje.content))

cliente.run(llave)