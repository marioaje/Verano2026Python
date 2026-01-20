#Abstracion...............
#Creacion o modelar los atributos del objeto
class Profesor:
    def __init__(self, nombre, edad, correo, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.especialidad = especialidad
