import zipfile

class Unzip:
    def __init__(self, filepath, destination):
        self.filepath = filepath
        self.destination = destination
    def start(self):
        with zipfile.ZipFile(self.filepath, 'r') as zip_ref:
            print("Extracting " + self.filepath + " to " + self.destination)
            zip_ref.extractall(self.destination)
            print("Extraction finished")