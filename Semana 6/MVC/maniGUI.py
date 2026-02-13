import tkinter as tk

from controller.habitacionesController import HabitacionController
from view.habitacionesGUI import HabitacionesGUI


root = tk.Tk()
root.title("Menu Principal")
root.geometry("900x900")


habitacionController = HabitacionController()

tk.Button(root, text="Gestion de Habitaciones", command=lambda: HabitacionesGUI(root, habitacionController)).pack()


root.mainloop()

