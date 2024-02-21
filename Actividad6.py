class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: \n")
        self.edad = int(input("Ingrese la edad: \n"))

    def imprimir(self):
        return self.nombre, self.edad

class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = float(input("Ingrese el deposito:\n"))

    def imprimir(self):
        super().imprimir()
        print("Deposito: ", self.deposito)
    def impuestos(self):
        if self.deposito > 4000:
            print(f'El ciudadano {self.nombre} deba pagar impuestos')
        else:
            print("El ciudadano ", self.nombre, " no debe pagar impuestos")

ciudadano1 = Ciudadano()
ciudadano1.impuestos()