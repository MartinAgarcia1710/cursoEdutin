
ventasMensuales = {
    "Enero": 0,
    "Febrero": 0,
}

print("CUENTA VENTAS ANUAL")
varAux = 1;
acumuladorMensual = []

while varAux != 0:
    montoVenta = float(input("Ingrese el monto de la venta\n"))
    mesVenta = int(input("Ingrese el mes de la venta\n"))
    if mesVenta == 1:
        ventasMensuales["Enero"] += montoVenta
    varAux = int(input("Desea seguir cargando ventas? (0: No, 1: Si\n"))

print(ventasMensuales)
