from env.config import *
from src.download import Download
from src.unzip import Unzip
from src.utils import Directory, File

BEPINEX_ZIP = Download(url=URL_BEPINEX).start()
Unzip(path=BEPINEX_ZIP, destination=CARX_FOLDER).start()
File(path=BEPINEX_ZIP).delete()

KINO_ZIP = Download(url=URL_KINO).start()
Directory(path=PLUGINS_FOLDER).check()
Unzip(path=KINO_ZIP, destination=PLUGINS_FOLDER).start()
File(path=KINO_ZIP).delete()

# ***NOT WORKING YET, LEAVE COMMENTED***
# NVA_ZIP = Download(url=URL_NVA).start()
# Unzip(path=NVA_ZIP, destination=PLUGINS_FOLDER).start()
# File(path=NVA_ZIP).delete()