from datetime import datetime

""" 
Gestor de tareas que permite crear, completar y eliminar tareas
Clases: Tarea y GestorTareas
"""

class Tarea:
    """
    Esta clase es para representar la idea de una tarea que debe ser completada
    Proporciona métodos para crearla y completarla
    """

    def __init__(self, descripcion: str):
        # descripcion: título o descripción de la tarea
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now() # La fecha actual
        self.completada = False

    # Actualiza el booleano "completada" a True
    def completar(self):
        self.completada = True
    
    # Devuelve una cadena que representa la tarea, con su descripción, estado y fecha de creación.
    def __str__(self):
        return f"{self.descripcion} se creó a {self.fecha_creacion}, completada: {self.completada}"

class GestorTareas:
    """ 
    Esta clase permite al usuario agregar nuevas tareas, marcarlas como completadas, eliminar tareas, 
    y ver todas las tareas en existencia
    """

    def __init__(self):
        # tareas: lista que almacenará las instancias de la clase "Tarea"
        self.tareas = []

    # Recibe una instancia de la clase Tarea y la agrega a la lista de tareas
    def agregar_tarea(self, tarea):
        # si "tarea" es una instancia de la clase Tarea, la añadimos a la lista
        if isinstance(tarea, Tarea):
            self.tareas.append(tarea)
            return True
        else:
            return False
    
    # Marca como completada la tarea en la posición "num_tarea"
    def completar_tarea(self, num_tarea):
        # num_tarea es el índice de la tarea + 1
        # debe estar en el rango de [1, tamaño de la lista]
        if num_tarea >= 1 and num_tarea <= len(self.tareas):
            self.tareas[num_tarea - 1].completar()
            return True
        else:
            return False
        
    # Elimina la tarea en la posición "num_tarea"
    def eliminar_tarea(self, num_tarea):
        # num_tarea es el índice de la tarea + 1
        # debe estar en el rango de [1, tamaño de la lista]
        if num_tarea >= 1 and num_tarea <= len(self.tareas):
            del self.tareas[num_tarea - 1]
            return True
        else:
            return False

    # Muestra por pantalla todas las tareas: su descripción, estado y fecha de creación
    def mostrar_tareas(self):
        for index, tarea in enumerate(self.tareas):
            print(f"Tarea {index + 1}: ", end="")
            print(tarea)

def main():
    # Creamos una instancia de GestorTareas 
    gestor = GestorTareas()

    def comprobar():
        if not gestor.tareas: # Si la lista está vacía
            print("Ninguna tarea creada aún")
            return True

    while True:
        # Mostramos las opciones disponibles
        print("\nOpciones disponibles:")
        print("1. Crear una tarea", "2. Completar una tarea", "3. Eliminar una tarea", "4. Mostrar lista de tareas", "5. Salir", sep="\n")
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                # Crear una tarea
                descripcion = input("Introduzca la descripción de la tarea: ")
                while not descripcion: # Mientras que sea una cadena vacía
                    descripcion = input("No escribiste nada, cabrón. Introduzca la descripción de la tarea: ")

                gestor.agregar_tarea(Tarea(descripcion))
                print("Tarea creada exitosamente")
            case "2": # Completar una tarea
                # Si no hay ninguna tarea, saltamos a la siguiente iteración del bucle
                if comprobar(): continue
                
                print("Introduzca el número de tarea a completar (a partir de 1). O presione -1 para completar todas las tareas: ", end="")
                num_tarea = input()

                if num_tarea == "-1":
                    for tarea in gestor.tareas: tarea.completar()
                    print("Todas las tareas completadas exitosamente")
                    continue

                # Mientras que no sea un número, seguiremos pidiendo la entrada. Luego, la convertimos a entero
                while not num_tarea.isdigit():
                    num_tarea = input("Eso no es un entero. Introduzca el número de tarea a completar (a partir de 1): ")
                num_tarea = int(num_tarea)

                # Validamos que esté en el rango
                while num_tarea < 1 or num_tarea > len(gestor.tareas):
                    num_tarea = int(input("Valor fuera de rango. Introduzca el número de tarea a completar (a partir de 1): "))
                
                gestor.completar_tarea(num_tarea)
                print(f"Tarea {num_tarea} completada exitosamente")
            case "3": # Eliminar una tarea
                if comprobar(): continue

                print("Introduzca el número de tarea a eliminar (a partir de 1). O presione -1 para eliminar todas las tareas: ", end="")
                num_tarea = input()

                if num_tarea == "-1":
                    gestor.tareas.clear()
                    print("Todas las tareas eliminadas exitosamente")
                    continue
                
                while not num_tarea.isdigit():
                    num_tarea = input("Eso no es un entero. Introduzca el número de tarea a eliminar (a partir de 1): ")
                num_tarea = int(num_tarea)

                # Validamos que esté en el rango
                while num_tarea < 1 or num_tarea > len(gestor.tareas):
                    num_tarea = int(input("Valor fuera de rango. Introduzca el número de tarea a eliminar (a partir de 1): "))

                gestor.eliminar_tarea(num_tarea)
                print(f"Tarea {num_tarea} eliminada exitosamente")
            case "4": # Mostrar lista de tareas
                if comprobar(): continue
                gestor.mostrar_tareas()
            case "5": 
                break # Salimos
            case _: # Cualquier otra entrada
                print("Opción inválida")

main()

# TODO: escribir las salidas en un archivo de texto
# HACER UNA APLICACIÓN WEB ASÍ