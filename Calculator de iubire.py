print("Calculator de dragoste")
nume1 = str(input("Nume prima persoana: "))
nume2 = str(input("Nume a doua persoana: "))
nume1 = nume1.lower()
nume2 = nume2.lower()
true = nume1.count("t") + nume1.count("r") + nume1.count("u") + nume1.count("e") + nume2.count("t") + nume2.count("r") + nume2.count("u") + nume2.count("e")
love = nume2.count("l") + nume2.count("o") + nume2.count("v") + nume2.count("e") + nume1.count("l") + nume1.count("o") + nume1.count("v") + nume1.count("e")
true_love = int(str(true) + str(love))
if 10 < true_love > 90:
    print(f"Scorul tau este {true_love}, e bine cu voi")
elif 40 >= true_love <= 50:
    print(f"Your score is {true_love}, sunteti ok .")
else:
    print(f"Your score is {true_love}....da...")