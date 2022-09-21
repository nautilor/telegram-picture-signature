#!/usr/bin/env python3

from telegram import Update, Document, File
from telegram.ext import CallbackContext, MessageHandler, Filters
from root.constant.constant import (
    DATE_FORMAT,
    FONT_LOCATION,
    FONT_SIZE,
    LOCKED_SINCE,
    LOCKED_SINCE_FORMAT,
    PICTURE_OUTPUT,
    SIGNATURE,
    USER_ID,
)
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os


def format_date():
    return "Date: %s" % datetime.now().strftime(DATE_FORMAT)


def calculate_days():
    date: datetime = datetime.strptime(LOCKED_SINCE, LOCKED_SINCE_FORMAT)
    days: int = (datetime.now() - date).days
    if days < 2:
        return f"\nLocked for: {days} day"
    else:
        return f"\nLocked for: {days} days"


def add_signature_to_picture():
    try:
        image: Image = Image.open(PICTURE_OUTPUT)
        draw: ImageDraw = ImageDraw.Draw(image)
        font: ImageFont = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)
        signature: str = format_date() + calculate_days() + SIGNATURE
        hadjustment = len(signature.split("\n"))
        height = image.height - ((FONT_SIZE * 2) * hadjustment) + (15 * hadjustment)
        draw.text((FONT_SIZE, height), signature, font=font, fill=(255, 255, 255))
        image.save(PICTURE_OUTPUT)
    except Exception:
        return "Unable to add signature to picture"


def delete_image():
    try:
        os.remove(PICTURE_OUTPUT)
    except Exception:
        return "Unable to delete picture"


def handle_image(update: Update, context: CallbackContext):
    errors = []
    delete_image()
    try:
        document: Document = update.message.document
        file: File = document.get_file()
        file.download(PICTURE_OUTPUT)
    except Exception:
        errors.append("Unable to download picture")
    errors.append(add_signature_to_picture())
    try:
        update.effective_message.reply_document(open(PICTURE_OUTPUT, "rb"))
        update.effective_message.delete()
    except Exception:
        errors.append("Unable to send image back")
    errors.append(delete_image())
    errors = [error for error in errors if error]
    if errors:
        update.effective_message.reply_text(
            "SOME ERRORS OCCURRED: %s" % "\n- ".join(errors), parse_mode="HTML"
        )


picture_handler = MessageHandler(
    (Filters.chat_type.private & Filters.document & Filters.user(USER_ID)), handle_image
)
