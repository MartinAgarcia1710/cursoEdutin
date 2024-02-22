def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    '''
        Ante un posible error en tiempo de ejecucion podemos usar excepciones, la idea es capturar posibles errores
        que puedan ocurrir y anticiparnos para que el programa no se corte y pueda seguir su flujo hasta terminar.
        En este caso, si ingresan como segundo numero un 0 no se podria dividir, ademas generaria que el programa se
        corte. Con la excepcion notificamos el error y la operacion no se realizara pero el programa seguira su
        flujo luego de comunicar el error.
    '''
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operacion no realizada"
'''
    En este caso, la excepcion es por si ingresa un valor que no sea de tipo numerico.
    La excepcion es capturada y pide que se vuelva a ingresar. Es una forma de validar mas correcta y menos 
    limitada a la de usar ciclos para volver a ingresar datos erroneos.
'''
try:
    numero1 = (int(input("Ingrese el primer numero:\n")))
except ValueError:
    numero1 = (int(input("Solo se elementos de tipo numerico\nIngrese el primer numero nuevamente:\n")))

try:
    numero2 = int(input("Ingrese el segundo numero\n"))
except ValueError:
    numero2 = (int(input("Solo se elementos de tipo numerico\nIngrese el segundo numero nuevamente:\n")))

signo = input("Ingrese el operador matematico: (+, -, *, /\n")

if signo == "+":
    print(suma(numero1, numero2))
elif signo == "-":
    print(resta(numero1, numero2))
elif signo == "*":
    print(multiplicacion(numero1, numero2))
elif signo == "/":
    print(division(numero1, numero2))
else:
    print("Signo no valido... cerrando programa")
print("Operacion realizada, adios")