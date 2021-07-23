import os

class Directory:
    def __init__(self, path):
        self.path = path
    def check(self):
        if(not os.path.isdir(self.path)):
            print("Folder " + self.path + " not found!\nCreating...")
            os.mkdir(self.path)
            print("Folder created succesfully!")
        else:
            print("Folder " + self.path + " already exists")

class File:
    def __init__(self, path):
        self.path = path
    def delete(self):
        print("Deleting file " + self.path)
        os.remove(self.path)
        print("File deleted")