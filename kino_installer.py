from env.config import *
from src.download import Download
from src.unzip import Unzip
from src.utils import Directory

FULLPATH_BEPINEX_ZIP = Download(url=URL_BEPINEX).start()
Unzip(filepath=FULLPATH_BEPINEX_ZIP, destination=CARX_FOLDER).start()

FULLPATH_KINO_ZIP = Download(url=URL_KINO).start()
Directory(path=PLUGINS_FOLDER).check()
Unzip(filepath=FULLPATH_KINO_ZIP, destination=PLUGINS_FOLDER).start()