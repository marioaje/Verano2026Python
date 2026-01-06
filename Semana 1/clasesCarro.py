#El nombre de la clase
class claseCarro:    
#El constructor el inicializador las variables ( atributos )
    def __init__(self, placa, modelo, marca, cantidadPuertas, color):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.cantidadPuertas =cantidadPuertas 
        self.color = color

#La seccion de obtener o los GETTERS
    def getplaca(self):
        return self.placa

    def getmodelo(self):
        return self.modelo

    def getmarca(self):
        return self.marca

    def getcantidadPuertas(self):
        return self.cantidadPuertas

    def getcolor(self):
        return self.color


#La seccion de obtener o los SETTERS
    def setplaca(self, placa):
        self.__placa = placa

    def setmodelo(self, modelo):
        self.modelo = modelo

    def setmarca(self, marca):
        self.__marca = marca

    def setcantidadPuertas(self, cantidadPuertas):
        self.__cantidadPuertas = cantidadPuertas

    def setcolor(self, color):
        self.__color = color

#funcionesaprte
    def queCantidadPuertas(self, cantidadPuertas):
        if cantidadPuertas < 3:
            print("Es un carro peque")
        else:
            print("Es un carro grande")    

    def conviertoEnMayuscula(self, daot):
        return daot.upper()
#Usando la clase



carro = claseCarro( "123", "2006", "Toyota", 3, "Azul" )

print(carro.getplaca())
print(carro.getmarca())
print(carro.conviertoEnMayuscula( carro.getmarca() ))
carro.queCantidadPuertas(12)
