import random
print("Alegere aleatoare valoare list+split")
names_string = input("Nume persoane separate cu , : ")
names = names_string.split(",")
aleator = names[random.randint(0, len(names)-1)]
print(f"{aleator} face cinste!")

# merge si cu choice(aleator) dar asa e mai bine pentu a invata
