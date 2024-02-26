from paquetes.Calculos import *
from paquetes.subpaquetes.sub import *
'''
    Un paquete es una sub carpeta en nuestra carpeta de proyectos en la cual guardamos archivos con codigo para 
    reutilizacion, para llegar a ellas con import hay que usar nomenclatura del punto con la ruta de las carpetas
    como en c++ haciamos con / 
    Se pueden armar tantas subcarperas como se quiera, una dentro de la otra. 
    Para armar paquetes, cada carperta y sub carpera que utilicemos como paquete debe contener un archivo de python 
    llamado: __init__.py
'''
print(suma(5, 5))
devolver(5)