# Calculator BMI
print("Calculator BMI")
greutate = input("Ce greutate ai? kg\n")
greutate = float(greutate)
inaltime = input("Ce inaltime ai? m\n")
inaltime = float(inaltime)
bmi = greutate/(inaltime**2)
print("BMI= ",int(bmi))