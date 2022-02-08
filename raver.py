from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from numpy import empty
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "portugal")
engine.setProperty("rate", 180)
engine.runAndWait()


bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f'Botzada do Aloes {bot.user}\nDoubleG *Copyright*')


@bot.event
async def on_message(message):
    if message.channel.name == 'bot':
        connected = message.author.voice
        # xablau = type(VoiceClient.is_connected())
        if connected:
            xablau = await connected.channel.connect()

        # msg = 'Quem falou foi {0.author.name}: {0.content}'.format(message)
        if not message.content.startswith('Data atual'):
            print(f'{message.author}: {message.content}')
            engine.say(message.content)
            engine.runAndWait()

        else:
            print('Não permitido')


# @bot.command(name='conectar')
# async def join(self, ctx):
#     connected = ctx.author.voice
#     if connected:
#         await connected.channel.connect()


bot.run("OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o")
