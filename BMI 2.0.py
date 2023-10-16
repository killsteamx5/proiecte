inaltime = float(input("Introdu inaltimea (m): \n"))
greutate = float(input("Introdu greutatea (kg): \n"))
bmi=round(greutate/inaltime**2)
if bmi < 18.5:
    print(f"BMI-ul tau este {bmi},  sub greutatea normala")
elif bmi < 25:
    print(f"BMI-ul tau este {bmi},  greutatea normala")
elif bmi < 30:
    print(f"BMI-ul tau este {bmi}, supraponderal")
elif bmi <35:
    print(f"BMI-ul tau este {bmi}, obez")
elif bmi >35:
    print(f"BMI-ul tau este {bmi}, obez morbid")
else:
    print("Nu esti mort inca?...")