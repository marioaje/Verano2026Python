#Mi variables
personas = ["Mario", "Isaac", "Alberto","Sasha"]
textoRespuesta = ""

#Funciones
def mostrar():
   print("Los usuarios del sistema: ", personas)

def buscar(usuarioNombre):
    if usuarioNombre in personas:
        indice =personas.index(usuarioNombre)
    else:
        indice =-1
    return indice

def buscarAlumno():
    print("Buscar")
    nombreBuscar=input("Ingrese el nombre a buscar en la lista: ")
    if nombreBuscar in personas:
      indice=personas.index(nombreBuscar)
      print(nombreBuscar,"Si se encuentra en la lista")
    else:
      print("No se encuentra el nombre ingresado en la lista")  
       
def borrarAlumno(nombre):
    #un if para verificar y eliminar
    #para evitar duplicar codigo
    # if usuarioNombre in personas:
    #     indice =personas.index(usuarioNombre)
    # else:
    #     indice =-1
    personas.remove(nombre)
    print("El nombre:",nombre,"fue Eliminado")

def buscarDos(personas,nombre):
    if nombre in personas:
     print("el usuario si esxiste")
    else:
       print("el usuario no existe")

def modificarAlumno(nombre, nombreModificar):
    indice = personas.index(nombre)
    personas[indice] = nombreModificar
    print("Modificado")

def modificar(nombreModificar, indice):
   personas[indice] = nombreModificar

def borrar(nombre):
    print("Borrar")
    indice = -1
    return indice    

mostrar()
#modificar()
# usuarioNuevo = input("Ingrese un nuevo usuario: ")
# personas.append(usuarioNuevo)#Insertar elementos en un arreglo

# print("Los usuarios del sistema", personas)

# usuarioNombre = input("Ingrese el usuario a buscar: ")
# posicion = buscar(usuarioNombre)


# if posicion == -1:
#     textoRespuesta = "No encontro datos para"
# else:
#     textoRespuesta = "Se encontro datos para"    

# print (textoRespuesta, usuarioNombre, "en el identificador: ", posicion)

# usuarioNombreBorrar = input("Ingrese el usuario a buscar y eliminar: ")

# posicion = buscar(usuarioNombreBorrar)

# if posicion == -1:
#     textoRespuesta = "No encontro datos para", usuarioNombreBorrar
# else:
#     borrarAlumno(usuarioNombreBorrar)
#     textoRespuesta = "Se encontro datos para", usuarioNombreBorrar    

# print(textoRespuesta)


usuarioNombreModificar = input("Ingrese el usuario a buscar y modificar: ")
posicion = buscar(usuarioNombreModificar)

if posicion == -1:
    textoRespuesta = "No encontro datos para", usuarioNombreModificar
else:
    nuevoNombre = input("Ingrese el nuevo nombre: ")
    modificar(nuevoNombre, posicion)
    textoRespuesta = "Se encontro datos para", usuarioNombreModificar    

print(textoRespuesta)
mostrar()
#La seccion de buscar
#La seccion de modificar
#La seccion de borrar
#= es para asignar un valor
#== es para comparar un valor
#=== es para comparar un valor + el tipo de dato