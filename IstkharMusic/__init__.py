import logging
import time
from pyrogram import Client

from IstkharMusic.core.bot import Istu
from IstkharMusic.core.git import git
from IstkharMusic.core.dir import dirr
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb
from IstkharMusic.logging import LOGGER

dirr()
git()
dbb()

# Here is the fix! We actually build the bot instance here.
app = Istu()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
