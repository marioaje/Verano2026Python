nombres = ["Mario","Isaac","Alberto", "Cindy","Roger","Sasha"]
nombres.sort()
print(nombres)

def ordenamientoBurbuja(lista):
    lista = [x.lower() for x in lista ]
    numeroElementos = len(lista)
    for item in range(numeroElementos):
        for itemSecundario in range (0, numeroElementos - item - 1 ):
            if lista[itemSecundario] > lista[item+1]:
                lista[itemSecundario], lista[itemSecundario + 1] = lista[itemSecundario + 1], lista[itemSecundario]

    return lista
    
#print(ordenamientoBurbuja(nombres))