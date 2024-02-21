'''
    Primera actividad, pedido de datos, ingreso de los mismos
    se procesan operaciones básicas
    por ultimo se comparan y arroja true o false segun
    corresponda
'''

#Pedido de datos
primerNumero = int(input("Ingresa el primer numero: " ))
segundoNumero = int(input("Ingresa el segundo numero: "))
#operaciones
#esta forma muestra la operacion antes de mostrar el resultado
print(primerNumero, "+", segundoNumero, "=", primerNumero + segundoNumero)
#esta forma muestra solo el resultado
print(f'La suma de ambos numeros es {primerNumero + segundoNumero}')
print(f'La resta de ambos numeros es {primerNumero - segundoNumero}')
print(f'La multiplicacion de ambos numeros es {primerNumero * segundoNumero}')
print(f'La division de numeros es {primerNumero / segundoNumero}')
#relaciones
print(f'Son iguales? {primerNumero == segundoNumero}')
print(f'El primer numero es mayor? {primerNumero > segundoNumero}')
print(f'El segundo numero es mayor? {segundoNumero > primerNumero}')
