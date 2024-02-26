import random
#from random import *
from Clases import *
'''
    No solo se pueden importar bibliotecas o codigos de terceros, sino tambien archivos que yo creo como clases.
    como en c++ el include, es lo mismo.
'''
'''
    import incluye en el archivo a TODA la libreria llamada, si solo quiero un fragmento puedo utilizar FROM
    quedando, siguiendo el ejemplo de este programa, 
            from random import choice
    Si opto por esto, cuando llamo a choice no tengo que especificar de que libreria es, por lo tanto quedaria
            ganador = choice(["Leandro", "Edgard", "Leonor", "Flora"]) 
    Si no quiero especificar a cada rato a que modulo pertenece la funcion o metodo que llamo lo que tengo que hacer es
    importarlo de la manera que está escrito debajo de import random, está comentado ya que decidí utilizar en otro.
    En programas sencillos y muy cortos como estos de práctica no hay problema de importar todo pero en programas 
    complejos y con muchas lineas de codigo importar todo es reservar un espacio muy grande en memoria, por lo que no
    optimiza el codigo y consume recursos.
'''
print("\t\tSORTEO DE LOTERIA RIFAS -CANGUROBINGO-")
print("Participantes:\nLeandro\nEdgard\nLeonor\nFlora")

ganador = random.choice(["Leandro", "Edgard", "Leonor", "Flora"])

print(f'El ganador es....{ganador}\n')

numero = int(input(f'{ganador}, podes duplicar tu premio si ingresas un numero y aciertas\nElige un numero entre 1 y 50\n'))

sorteado = random.randint(1, 50)
print(f'El numero ganador es:{sorteado}')

if numero == sorteado:
    print("GANASTE")
else:
    print("CUA CUA CUA CUA... SUERTE PARA LA PROXIMA")

roberto = Persona("Roberto", 55, 35456987, "masculino")
print(roberto.saludar())