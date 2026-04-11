import logging
import time
from pyrogram import Client

from IstkharMusic.core.bot import app
from IstkharMusic.core.git import git
from IstkharMusic.core.dir import dir
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb
from IstkharMusic.logging import LOGGER

dir()
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
