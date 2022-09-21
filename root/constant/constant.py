#!/usr/bin/env python3

from os import environ
from datetime import datetime

USER_ID = int(environ.get("USER_ID", "0"))
TOKEN = environ.get("TOKEN", "")
SIGNATURE = environ.get("SIGNATURE", "")
LOCKED_SINCE_FORMAT = "%Y/%m/%d"
LOCKED_SINCE = environ.get("LOCKED_SINCE", datetime.now().strftime(LOCKED_SINCE_FORMAT))
PICTURE_OUTPUT = "output/out.png"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
FONT_LOCATION = "font/JetBrains.ttf"
FONT_SIZE = 40
