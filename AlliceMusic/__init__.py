from AlliceMusic.core.bot import ALLICE
from AlliceMusic.core.dir import dirr
from AlliceMusic.core.git import git
from AlliceMusic.core.userbot import Userbot
from AlliceMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ALLICE()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
