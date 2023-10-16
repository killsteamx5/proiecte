def adunare(n1, n2):
    """aduna valoarea a 2 numere"""
    return n1 + n2


def inmultire(n1, n2):
    """inmulteste valoarea a 2 numere"""
    return n1 * n2


def impartire(n1, n2):
    """impartirea a 2 valori"""
    return n1 / n2


def scadere(n1, n2):
    """Scaderea dintre 2 numere"""
    return n1 - n2


def rest(n1, n2):
    """Restul impartirii dintre 2 numere"""
    return n1 % n2


def cat(n1, n2):
    """Catul impartirii dintre 2 numere"""
    return n1 // n2

def calculator ():
    operatori = {scadere: "-",
                 adunare: "+",
                 inmultire: "*",
                 impartire: "/",
                 rest: "%",
                 cat: "//", }
    rezultat = 0
    final = False
    x = "da"
    while x == "da":
        if rezultat == 0:
            n1 = float(input("n1 = "))
        elif rezultat > 0 or rezultat < 0:
            n1 = rezultat
        n2 = float(input("n2 = "))
        operator = input("Ce operatie vrei sa faci? (-,+,*,/,%,//): ")
        if operator == operatori[scadere]:
            rezultat = scadere(n1, n2)
        elif operator == operatori[adunare]:
            rezultat = adunare(n1, n2)
        elif operator == operatori[inmultire]:
            rezultat = inmultire(n1, n2)
        elif operator == operatori[impartire]:
            rezultat = impartire(n1, n2)
        elif operator == operatori[cat]:
            rezultat = cat(n1, n2)
        elif operator == operatori[rest]:
            rezultat = rest(n1, n2)
        print(f"{n1} {operator} {n2} = {rezultat}")
        x = input("Mai continui operatiile cu acest rezultat? (da/nu): ")
        if x == "nu":
            final = True
            print(f"Rezultat = {rezultat}")
            calculator()
calculator()