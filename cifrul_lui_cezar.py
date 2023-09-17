from alfabet import alfabet
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cezar(text,shift,direction):

    if direction == "encode".lower():
        text_nou = ""
        for cuv_nou in text:
            cuv_nou = alfabet.index(cuv_nou)+shift
            if cuv_nou > alfabet.count(",")+1:
                alfabet.extend(alfabet)
            text_nou += alfabet[cuv_nou]
        print(f"The encoded text is {text_nou}")


    elif direction == "decode".lower():
        text_nou1 = ""
        for cuv_nou1 in text:
            cuv_nou1 = alfabet.index(cuv_nou1) - shift
            if cuv_nou1 > alfabet.count(",") + 1:
                alfabet.extend(alfabet)
            text_nou1 += alfabet[cuv_nou1]
        print(f"The decoded text is {text_nou1}")

cezar(text,shift,direction)