student_scores = input("Introdu o lista de scoruri ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
high_score = 0
for score in student_scores:
    if  high_score <= score:
        high_score = score
print(f"Cel mai mare scor e:  {high_score}")
