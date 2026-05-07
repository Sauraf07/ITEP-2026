class Time:
    def __init__(self,hr,mn,sc):
        self.__hr = hr
        self.__mn = mn
        self.__sc = sc

    def display(self):
        print(f"{self.__hr}Hr : {self.__mn}M : {self.__sc} S")
    
    def __add__(self, other):
        temp = Time(0,0,0)
        temp.__hr = self.__hr + other.__hr
        temp.__mn = self.__mn + other.__mn
        temp.__sc = self.__sc + other.__sc
        if temp.__sc >= 60:
            temp.__mn += 1
            temp.__sc -= 60
        if temp.__mn >= 60:
            temp.__hr += 1
            temp.__mn -= 60
        return temp
    def __Sub__(self, other):
        temp = Time(0,0,0)
        temp.__hr = self.__hr - other.__hr
        temp.__mn = self.__mn - other.__mn
        temp.__sc = self.__sc - other.__sc
        if temp.__sc < 0:
            temp.__mn -= 1
            temp.__sc += 60
        if temp.__mn < 0:
            temp.__hr -= 1
            temp.__mn += 60
        return temp
    def __mul__(self, other):
        temp = Time(0,0,0)
        temp.__hr = self.__hr * other.__hr
        temp.__mn = self.__mn * other.__mn
        temp.__sc = self.__sc * other.__sc
        if temp.__sc >= 60:
            temp.__mn += temp.__sc // 60
            temp.__sc = temp.__sc % 60
        if temp.__mn >= 60:
            temp.__hr += temp.__mn // 60
            temp.__mn = temp.__mn % 60
        return temp
    def __divide__(self, other):
        temp = Time(0,0,0)
        temp.__hr = self.__hr // other.__hr
        temp.__mn = self.__mn // other.__mn
        temp.__sc = self.__sc // other.__sc
        return temp
    

t1 = Time(2,45,30)
t2 = Time(1,30,45)
t1.display()
t2.display()
t3 = t1 + t2
t3.display()
t4 = t1 - t2
t4.display()
t5 = t1 * t2
t5.display()
t6 = t1 / t2
t6.display()
