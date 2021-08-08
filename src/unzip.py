import zipfile

class Unzip:
    def __init__(self, path, destination):
        self.path = path
        self.destination = destination
    def start(self):
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            print("Extracting " + self.path.rsplit('/', 1)[1])
            zip_ref.extractall(self.destination)