#FUNCIONES
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del 1 al 6: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            return opcion
        except ValueError:
            print("Opción invalida, Ingrese un número entero del 1 al 6")

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("Agregar producto")
    print("Eliminar producto")
    print("Salir")
    print("==========================")

def stock_categoria(productos, ventas, categoria):
    total_stock = 0
    for codigo, datos in productos.items():
        if datos[1] == categoria:
            total_stock += ventas[codigo][1]
    print(f"El total del stock disponible es de: {total_stock}")

def busqueda_precio(productos, ventas, precio_min, precio_max):
    resultados = []
    for codigo, datos in ventas.items():
        precio = datos[0]
        stock = datos[1]
        if precio_min <= precio <= precio_max and stock != 0:
            nombre_producto = productos[codigo][0]
            resultados.append(f"{nombre_producto}--{codigo}")

def buscar_codigo(ventas, codigo):
    return codigo in ventas

def actualziar_precio(ventas, codigo, nuevo_precio):
    if buscar_codigo(ventas, codigo):
        ventas[codigo][0] = nuevo_precio
        return True
    else
        return False

def validar_codigo_nuevo(productos, codigo):
    if codigo.strip() == "":
        return False
    if codigo in productos:
        return False
    return True

def validar_texto_no_vacio(texto):
    return texto.strip() != ""

def validar_tamano(tamano):
    return tamano in ("chico", "mediano", "grande")

def validar_temporada(respuesta):
    return respuesta in ("s", "n")

def validar_numero_entero_positivo():
    try:
        valor = int(valor_texto)
        return valor > 0
    except ValueError:
        return False
    
def validar_entero_no_negativo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor >= 0
    except ValueError:
        return False

def agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche, es_temporada, precio, stock_disponible, productos, ventas):
    if codigo in productos:
        return False
    
    productos[codigo] = [nombre_producto, categoria, tamano, tipo_leche, es_temporada]

    ventas[codigo] = [precio, stock_disponible]

    return True

def eliminar_producto(codigo, productos, ventas):
    if buscar_codigo(codigo, ventas):
        del productos[codigo]
        del ventas[codigo]
        return True
    else:
        return False
        
#CODIGO PRINCIPAL
productos = {
    'P001': ['Capuccino Clásico', 'cafe', 'mediano', 'entera', False],
    'P002': ['Latte Vainilla', 'cafe', 'grande', 'descremada', True],
    'P003': ['Té Verde Helado', 'te', 'mediano', 'sin leche', False],
    'P004': ['Mocha Avellana', 'cafe', 'grande', 'entera', True],
    'P005': ['Chocolate Caliente', 'bebida', 'chico', 'entera', False],
    'P006': ['Té Chai Latte', 'te', 'mediano', 'descremada', True],
    }

ventas = {
    'P001': [2500, 15],
    'P002': [3200, 0],
    'P003': [2800, 10],
    'P004': [3500, 4],
    'P005': [2200, 7],
    'P006': [3100, 9],
    }

continuar = True
while continuar:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese categoría a consultar: ")
        stock_categoria(categoria, productos, ventas)

    elif opcion == 2:
        precio_min = None
        precio_max = None
        while precio_min is None or precio_max is None:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
            except ValueError:
                print("Debe ingresar valores enteros")
                precio_min = None
                precio_max = None

        busqueda_precio(precio_min, precio_max, productos, ventas)

    elif opcion == 3:
        repetir = "s"
        while repetir == "s":
            codigo = input("Ingrese código del producto: ").upper()

            nuevo_precio_valido = False
            while not nuevo_precio_valido:
                nuevo_precio_texto = input("Ingrese nuevo precio: ")
                if validar_entero_positivo(nuevo_precio_texto):
                    nuevo_precio = int(nuevo_precio_texto)
                    nuevo_precio_valido = True
                else:
                    print("El precio debe ser un entero positivo")

            if actualizar_precio(codigo, nuevo_precio, ventas):
                print("Precio actualizado")
            else:
                print("El código no existe")

            repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

    elif opcion == 4:
        codigo = input("Ingrese código del producto: ").upper()

        if not validar_codigo_nuevo(codigo, productos):
            print("El código no es válido o ya existe")
        else:
            nombre_producto = input("Ingrese nombre del producto: ")
            if not validar_texto_no_vacio(nombre_producto):
                print("El nombre no puede estar vacío")
            else:
                categoria = input("Ingrese categoría: ")
                if not validar_texto_no_vacio(categoria):
                    print("La categoría no puede estar vacía")
                else:
                    tamano = input("Ingrese tamaño (chico/mediano/grande): ").lower()
                    if not validar_tamano(tamano):
                        print("El tamaño ingresado no es válido")
                    else:
                        tipo_leche = input("Ingrese tipo de leche: ")
                        if not validar_texto_no_vacio(tipo_leche):
                            print("El tipo de leche no puede estar vacío")
                        else:
                            es_temporada_resp = input("¿Es producto de temporada? (s/n): ").lower()
                            if not validar_es_temporada(es_temporada_resp):
                                print("Debe responder 's' o 'n'")
                            else:
                                precio_texto = input("Ingrese precio: ")
                                if not validar_entero_positivo(precio_texto):
                                    print("El precio debe ser un entero positivo")
                                else:
                                    stock_texto = input("Ingrese stock disponible: ")
                                    if not validar_entero_no_negativo(stock_texto):
                                        print("El stock debe ser un entero ""mayor o igual a cero")
                                    else:
                                        es_temporada = (es_temporada_resp == "s")
                                        precio = int(precio_texto)
                                        stock_disponible = int(stock_texto)

                                        if agregar_producto(codigo, nombre_producto,categoria, tamano,tipo_leche, es_temporada, precio, stock_disponible, productos, ventas):
                                            print("Producto agregado")
                                        else:
                                            print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese código del producto a eliminar: ").upper()

        if eliminar_producto(codigo, productos, ventas):
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        continuar = False




