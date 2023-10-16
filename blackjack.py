import random


def special(scorspec=0,y=range(0,11),):
    for x in carte:
        if x == "A":
            if scorspec + 11 > 21:
                scorspec += 1
            elif scorspec + 11 <= 21:
                scorspec += 11
        if x == "J":
            scorspec += 10
        if x == "Q":
            scorspec += 10
        if x == "K":
            scorspec += 10
    for x in carte:
        try:
            if x == y.index(x):
                scorspec += x
        except ValueError:
            x = 0
    return scorspec


def special_c(scorspec1=0,y=range(0,11)):
    for x in calculator:
        if x == "A":
            if scorspec1 + 11 > 21:
                scorspec1 += 1
            elif scorspec1 + 11 <= 21:
                scorspec1 += 11
        if x == "J":
            scorspec1 += 10
        if x == "Q":
            scorspec1 += 10
        if x == "K":
            scorspec1 += 10
    for x in calculator:
        try:
            if x == y.index(x):
                scorspec1 += x
        except ValueError:
            x = 0
    return scorspec1
logo = """
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/   

 """
print(logo)
carti = {0: "A", 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "J", 12: "Q", 13: "K"}
# print(carti)
carte = [random.choice(carti), random.choice(carti)]
carte_ascunsa = [random.choice(carti)]
calculator = ["_", random.choice(carti)]
scor = 0
scor_c = 0
end = False
if input("incepi un nou joc? d/n: ") == "d":
    scor = special()
    scor_c = special_c()
    print(f"Cartile tale: {carte},suma carti: {scor}")
    print(f"Cartile PC-ului {calculator},suma carti: {scor_c}")
    while end is False:
        trage = input("mai tragi o carte? d/n ")
        if trage == "d":
            carte.append(random.choice(carti))
            scor = special()
            scor_c = special_c()
            print(f"Cartile tale: {carte},suma carti: {scor}")
            print(f"Cartile PC-ului {calculator},suma carti: {scor_c}")
            if scor > 21:
                print(f"Scorul tau este {scor} iar scorul calculatorului este {scor_c},ai pierdut! :(")
                end = True
        elif trage == "n":
            calculator[0] = carte_ascunsa[0]
            while scor_c <= scor and scor_c <= 21:
                calculator.append((random.choice(carti)))
                scor_c = special_c()
                print(f"Cartile tale: {carte},suma carti: {scor}")
                print(f"Cartile PC-ului {calculator},suma carti: {scor_c}")
            if scor > scor_c and scor <= 21:
                print(f"Scorul tau este {scor} iar scorul calculatorului este {scor_c},ai castigat! :)")
                end = True
            elif scor < scor_c and scor_c <= 21:
                print(f"Scorul tau este {scor} iar scorul calculatorului este {scor_c},ai pierdut! :(")
                end = True
            elif scor_c > 21:
                print(f"Scorul tau este {scor} iar scorul calculatorului este {scor_c},ai castigat! :)")
                end = True
