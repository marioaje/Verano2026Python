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
        tk.Button(frame, text="Registrar", command=self.registrar).grid(row=4, column=0)
        tk.Button(frame, text="Buscar", command=self.buscar).grid(row=5, column=0)
        tk.Button(frame, text="Cambiar Estado", command=self.cambiar_estado).grid(row=6, column=0)
        tk.Button(frame, text="Ordenar", command=self.ordenar_precio).grid(row=7, column=0)
    
    def crearTabla(self):
        frame = tk.LabelFrame(self.window, text="Lista Habitaciones", padx=10, pady=10 )
        frame.pack(side="right", padx=10, pady=10)
  
        #datos
        columnas = ("numero","precio","tipo","estado")        
        self.tabla = ttk.Treeview(frame, columns= columnas, show="headings" )
        
        for col in columnas:
            self.tabla.heading(col, text=col )
            self.tabla.column(col, width=100)
        
        self.tabla.pack()
        
        
    def refrescarTabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for items in self.controller.habitaciones:
            self.tabla.insert("", tk.END, values=(items.numero,items.precio, items.tipo, items.estado ))
            
            
    def registrar(self):
        numero = self.txtnumero.get().strip()
        tipo = self.txttipo.get().strip()
        precio = self.txtprecio.get().strip()
        estado = self.txtestado.get().strip()
        
        if not numero or not tipo or not precio or not estado:
            messagebox.showwarning("Mensaje de warning", "Existen campos vacios")
            return
        try:  
            self.controller.registrar(numero, tipo, precio, estado)
            self.refrescarTabla()
        except Exception as exMensj:    
            messagebox.showerror("Mensaje de error", f"Detalles de error{exMensj}")
            
            
    def ordenar_precio(self):
        self.controller.ordenar_precio()
        self.refrescarTabla()
    
    def buscar(self):
        numero = self.txtnumero.get().strip()        
        if not numero:
            messagebox.showwarning("Mensaje de warning", "Ingrese el numero de habitacion")
            return
        
        habitacion = self.controller.buscar(numero)
        if habitacion:            
            messagebox.showinfo("Mensaje de info", f"Detalles de info {habitacion.mostrar_info()}")
        else:
            messagebox.showinfo("Mensaje de info", "Sin datos")


    def cambiar_estado(self):
        numero = self.txtnumero.get().strip()
          
        if not numero:
            messagebox.showwarning("Mensaje de warning", "Ingrese el numero de habitacion")
            return
        
        habitacion = self.controller.buscar(numero)
        if habitacion:
            self.controller.cambiar_estado(numero)
            self.refrescarTabla()
            return
            
        else:
            messagebox.showinfo("Mensaje de info", "Sin datos")          
#        

