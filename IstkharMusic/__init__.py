import logging
import time
from pyrogram import Client

# We import Istu here but rename it to 'app' so __main__.py is happy!
from IstkharMusic.core.bot import Istu as app
from IstkharMusic.core.git import git
from IstkharMusic.core.dir import dirr  # <-- Changed to dirr
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb
from IstkharMusic.logging import LOGGER

dirr()  # <-- Changed to dirr()
git()
dbb()

userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
