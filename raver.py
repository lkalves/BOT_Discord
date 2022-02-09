from discord.ext import commands
# from discord.ext.commands import Bot
# from discord.voice_client import VoiceClient
from numpy import empty
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 180)
engine.runAndWait()

AUTHOR = 'LK'

bot = commands.Bot("!")


def is_connected(channel):
    for voice_client in bot.voice_clients:
        if voice_client.channel == channel:
            return True
    return False


@bot.event
async def on_ready():
    print(f'Botzada do Aloes {bot.user}\nDoubleG *Copyright*')


@bot.event
async def on_message(message):
    # if message.channel.name == 'bot' and message.author.name == AUTHOR and message.content == '!leave':
    #     message.author.voice.channel.disconnect()

    if message.channel.name == 'bot' and message.author.name == AUTHOR:
        if not is_connected(message.author.voice.channel):
            await message.author.voice.channel.connect()

        # msg = 'Quem falou foi {0.author.name}: {0.content}'.format(message)
        if not message.content.startswith('Data atual'):
            print(f'{message.author}: {message.content}')
            engine.say(message.content)
            engine.runAndWait()
        else:
            print('Não permitido')


@bot.command(name="leave", pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    if voice_client:
        await voice_client.disconnect()
        print("Bot left the voice channel")
    else:
        print("Bot was not in channel")


def main():
    bot.run("OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o")


if __name__ == "__main__":
    main()
