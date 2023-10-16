print("Calculator nota de plata\n")
suma_nota = input("Cat valoreaza nota de plata in RON? \n")
suma_nota = float(suma_nota)
persoane = input("Cate persoane impart nota de plata? \n")
persoane = int(persoane)
da_nu = input("Vrei sa lasi bacsis? (1=da iar 0=nu) \n")
da_nu = int(da_nu)
if da_nu == 0:
    print("Suma totala de plata este: \n", suma_nota / persoane)
if da_nu == 1:
    bacsis = input("Cat vrei sa lasi bacsis? \n")
    bacsis = float(bacsis)
    suma_totala = suma_nota + bacsis
    print("Suma totala de plata este: \n", suma_totala / persoane)
