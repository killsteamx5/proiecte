def capital_indexes(cuvant=""):
    lista = []
    cuvant_nou = []
    for x in cuvant:
        cuvant_nou.append(x)
    for y in range(0,len(cuvant)):
        if cuvant_nou[y] == cuvant_nou[y].upper():
            lista.append(y)
    print(lista)
    return lista


capital_indexes("TeST")

