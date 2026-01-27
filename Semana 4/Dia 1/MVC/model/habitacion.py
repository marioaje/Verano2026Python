#Abstracion...............
#Creacion o modelar los atributos del objeto
class Habitacion:

    contadorId = 1

    def __init__(self, numero, precio, estado, tipo):
        self.numero = numero
        self.precio = precio
        self.tipo = tipo
        self.estado = estado 
        self.idHabitacion = Habitacion.contadorId
        Habitacion.contadorId += 1

        


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    def getNumero(self):
        return self.numero
    
    def getPrecio(self):
        return self.precio
    
    def getEstado(self):
        return self.estado
    
    def getIdHabitacion(self):
        return self.idHabitacion
        

#ayuda a solo acceder al atributo que se quiere modificar         
#set

    def setNumero(self, numero):
        self.numero = numero
    
    def setPrecio(self, precio):
        self.precio = precio
        
    def setEstado(self, estado):
        self.estado = estado
            
        self.numero = numero
        self.precio = precio
        self.estado = estado 
        self.idHuesped = Habitacion.contadorId
        Habitacion.contadorId += 1

#Metodo poliformismo
#

    def mostrar_info(self):
        return f" numero: { self.numero } precio: { self.precio } estado: { self.estado }" 

# 
# Atributos:
# 
# número
# 
# tipo (“Sencilla”, “Doble”, “Suite”)
# 
# precio
# 
# estado (“Disponible”, “Ocupada”)
# 
# Métodos:
# 
# mostrar_info()