import os
import requests

class Download:
    def __init__(self, url):
        self.url = url
        self.filename = self.url.rsplit('/', 1)[1]
        self.fullpath = os.getcwd() + "//" + self.filename
    def start(self):
        print("Downloading " + self.filename)
        self.r = requests.get(self.url, allow_redirects=True)
        open(self.filename, "wb").write(self.r.content)
        print("Download completed")
        return self.fullpath