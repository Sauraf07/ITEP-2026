'''
26. Media Player
Abstract:
MediaPlayer
Derived:
AudioPlayer
VideoPlayer
Implement play functionality.
'''
from abc import *
class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass    
class AudioPlayer(MediaPlayer):
    def play(self):
        print("Playing audio")
class VideoPlayer(MediaPlayer):
    def play(self):
        print("Playing video")
a = AudioPlayer()
a.play()
v = VideoPlayer()
v.play()