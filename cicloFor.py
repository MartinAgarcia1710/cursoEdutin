'''
numero = int(input("Ingrese un numero: "))

for x in range(numero):
    numero -= 1
    print(f'Ahora el numero vale {numero}')
'''

numero = int(input("De que numero queres que se muestre la tabla de multiplicar? "))

for x in range(1, 11):
    print(f'{x} x {numero} = {numero * x}')