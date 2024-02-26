nombreUsuario = input("Introduce nombre de usuario:\n")
edad = input("Introduce tu edad:\n")
while(edad.isdigit() == False):
    print("Debes introduciar solo numeros")
    edad = input("Intenta de nuevo ingresando solo numeros\n ")
print(f'Edad ingresada originalmente:\n{edad}\n')
#el método isdigit devuelve true o false segun sea una cadena de numeros o no
print("ISDIGIT")
print(f'La edad ingresada es un numero? {edad.isdigit()}')
print("NOMBRE DE USUARUO INGRESADO ORIGINALMENTE")
print(f'El nombre de usuario es: {nombreUsuario}\n')
#La función upper transforma la cadena en mayúsculas
print("UPPER")
print(f'El nombre de usuario es: {nombreUsuario.upper()}\n')
#El método lower transdorma a la cadena en minusculas
print("LOWER")
print(f'El nombre de usuario es: {nombreUsuario.lower()}\n')
#El método CAPITALIZE pone en mayúscula a la primera letra de la cadena
print("CAPITALIZE")
print(f'El nombre de usuario es: {nombreUsuario.capitalize()}\n')
'''
    Todo input que no tenga como prefijo el tipo de dato, python lo toma como una cadena (string).
    Si se pide un numero y no se especifica que es INT, a la hora de manipular ese dato se puede
    castear... Ejemplo abajo:
'''
if int(edad) < 18:
    print("Es una persona menor de edad")
elif int(edad) >= 18:
    print("Es una persona mayor de edad")
elif int(edad) > 64:
    print("Es una persona mayor de edad y jubilada")
