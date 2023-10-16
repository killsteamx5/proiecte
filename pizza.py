print("Bine ai venit  la Florea pizza!\n")
size = input("Ce dimensiune sa aibe pizza? S, M, sau L \n")
salam = input("Vrei salam extra? Y sau N \n")
branza = input("Vrei branza extra? Y sau N \n")
nota = 0
if size == str("S"):
    nota += 15
elif size == str("M"):
    nota += 20
elif size == str("L"):
    nota += 25
if salam == str("Y") and size == str("S"):
    nota += 2
if salam == str("Y"):
    if size == str("M") or size == str("L"):
        nota += 3
if branza == str("Y"):
    nota += 1
print(f"Nota totala de plata este de ", nota, " RON.")
#DE TINUT MINTE NEAPARAT! CA SA ADAUGI O VALOARE SUPLIMENTARA LA O VARIABILA FOLOSESTI += SI !NU! =+
# nu e aceeasi treaba si nu iti va adauga o val noua peste cea veche