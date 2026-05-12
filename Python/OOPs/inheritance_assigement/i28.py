'''
28. Authentication System
Abstract:
Authentication
Derived:
OTPAuth
GoogleAuth
FacebookAuth
'''
from abc import *
class Authentication(ABC):
    @abstractmethod
    def auth(self):
        pass
class OTPAuth(Authentication):
    def auth(self):
        print("OTP Authentication")
class GoogleAuth(Authentication):
    def auth(self):
        print("Google Authentication")
class FacebookAuth(Authentication):
    def auth(self):
        print("Facebook Authentication")
o = OTPAuth()
o.auth()
g = GoogleAuth()
g.auth()
f = FacebookAuth()
f.auth()
