from discord.ext import commands
import discord
import pyttsx3
from multiprocessing import Lock


engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 170)
engine.runAndWait()

AUTHOR = ['LK', 'Pseudao']
CANAL = 'bot'
TOKEN = "OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o"

mutex = Lock()
bot = commands.Bot("!")
f = 'sou lindo'
# rafao


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
    with mutex:
        if (message.channel.name == CANAL and message.author.name in AUTHOR) or message.channel.name == 'canal-do-alan':
            if not is_connected(message.author.voice.channel):
                bot.vc = await message.author.voice.channel.connect()
            print(f'{message.author}: {message.content}')
            engine.save_to_file(message.content, 'test.webm')
            engine.runAndWait()
            source = await discord.FFmpegOpusAudio.from_probe(executable='D:\\DEV\\Projetos\\Webhook_Discord\\ffmpeg\\ffmpeg.exe', source='test.webm')
            bot.vc.play(source)


def main():
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
