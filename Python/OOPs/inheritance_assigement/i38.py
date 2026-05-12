'''
38. File Compression Tool
Methods:
compress()
Implement:
ZIPCompression
RARCompression
'''
from abc import *
class Compression(ABC):
    @abstractmethod
    def compress(self):
        pass    

class ZIPCompression(Compression):
    def compress(self):
        print("File Compressed by ZIP")
class RARCompression(Compression):
    def compress(self):
        print("File Compressed by RAR")
z = ZIPCompression()
z.compress()
r = RARCompression()
r.compress()
