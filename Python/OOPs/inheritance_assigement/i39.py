'''
39. Navigation System
Methods:
navigate()
Implement:
GoogleMaps
AppleMaps
'''
from abc import *
class Navigation(ABC):
    @abstractmethod
    def navigate(self):
        pass
class GoogleMaps(Navigation):
    def navigate(self):
        print("Navigation by Google Maps")
class AppleMaps(Navigation):
    def navigate(self):
        print("Navigation by Apple Maps")
g = GoogleMaps()
g.navigate()
a = AppleMaps()
a.navigate()
