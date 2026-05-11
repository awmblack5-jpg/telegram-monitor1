from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline
import asyncio
import requests

# =========================
# TELEGRAM API (حسابك)
# =========================
api_id = 20772917
api_hash = "775e8d51df877fd040a882e63fe94cad"

# الشخص اللي تراقبه
username = "@non_899"

# =========================
# BOT INFO (الإشعار)
# =========================
BOT_TOKEN = "6544064207:AAEtMyFiquuJaX1SR3W8eE6pWqnhrm6RCs0"
CHAT_ID = "6279357262"

client = TelegramClient("session", api_id, api_hash)

was_online = False

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

async def main():
    global was_online

    await client.start()
    print("🚀 BOT STARTED")

    while True:
        try:
            user = await client.get_entity(username)

            # إذا Online
            if isinstance(user.status, UserStatusOnline):

                if not was_online:
                    print("🔔 ONLINE DETECTED")
                    send_message(f"🔔 {username} صار ONLINE!")
                    was_online = True

            else:
                was_online = False

            await asyncio.sleep(10)

        except Exception as e:
            print("ERROR:", e)
            await asyncio.sleep(5)

with client:
    client.loop.run_until_complete(main())