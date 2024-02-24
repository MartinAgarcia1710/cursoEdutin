class Persona:
    def __init__(self, nombre, edad, dni, genero):
        #Con __ hago que se produzca encapsulamiento, de esta forma simulo atributos privados
        #y que no puedan ser accedidos desde el interior ya que por defecto, los atributos
        #en python son publicos.
        self.__nombre = nombre
        self.edad = edad
        self.dni = dni
        self.genero = genero

    def saludar(self):
        return print("Hola mi nombre es: ", self.__nombre)
    def setNombre(self, valor):
        self.__nombre = valor
    def getNombre(self):
        return self.__nombre

class Empleado(Persona):
    def __init__(self, nombre, edad, dni, genero, sueldo):
        super().__init__(nombre, edad, dni, genero)
        self.sueldo = sueldo

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

class Auto():
    def __init__(self):
        self.largo = 0
        self.ancho = 0
        self.color = "negro"
        self.enMarcha = False

    def arrancar(self):
        self.enMarcha = True
        if self.enMarcha:
            chequeo = self.__chequeoInterno()
        if self.enMarcha and chequeo:
            return "El auto está en marcha"
        elif self.enMarcha and chequeo == False:
            return "Error en chequeo, Consulte a su mecánico"
        else:
            return "El auto está parado"
    def estado(self):
        print(f'El auto tiene {self.ancho} de acho, {self.largo} de largo y es color {self.color}')
    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        self.nafta = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.nafta == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return  True
        else:
            return False



coche = Auto()
coche.arrancar()
roberto = Persona("Roberto",40, 30123456, "Masculino")
print(coche.estado())
print(roberto.edad, " años")
