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
    print("DIVISION")
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operacion no realizada"