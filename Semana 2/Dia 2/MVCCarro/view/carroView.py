
#Recordatorio lo que esta adentro de los parentesis parametros
def mostrandoDatos(carroObjeto):
    print(carroObjeto.mostrandoDatos)

def mostrandoMensaje(mensaje):
    print(mensaje)    

#Donde nos muestre todo lo que tiene el sistema en el arreglo
def mostrarLista(carroObjeto):
    print("Lista de autos disponibles\n")   

    if not carroObjeto:
        print("No hay datos")
    else:
        for datoIndividual in carroObjeto:
             print(datoIndividual.mostrandoDatos())   
    print("Fin de la lista")         