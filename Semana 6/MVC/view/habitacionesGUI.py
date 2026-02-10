import tkinter as tkGUI
# from tkinter import ttkAuxiliar
# from tkinter import messagebox


class HabitacionesGUI:
    
    def __init__(self, baseGUI):
        self.baseGUI = baseGUI
        self.baseGUI.title("Sistema en habitaciones")
        self.baseGUI.geometry("700x400")
        
        #Paneles
        #self.frame_form = tk(Tramas, inputs labels, textareas, choose)
        self.frame_form = tkGUI.Frame(baseGUI )
        self.frame_form.grid(row=0, column=0)
        
        
        self.formularioCrear()
        #Siempre creen funciones como las que hicimso en la vista
        
    def formularioCrear(self):
        tkGUI.Label(self.frame_form, text ="Etiqueta" ).grid(row=0, column=0)
        self.campoText= tkGUI.Entry(self.frame_form)
        self.campoText.grid(row=0, column=1)
        
 
if __name__ == "__main__":     
     baseGUI = tkGUI.Tk()
     app = HabitacionesGUI(baseGUI)
     baseGUI.mainloop()       
 
 