import dotenv
import discord
import gtts
import os
import traceback
import sys
import platform
from time import sleep
from discord.ext import commands
from datetime import datetime
from mutagen.mp3 import MP3

dotenv.load_dotenv(dotenv.find_dotenv())

bot = commands.Bot("!")

CANAL = os.getenv('CANAL')
AUTHOR = os.getenv('AUTHOR')
CANALEXC = os.getenv('CANAL_EXC')


async def remove_file(file_path):
    os.remove(file_path)


def is_connected(channel):
    for voice_client in bot.voice_clients:
        if voice_client.channel == channel:
            return True
    return False


async def reproduce_audio(message):
    channel = message.channel
    author = message.author
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    if author.voice is None:
        await channel.send('Você não está conectado em um canal de voz')

    if not is_connected(author.voice.channel):
        bot.vc = await author.voice.channel.connect()

    if is_connected(author.voice.channel) and message.clean_content.startswith('+dc'):
        await bot.vc.disconnect()
        return

    print(f'{author}: {message.clean_content}')
    txt = message.clean_content.lower()

    try:
        aud = f"audio/{timestamp}.mp3"
        tts = gtts.gTTS(txt, lang='pt', slow=False)
        tts.save(aud)
        if (platform.system() == 'Windows'):
            source = await discord.FFmpegOpusAudio.from_probe(source = f'audio/{timestamp}.mp3', executable = 'tools/ffmpeg/ffmpeg.exe')
        else:
            source = await discord.FFmpegOpusAudio.from_probe(f'audio/{timestamp}.mp3')
        
        bot.vc.play(source)
        audio = MP3(f"audio/{timestamp}.mp3")
        sleep(audio.info.length)
        await remove_file(aud)

    except Exception as e:
        tb = sys.exc_info()
        traceback.print_tb(tb)
        print(f"Exception: {e}")


@bot.event
async def on_ready():
    print(f'Botzada {bot.user}\nDoubleG *Copyright*')


@bot.event
async def on_message(message):
    if (message.clean_content.startswith(('/', '#', '-', '!'))):
        return
    
    if (message.channel.name == CANAL and message.author.name in AUTHOR) or message.channel.name == CANALEXC:
        print(f"Tem mensagem nova! Mensagem: {message.clean_content}")
        await reproduce_audio(message)


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    main()
