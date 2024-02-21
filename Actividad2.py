nombre = str(input("Ingresar nombre de cliente: "))
valorCompra = float(input("Ingrese valor de compra: "))

if valorCompra < 80:
    valorFinal = valorCompra
elif valorCompra >= 80 and valorCompra < 150:
    valorFinal = valorCompra - (valorCompra * 10 / 100)
    print("10 % DE DESCUENTO")
elif valorCompra >= 150 and valorCompra <= 300:
    valorFinal = valorCompra - (valorCompra * 15 / 100)
    print("15 % DE DESCUENTO")
elif valorCompra > 300 and valorCompra <= 500:
    valorFinal = valorCompra - (valorCompra * 20 / 100)
    print("20 % DE DESCUENTO")

print(f'El Cliente {nombre} realizó una venta de ${valorCompra} y con descuento queda en ${valorFinal}')
print(f'Felicitaciones, tuvo un descuento de: ${valorCompra - valorFinal}')