#calculadoraView.py

#la vista va a recibir del controller 
def presntardatos(calculadoraModell):
    print(calculadoraModell.presntardatos())

def mostraResultado(operacion, resultado):
    print(f"\nResultado de la {operacion}: {resultado}")