
ventasMensuales = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10: 0,
    11: 0,
    12: 0,
}

print("CUENTA VENTAS ANUAL")

while True:
    print("1. Cargar ventas\n2. Recaudación mensual\n3. Salir\n")
    opcion = int(input("Seleccionar opcion:\n"))
    if opcion == 1:
        numeroCliente = 1
        print("Para finalizar la carga de ventas indique numero de cliente <0>\n")
        numeroCliente = int(input("Ingrese numero de cliente\n"))
        while numeroCliente != 0:
            montoVenta = float(input("Ingrese el monto de la venta\n"))
            mesVenta = int(input("Ingrese el mes de la venta\n"))
            while mesVenta > 12:
                mesVenta = int(input("Mes incorrecto, vuelva a ingresar\n"))
            numeroCliente = int(input("Ingrese numero de cliente\n"))
            ventasMensuales[mesVenta] += montoVenta

    elif opcion == 2:
        for x in ventasMensuales:
            print(ventasMensuales[x])
    elif opcion == 3:
        exit()
    else:
        print("Opcion no valida")


