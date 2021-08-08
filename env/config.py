# URLs
from tkinter import Tk
from tkinter.filedialog import askdirectory

URL_BEPINEX = "https://github.com/BepInEx/BepInEx/releases/download/v5.4.15/BepInEx_x64_5.4.15.0.zip"
URL_KINO = "https://github.com/trbflxr/kino/releases/download/v2.6.0/release_2.6.0.zip"

tk = Tk()
tk.withdraw()
path = askdirectory(title='SELECT CARX FOLDER')

if "steamapps/common/CarX Drift Racing Online" in path:
    CARX_FOLDER = path
else:
    print("INCORRECT CARX FOLDER!")
    input("Press ENTER to exit...\n")
    exit()

tk.destroy()

# Folders
BEPINEX_FOLDER = CARX_FOLDER + "/BepInEx"
PLUGINS_FOLDER = BEPINEX_FOLDER + "/plugins"
KN_BASE_FOLDER = PLUGINS_FOLDER + "/KN_Base"