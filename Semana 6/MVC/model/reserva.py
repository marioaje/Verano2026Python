#Abstracion...............
#Creacion o modelar los atributos del objeto

class Reserva:

    contadorId = 1

    def __init__(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida):
        self.numero_habitacion = numero_habitacion
        self.id_huesped = id_huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida 
        self.idReserva = Reserva.contadorId
        Reserva.contadorId += 1

#Encapsulamiento protege el ingreso directo a los atributos.
#get
    def getNumero_habitacion(self):
        return self.numero_habitacion
    
    def getId_huesped(self):
        return self.id_huesped
    
    def getFecha_entrada(self):
        return self.fecha_entrada
    
    def getFecha_salida(self):
        return self.fecha_salida    

    def getIdReserva(self):
        return self.idReserva
    
#ayuda a solo acceder al atributo que se quiere modificar         
#set

    def setNumero_habitacion(self, numero_habitacion):
        self.numero_habitacion = numero_habitacion
    
    def setId_huesped(self, id_huesped):
        self.id_huesped = id_huesped

    def setFecha_entrada(self, fecha_entrada):
        self.fecha_entrada = fecha_entrada
        
    def setFecha_salida(self, fecha_salida):
        self.fecha_salida = fecha_salida        

#Metodo poliformismo
#   
    def mostrar_info(self):
        return f"id: {self.idReserva} id_huesped: { self.id_huesped } fecha_entrada: { self.fecha_entrada }  fecha_salida: { self.fecha_salida } " 



#id autoincremental

#numero_habitacion

#id_huesped

#fecha_entrada

#fecha_salida

#Métodos:

#mostrar_info()