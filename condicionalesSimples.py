'''
    Hacer un programa que pida un numero y si es positivo que imprima
    por pantalla "ES POSITIVO", de lo contrario "ES NEGATIVO". En caso
    de que se a cer "ES CERO"
'''

numero = int(input("Ingresar numero"))

if numero > 0:
    print("ES POSITIVO")
elif numero == 0:
    print("ES CERO")
else:
    print("ES NEGATIVO")