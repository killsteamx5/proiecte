num1=float(input("Primul nr. "))
operator=(input("operator "))
num2=float(input("al 2 lea numar "))
if(operator=="+"):
    print("Rezultat=",(num1+num2))
if(operator=="-"):
    print("Rezultat=",(num1-num2))
if(operator=="*"):
    print("Rezultat=",(num1*num2))
if(operator=="/"):
    print("Rezultat=",(num1/num2))
if(operator=="//"):
    print("Rezultat=",(num1//num2))
if(operator=="**"):
    print("Rezultat=",(num1**num2))

#5functie care sa numere nr de cuvinte dintr un paragraf , odata prin string si odata cu list. "1 paragraf 3 4 prop lungi"