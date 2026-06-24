def mostrar_menu():
    print("=====MENU PRINCIPAL=====")
    print("1.- Agregar Reserva")
    print("2.- Buscar Reserva")
    print("3.- Eliminar Reserva")
    print("4.- Confirmar Reservas")
    print("5.- Mostrar Reservas")
    print("6.- Salir")
    
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1 - 6): "))
            if opcion < 1 or opcion > 6:
                print("El número de la opción debe estar entre el 1 y el 6.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número no un caracter")
    
    return opcion    

def validar_nombre(name):
    return name.strip() != ""

def validar_numero_habitacion(numero_habitacion):
    return numero_habitacion.isdigit() and int(numero_habitacion) >= 1 and int(numero_habitacion) <= 200

def validar_cantidad_noches(cantidad_noches):
    return cantidad_noches.isdigit() and int(cantidad_noches) > 0
    

def agregar_reserva(lista):
    nombre_completo = input("Ingrese el nombre completo del huesped: ")
    correcto = validar_nombre(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacío.")
        return
    
    habitacion = input("Ingrese el número de la habitación: ")
    correcto = validar_numero_habitacion(habitacion)
    if not correcto:
        print("El número de habitación debe ser un entero del 1 al 200.")
        return
            
    noches = input("Ingrese la cantidad de noches: ")
    correcto = validar_cantidad_noches(noches)
    if not correcto:
        print("La cantidad de noches debe ser un número entero positivo")
        return
        
    reserva = {
        "huesped": nombre_completo.strip(),
        "habitacion": int(habitacion),
        "noches": int(noches),
        "confirmada": False
    }
    
    lista.append(reserva)
    print("Reserva agregada correctamente")
    
def buscar_reserva(lista_r, nombre_r):
    for r in range(len(lista_r)):
        if nombre_r == lista_r[r]["huesped"]:
            return r
    return -1

def confirmar_reserva(lista_r):
    for r in lista_r:
        if r["noches"] >= 2:
            r["confirmada"] = True
        else:
            r["confirmada"] = False
