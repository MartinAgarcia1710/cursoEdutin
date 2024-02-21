print("CUENTA VENTAS ANUAL")
varAux = 1;
acumuladorMensual = []

while varAux != 0:
    montoVenta = float(input("Ingrese el monto de la venta\n"))
    mesVenta = int(input("Ingrese el mes de la venta\n"))
    acumuladorMensual[mesVenta - 1] += montoVenta
    varAux = int(input("Desea seguir cargando ventas? (0: No, 1: Si\n"))

print(acumuladorMensual)
