import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista = [rock,paper,scissors]
variante = int(input(f"alege piatra 0 hartie 1 foarfece 2:\n "))
pc = random.randint(0,2)
if variante == pc:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Remiza")
elif variante == 0 and pc == 1:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai pierdut")
elif variante == 0 and pc == 2:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai castigat")
elif variante == 1 and pc == 2:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai pierdut")
elif variante == 1 and pc == 0:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai castigat")
elif variante == 2 and pc == 1:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai castigat")
elif variante == 2 and pc == 0:
  print(f"ai ales{lista[variante]}\niar calculatorul a ales {lista[pc]}\n Ai pierdut")