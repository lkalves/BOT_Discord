import os
import platform
import shutil
import sys
import traceback
from datetime import datetime
from time import sleep

import discord
import dotenv
import gtts
from discord.ext import commands
from mutagen.mp3 import MP3

# dotenv.load_dotenv(dotenv.find_dotenv())
var_env = dotenv.get_variables('D:\DEV\Projetos\BOT_Discord\.env')

bot = commands.Bot("!", intents=discord.Intents().all())

CANAL =var_env['CANAL']
AUTHOR = var_env['AUTHOR']
CANAL_EXC = var_env['CANAL_EXC']


async def remove_file(file_path):
    os.remove(file_path)


async def delete_files(message):
    if os.path.isdir('audio'):
        shutil.rmtree('audio')
        await message.channel.send('Áudios removidos com sucesso!')
        return
    await message.channel.send('Não possui áudios a serem removidos!')


def create_folder():
    os.mkdir('audio')


def is_connected(channel):
    for voice_client in bot.voice_clients:
        if voice_client.channel == channel:
            return True
    return False


async def reproduce_audio(message):
    '''
    Essa função é responsavél por validar se o user está conectado ou não no canal de voz,
    também é responsavél por enviar instruções no canal de texto e por fim ele também faz
    a reprodução da mensagem em formato de audio.
    '''
    channel = message.channel
    author = message.author
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    if author.voice is None:
        await channel.send(
            'Você não está conectado em um canal de voz')
        return

    if not is_connected(author.voice.channel):
        bot.vc = await author.voice.channel.connect()
        await message.channel.send(
            'Para ter mais informações utilize o comando "+help"')

    txt = message.clean_content.lower()

    try:
        aud = f"audio/{timestamp}.mp3"
        tts = gtts.gTTS(txt, lang='pt', slow=False)

        if not (os.path.isdir('audio')):
            create_folder()

        tts.save(aud)

        if platform.system() == 'Windows':
            source = await discord.FFmpegOpusAudio.from_probe(
                source=f'audio/{timestamp}.mp3',
                executable='tools/ffmpeg/ffmpeg.exe')
        else:
            source = await discord.FFmpegOpusAudio.from_probe(
                f'audio/{timestamp}.mp3')
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
    """
    :param message: responsavel por trazer as informações do Discord de usuario e mensagem
    :return: reproduçao do audio que é enviado para o discord em forma de mp3
    """
    content = message.clean_content
    if message.author.bot is False:
        if content.startswith(('/', '#', '-', '!')):
            return

        if is_connected(message.author.voice.channel) and content.startswith('+dc'):
            await bot.vc.disconnect()
            return

        if content.startswith('+help'):
            await message.channel.send('''
+removefiles = Remove arquivos de audio salvos.
+dc = Desconecta o bot do canal de voz.
            ''')
            return

        if content.startswith('+removefiles'):
            await delete_files(message)
            return

        if content.startswith('+'):
            return

        if (message.channel.name in CANAL and message.author.name in AUTHOR) or message.channel.name == CANAL_EXC:
            print(
                f"Tem mensagem nova de {message.author.name}!\nMensagem: {content}\n")
            await reproduce_audio(message)
    else:
        return


def main():
    bot.run(var_env['TOKEN'])


if __name__ == "__main__":
    main()
