'''
    El generador hace que devuelva solo un elemento, evitando asi el consumo de recursos, el yield deja la funcion
    en suspencion, cada vez que se la vuelva a llamar retoma de donde quedo la ultima vez, a diferencia de las
    funciones tradicionales que arman o recorren toda una lista y al retornar desaparece, si se la vuelve a llamar
    empieza de cero.
'''

def generadorDePares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1

def devuelveCiudades(*ciudades):
    for x in ciudades:
        yield from x
'''
    yield from lo que hace es simular un ciclo anidado, para ingresar en los sub elementos que integran al elemento
    de la lista, en este caso ciudades, Al ser una cadena lo que devuelve en cada llamado es los caracteres de cada
    cadena. 
'''
ciudadesDevueltas = devuelveCiudades("Tokio", "Madrid", "Buenos Aires", "Lisboa", "Nueva York", "Auckland")
devuelvePares = generadorDePares(10)

print(next(devuelvePares))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")
print(next(devuelvePares))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")
print(next(devuelvePares))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")

print(next(ciudadesDevueltas))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")
print(next(ciudadesDevueltas))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")
print(next(ciudadesDevueltas))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")
print(next(ciudadesDevueltas))
print("Sigue el codigo\n\t\t|\n\t\t|\n\t\t|")