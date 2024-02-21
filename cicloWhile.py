montoVenta = float(input("Ingrese monto de la venta:\n"))
totalArticulosVendidos = 0
totalValorVentas = 0
while montoVenta != 0:
    cantidadArticulos = int(input("Ingrese cantidad de articulos vendidos:850\n"))
    totalArticulosVendidos += cantidadArticulos
    totalValorVentas += montoVenta

    montoVenta = float(input("Ingrese monto de la venta: (presione cero para finalizar)\n"))

print(f'El monto total de ventas es: ${totalValorVentas}\nLa cantidad de articulos vendidos es: {totalArticulosVendidos}')
