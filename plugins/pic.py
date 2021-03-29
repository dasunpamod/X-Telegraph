# This is bot coded by @Noob_admin and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners
# Updated by X-Noid

import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text="Hi,\nI'm X-Telegraph!\nYou can upload telegram photos to telegra.ph !\n\n/help for more details!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                       "Source", url="https://github.com/X-Gorn/X-Telegraph"
                   ),
                   InlineKeyboardButton("Project Channel", url="https://t.me/xTeamBots"),
                ],
                [InlineKeyboardButton("Author", url="https://t.me/xgorn")],
            ]
        ),
        reply_to_message_id=message.message_id
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text= "Steps to use the bot!\n\n1. Send Telegram Photo/GIF/Video (Max 5MB) (Compressed)\n2. Wait a few seconds and the photo/GIF/Video will be uploaded to telegra.ph\n\nIf bot didn't respond, contact @xgorn",
        reply_to_message_id=message.message_id
    )
    
@pyrogram.Client.on_message(pyrogram.filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>Uploading</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @xgorn")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@pyrogram.Client.on_message(pyrogram.filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @xgorn")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

@pyrogram.Client.on_message(pyrogram.filters.animation)
async def getanime(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    animdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".gif"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=animdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(animdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @xgorn")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(animdir)
    except:
        pass

@pyrogram.Client.on_message(pyrogram.filters.text)
async def text(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text="Hi,\nI'm X-Telegraph!\nYou can upload telegram Photos, GIFs and Videos to telegra.ph !\n\n/help for more details!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                       "Source", url="https://github.com/X-Gorn/X-Telegraph"
                   ),
                   InlineKeyboardButton("Project Channel", url="https://t.me/xTeamBots"),
                ],
                [InlineKeyboardButton("Author", url="https://t.me/xgorn")],
            ]
        ),
        reply_to_message_id=message.message_id
    )

