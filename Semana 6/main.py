import tkinter as tk

#from grid import gridGUI
#from inicio import icicioGUI
from inicio import inicioGUI
from formulario import Formulario
#class inicioGUI:

baseGUI = tk.Tk()
baseGUI.title("Clases de Progra Menu Inicial")
baseGUI.geometry("600x300")

tk.Button(baseGUI, text="Formulario de inicio", command=lambda: inicioGUI(baseGUI)).pack()
tk.Button(baseGUI, text="Formulario", command=lambda: Formulario(baseGUI)).pack()


baseGUI.mainloop()
