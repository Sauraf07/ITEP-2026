# a = []
# a = (1,2)
# a = {}
# a = {'a':'saurav'}
# a = ' '
a = "saurav"
match a:
    case []:print("empty list match ")
    case (1,2):print("Set match ")
    case {}:print("Dict match ")
    case {'a':'saurav'}:print("name dict match")
    case ' ':print("empty string match ")
    case "saurav":print("Saurav match ")
