#Mi variables
           #0      ,1        ,2          ,3
#Mi variable ahora debe recibir clases, en lugar de un solo nombre
#personas = [ {nombre, edad}, {nombre, edad }, {nombre, edad },{nombre, edad }]
#class persona
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDato(self):
        return "Nombre:",self.nombre,", edad:", self.edad
    
    #seccion de gets
    def getnombre(self):
        return self.nombre    
    
    def getedad(self):
        return self.edad    
#esta es la clase, archivo aparte


personasArreglo = []
textoRespuesta = ""

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", personasArreglo)
   for items in personasArreglo:
       #print(items.mostrarDato())
        resultadoTemporal = "El nombre es:", items.getnombre()
        print(resultadoTemporal)
   
#volvemos a pasar la variable del tipo arreglo
def buscar(usuarioNombre):
    #este if cambia, debido a que deben buscar dentro de los getdelnombre
    if usuarioNombre in personasArreglo:
        indice = personasArreglo.index(usuarioNombre)
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
    personasArreglo.remove(nombre)
    print("El nombre: ",nombre," fue Eliminado")

def modificar(nombreModificar, indice):
   personasArreglo[indice] = nombreModificar

def insertar(nombre, edad):
    nuevosDatos = persona(nombre, edad)
    personasArreglo.append(nuevosDatos)
    print("Datos almacenados existosamente")


###################################Aca va el sistema

nombre = input("Ingrese el nombre de la persona: ")
edad = input("Ingrese la edad de la persona: ")

insertar(nombre, edad)
mostrar()
#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato