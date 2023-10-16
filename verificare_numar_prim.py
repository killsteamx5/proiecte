# Write your code below this line 👇
def prime_checker(number):
    divizor = 1
    test = False
    while test is False and divizor < n:
        divizor += 1
        if divizor < n:
            if number % divizor == 0:
                test = True
                if test == True:
                    print("It's not a prime number.")
        else:
            print("It's a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
