
class Persona:
    def __init__(self, nombre, edad, dni, genero):
        #Con __ hago que se produzca encapsulamiento, de esta forma simulo atributos privados
        #y que no puedan ser accedidos desde el interior ya que por defecto, los atributos
        #en python son publicos.
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.genero = genero

    def saludar(self):
        return print("Hola mi nombre es: ", self.nombre)
    def setNombre(self, valor):
        self.nombre = valor
    def getNombre(self):
        return self.nombre
#----------------------------------------------------------------------------------- CLASE EMPLEADO
class Empleado(Persona):
    def __init__(self , nombre, edad, dni, genero, sueldo):
        super().__init__(nombre, edad, dni, genero)
        self.sueldo = sueldo
    #metodo sobre escrito de la clase padre
    def saludar(self):
        super().saludar()
        print("y mi sueldo es $", self.sueldo)
#-------------------------------------------------------------------------------------- CLASE VEHICULOS
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
#-------------------------------------------------------------------------------------CLASE AUTO
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
    def presentacion(self):
        print("Soy un auto")


'''
    Cuando hay herencia multiple y existen constructores den las clases padres, la clase hija
    va a priorizar el constructor de la primera que se ponga en los (). En este caso la prioridad
    la tendrá la clase Vehiculos, pues figura antes que Auto
'''
class AutoFamiliar(Vehiculos, Auto):
    def presentacion(self):
        print("Soy un auto familiar")

#-------------------------------------------------------------------------------------- POLIMORFISMO
'''
    
'''
def presentacionVehiculos(vehiculo):
    vehiculo.presentacion()



#coche = Auto()
#coche.arrancar()
roberto = Empleado("Roberto",40, 30123456, "Masculino", 50000)
#print(coche.estado())
#print(roberto.edad, " años")
roberto.saludar()
'''
    En programas complejos y con muchas clases, herencias y herencias multiples puede ser muy util
    la funcion isinstance(), la cual devuelve True o False dependiendo de si el objeto pertenece o no
    a la clase que enviamos como parametro. 
'''
print(isinstance(roberto, Vehiculos))
print(isinstance(roberto, Persona))
vehi1 = Auto()
vehi2 = AutoFamiliar("fd", "dfs")

presentacionVehiculos(vehi1)
presentacionVehiculos(vehi2)