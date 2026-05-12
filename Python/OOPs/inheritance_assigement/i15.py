'''
15. Sports Management
Player
CricketPlayer
Captain(CricketPlayer)
Add captain-specific functionality.
'''
class Player:
    def role(self):
        pass
class Cricker(Player):
    def role(self):
        print("I Play Cricket")
class Captain(Cricker):
    def role(self):
        print("I am the Captain")

c = Cricker()
c.role()
cap = Captain()
cap.role()