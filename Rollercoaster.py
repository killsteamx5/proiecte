print("Bine ai venit la Rollercoaster Nicolina!")
pret = 0
inaltime = float(input("Ce inaltime ai? "))
if inaltime < 120:
    print("Ne pare rau dar nu aveti inaltimea necesara.")
else:
    varsta = int(input("Ce varsta ai? "))
    if varsta < 12:
        pret += 5
    elif varsta > 12:
        pret += 7
    elif varsta > 18:
        pret += 12
    elif 45 <= varsta <= 55:
        pret = 0
    poze = input("Vrei si poze? D sau N \n")
    if poze == "D":
        pret += 3
        print(f"Pretul final este de {pret} RON.")
    else:
        print(f"Pretul final este de {pret} RON.")
