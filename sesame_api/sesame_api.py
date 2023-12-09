import requests

class SesameAPI:
  BASE_URL = "https://app.candyhouse.co/api/sesame2"

  def __init__(self, api_key, uuid, secret_key):
    self.api_key = api_key
    self.uuid = uuid
    self.secret_key = secret_key

  def get_lock_status(self):
    headers = {"X-API-KEY": self.api_key}
    response = requests.get(f"{self.BASE_URL}/{self.uuid}", headers=headers)

    if response.status_code != 200:
      raise Exception("Failed to get lock status")

    data = response.json()
    lock_status = data["CHSesame2Status"]

    return lock_status