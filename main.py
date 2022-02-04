from tracemalloc import start
from discord.ext import commands
import pyttsx3

bot = commands.Bot("!")

engine = pyttsx3.init()
engine.setProperty("voice", "portugal")
engine.setProperty("rate", 180)

engine.runAndWait()


@bot.event
async def on_ready():
    print(f'Botzada do Aloes {bot.user}\nDoubleG *Copyright*')


@bot.event
async def on_message(message):
    if message.channel.name == 'canal-do-alan':
        # msg = 'Quem falou foi {0.author.name}: {0.content}'.format(message)
        if not message.content.startswith(':'):
            print(f'{message.author}: {message.content}')
            engine.say(message.content)
            engine.runAndWait()
        else:
            print('Não permitido')

bot.run("OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o")
