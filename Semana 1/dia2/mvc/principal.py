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

    _calculadoraController.presntardatos(modelo_calculadoraModell)

    #aca deberia llamar ....

principal()    

