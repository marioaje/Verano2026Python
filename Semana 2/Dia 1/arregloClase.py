#Mi variables
           #0      ,1        ,2          ,3
#Mi variable ahora debe recibir clases, en lugar de un solo nombre
#personas = [ {nombre, edad}, {nombre, edad }, {nombre, edad },{nombre, edad }]
personas = ["Mario", "Isaac", "Alberto","Sasha"]
textoRespuesta = ""

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", personas)

def buscar(usuarioNombre):
    if usuarioNombre in personas:
        indice = personas.index(usuarioNombre)
    else:
        indice =-1
    return indice

def borrar(nombre):
    #un if para verificar y eliminar
    #para evitar duplicar codigo
    # if usuarioNombre in personas:
    #     indice =personas.index(usuarioNombre)
    # else:
    #     indice =-1
    personas.remove(nombre)
    print("El nombre: ",nombre," fue Eliminado")

def modificar(nombreModificar, indice):
   personas[indice] = nombreModificar


#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato