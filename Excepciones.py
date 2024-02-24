import math
'''
    Todo TRY debe tener al menos un EXCEPT o el FINALLY, si solo tuviera este ultimo a continuacion de TRY
    El error se produciria pero las lineas de codigo dentro del FINALLY se ejecutan y termina el programa.
'''
def raiz(n1):
    if n1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(n1)
'''
    El motivo de por que esta esta funcion y lo que es RAISE esta explicado mas abajo, en el bloque
    if (elif) donde se la llama.
'''
def suma(n1, n2):
    print("SUMA")
    return n1 + n2

def resta(n1, n2):
    print("RESTA")
    print("RESTA")
    return n1 - n2

def multiplicacion(n1, n2):
    print("MULTIPLICACION")
    return n1 * n2

def division(n1, n2):
    '''
        Ante un posible error en tiempo de ejecucion podemos usar excepciones, la idea es capturar posibles errores
        que puedan ocurrir y anticiparnos para que el programa no se corte y pueda seguir su flujo hasta terminar.
        En este caso, si ingresan como segundo numero un 0 no se podria dividir, ademas generaria que el programa se
        corte. Con la excepcion notificamos el error y la operacion no se realizara pero el programa seguira su
        flujo luego de comunicar el error.
    '''
    print("DIVISION")
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operacion no realizada"

'''
    En este caso, la excepcion es por si ingresa un valor que no sea de tipo numerico.
    La excepcion es capturada y pide que se vuelva a ingresar. Es una forma de validar mas correcta y menos 
    limitada a la de usar ciclos para volver a ingresar datos erroneos. Aca usamos la excepcion dentro de 
    un while true para que salga del mismo una vez que ingresen datos validos.
'''
while True:
    try:
        numero1 = (int(input("Ingrese el primer numero:\n")))
        numero2 = int(input("Ingrese el segundo numero\n"))
        break
    except ValueError:
        print("Solo se permite elementos de tipo numerico\nINTENTE NUEVAMENTE:\n")
    except:
        print("ERROR!")
'''
    Un try puede tener tantos except como se necesite. Tambien se puede hacer un except generico donde no
    se especifique cual fue el error pero si ocurre, el programa no se detenga. Poco recomendable ya que no
    brinda informacion pero es valido y funciona. 
'''
signo = input("Ingrese el operador matematico: (+, -, *, /\n")

if signo == "+":
    print(suma(numero1, numero2))
elif signo == "-":
    print(resta(numero1, numero2))
elif signo == "*":
    print(multiplicacion(numero1, numero2))
elif signo == "/":
    print(division(numero1, numero2))
elif signo == "$":
    '''
        Esto fue agregado para implementar el RAISE, logicamente cuando se quiere la raiz de un numero solo
        se ingresara 1, para no modificar todo el "programa" lo agregue como extra. El RAISE esta en la funcion
        raiz pero el error se captura en el programa principal cuando se elige la raiz. Lo ideal de RAISE es 
        generar la clase para darle mas forma, en programas como este tan sensillos no tiene mucho sentido pero
        si lo tiene cuando se trabaja con POO y base de datos (posibles errores de conexion a la BD)
    '''
    try:
        print(raiz(numero1))
    except ValueError as ErrorDeNumeroNegativo:
        print(ErrorDeNumeroNegativo)
else:
    print("Signo no valido... cerrando programa")

print("Operacion realizada, adios")

'''
    FINALLY:
    En algunos casos, se puede agregar el finally luego del ultimo except, en casos como este 
    programa no seria necesario, si lo sera en programas mas complejos, en los cuales hara
    la diferencia. Por ejemplo si trabamos con base de datos, dentro del finally estaria el close,
    asegurando que esa linea de codigo se ejecute SI o SI y no corramos riesgos
'''