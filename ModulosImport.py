import random
'''
    import incluye en el archivo a TODA la libreria llamada, si solo quiero un fragmento puedo utilizar FROM
    quedando, siguiendo el ejemplo de este programa, 
            from random import choice
    Si opto por esto, cuando llamo a choise no tengo que especificar de que libreria es, por lo tanto quedaria
            ganador = choice(["Leandro", "Edgard", "Leonor", "Flora"]) 
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