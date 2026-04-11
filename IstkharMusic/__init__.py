from IstkharMusic.core.dir import dirr
from IstkharMusic.core.git import git
from IstkharMusic.core.userbot import Userbot
from IstkharMusic.misc import dbb, 
from .logging import LOGGER

dirr()
git()
dbb()

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

