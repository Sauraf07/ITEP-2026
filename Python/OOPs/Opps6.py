class Time:
    def __init__(self,hr,mn,sc):
        self.__hr = hr
        self.__mn = mn
        self.__sc = sc

    def __add__(self, other):
        
        