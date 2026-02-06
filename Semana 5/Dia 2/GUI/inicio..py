import tkinter as tkGUI
from tkinter import messagebox


#Funciones

def registrar():
    nombre=inputsEntrada.get()
    messagebox.showinfo("Mensaje de info", f"Detalles de info {nombre}")
    messagebox.showerror("Mensaje de error", "Detalles de error")
    messagebox.showwarning("Mensaje de warning", "Detalles de warning")




#Generamos la ventana GUI

ventanaGUI = tkGUI.Tk()

ventanaGUI.title("Clases de Progra")
ventanaGUI.geometry("600x300")

label = tkGUI.Label(ventanaGUI, text="Saludos clase", font=("Arial", 16))
inputsEntrada = tkGUI.Entry(ventanaGUI)
tkGUI.Button(ventanaGUI, text="Registrar", command=registrar).pack()
# tkGUI.Label(ventanaGUI, text="Saludos clase top", font=("Arial", 16)).pack(side="top" )
# tkGUI.Label(ventanaGUI, text="Saludos clase derec", font=("Arial", 16)).pack(side="right" )
# tkGUI.Label(ventanaGUI, text="Saludos clase izq", font=("Arial", 16)).pack(side="left" )
# tkGUI.Label(ventanaGUI, text="Saludos clase bottom", font=("Arial", 16)).pack(side="top" )
label.pack() #
inputsEntrada.pack()