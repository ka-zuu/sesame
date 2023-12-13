from sesame_api import SesameAPI
from discord_notifier import DiscordNotifier
import config

def main():
  # Discord通知のインスタンスを作成
  notifier = DiscordNotifier(config.DISCORD_WEBHOOK_URL)

  # 鍵ごとにSesame APIのインスタンスを作成し、開閉状態を取得
  for key_name, key_config in config.SESAME_KEYS.items():
    # Sesame APIのインスタンスを作成
    sesame = SesameAPI(config.SESAME_API_KEY, key_config["UUID"], key_config["SECRET"])

    # 鍵の開閉状態を取得
    lock_status = sesame.get_lock_status()

    # 鍵が開いている場合だけ、通知メッセージに追加
    if lock_status == "unlocked":
      notifier.add_message(f"{key_name}: 鍵が開いています！")

  # 開いている鍵の開閉状態をDiscordに通知
  if notifier.has_messages():
    notifier.send_messages()

if __name__ == "__main__":
  main()