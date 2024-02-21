#FUNCION
def tablaMultiplicacion(numero = None):
    if numero == None:
        print("EROR! No se ha ingresado un numero!")
    else:
        print(f'TABLA DE MULTIPLICAR DE {numero}')
        for x in range(1, 11):
            print(f'{x} x {numero} = {numero * x}')

valor = int(input("Ingrese numero para ver su tabla de multiplicar:\n"))

#COMIENZA EL PROGRAMA
tablaMultiplicacion(valor)