'''
34. Cloud Storage Interface
Methods:
upload()
download()
Implement:
GoogleDrive
Dropbox
'''
from abc import *
class Storage(ABC):
    @abstractmethod
    def uplode(self):
        pass

    @abstractmethod
    def download(self):
        pass

class GoogleDrive(Storage):
    def uplode(self):
        print("File Uploding to Google Drive")

    def download(self):
        print("File downloading from google drive ")

class Dropbox(Storage):
    def uplode(self):
        print("File Uploding to dropbox")

    def download(self):
        print("File downloading from dropbox ")

g = GoogleDrive()
g.uplode()
g.download()
d = Dropbox()
d.uplode()
d.download()
