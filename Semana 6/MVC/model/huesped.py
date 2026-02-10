#Abstracion...............
#Creacion o modelar los atributos del objeto
class Huesped:

    contadorId = 1

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono 
        self.idHuesped = Huesped.contadorId
        Huesped.contadorId += 1


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    def getNombre(self):
        return self.nombre
    
    def getTelefono(self):
        return self.telefono
    
    def getIdHuesped(self):
        return self.idHuesped    


#ayuda a solo acceder al atributo que se quiere modificar         
#set

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTelefono(self, telefono):
        self.telefono = telefono



#Metodo poliformismo
#   
    def mostrar_info(self):
        return f"id: {self.idHuesped} nombre: { self.nombre } telefono: { self.telefono } " 


#Atributos:

#id autoincremental

#nombre

#telefono

#Métodos:

#mostrar_info()