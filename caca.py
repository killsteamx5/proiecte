inaltimi = input("introdu 'inaltimile' studentilor cu spatiu ").split()
for n in range(0, len(inaltimi)):
    inaltimi[n] = int(inaltimi[n])
lungime = 0
for lungime in range(0,n-1):
    lungime += 1
suma = 0
for medie in range(0,lungime-1):
    suma += int(inaltimi[medie])
media = suma/lungime
print(round(media))