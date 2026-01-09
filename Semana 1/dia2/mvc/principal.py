#Es el encargado de llamar los archivos view

#Comento hacer un calculadora
#datoa, datob, resultado

#terminemos----

#llamar el controlador, 
from controller.calculadoraController import calculadoraController

def principal():
#pasar parametros
    datoa = int(input("Ingresa el datoa: "))
    datob = int(input("Ingresa el datob: "))

    #instancia o declarar la clase una variable
    _calculadoraController = calculadoraController()

    #creemos el modelo
    modelo_calculadoraModell = _calculadoraController.agregardatos(datoa, datob)

    print("\n=== Operaciones en MVC===")
    print("1. Sumar")

    opcion = int(input("Seleccione una operacion (1--#)"))

    _calculadoraController.operaciones(modelo_calculadoraModell, opcion)


    _calculadoraController.presntardatos(modelo_calculadoraModell)

    #aca deberia llamar ....

principal()    

