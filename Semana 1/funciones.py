#Una funcion sin retorno.

def mostrarSaludos():
    print("Bienvenidos al 2026")

mostrarSaludos()    


def funcionRetornando(a,b):
    return a + b

unavariable = funcionRetornando(12,9)
print( unavariable )

print (funcionRetornando(12,9))


def funcionConVariosArgumentos(nombre, edad):
    return f" Soy {nombre} y mi edad es: {edad} "


print( funcionConVariosArgumentos("Mario", "12") )