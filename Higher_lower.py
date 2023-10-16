import random
print("Higher Lower!")
variante = {"nimic": 10, "florea": 100, "caca": 25, "maca": 123, "sdas": 3132, "buga": 1}
nume1 = random.choice(list(variante))
scor_n1 = variante[nume1]
end = False
scor = 0
while end is False:
    del variante[nume1]
    if len(list(variante)) == 0:
        print("Ti a dat indiciul cu len Razvan, gandeste mai simplu cateodata si nu te complica!")
        end = True
        break
    nume2 = random.choice(list(variante))
    scor_n2 = variante[nume2]
    intrebare = input(f"nume1: {nume1} - {scor_n1}\nnume2: {nume2} - ?\n{nume2} are scorul mai 'mare' sau mai 'mic' decat {nume1}?")
    if intrebare == "mic":
        if scor_n2 <= scor_n1:
            scor += 1
            print(f"Corect!\nscor: {scor}")
        elif scor_n2 > scor_n1:
            print(f"Ai gresit!\nscor final: {scor}")
            end = True
    elif intrebare == "mare":
        if scor_n2 >= scor_n1:
            scor += 1
            print(f"Corect!\nscor: {scor}")
        elif scor_n2 < scor_n1:
            print(f"Ai gresit!\nscor final: {scor}")
            end = True
    elif intrebare != "mic" or intrebare != "mare":
        print(f"nu ai introdus bine!\nscor final: {scor}")
        end = True
    nume1 = nume2
    scor_n1 = variante[nume1]
