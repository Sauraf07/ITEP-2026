'''
10. Movie Ticket Booking
Parent:
Ticket
Derived:
GoldTicket
PlatinumTicket
VIPTicket
Apply pricing logic.
'''
class Ticket:
    def pricing(self):
        pass
class GoldTicket(Ticket):
    def pricing(self):
        print("You Will get higer benifits")
class PlatinumTicket(Ticket):
    def pricing(self):
        print("You Will get More benifits then Goldticket")

class VIPTicket(Ticket):
    def pricing(self):
        print("You Will Get VIP Services")

g = GoldTicket()
g.pricing()
p = PlatinumTicket()
p.pricing()
v = VIPTicket()
v.pricing()