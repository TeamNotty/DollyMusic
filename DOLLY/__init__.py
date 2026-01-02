from DOLLY.core.bot import NOTTY
from DOLLY.core.dir import dirr
from DOLLY.core.git import git
from DOLLY.core.userbot import Userbot
from DOLLY.utils.inline import help_back_markup

from DOLLY.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NOTTY()
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
