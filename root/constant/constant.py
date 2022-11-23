#!/usr/bin/env python3

from os import environ


USER_ID = int(environ.get("USER_ID", "0"))
TOKEN = environ.get("TOKEN", "")
SIGNATURE = environ.get("SIGNATURE", "")
PICTURE_OUTPUT = "output/out.png"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
FONT_LOCATION = "font/JetBrains.ttf"
FONT_SIZE = 20
