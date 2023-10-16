from alfabet import alfabet
directie = input("Scrie 'encode' ca sa criptezi sau 'decode' ca sa decriptezi:\n")
text = input("Introdu mesajul:\n").lower()
salt = int(input("Intrudu numarul de salturi:\n"))

def cezar(text,salt,directie):

    if directie == "encode".lower():
        text_nou = ""
        for cuv_nou in text:
            if cuv_nou == ' ':
                text_nou += ' '
                continue
            cuv_nou = alfabet.index(cuv_nou)+salt
            if cuv_nou > alfabet.count(",")+1:
                alfabet.extend(alfabet)
            text_nou += alfabet[cuv_nou]
        print(f"Textul criptat este: {text_nou}")
    elif directie == "decode".lower():
        text_nou1 = ""
        for cuv_nou1 in text:
            if cuv_nou1 == ' ':
                text_nou1 += ' '
                continue
            cuv_nou1 = alfabet.index(cuv_nou1) - salt
            if cuv_nou1 > alfabet.count(",") + 1:
                alfabet.extend(alfabet)
            text_nou1 += alfabet[cuv_nou1]
        print(f"Textul decodat este: {text_nou1}")

cezar(text,salt,directie)