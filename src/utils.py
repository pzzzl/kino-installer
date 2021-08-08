import os

class Directory:
    def __init__(self, path):
        self.path = path
    def check(self):
        if(not os.path.isdir(self.path)):
            print("Folder " + self.path.rsplit('/', 1)[1] + " not found. Creating...")
            os.mkdir(self.path)
        else:
            print("Folder " + self.path.rsplit('/', 1)[1] + " already exists")

class File:
    def __init__(self, path):
        self.path = path
    def delete(self):
        print("Deleting file " + self.path.rsplit('/', 1)[1])
        os.remove(self.path)