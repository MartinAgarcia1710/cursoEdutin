import pickle
#Esta libreria es la que me permite manipular archivos binarios.

class Celular():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def mostrar(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}')

celu1 = Celular("I-phone", "13 PRO MAX", "Aquamarine")

fichero = open("listaCelulares", "ab")
pickle.dump(celu1, fichero)
fichero.close()

fichero = open("listaCelulares", "rb")
celu2 = pickle.load(fichero)
fichero.close()

celu2.mostrar()