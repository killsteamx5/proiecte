# Verificator an bisect
an = int(input("Ce an vrei sa verifici? \n"))
if an % 4 != 0:
    print(f"Anul {an} nu este bisect")
elif an % 4 == 0:
    if an % 100 != 0:
        if an % 400 != 0:
            print(f"Anul {an}  este bisect")
elif an % 4 == 0:
    if an % 100 != 0:
        print(f"Anul {an} este bisect")
