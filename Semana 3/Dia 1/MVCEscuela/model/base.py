#Abstracion...............
#Creacion o modelar los atributos del objeto
class BaseDatos:
    
    def __init__(self, fechacreacion, fechamodificacion, usuariocreacion, usuariomodificacion):
        self.fechacreacion = fechacreacion
        self.fechamodificacion = fechamodificacion
        self.usuariocreacion = usuariocreacion
        self.usuariomodificacion = usuariomodificacion


        

