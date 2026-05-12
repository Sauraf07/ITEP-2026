'''
20. Gaming Characters
Character
Warrior
SuperWarrior
Add special powers.
'''
class Character:
    def poewrs(self):
        pass
class Worrior(Character):
    def poewrs(self):
        print("I am Very Powerful")

class SuperWorrior(Worrior):
    def poewrs(self):
        print("I am the most powerful ")

s = Worrior()
s.poewrs()
d = SuperWorrior()
d.poewrs()