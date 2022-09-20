#!/usr/bin/env python3

from telegram.ext import Updater, Dispatcher
from root.constant.constant import TOKEN
from root.handler.image_handler import picture_handler


def initialize_bot():
    updater: Updater = Updater(TOKEN)
    add_handlers(updater.dispatcher)
    updater.start_polling(drop_pending_updates=True)

def add_handlers(dispatcher: Dispatcher):
    dispatcher.add_handler(picture_handler)