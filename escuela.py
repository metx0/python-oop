# Clase Estudiante que representa a un estudiante de una clase
# Atributos: el nombre, la edad y la calificación (nota)

class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad

        if nota >= 0 and nota <= 100:
            self.nota = nota 
        else:
            print(f"La nota de {nombre} debe estar en el rango de (0-100)")

    # Método para obtener la nota del estudiante
    def get_nota(self):
        return self.nota
    
    # Método para obtener el nombre del estudiante
    def get_nombre(self):
        return self.nombre

# Clase Curso que representa un curso escolar
# Atributos: el nombre del curso y el número máximo de estudiantes que se pueden meter

class Curso:
    def __init__(self, nombre, max_estudiantes):
        self.nombre = nombre
        self.max_estudiantes = max_estudiantes # La capacidad máxima de estudiantes en el curso
        self.estudiantes = [] # Lista que representa a los estudiantes en el curso

    # Método para añadir a un estudiante al curso, o sea, añadirlo a la lista "estudiantes"   
    # param "estudiante": una instancia de la clase "Estudiante"
    def agregar_estudiante(self, estudiante):
        # Tenemos que comprobar que la longitud de la lista estudiantes sea menor a max_estudiantes
        if len(self.estudiantes) < self.max_estudiantes:
            self.estudiantes.append(estudiante)
            return True
        
        print(f"No se pudo agregar a {estudiante.nombre}. Se ha alcanzado la capacidad máxima del curso")
    
    # Método para obtener el promedio de las notas de los estudiantes
    def calcular_nota_promedio(self):
        # Obtendremos la suma de las notas de los estudiantes y la dividiremos entre el total de estudiantes
        suma_notas = 0

        for estudiante in self.estudiantes:
            suma_notas += estudiante.get_nota()

        return suma_notas / len(self.estudiantes)

    # Método para obtener la nota más alta y a quién corresponde
    def calcular_nota_mayor(self):
        nota_mayor = 0

        for estudiante in self.estudiantes:
            if estudiante.get_nota() > nota_mayor:
                nota_mayor = estudiante.get_nota()
                nombre_mayor = estudiante.get_nombre()

        return nota_mayor, nombre_mayor

def main():
    # Crearemos estudiantes, un curso y añadiremos los estudiantes a dicho curso
    Manuel = Estudiante("Manuel", 18, 100)
    Juan = Estudiante("Juan", 18, 90)
    Jorge = Estudiante("Jorge", 20, 85)
    Miguel = Estudiante("Miguel", 18, 90)
    Soto = Estudiante("Soto", 18, 83)

    estudiantes = [Manuel, Juan, Jorge, Miguel, Soto]
    quimica = Curso("Química", 5) # Creamos el curso

    # Agregamos a los estudiantes
    for estudiante in estudiantes:
        quimica.agregar_estudiante(estudiante)

    # Vamos a imprimir los nombres de los estudiantes en el curso y sus notas
    for estudiante in quimica.estudiantes: # Para cada elemento de la lista
        print(estudiante.nombre, "->", estudiante.get_nota())

    # Imprimiremos datos relacionados a las calificaciones de los estudiantes
    print("El promedio de las notas de los estudiantes es:", quimica.calcular_nota_promedio())

    nota_mayor, nombre_mayor = quimica.calcular_nota_mayor()
    print(f"La nota mayor es de {nota_mayor} que corresponde a {nombre_mayor}")

main()