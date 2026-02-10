import tkinter as tkGUI
from tkinter import ttk, messagebox

baseGUI = tkGUI.Tk()
baseGUI.title("Datos")
baseGUI.geometry("300x300")

#datos
columnas = ("Id", "Nombre")

tabla = ttk.Treeview(baseGUI, columns= columnas, show="headings" )
tabla.heading("Id", text="Id" )
tabla.heading("Nombre", text="Nombre" )

tabla.column("Id", width=100)
tabla.column("Nombre", width=100)

tabla.insert("", tkGUI.END, values=(1, "Mario"))


tabla.pack()
