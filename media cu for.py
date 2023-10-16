#10 10 10 15 15
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
lungime = 0
for student in student_heights:
    lungime += 1
suma = 0
for medie in student_heights:
    suma += medie
media = suma/lungime
print(round(media))