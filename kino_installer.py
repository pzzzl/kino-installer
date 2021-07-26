from env.config import *
from src.download import Download
from src.unzip import Unzip
from src.utils import Directory, File

BEPINEX_ZIP = Download(url=URL_BEPINEX).start()
Unzip(path=BEPINEX_ZIP, destination=CARX_FOLDER).start()
File(path=BEPINEX_ZIP).delete()

KINO_ZIP = Download(url=URL_KINO).start()
Directory(path=PLUGINS_FOLDER).check()
Directory(path=KN_BASE_FOLDER).check()
Directory(path=TUNES_FOLDER).check()
Directory(path=VISUALS_FOLDER).check()
Unzip(path=KINO_ZIP, destination=PLUGINS_FOLDER).start()
File(path=KINO_ZIP).delete()

NVA_ZIP = Download(url=URL_NVA).start()