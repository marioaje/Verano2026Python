# === SISTEMA DE CONDOMINIOS COSTAMAR ===
# 1. Gestionar Habitaciones
# 2. Gestionar Huéspedes
# 3. Gestionar Reservas
# 4. Reportes
# 5. Salir
from controller.habitacionesController import HabitacionController


def main():

    hCtrl = HabitacionController()


    while True:
        print("""
            === SISTEMA DE CONDOMINIOS COSTAMAR ===
            1. Gestión de Habitaciones
            2. Gestión de Huéspedes
            3. Gestión de Reservas
            4. Reportes
            5. Salir
            """)

        op = input("Seleccione: ")
#numero, tipo, precio, estado
        if op == "1":
            menu_habitaciones(hCtrl)

        elif op == "2":
            menu_habitaciones(hCtrl)

        elif op == "3":
            menu_habitaciones(hCtrl)

        elif op == "4":
            menu_habitaciones(hCtrl)

        elif op == "5":
            break

def menu_habitaciones(ctrl):
    print("""
            --- Habitaciones ---
            1. Registrar
            2. Listar
            3. Buscar
            4. Cambiar Estado
            5. Ordenar por Precio
            6. o Cualquier tecla para regresar
            """)
    op = input("Seleccione: ")

    if op == "1":
        numero = input("Número: ")
        tipo = input("Tipo: ")
        precio = input("Precio: ")
        estado = input("Estado: ")
        ctrl.registrar(numero, tipo, precio, estado)

    elif op == "2":
        ctrl.listar()
        
    elif op == "3":
        ctrl.listar()

    elif op == "4":
        ctrl.listar()


   

if __name__ == "__main__":
    main()
