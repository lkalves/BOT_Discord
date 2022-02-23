
from discord.ext import commands
import asyncio

TOKEN = "OTM4Nzg1ODU4ODU1Nzk2NzY2.YfvWdg.34gNUwxBfwwA8IRsf0YwesolA-o"


bot = commands.Bot("!")


async def main():
    print(await pegarUser(268198611941195776))


async def pegarUser(id):
    a = bot.get_user(id)
    return a


asyncio.run(main())
