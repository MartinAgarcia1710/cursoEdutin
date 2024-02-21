#FUNCION QUE CONVIERTE DOLARES
def dolar(valor, monedaAconvertir):
    if monedaAconvertir == 1:
        print("convirtiendo dolares a pesos colombianos")
        return valor * 3750
    elif monedaAconvertir == 2:
        print("convirtiendo dolares a yuanes")
        return valor * 6.37
    elif monedaAconvertir == 3:
        print("convirtiendo dolares a libras esterlinas")
        return valor * 0.76

#FUNCION QUE CONVIERTE EUROS
def euro(valor, monedaAconvertir):
    if monedaAconvertir == 1:
        print("convirtiendo euros a pesos colombianos")
        return valor * 4000
    elif monedaAconvertir == 2:
        print("convirtiendo euros a yuanes")
        return valor * 6.93
    elif monedaAconvertir == 3:
        print("convirtiendo euros a libras esterlinas")
        return valor * 0.83
#COMIENZA PROGRAMA

print("\t\tCONVERSOR DE MONEDAS")

    #SE ELIGE EL TIPO DE MONEDA QUE POSEE
print("SELECCIONE TIPO DE MONEDA QUE POSEE")
print("1. Dolar\n2. Euro")
    #SE INGRESA EL TIPO DE MONEDA QUE POSEE
monedaActual = int(input())
    #VALIDA QUE NO SE INGRESE UN NUMERO MAYOR A 2 PUES NO HAY MAS DE DOS MONEDAS
if monedaActual > 2:
    print("ERROR, REINICIE")
    exit()
    #SE INGRESA EL MONTO A CONVERTIR
print("QUE MONTO DESEA CONVERTIR?")
valor = float(input())
    #SE VALIDA QUE NO SE INGRESE UN NUMERO NEGATIVO
if valor < 0:
    print("NO SE PUEDEN INGRESAR VALORES INFERIORES A CERO, REINICIE")
    exit()
    #SE ELIGE LA MONEDA A CONVERTIR
print("A QUE MONEDA QUIERE CONVERTIR DICHO MONTO")
print("1. Peso colombiano\n2. Yuanes\n3. Libras esterlinas")
monedaAconvertir = int(input())
if monedaAconvertir > 3:
    print("INCORRECTO, REINICIE")
    exit()

if monedaActual == 1:
    resultado = dolar(valor, monedaAconvertir)
elif monedaActual == 2:
    resultado = euro(valor, monedaAconvertir)

print(resultado)
