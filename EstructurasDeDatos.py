#LISTAS
#Aparentemente dinamicas, ya que no es necesario declarar cuantos elementos va a tener como en c++
listaDeNumeros = []
#carga de numeros en la lista, en este caso el ciclo for determina cantidad de elementos dentro
for x in range(5):
    print(f'posicion: {x + 1} indice {x} ... ingresa')
    #con la funcion append se agregan los elementos
    listaDeNumeros.append(int(input()))
#sort los ordena de menor a mayor dentro de la lista
listaDeNumeros.sort()
print(f'\nLISTADO\n {listaDeNumeros}')
print("**************************************")
for x in listaDeNumeros:
    #otra forma de mostrar lo que tiene la lista (no se muestran los corchetes)
    print(x)
#CONTAR CUANTAS VECES EXISTE UN DETERMINADO VALOR DENTRO DE UNA LISTA, count lleva como parametro el valor a contar dentro de la lista
listaDeNumeros.count(10)

#eliminar elementos de la lista
#remove toma como parametro un elementos existente dentro de la lista, si existe el 2 lo busca y lo elimina
listaDeNumeros.remove(10)
print("Lista sin el contenido 10\n")
print(f'\nLISTADO\n {listaDeNumeros}')

#pop toma como parametro el indice de la lista
listaDeNumeros.pop(1)

print("lista sin el indice 2")
print(f'\nLISTADO\n {listaDeNumeros}')

#del toma como parametro entre [] el indice del elemento a eliminar
del listaDeNumeros[0]
print("Lista sin el incide 0")
print(f'\nLISTADO\n {listaDeNumeros}')

#clear borra el contenido de toda la listra
listaDeNumeros.clear()
print("LISTA VACIA")
print(f'\nLISTADO\n {listaDeNumeros}')