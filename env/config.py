from src.utils import Path

URL_BEPINEX = "https://github.com/BepInEx/BepInEx/releases/download/v5.4.15/BepInEx_x64_5.4.15.0.zip"
URL_KINO = "https://github.com/trbflxr/kino/releases/download/v2.6.1/release_2.6.1.zip"

CARX_FOLDER = Path(title="SELECT CARX FOLDER").ask()

if "steamapps/common/CarX Drift Racing Online" not in CARX_FOLDER:
    print("Incorrect CarX folder!")
    input("Press ENTER to exit...\n")
    exit()

# Folders
BEPINEX_FOLDER = CARX_FOLDER + "/BepInEx"
PLUGINS_FOLDER = BEPINEX_FOLDER + "/plugins"
KN_BASE_FOLDER = PLUGINS_FOLDER + "/KN_Base"