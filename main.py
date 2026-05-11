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
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=data)

async def main():
    global was_online

    print("STARTED")

    await client.start()

    print("LOGGED IN")

    while True:
        user = await client.get_entity(username)

        print("CHECKING...")

        if isinstance(user.status, UserStatusOnline):

            print("ONLINE!")

            if not was_online:
                send_message(f"{username} is ONLINE!")
                was_online = True

        else:
            was_online = False

        await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())