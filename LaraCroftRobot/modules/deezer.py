# hmm
import os

import requests
from pyrogram.types import Message

from LaraCroftRobot import pbot
from pyrogram.types import filters


@pbot.on_message(filters.command("deezer"))
async def song(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please send the song name with `/song` command.")
        return
    text = message.text.split(None, 1)[1]
    print(text)
    await message.reply_text(f"Processing, your input is {str(text)}")
    link = f"https://api.deezer.com/search?q={text}&limit=1"
    dato = requests.get(url=link).json()
    match = dato.get("data")
    urlhp = match[0]
    urlp = urlhp.get("link")
    urlhp["album"]["cover_big"]
    polu = urlhp.get("artist")
    replo = urlp[29:]
    print(replo)
    urlp = f"https://starkapi.herokuapp.com/deezer/{replo}"
    datto = requests.get(url=urlp).json()
    mus = datto.get("url")
    sname = f"""{urlhp.get("title")}.mp3"""
    doc = requests.get(mus)
    with open(sname, "wb") as f:
        f.write(doc.content)
    await message.reply_audio(
        audio=sname, title=urlhp.get("title"), performer=polu.get("name")
    )
    os.remove(sname)
