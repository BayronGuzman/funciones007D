# FUNCIONES
def ficha_producto(nombre, precio, stock): #No importa el orden de los parametros
    print("===================")
    print(f"||Nombre del producto: {nombre} ||")
    print(f"||Nombre del producto: {stock} ||")
    print(f"||Nombre del producto: {precio} ||")
    print("===================")

# CODIGO PRINCIPAL

try:
    nombre = input("Ingrese su nombre: ")
except ValueError:
    print("Debe ingresar números")
    
while True:
    try:
        stock1 = int(input("Ingrese el stock: "))
        if stock1 < 0:
            print("Debe ser mayor o igual a o")
        else:
            break
    except ValueError:
        print("Debe ingresar números")
        
while True:
    try:
        precio1 = int(input("Ingrese el precio: "))
        if stock1 <= 0:
            print("Debe ser mayor o igual a o")
        else:
            break
    except ValueError:
        print("Debe ingresar números")

ficha_producto(nombre, precio1, stock1)