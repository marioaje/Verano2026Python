import tkinter as tk
from tkinter import ttk, messagebox


class HabitacionesGUI:

    def __init__(self, root, habitacionController):
        self.controller = habitacionController
        
        self.window = tk.Toplevel(root)
        self.window.title("Habitacion")
        self.window.geometry("800x500")
        self.crearFormulario()
        self.crearTabla()
        self.refrescarTabla()

    def crearFormulario(self):
        frame = tk.LabelFrame(self.window, text="Formulario Habitaciones", padx=10, pady=10 )
        frame.pack(side="left", padx=10, pady=10)
        
        #numero
        tk.Label(frame, text="numero").grid(row=0, column=0)
        self.txtnumero = tk.Entry(frame)
        self.txtnumero.grid(row=0, column=1)        

        #precio
        tk.Label(frame, text="precio").grid(row=1, column=0)
        self.txtprecio = tk.Entry(frame)
        self.txtprecio.grid(row=1, column=1)
        
        #tipo
        tk.Label(frame, text="tipo").grid(row=2, column=0)
        self.txttipo = tk.Entry(frame)
        self.txttipo.grid(row=2, column=1)
        
        #estado
        tk.Label(frame, text="estado").grid(row=3, column=0)
        self.txtestado = tk.Entry(frame)
        self.txtestado.grid(row=3, column=1)
        
        
        #botones
        tk.Button(frame, text="Registrar").grid(row=4, column=0)
        tk.Button(frame, text="Buscar").grid(row=5, column=0)
        tk.Button(frame, text="Cambiar").grid(row=6, column=0)
        tk.Button(frame, text="Ordenar").grid(row=7, column=0)
    
    def crearTabla(self):
        frame = tk.LabelFrame(self.window, text="Lista Habitaciones", padx=10, pady=10 )
        frame.pack(side="right", padx=10, pady=10)
  
# #datos
        columnas = ("numero","precio","tipo","estado")        
        self.tabla = ttk.Treeview(frame, columns= columnas, show="headings" )
        
        for col in columnas:
            self.tabla.heading(col, text=col )
            self.tabla.column(col, width=100)
        
        self.tabla.pack()
        
        
        
        
    def refrescarTabla(self):
        #self.tabla.delete(*self.tabla.get_children())
        for items in self.controller.habitaciones:
            self.tabla.insert("", tk.END, values=(items.numero,items.precio, items.tipo, items.estado ))
#                 self.numero = numero
#         self.precio = precio
#         self.tipo = tipo
#         self.estado = estado         
# 
# tabla = ttk.Treeview(baseGUI, columns= columnas, show="headings" )
# tabla.heading("Id", text="Id" )
# tabla.heading("Nombre", text="Nombre" )
# 
# tabla.column("Id", width=100)
# tabla.column("Nombre", width=100)
# 
# tabla.insert("", tkGUI.END, values=(1, "Mario"))
# 
# 
# tabla.pack()
        

#         self.idHabitacion = Habitacion.contadorId
    #         FRAME
    #         GRID
    #         PACK
        

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
# 
# import csv, os
# from datetime import datetime
# from model.habitacion import Habitacion
# import view.habitacionesView as vista
# 
# 
# BASE = os.path.dirname(os.path.dirname(__file__))
# ARCHIVO = os.path.join(BASE, "data", "habitaciones.csv")
# LogFile = os.path.join(BASE, "log", "errores.txt")
# 
# 
# class HabitacionController:
# 
#     def __init__(self):
#         self.habitaciones = []
#         self.cargar()
# 
#     def guardarError(self, errorTexto):
#         try:        
#             fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             with open(LogFile, "a", encoding="utf-8") as file:
#                 file.write(f"{fecha} --> {errorTexto}\n")
#         except Exception as nombreError:
#             print(f"Error fatal al guardar logs {nombreError} ")
#             #una notificacion por correo
#                        
#     #que pasa si solo dejamos asi???                       
# 
#     def cargar(self):
#         try:
# #             if not os.path.exists(ARCHIVO):
# #                return
#             with open(ARCHIVO, "r", encoding="utf-8") as file:
#                 reader = csv.reader(file)
#                 for numero, tipo, precio, estado in reader:
#                     self.habitaciones.append(Habitacion(numero, tipo, precio, estado))
#            
#         except Exception as nombreError:
#             self.guardarError(f"Error cargando los datos de la habitacion {nombreError}")
#             vista.mensaje( f"(X) Error cargando los datos de la habitacion")
#         
# 
#     def guardar(self):
#         #try
#         with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             for item in self.habitaciones:                
#                 writer.writerow([item.numero, item.tipo, item.precio, item.estado])
# 
#     def registrar(self, numero, tipo, precio, estado):
#         
#         #try
# #                 habitacion= buscar
# #         
# #         if self.estado == "Ocupada"
# #         
#         self.habitaciones.append(Habitacion( numero, precio, estado, tipo))
#         self.guardar()
#         vista.mensaje("Habitación registrada.")
# 
#     def listar(self):
#         #try
#         vista.mostrar_lista(self.habitaciones)
# 
#     def buscar(self, numero):
#         #try
#         for h in self.habitaciones:
#             if h.numero == numero:
#                 return h
#         return None
# 
#     def cambiar_estado(self, numero):
#         h = self.buscar(numero)
#         if h:
#             h.estado = "Ocupada" if h.estado == "Disponible" else "Disponible"
#             self.guardar()
#             vista.mensaje("Estado actualizado.")
#         else:
#             vista.mensaje("Habitación no encontrada.")
# 
#     def ordenar_precio(self):
#         self.habitaciones.sort(key=lambda x: x.precio)
#         vista.mensaje("Habitaciones ordenadas por precio.")
#         self.listar()
# 
# 
# 
#            
# 
