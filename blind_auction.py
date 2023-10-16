print(f"Welcome to secret auction \n")
end = False
biduri = []
nume = []
mare = 0
pozitie = 0
auctioneers = {"name": nume, "bid": biduri, }
while end is False:
    nume.append(input("what is your name?: ").split(" "))
    biduri.append(int(input("What is your bid (RON)?: ")))
    ask = input("Are there any more bidders? yes/no: ").lower()
    if ask == "no":
        end = True
        for x in biduri:
            if mare < x:
                mare = x
pozitie = biduri.index(mare)
castigator = auctioneers["name"][pozitie][0]
print(f"Felicitari {castigator} ! Cu bid-ul de {mare} sa fii sanatos!")
