import tkinter as tkGUI

#Generamos la ventana GUI

ventanaGUI = tkGUI.Tk()

ventanaGUI.title("Clases de Progra")
ventanaGUI.geometry("600x300")

label = tkGUI.Label(ventanaGUI, text="Saludos clase", font=("Arial", 16))
label.pack()