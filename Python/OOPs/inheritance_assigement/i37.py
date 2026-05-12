'''
37. Social Login System
Methods:
login()
Implement:
GoogleLogin
GitHubLogin
LinkedInLogin
'''
from abc import *
class Login(ABC):
    @abstractmethod
    def login(self):
        pass
class GoogleLogin(Login):
    def login(self):
        print("Login by Google")
class GitHubLogin(Login):
    def login(self):
        print("Login by GitHub")
class LinkedInLogin(Login):
    def login(self):
        print("Login by LinkedIn")
g = GoogleLogin()
g.login()
gh = GitHubLogin()
gh.login()
l = LinkedInLogin()
l.login()
