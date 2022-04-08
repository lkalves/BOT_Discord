from time import sleep
import dotenv
from discord.ext import commands
import discord
from multiprocessing import Lock
import gtts
import os
from datetime import datetime

import traceback
import sys

dotenv.load_dotenv(dotenv.find_dotenv())

mutex = Lock()
bot = commands.Bot("!")

CANAL = os.getenv('CANAL')
AUTHOR = os.getenv('AUTHOR')
CANALEXC = os.getenv('CANAL_EXC')


async def remove_file(file_path):
    sleep(5)
    os.remove(file_path)


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
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    print(message.clean_content)

    with mutex:

        if author.voice is None:
            await channel.send('Você não está conectado em um canal de voz')

        if (channel.name == CANAL and author.name in AUTHOR) or channel.name == CANALEXC:
            if not is_connected(author.voice.channel):
                bot.vc = await author.voice.channel.connect()

            if is_connected(author.voice.channel) and message.clean_content.startswith('!dc'):
                await bot.vc.disconnect()
                return

            print(f'{author}: {message.clean_content}')
            txt = message.clean_content.lower()

            try:
                aud = f"audio/{timestamp}.mp3"
                tts = gtts.gTTS(txt, lang='pt', slow=False)
                tts.save(aud)
                source = await discord.FFmpegOpusAudio.from_probe(source=f'audio/{timestamp}.mp3', executable='tools/ffmpeg/ffmpeg.exe')
                bot.vc.play(source)
                await remove_file(aud)

            except Exception:
                ex_type, ex, tb = sys.exc_info()
                traceback.print_tb(tb)
                print('Deu pau!')


def main():
    bot.run(os.environ['TOKEN'])


if __name__ == "__main__":
    main()
