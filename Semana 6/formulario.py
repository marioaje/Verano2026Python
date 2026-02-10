import tkinter as FormularioGUI


class Formulario:
    def __init__(self, baseMainGUI):
        self.baseMainGUI = FormularioGUI.Toplevel(baseMainGUI)
        self.baseMainGUI.title("Formulario Base")
        self.baseMainGUI.geometry("300x250")
        
        
        FormularioGUI.Label( self.baseMainGUI, Text="Formularios Bases").pack()
        