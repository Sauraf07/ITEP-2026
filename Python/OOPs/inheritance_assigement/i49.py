'''
49. Movie Streaming Platform
Features:
movies
subscriptions
watch history
Use abstract subscription plans.
'''
from abc import *
class MovieStreaming(ABC):
    @abstractmethod
    def movies(self):
        pass
    @abstractmethod
    def subscriptions(self):
        pass
    @abstractmethod
    def watchhistory(self):
        pass
class Netflix(MovieStreaming):
    def movies(self):
        print("Movies available")

    def subscriptions(self):
        print("Subscription plans available")

    def watchhistory(self):
        print("Watch history maintained")
n1 = Netflix()
n1.movies()
n1.subscriptions()
n1.watchhistory()
