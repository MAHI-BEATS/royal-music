# --- Top of file ---
import logging
import time
from pyrogram import Client
# ... other basic setup imports ...

# --- Bottom of file ---
from IstkharMusic.core.bot import Istu
from IstkharMusic.core.git import git
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb

dirr()
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

