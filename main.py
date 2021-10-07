from pyrogram.types import (
  Message, 
)
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
TOKEN = os.environ.get("TOKEN", None) 


kuki = Client(
      "KukiBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TOKEN,
)

@kuki.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  if message.text and not message.document:
        if not kuki_message(context, message):
            return
        Message = message.text
        kuki.send_chat_action(chat_id, action="typing")
        kukiurl = requests.get('https://kuki-api.tk/api/Raiden/moezilla/message='+Message)
        Kuki = json.loads(kukiurl.text)
        kuki = Kuki['reply']
        sleep(0.3)
        message.reply_text(kuki, timeout=60)


messageprivate = '''
Hi, I'm Joey AI Bot
'''

messagegroup = '''
Hi, I'm Joey AI bot
'''





@kuki.on_message(filters.command("start"))
async def start(_, message):
    self = await kuki.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Support", url="https://t.me/KayAspirerProject"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))




kuki.run()
