import tkinter as tkil

from view.menu import menu
from controller.HabitacionController import HabitacionController

habitacionController = HabitacionController()

baseGUI = tkil.Tk()

menu(baseGUI, habitacionController)


baseGUI.mainloop()