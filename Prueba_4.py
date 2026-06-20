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

def validar_nombre(nombre):
    return nombre.strip() != ""
    
def validar_especie(especie):
    especie = ["perro", "gato", "ave"]
    return especie.lower()

def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0

def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar en blanco")
        return
    
    especie = input("Ingrese la especie de la mascota: ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie debe ser perro,gato o ave")
        return
    
    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("La edad debe ser un numero entero mayor a 0")
        return
    
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "vacunada": False
    }
    
    lista.append(mascota)
    print("Mascota agregada correctamente")
    
def buscar_mascota(lista_m, nombre_m):
    for m in len(lista_m):
        if nombre_m == lista_m[m]["nombre"]:
            return m
        else:
            return -1
    
def eliminar_mascota(lista_m, nombre_m):
    mascota_eliminar = buscar_mascota(lista_m, nombre_m)
    
    
# CODIGO PRINCIPAL
# Declarar lista
lista_mascotas = []
# Declarar booleano
vacunada = False

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()
    
    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        nombre_buscar = input("Ingrese el nombre de la mascota a buscar: ")
        posicion = buscar_mascota(lista_mascotas, nombre_buscar)
        if posicion != -1:
            print("Mascota encontrada")
            print(f"Mascota: {lista_mascotas[posicion]}")
        else:
            print("Mascota no encontrada")
    elif op == 3:
        