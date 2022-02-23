from discord_webhook import DiscordWebhook
from time import sleep

# ENVIA A MENSAGEM E APAGA APÓS 10 SEGUNDOS

webhook = DiscordWebhook(
    url='https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw', content='sou gay e chupo pau')
sent_webhook = webhook.execute()
sleep(1)
webhook.delete(sent_webhook)
