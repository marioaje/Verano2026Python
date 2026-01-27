import sys

import os

sys.stdout.reconfigure(encoding="utf-8")

import csv

BASE_DIR = os.path.dirname(__file__) #lee la base del archivo Dia 2

ARCHIVO = os.path.join(BASE_DIR, 'csv', 'personas.csv')

#'csv/personas.csv'

####???
def guardarPersona(id, nombre, edad):
    #open    (src, atributos, lectura, systemaenco)
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoparaguardar:
              writer = csv.writer(archivoparaguardar)
              
              writer.writerow([id, nombre, edad])
              
              print("Se guardaron datos")
              
 
 
def mostrarPersonas():
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            print(item)
            
def mostrarPersonasId(id):
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] == str(id):
                return item           


def modificarPersonas(id, nombre, edad):
   # print(id, nombre, edad)
    arregloVacio = []
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] == str(id):
                item[1] = nombre
                item[2] = edad
                
            arregloVacio.append(item)
            
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
        writer = csv.writer(archivoparaescribir)
        writer.writerows(arregloVacio)
  
    print("actualizo la persona")   
    #print(arregloVacio)



def eliminarPersonas(id):
   # print(id, nombre, edad)
    arregloVacio = []
    
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoparaleer:
        reader = csv.reader(archivoparaleer)
        
        for item in reader:
            if item[0] != str(id):                               
                arregloVacio.append(item)
            
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoparaescribir:
        writer = csv.writer(archivoparaescribir)
        writer.writerows(arregloVacio)
  
    print("Elimino la persona")   
    #print(arregloVacio)

print(mostrarPersonasId(3))
#guardarPersona(3, "Isaac", 21)
modificarPersonas(3, "Alberto", 11)
print(mostrarPersonasId(3))
eliminarPersonas(2)
mostrarPersonas()
