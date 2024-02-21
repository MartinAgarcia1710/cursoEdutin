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


roberto = Persona("Roberto",40, 30123456, "Masculino")
#print(roberto.saludar())
print(roberto.edad, " años")