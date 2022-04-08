from sys import executable
import dotenv
from discord.ext import commands
import discord
from multiprocessing import Lock
from tools.messageHandler import verifyUser, removeUserID
import gtts
import os

dotenv.load_dotenv(dotenv.find_dotenv())

mutex = Lock()
bot = commands.Bot("!")

CANAL = os.getenv('CANAL')
AUTHOR = os.getenv('AUTHOR')
CANALEXC = os.getenv('CANAL_EXC')


def is_connected(channel):
    for voice_client in bot.voice_clients:
        if voice_client.channel == channel:
            return True
    return False


@bot.event
async def on_ready():
    print(f'Botzada {bot.user}\nDoubleG *Copyright*')


@bot.event
async def on_message(message):
    channel = message.channel
    author = message.author

    with mutex:
        if author.voice is None:
            await channel.send('Você não está conectado em um canal de voz')

        if (channel.name == CANAL and author.name in AUTHOR) or channel.name == CANALEXC:
            if not is_connected(author.voice.channel):
                bot.vc = await author.voice.channel.connect()

            if is_connected(author.voice.channel) and message.content.startswith('!dc'):
                await bot.vc.disconnect()

            print(f'{author}: {message.content}')
            txt = message.content.lower()
            verifyUser(txt)
            removeID = removeUserID(message.content)

            tts = gtts.gTTS(removeID, lang='pt', slow=False)
            tts.save("audio/test.mp3")
            source = await discord.FFmpegOpusAudio.from_probe('audio/test.mp3')

            bot.vc.play(source)


def main():
    bot.run(os.environ['TOKEN'])


if __name__ == "__main__":
    main()
