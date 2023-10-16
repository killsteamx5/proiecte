x = range(1,101)
for numar in x:
    if numar % 3 == 0 and numar % 5 == 0:
        print("Fizz Buzz")
    elif numar % 3 == 0:
        print("Fizz")
    elif numar % 5 == 0:
        print("Buzz")
    elif numar % 2 == 0:
        print(numar)
    else:
        print(numar)