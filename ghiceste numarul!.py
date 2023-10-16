import random
inchide = False
scor = 0
viata = 0
NR_GHICIT = random.randint(1, 100)
final = False


def incercare():
    global viata
    global final
    global scor
    numar = int(input("Ghiceste numarul: "))
    if numar < NR_GHICIT:
        viata -= 1
        print(f"Numarul {numar} este prea mic! Mai ai {viata} incercari!")
    if numar > NR_GHICIT:
        viata -= 1
        print(f"Numarul {numar} este prea mare! Mai ai {viata} incercari!")
    if numar == NR_GHICIT:
        scor += 1
        print(f"Numarul {numar} este numarul magic! mai aveai {viata} incercari ramase,ai castigat! :)\nScor: {scor}")
        final = True


while inchide is not True:
    print("Ghiceste Numarul!")
    start = input("incepe joc nou? d/n:")
    if start == "d":
        dificultate = input("Introdu 'usor' sau 'greu' de la tastatura pentru a alege dificultatea jocului: ")
        if dificultate == "usor":
            viata = 10
            print(f"Ai {viata} incercari!")
            while final is not True and viata > 0:
                incercare()
        elif dificultate == "greu":
            viata = 5
            incercare()
            print(f"Ai {viata} incercari!")
        elif dificultate != "usor" or dificultate != "greu":
            print("Ai scris gresit dificultatea!")
    elif start == "n":
        print(f"Scor final: {scor}")
        inchide = True
