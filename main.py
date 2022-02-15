from discord.ext import commands
import discord
import pyttsx3


speaker = pyttsx3.init()
speaker.setProperty("voice", "brazil")
speaker.setProperty("rate", 170)
speaker.runAndWait()

AUTHOR = 'alansousa'
TOKEN = "OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o"

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
    if message.channel.name == 'canal-do-alan' and message.author.name == AUTHOR:
        if not is_connected(message.author.voice.channel):
            bot.vc = await message.author.voice.channel.connect()
        print(f'{message.author}: {message.content}')
        speaker.save_to_file(message.content, 'test.webm')
        speaker.runAndWait()
        source = await discord.FFmpegOpusAudio.from_probe(executable='D:\\DEV\\Projetos\\Webhook_Discord\\ffmpeg\\ffmpeg.exe', source='test.webm')
        bot.vc.play(source)


# @bot.command(pass_context=True)
# async def dc(self, ctx):
#     server = ctx.message.guild.voice_client
#     await ctx.voice_client.disconnect()


def main():
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
