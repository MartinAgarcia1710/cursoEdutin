from io import *
'''
    manejo de archivos de texto. al igua que c++ open y close. el metodo
    w es para escribir
    r es para leer
    a es para agregar
'''
archivoTexto = open("pruebadetexto.txt", "w")

frase = "Esta es la prueba para manipular archivos de texto desde python"

archivoTexto.write(frase)

archivoTexto.close()

archivoTexto = open("pruebadetexto.txt", "a")

frase = "\nEsta linea es agregada con append"

archivoTexto.write(frase)

archivoTexto.close()

archivoTexto = open("pruebadetexto.txt", "a")

archivoTexto.seek(0 )

frase = "\nEsta linea es agregada adelante de todo con el metodo seek"

archivoTexto.write(frase)

archivoTexto.close()