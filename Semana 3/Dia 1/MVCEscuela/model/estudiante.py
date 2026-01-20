#Abstracion...............
#Creacion o modelar los atributos del objeto
class Profesor:
    def __init__(self, nombre, edad, correo, fechaingreso, grado):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.fechaingreso = fechaingreso
        self.grado = grado


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def getCorreo(self):
        return self.correo        

#ayuda a solo acceder al atributo que se quiere modificar         
#set

    def setNombre(self, nombre):
        return self.nombre
    
    def setEdad(self, edad):
        return self.edad

    def setCorreo(self, correo):
        return self.correo        
