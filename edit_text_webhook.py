from discord_webhook import DiscordWebhook
from time import sleep

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw',
                         content='O alan é muito foda, o alan é muito foda')
sent_webhook = webhook.execute()
webhook.content = 'O Dash é muito foda, o dash é muito foda'
sleep(10)
sent_webhook = webhook.edit(sent_webhook)
