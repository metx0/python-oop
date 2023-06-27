import math

class Perro:
    # Definimos métodos y operaciones que pueden ser realizados por objetos de esta clase
    # Python siempre pasa la referencia del objeto en cuestión al primer argumento de los métodos, que por convención se llama "self"
    # por eso debemos poner "self" como el primer parámetro de todos los métodos que definamos

    # El constructor de la clase se llama cada que se crea una nueva instancia de la clase
    # No necesitamos escribir los atributos de la clase antes 
    def __init__(self, nombre, raza): 
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"Guau guau, me llamo {self.nombre}")
    
    def get_nombre(self): 
        return self.nombre
    
    def get_raza(self):
        return self.raza
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_raza(self, nueva_raza):
        self.raza = nueva_raza

    # Una representación en cadena del objeto, que nos dice sus atributos
    def to_string(self):
        return f"Me llamo {self.nombre} y soy de raza {self.raza}"

mi_perro = Perro("Firulais", "Mestizo")
mi_perro.ladrar()
mi_perro.set_raza("Bulldog")
print(mi_perro.to_string())

class Circulo:
    # Tendrá de atributo el radio
    def __init__(self, radio):
        self.radio = radio

    # Calcular el área y la circunferencia del círculo
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_circunf(self):
        return 2 * math.pi * self.radio

"""circulo_1 = Circulo(2.55)
print(circulo_1.calcular_area())
print(circulo_1.calcular_circunf())"""