def mensajeError(mensaje):
    return "XXX Mensaje: ", mensaje

def mensajeExito(mensaje):
    return "OK Mensaje: ", mensaje

def mensajeAdvertencia(mensaje):
    return "!!! Mensaje: ", mensaje


def mensajePersonalizado(tipo, mensaje):
    if tipo == 0:
       return "OK Mensaje: ", mensaje
    elif tipo == -1:
        return "Sin datos Mensaje: ", mensaje
    elif tipo == 1:
        return "datos Mensaje: ", mensaje    
    else:
       return "Error desconocido Mensaje: ", mensaje 