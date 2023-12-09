from sesame_api import SesameAPI
from discord_notifier import DiscordNotifier
import config

def main():
  # Discord通知のインスタンスを作成
  notifier = DiscordNotifier(config.DISCORD_WEBHOOK_URL)

  # 鍵ごとにSesame APIのインスタンスを作成し、開閉状態を取得
  for uuid, secret_key in [(config.SESAME_KEY_UPPER_UUID, config.SESAME_KEY_UPPER_SECRET), (config.SESAME_KEY_DOWNER_UUID, config.SESAME_KEY_DOWNER_SECRET)]:
    # Sesame APIのインスタンスを作成
    sesame = SesameAPI(config.SESAME_API_KEY, uuid, secret_key)

    # 鍵の開閉状態を取得
    lock_status = sesame.get_lock_status()

    # 鍵の開閉状態を通知メッセージに追加
    notifier.add_message(lock_status)

  # すべての鍵の開閉状態をDiscordに通知
  notifier.send_messages()

if __name__ == "__main__":
  main()