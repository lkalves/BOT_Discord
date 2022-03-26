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
        if (message.channel.name == (os.getenv('CANAL')) and message.author.name in (os.getenv('AUTHOR'))) or message.channel.name == (os.getenv('CANAL_EXC')):
            if not is_connected(message.author.voice.channel):
                bot.vc = await message.author.voice.channel.connect()
            if is_connected(message.author.voice.channel) and message.content.startswith('!dc'):
                await bot.vc.disconnect()
            print(f'{message.author}: {message.content}')
            verifyUser(message.content)
            removeID = removeUserID(message.content)
            tts = gtts.gTTS(removeID, lang='pt', slow=False)
            tts.save("audio/test.mp3")
            source = await discord.FFmpegOpusAudio.from_probe(
                'audio/test.mp3'
            )
            bot.vc.play(source)


def main():
    bot.run(os.environ['TOKEN'])


if __name__ == "__main__":
    main()
