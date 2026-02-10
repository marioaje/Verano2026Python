import tkinter as tkGUI
from tkinter import messagebox


#funciones
def sumar():
    messagebox.showinfo("Mensaje de info", "Realizando Suma")

#ventana de calculadora
ventanaGUI = tkGUI.Tk()

ventanaGUI.title("Calculadora")
ventanaGUI.geometry("300x250")

# 
# frameTitulo=tkGUI.Frame(ventanaGUI, bg="blue", width="100")
# frameTitulo.pack(side="left", fill="y")
# 
# 
# tkGUI.Label(frameTitulo, text="Calculadora Cientifica").pack(pady=2)


tkGUI.Label(ventanaGUI, text="Calculadora").grid(row=0, column=2, padx=1, pady=1)

#----------------------------------------------- 0
#0-label 1-input
tkGUI.Label(ventanaGUI, text="Dato 1:").grid(row=1, column=0,padx=1, pady=1)
datoA = tkGUI.Entry(ventanaGUI)
datoA.grid(row=1, column=1, padx=1, pady=1)
#-----------------------------------------------
#label input
tkGUI.Label(ventanaGUI, text="Dato 2:").grid(row=2, column=0)
datoB = tkGUI.Entry(ventanaGUI)
datoB.grid(row=2, column=1, padx=1, pady=1)
#-----------------------------------------------
#label resultado
tkGUI.Label(ventanaGUI, text="Resultado:").grid(row=3, column=0)
datoResultado = tkGUI.Entry(ventanaGUI)
datoResultado.grid(row=3, column=1, padx=1, pady=1)
#-----------------------------------------------
#+       -          /            *
tkGUI.Button(ventanaGUI, text="Sumar", command=sumar).grid(row=4, column=0)
tkGUI.Button(ventanaGUI, text="Restar", command=sumar).grid(row=4, column=1)
tkGUI.Button(ventanaGUI, text="Multiplicar", command=sumar).grid(row=4, column=2)

#-----------------------------------------------
#raiz    !         potencia

tkGUI.Button(ventanaGUI, text="Multiplicar", command=sumar).grid(row=5, column=0)
tkGUI.Button(ventanaGUI, text="Raiz", command=sumar).grid(row=5, column=1)
tkGUI.Button(ventanaGUI, text="Potencia", command=sumar).grid(row=5, column=2)
ventanaGUI.mainloop()