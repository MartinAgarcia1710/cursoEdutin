import Clases
agenda = {
    "Eusebio": 1168971258,
    "Genoveva": 1159873654,
    "Romulo": 1147962973,
    "Rita": 1154978264,
}
'''
    consultando = True
    Al principio regí al ciclo while con la variable consultando pero en la opcion salir
    utilice exit() por lo que me pareció innecesaria la variable antes mencionada y cambie
    al ciclo while por un while true. Mientras el usuario navegue por las opciones el ciclo
    debe seguir dando vueltas y si desea salir, con la opcion 5 cierra el programa.
'''

while True:
    print("\t\tAGENDA\n")
    print("1. Consultar\n2. Añadir\n3. Modificar\n4. Borrar\n5. Salir\n")
    opcion = int(input("Seleccione opcion\n"))

    #VALIDA QUE INGRESE UN NUMERO CORRECTO DE OPCION
    while opcion not in (1, 2, 3, 4, 5):
        opcion  = int(input("incorrecto, ingrese de nuevo\n"))

    if opcion == 1:
        print("\tConsultar\n")
        nombre = input("Ingrese contacto a consultar:\n")
        if nombre not in agenda:
            print("Ese contacto no existe.\n")
        else:
            telefono = agenda[nombre]
            print(nombre, ": ", telefono)
    elif opcion == 2:
        print("\tAñadir\n")
        nombre = input("Ingrese nombre de contacto nuevo:\n")
        if nombre in agenda:
            print("Ese contacto ya existe.\n")
        else:
            telefono = int(input("Ingrese el numero de telefono.\n"))
            agenda[nombre] = telefono
            print("Añadido exitosamente")
    elif opcion == 3:
        print("\tModificar\n")
        nombre = input("Ingrese el nombre de contacto que desea modificar:\n")
        if nombre not in agenda:
            print("Ese contacto no existe\n")
        else:
            telefono = int(input("Ingrese el nuevo numero de este contacto:\n"))
            agenda[nombre] = telefono
            print("Modificacion exitosa\n")
    elif opcion == 4:
        print("\tBorrar\n")
        nombre = input("Ingrese nombre de contacto que desea borrar:\n")
        if nombre not in agenda:
            print("Ese contacto no existe\n")
        else:
            del agenda[nombre]
            print(nombre, "exitosamente borrado")
    else:
        print("GRACIAS, VUELVA PRONTOS")
        exit()