import tkinter as tkGUI
from tkinter import messagebox

class inicioGUI:
#Funciones
    def __init__(self, baseGUI):
        #self.root,raiz, baseGUI, interfaz
        self.baseGUI = tkGUI.Toplevel(baseGUI)
        self.baseGUI.title("Clases de Progra")
        self.baseGUI.geometry("600x300")
        
        tkGUI.Label(self.baseGUI, Text="Formulario Inicio").pack()



#Generamos la ventana GUI
# 
# ventanaGUI = tkGUI.Tk()
# 
# ventanaGUI.title("Clases de Progra")
# ventanaGUI.geometry("600x300")
# 
# label = tkGUI.Label(ventanaGUI, text="Saludos clase", font=("Arial", 16))
# inputsEntrada = tkGUI.Entry(ventanaGUI)
# tkGUI.Button(ventanaGUI, text="Registrar", command=registrar).pack()
# label.pack() #
# inputsEntrada.pack()
#     
#     
#     
#     
#     def registrar():
#         nombre=inputsEntrada.get()
#         messagebox.showinfo("Mensaje de info", f"Detalles de info {nombre}")
#         messagebox.showerror("Mensaje de error", "Detalles de error")
#         messagebox.showwarning("Mensaje de warning", "Detalles de warning")


