import os
import requests
from env.config import CARX_FOLDER

class Download:
    def __init__(self, url):
        self.url = url
        self.filename = self.url.rsplit('/', 1)[1]
        self.fullpath = CARX_FOLDER + "//" + self.filename
        print(self.fullpath)
    def start(self):
        print("Downloading " + self.filename)
        self.r = requests.get(self.url, allow_redirects=True)
        open(self.fullpath, "wb").write(self.r.content)
        return self.fullpath