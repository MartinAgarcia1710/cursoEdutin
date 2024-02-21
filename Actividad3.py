'''
    La actividad del curso era el calculo de un promedio como se ve
    en el "CODIGO 1"
    Para hacer algo un poco mas complejo y combinar herramientas
    realice una variante con ciclos combinados y condicionales
    anidados para usar las herramientas vistas hasta el momento,
    esto esta en el "CODIGO 2"
'''

'''
#CODIGO 1
print("CALCULADORA DE PROMEDIOS")

nombre = str(input("Ingresar nombre del alumno:\n"))
cantidadDeMaterias = int(input("Igrese cantidad de materias a promediar:\n"))
cantidadNotas = cantidadDeMaterias
acumuladorNotas = 0

while cantidadDeMaterias != 0:
    nota = float(input("Ingrese Nota:\n"))
    acumuladorNotas += nota
    cantidadDeMaterias -= 1
promedio = round(acumuladorNotas / cantidadNotas , 2)

print(f'El alumno {nombre} tiene un promedio de {promedio}')
'''
#CODIGO 2
acumuladorNotas = 0
variableAux = 1

print("CALCULADORA DE PROMEDIOS")

while variableAux != 0:
    nombre = str(input("Ingresar Nombre del alumno\n"))
    cantidadNotas = int(input("Ingrese cantidad de notas:\n"))
    promedio = 0
    acumuladorNotas = 0

    for x in range(cantidadNotas):
        nota = float(input("Ingrese nota:\n"))
        acumuladorNotas += nota

    promedio = round(acumuladorNotas / cantidadNotas, 2)
    print(f'El promedio de {nombre} es: {promedio}\n')

    if promedio > 6:
        print("ALUMNO APROBADO")
        if promedio == 10:
            print("ALUMNO SOBRESALIENTE")
    elif promedio > 3:
        print("ALUMNO DESAPROBADO, DEBE RECUPERAR")
    else:
        print("ALUMNO APLAZADO, DEBE RECURSAR")

    variableAux = int(input("Desea seguir cargando alumnos? (1: Si ; 0: No\n"))