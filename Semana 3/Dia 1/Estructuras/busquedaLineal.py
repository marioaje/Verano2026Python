# es cuando busca sobre todos los elementos de una lista

def buscarId(self, id):   
    #print("Linea 40", id)     
    for items in self.carroArreglo: 
        #print("Linea 42", items.id, id)           
        if items.id == id:
            #print("Linea 43", id)     
            return items
    return None