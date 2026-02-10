# ✔ Habitaciones
# Registrar habitaciones
# 
# Listar habitaciones
# 
# Buscar por número
# 
# Cambiar estado “Disponible/Ocupada” ( un actualizar pero de un solo atributo)
# 
# Ordenar por precio (usar Bubble Sort o sort())
# 
# mostrar_info()

import csv, os
from datetime import datetime
from model.habitacion import Habitacion
import view.habitacionesView as vista


BASE = os.path.dirname(os.path.dirname(__file__))
ARCHIVO = os.path.join(BASE, "data", "habitaciones.csv")
LogFile = os.path.join(BASE, "log", "errores.txt")


class HabitacionController:

    def __init__(self):
        self.habitaciones = []
        self.cargar()

    def guardarError(self, errorTexto):
        try:        
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LogFile, "a", encoding="utf-8") as file:
                file.write(f"{fecha} --> {errorTexto}\n")
        except Exception as nombreError:
            print(f"Error fatal al guardar logs {nombreError} ")
            #una notificacion por correo
                       
    #que pasa si solo dejamos asi???                       

    def cargar(self):
        try:
#             if not os.path.exists(ARCHIVO):
#                return
            with open(ARCHIVO, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for numero, tipo, precio, estado in reader:
                    self.habitaciones.append(Habitacion(numero, tipo, precio, estado))
           
        except Exception as nombreError:
            self.guardarError(f"Error cargando los datos de la habitacion {nombreError}")
            vista.mensaje( f"(X) Error cargando los datos de la habitacion")
        

    def guardar(self):
        #try
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for item in self.habitaciones:                
                writer.writerow([item.numero, item.tipo, item.precio, item.estado])

    def registrar(self, numero, tipo, precio, estado):
        
        #try
#                 habitacion= buscar
#         
#         if self.estado == "Ocupada"
#         
        self.habitaciones.append(Habitacion( numero, precio, estado, tipo))
        self.guardar()
        vista.mensaje("Habitación registrada.")

    def listar(self):
        #try
        vista.mostrar_lista(self.habitaciones)

    def buscar(self, numero):
        #try
        for h in self.habitaciones:
            if h.numero == numero:
                return h
        return None

    def cambiar_estado(self, numero):
        h = self.buscar(numero)
        if h:
            h.estado = "Ocupada" if h.estado == "Disponible" else "Disponible"
            self.guardar()
            vista.mensaje("Estado actualizado.")
        else:
            vista.mensaje("Habitación no encontrada.")

    def ordenar_precio(self):
        self.habitaciones.sort(key=lambda x: x.precio)
        vista.mensaje("Habitaciones ordenadas por precio.")
        self.listar()



           
