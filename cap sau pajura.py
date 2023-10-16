import random
print("Cap sau pajura\n")
ban = random.randint(0, 1)
if ban == 1:
    print("Cap!")
#elif ban == 0:
else:
    print("Pajura!")

# Alternativ nu mai scrii elif si direct else pt ca oricum ai doar 2 valori si trebuie sa pui doar o conditie
