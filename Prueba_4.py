# FUNCIONES
def mostrar_menu():
    print("=========================")
    print("*****MENU PRINCIPAL*****")
    print("1.- Agregar Mascota")
    print("2.- Buscar Mascota")
    print("3.- Eliminar Mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar Mascota")
    print("6.- Salir")
    print("=========================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1 - 6): "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opción dl 1 al 6")
            else:
                break
        except ValueError:
            print("Opción invalida, debe ingresar un número")
    return opcion

# CODIGO PRINCIPAL
# Declarar lista
lista_mascotas = []
# Declarar booleano
vacunada = False

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()