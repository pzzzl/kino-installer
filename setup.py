from distutils.core import setup
import py2exe

setup(console=[{
    "script": "kino_installer.py",
    "icon_resources": [(0, "./public/ico/KiNO_INSTALLER_ICON.ico")]
}])