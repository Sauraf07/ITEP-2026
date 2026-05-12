'''
19. Mobile Phone Hierarchy
Phone
Smartphone
AndroidPhone
Add Android features.
'''
class Phone:
    def features(self):
        print("Android features supported")

class SmartPhone(Phone):
    def features(self):
        print("New Features Supported")

class AndroidPhone(SmartPhone):
    def features(self):
        return super().features()
    
p = AndroidPhone()
p.features()