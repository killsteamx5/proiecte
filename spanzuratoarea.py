# Spanzuratoarea

import random

from hangman_cuvinte import text, hangman, hangman_logo
print(hangman_logo)
# import re
# lista = re.split(r"[.,' ;\n]",text)
# varianta cu re e mai usoara si intuitiva dar inca nu am ajuns la importuri noi


lista = random.choice(text)
cuvant = []
cuv_asc = []
litere_incercate = []
viata = 0
final_joc = False
greseala = 0
for litera in lista:
    cuvant += litera
    cuv_asc.append("_")
while not final_joc:
    incercare = input("introdu o litera: ")
    litere_incercate.append(incercare)
    for litera in range(0, len(cuvant)):
        if incercare == cuvant[litera]:
            cuv_asc[litera] = cuvant[litera].replace("_", str(litera))
            print(f"{hangman[viata]}\nLitera {incercare} face parte din cuvant! Mai ai {cuv_asc.count('_')} litere de ghicit!\nLitere Incercate : {litere_incercate}\n{cuv_asc}")
        if cuvant == cuv_asc:
            print("Felicitari! Ai castigat!")
            final_joc = True
            break
    if incercare not in cuvant:
        viata += 1
        print(f"""{hangman[viata - 1]}
Litara {incercare} nu se portriveste!{cuv_asc}
Mai ai {7 - viata} incercari
Litere Incercate : {litere_incercate}""")
        if viata == 7:
            print(f"{cuvant}\nNu mai ai incercari! Ai pierdut!")
            final_joc = True
