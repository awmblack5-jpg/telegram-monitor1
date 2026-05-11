from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline
import asyncio
import requests

api_id = 20772917
api_hash = "775e8d51df877fd040a882e63fe94cad"

username = "@non_899"

BOT_TOKEN = "6544064207:AAEtMyFiquuJaX1SR3W8eE6pWqnhrm6RCs0"
CHAT_ID = "6279357262"

client = TelegramClient("session", api_id, api_hash)

was_online = False

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

async def main():
    global was_online

    await client.start()
    print("🚀 MONITOR ACTIVE")

    while True:
        try:
            user = await client.get_entity(username)

            if isinstance(user.status, UserStatusOnline):
                if not was_online:
                    send_message(f"🔔 {username} صار ONLINE!")
                    print("ONLINE DETECTED")
                    was_online = True
            else:
                was_online = False

        except Exception as e:
            print("ERROR:", e)

        await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())