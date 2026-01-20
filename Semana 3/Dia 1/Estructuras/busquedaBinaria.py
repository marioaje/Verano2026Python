nombres = ["Mario","Isaac","Alberto", "Cindy","Roger","Sasha"]

#             0    1        2          3         4     5       6
print(nombres)

def busquedaBinaria(lista, texto):
    lista = [x.lower() for x in lista ]
    print(lista)

    texto = texto.lower()

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        #calcula de la seccion binaria
        medio = (inicio + fin) // 2
        print(medio)
        if lista[medio] == texto:
            return medio
        elif texto < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1            



print(busquedaBinaria(nombres, "Isacc"))