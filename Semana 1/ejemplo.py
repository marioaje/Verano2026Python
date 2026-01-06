def pidaDatos():
    genero = input("Genero: ")
    cedula = input("Ingrese su cedula")
    residencia = input("Ingrese su residencia")
    estadoCivil =  input("Ingrese su estado civil")
    edad = int( input("Ingrese su edad") )

    return genero, cedula, residencia, estadoCivil, edad

def mostrarGenero(genero):
        print ( "El genero es: ", genero)


def esMayorEdad(edad):
      if edad > 17:
            print("Es mayor, de edad")
      else:
            print("Es menor, de edad")      


#Programa inicial

genero, cedula, residencia, estadoCivil = pidaDatos()
#return genero, cedula, residencia, estadoCivil, edad

mostrarGenero(genero)

esMayorEdad(edad)
