row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Unde bagi comoara? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
coloana = int(position) // 10
#alternativ, mai ai si varianta cu coloana = position[0]
linie = int(position) % 10
#-\- linie = position[1]
map[linie - 1][coloana - 1] = "X"
# map[int(linie) - 1][int(coloana - 1)] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

