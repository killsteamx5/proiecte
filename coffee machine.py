print("Coffee machine\n")
# TODO 1. Afisare selectie de cafele(espresso, caffee latte , simpla etc.
# TODO 2. Afisare pret cafea selectata
# TODO 3. Introducerea corecta a sumei in aparat + returnarea banilor in caz de lipsa in necesare preparat
# TODO 4. Compararea totalului de ingrediente necesare cu cel al preparatului(in caz de sunt suficiente materiale, fa produsul, daca nu returneaza "Ingrediente insuficiente, doriti sa selectati alt produs? "Da pentru a te intoarce la selectie 'Nu' pentru a returna banii.
cafea = 2500
lapte = 5000
apa = 10000
bani = 0
produs = [{
    "Denumire": "Espresso",
    "Cod": 0,
    "Descriere": "Cafea scurta fara lapte ",
    "Retetar": {"nec_cafea": 20,
                "nec_apa": 100,
                "nec_lapte": 0,
                "pret": 5,
                }
          },
          {
    "Denumire": "Caffee Latte",
    "Cod": 1,
    "Descriere": "Cafea cu lapte ",
    "Retetar": {"nec_cafea": 20,
                "nec_apa": 100,
                "nec_lapte": 0,
                "pret": 7,
                }
          },
          {
    "Denumire": "Cafea lunga",
    "Cod": 2,
    "Descriere": "Cafea cu surplus de apa ",
    "Retetar": {"nec_cafea": 20,
                "nec_apa": 100,
                "nec_lapte": 0,
                "pret": 6
                }
          }]
print("Produse disponibile\n")
alege = input(f'''
Denumire:{produs[0]["Denumire"]}\nCod:{produs[0]["Cod"]}\nDescriere:{produs[0]["Descriere"]}\nPret:{produs[0]["Retetar"]["pret"]}\n
Denumire:{produs[1]["Denumire"]}\nCod:{produs[1]["Cod"]}\nDescriere:{produs[1]["Descriere"]}\nPret:{produs[1]["Retetar"]["pret"]}\n
Denumire:{produs[2]["Denumire"]}\nCod:{produs[2]["Cod"]}\nDescriere:{produs[2]["Descriere"]}\nPret:{produs[2]["Retetar"]["pret"]}\n
Ce produs doriti? (introduce-ti codul produsului): ''')
if alege == "0" and cafea >= 20 and apa >= 100:
    suma = 0
    while suma < 5:
        suma += int(input("introdu suma de bani necesara (50 bani, 1 leu, 5 lei): "))
    if suma >= 5:
        cafea -= 20
        apa -= 100
        bani += 5
