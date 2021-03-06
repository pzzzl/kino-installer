try:
    from env.config import *
    from src.download import Download
    from src.unzip import Unzip
    from src.utils import Directory, File

    # DOWNLOAD & INSTALL BEPINEX
    BEPINEX_ZIP = Download(url=URL_BEPINEX).start()
    Unzip(path=BEPINEX_ZIP, destination=CARX_FOLDER).start()
    File(path=BEPINEX_ZIP).delete()

    # DOWNLOAD & INSTALL KINO
    KINO_ZIP = Download(url=URL_KINO).start()
    Directory(path=PLUGINS_FOLDER).check()
    Unzip(path=KINO_ZIP, destination=PLUGINS_FOLDER).start()
    File(path=KINO_ZIP).delete()

    # CREATE KINO FOLDER
    Directory(path=KN_BASE_FOLDER).check()

    print("\nKiNO installation finished succesfully!\n")
except Exception as err:
    print(err)

input("Press ENTER to exit...\n")
exit()