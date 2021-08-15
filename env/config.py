from src.utils import Path
import requests

URL_LATEST_VERSIONS = "https://raw.githubusercontent.com/pzzzl/kino-installer/main/version/latest.json"

response = requests.get(URL_LATEST_VERSIONS)
versions = response.json()

URL_KINO = versions["kino"]
URL_BEPINEX = versions["bepinex"]

CARX_FOLDER = Path(title="SELECT CARX FOLDER").ask()

if "steamapps/common/CarX Drift Racing Online" not in CARX_FOLDER:
    print("Incorrect CarX folder!")
    input("Press ENTER to exit...\n")
    exit()

# Folders
BEPINEX_FOLDER = CARX_FOLDER + "/BepInEx"
PLUGINS_FOLDER = BEPINEX_FOLDER + "/plugins"
KN_BASE_FOLDER = PLUGINS_FOLDER + "/KN_Base"