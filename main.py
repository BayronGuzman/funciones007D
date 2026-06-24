import Prueba_4_Resevas_Hotel as f #as le da un alias al nombre del archivo para acortarlo y sea mas facil de escribir

lista_reservas = []    
op = 0
while op != 6:
    f.mostrar_menu()
    op = f.ingresar_opcion()
    
    if op == 1:
        f.agregar_reserva(lista_reservas)
        
    elif op == 2:
        nombre_buscar = input("Ingrese el nombre que desea buscar: ")
        posicion = f.buscar_reserva(lista_reservas, nombre_buscar)
        if posicion != -1:
            print("****** Reserva encontrada *******")
            print(f"Nombre del huésped: {lista_reservas[posicion]['huesped']}")
            print(f"Número de la Habitación: {lista_reservas[posicion]['habitacion']}")
            print(f"Noches de Hospedaje: {lista_reservas[posicion]['noches']}")
            estado = "CONFIRMADA" if lista_reservas[posicion]['confirmada'] else "PENDIENTE"
            print(f"Estado: {estado}")
            print("*********************************")
        else:
            print(f"El huesped '{nombre_buscar}' no ha sido encontrado")
            
    elif op == 3:
        nombre_eliminar = input("Ingrese el nombre que desea buscar: ")
        pos = f.buscar_reserva(lista_reservas, nombre_eliminar)
        if pos != -1:
            lista_reservas.pop(pos)
        else:
            print(f"La reserva del huésped {nombre_eliminar} no se encuentra registrada")
            
    elif op == 4:
        f.confirmar_reserva(lista_reservas)
        
    elif op == 5:
        f.confirmar_reserva(lista_reservas)
        print("=== LISTAS DE RESERVAS ===\t")
        for r in lista_reservas:
            print(f"Huésped: {r['huesped']}")
            print(f"Habitación: {r['habitacion']}")
            print(f"Noches: {r['noches']}")
            if r['confirmada']:
                print("Estado: CONFIRMADA\t")
            else:
                print("Estado: PENDIENTE\t")
            print("***********************************************")
            
    elif op == 6:
        print("Gracias por usar el programa. Vuelva Pronto")