#Mi variables
           #0      ,1        ,2          ,3
#Mi variable ahora debe recibir clases, en lugar de un solo nombre
#personas = [ {nombre, edad}, {nombre, edad }, {nombre, edad },{nombre, edad }]
#class persona
class persona:
    idPersona = 1
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.idPersona = persona.idPersona
        persona.idPersona += 1

    def mostrarDato(self):
        return "Nombre:",self.nombre,", edad:", self.edad, ", idPersona:", self.idPersona
    
    #seccion de gets
    def getnombre(self):
        return self.nombre    
    
    def getedad(self):
        return self.edad    
    
    def getidePersona(self):
        return self.idPersona    

    def setnombre(self, nombre):
        self.nombre = nombre

    def setedad(self, edad):
        self.edad = edad
#esta es la clase, archivo aparte


personasArreglo = []
textoRespuesta = ""

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", personasArreglo)
   for items in personasArreglo:
        print(items.mostrarDato())
        resultadoTemporal = "El nombre es:", items.getnombre()
        #print(resultadoTemporal)
        #print(items)
   
#volvemos a pasar la variable del tipo arreglo
def buscar(usuarioNombre):
    #este if cambia, debido a que deben buscar dentro de los getdelnombre
    for items in personasArreglo:        
        if items.getnombre() == usuarioNombre:
            return items.getidePersona()
        # else:
        #     return -1
    return -1    

def buscarId(id):
    #este if cambia, debido a que deben buscar dentro de los getdelnombre
    for items in personasArreglo:        
        if items.getidePersona() == id:
            return items
        # else:
        #     return -1
    return None

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
   elementoPersona = buscarId(indice)#traemos el objeto desde el arreglo
   if elementoPersona:
       elementoPersona.setnombre(nombreModificar)
       print("Modificacion exitosa")
   else:
       print("Se cayo la demo")  
   

def insertar(nombre, edad):
    nuevosDatos = persona(nombre, edad)
    personasArreglo.append(nuevosDatos)
    print("Datos almacenados existosamente")


###################################Aca va el sistema

# nombre = input("Ingrese el nombre de la persona: ")
# edad = input("Ingrese la edad de la persona: ")

# insertar(nombre, edad)
insertar("nombre", 28)
insertar("Mrio", 28)
insertar("Isaac", 88)
mostrar()


usuarioNombreModificar = input("Ingrese el usuario a buscar: ")
posicion = buscar(usuarioNombreModificar)


if posicion == -1:
    textoRespuesta = "No encontro datos para", usuarioNombreModificar
else:
    nuevoNombre = input("Ingrese el nuevo nombre: ")
    modificar(nuevoNombre, posicion)
    textoRespuesta = "Se encontro datos para", usuarioNombreModificar    


mostrar()
#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato