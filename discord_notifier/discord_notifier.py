import requests
import json

class DiscordNotifier:
  def __init__(self, webhook_url):
    self.webhook_url = webhook_url
    self.messages = []

  def add_message(self, message):
    self.messages.append(message)

  def send_messages(self):
    data = {
      "content": "\n".join(self.messages)
    }
    response = requests.post(self.webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    if response.status_code != 204:
      raise Exception("Failed to send message to Discord")

    self.messages = []