
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(
    url='https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw', username="Webhook with files")

# send two images
with open("D:\DEV\Teste_DoubleG\Curso\sonho.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='sonho.png')
# with open("path/to/second/image.jpg", "rb") as f:
#     webhook.add_file(file=f.read(), filename='example2.jpg')
# remove 'example.jpg'
webhook.remove_file('example.jpg')
# only 'example2.jpg' is sent to the webhook
response = webhook.execute()
