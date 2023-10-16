# Calculator de viata pana la 90 ani
print("Calculator de viata pana la 90 ani")
varsta = input("Cati ani ai? \n")
varsta_final = int(varsta)
luna = 1080-(12*varsta_final)
sapt = 4680-(52*varsta_final)
zile = 32850-(365*varsta_final)

print(f"Mai ai:\n{luna} luni \n{sapt} saptamani \n{zile} zile de trait pana la 90 de ani")