from discord.ext import commands
import asyncio

TOKEN = "OTUxMzIxNzY5OTc1ODgxNzI5.YilxcA.shiB6AZjZ8khwIu37T5JPx4ghww"
bot = commands.Bot("!")


async def main():
    print(await pegarUser(268198611941195776))


async def pegarUser(id):
    a = bot.get_user(id)
    return a


asyncio.run(main())
