# Para el tema de herencia
# Ambas clases tienen de atributos nombre y edad y heredarán de la clase padre Mascota

class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def to_string(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} años")

    def hablar(self):
        print("Yo hablo como la mascota general")

class Gato(Mascota):
    # Queremos añadir el atributo de color a la clase, redefinir el constructor de la clase
    # Lo hacemos llamando al constructor de la clase padre y añadiendo el atributo de color
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad) # LLamamos al constructor de la clase padre Mascota, y le pasamos nombre y edad
        self.color = color

    # Si definimos un método que ya está definido en la clase Padre, este nuevo método lo sobreescribe automáticamente
    def hablar(self):
        print("Miau")
    
    def to_string(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad} años y soy {self.color}")

class Perro(Mascota):
    def hablar(self):
        print("Guau")

def main():
    m = Mascota("Masco", 10)
    m.hablar()

    g = Gato("Lolo", 15, "azul")

    # Podemos llamar al método to_string() porque Gato hereda de Mascota y dicho método está en esa clase
    g.to_string()
    g.hablar()

    p = Perro("Plom", 8)
    p.to_string()
    p.hablar()

main()