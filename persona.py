# Para el tema de atributos de clase y métodos de clase

class Persona:
    # Definimos un atributo de la clase, que será igual en todas las instancias de esta
    numero_de_personas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.aumentar_numero_personas()

    # Definiremos métodos de la clase
    # Utilizando el decorador @classmethod hacemos que se pase la referencia de la clase en lugar de la de la instancia
    @classmethod
    def get_numero_personas(cls):
        return cls.numero_de_personas

    @classmethod
    def aumentar_numero_personas(cls):
        cls.numero_de_personas += 1

p1 = Persona("Jolo")
p2 = Persona("Mimo")
p3 = Persona("Psa")
print(Persona.get_numero_personas())

# Los métodos estáticos son métodos que se incluyen en la clase pero no tienen relación con algún atributo de instancia o de clase
# Se usan en una clase solo para organizar las funciones y que estén mejor estructuradas

class Mates:
    @staticmethod
    def sumar5(x):
        return x + 5