import random
litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numere = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboluri = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
litera = []
simbol = []
numar = []
usor = ""
noua_parola = ""
print("Generator de parole!")
nr_litere = int(input("Cate litere vrei sa aibe parola?\n"))
nr_simboluri = int(input(f"Cate simboluri vrei?\n"))
nr_numere = int(input(f"Cate numere vrei?\n"))

for parola in range(0, nr_litere):
    if parola <= nr_litere:
        litera.append(random.choice(litere))
#print(litera)
for l in range(0, nr_numere):
    if l <= nr_numere:
        numar.append(random.choice(numere))
#print(type(numar))
for s in range(0, nr_simboluri):
    if s <= nr_simboluri:
        simbol.append(random.choice(simboluri))
#print(type(simbol))
parola = litera+numar+simbol
#print(parola)
scramble = random.sample(parola, len(parola))
#print(type(scramble))
#print(scramble)
#print(parola)
#print(type(parola))
for final in parola:
    usor += final
print(f"parola inainte de random.sample(): {usor}")
for nou in scramble:
    noua_parola += nou
print(f"Parola dupa metoda sample : {noua_parola}")
