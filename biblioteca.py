""" 
Simula un sistema de gestión de biblioteca
Definiremos las clases Libro, Biblioteca y Usuario 
Nota: El método __str__ se llama cuando se invocan las funciones print() y str() en el objeto. Retorna una cadena
"""

# Clase Libro: título: str, autor: str y disponible: bool
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True # ¿El libro está disponible?

    # Método que retorna la información del libro en una cadena
    def __str__(self):
        return f"Libro: {self.titulo} de {self.autor}"

# Clase Usuario: nombre y libros
# "libros" es una lista que contiene todos los libros prestados al usuario. Estos se añaden por la clase Biblioteca
class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []

    def __str__(self):
        return f"Usuario: {self.nombre}"

    # Método para mostrar la información de los libros en posesión, en forma de una lista de diccionarios  
    def get_libros(self):
        libros = [] 
        
        for libro in self.libros:
            info = {}
            info["Titulo"] = libro.titulo
            info["Autor"] = libro.autor
            libros.append(info)
        
        return libros

# La clase Biblioteca tendrá de atributo una lista que contendrá los libros 
class Biblioteca:
    def __init__(self):
        self.libros = [] # Lista de los objetos Libro como tal
    
    # Método para agregar un objeto Libro a la lista "libros"
    def agregar_libro(self, libro: Libro):
        # Si es de la clase libro, lo añadimos, si no, mostramos un error
        if isinstance(libro, Libro):
            self.libros.append(libro) 
        else:
            print(f"Error: el objeto {libro} debe ser una instancia de la clase Libro")
    
    # Retorna una lista de diccionarios de libros que coincidan con el título dado
    def buscar_libro_por_titulo(self, titulo: str):
        libros_encontrados = [] 

        # Usamos la búsqueda lineal
        for libro in self.libros:
            if libro.titulo == titulo:
                info = {}
                info["Titulo"] = libro.titulo
                info["Autor"] = libro.autor
                libros_encontrados.append(info)
        
        return libros_encontrados

    # Retorna una lista de libros que coincidan con el autor dado
    def buscar_libro_por_autor(self, autor: str):
        libros_encontrados = [] 

        # Usamos la búsqueda lineal
        for libro in self.libros:
            if libro.autor == autor:
                info = {}
                info["Titulo"] = libro.titulo
                info["Autor"] = libro.autor
                libros_encontrados.append(info)
        
        return libros_encontrados
    
    # Método para buscar el libro por su título, prestarlo al usuario añadiéndolo a su lista y actualizar el estado del libro
    def prestar_libro(self, titulo: str, usuario: Usuario):
        # Validar que el título que se recibe esté en los libros 
        titulos = [libro.titulo for libro in self.libros]
        if titulo not in titulos: 
            print(f"El título {titulo} no se encuentra en los libros actuales")
            return False

        for libro in self.libros:
            if libro.titulo == titulo:
                # Si está disponible, lo prestamos. Si no, retornamos False
                if libro.disponible == True:
                    usuario.libros.append(libro)
                    libro.disponible = False
                    return True
                else: 
                    print(f"El libro {titulo} no se encuentra disponible actualmente")
                    return False
                    
    # Método que busca el libro por su título, quitarlo de la lista de libros del usuario, y actualizar el estado del libro
    def devolver_libro(self, titulo: str, usuario: Usuario):
        for libro in self.libros:
            if libro.titulo == titulo:
                # Removemos el libro de la lista de libros del usuario
                usuario.libros.remove(libro)
                libro.disponible = True
                break
    
    # Retorna una lista que contiene diccionarios de los libros
    def get_info_libros(self):
        libros = [] 
        
        for libro in self.libros:
            info = {}
            info["Titulo"] = libro.titulo
            info["Autor"] = libro.autor
            libros.append(info)
        
        return f"Los libros en la biblioteca son: {libros}"

# Test
# Crearemos objetos Libro, los añadiremos a una biblioteca, creamos usuarios y les prestamos los libros
def main():
    biblioteca1 = Biblioteca()
    # Creamos los libros
    lib1 = Libro("El Extranjero", "Albert Camus")
    lib2 = Libro("It", "Stephen King")
    lib3 = Libro("El Extranjero", "Sartre")
    lib4 = Libro("Salem's Lot", "Stephen King")

    # Creamos los usuarios
    user1 = Usuario("Juan")
    user2 = Usuario("Manuel")

    biblioteca1.agregar_libro(lib1)
    biblioteca1.agregar_libro(lib2)
    biblioteca1.agregar_libro(lib3)
    biblioteca1.agregar_libro(lib4)
    
    print(biblioteca1.get_info_libros())
    print(biblioteca1.buscar_libro_por_titulo("El Extranjero"))
    print(biblioteca1.buscar_libro_por_autor("Stephen King"))

    # Prestar y devolver libros
    print(biblioteca1.prestar_libro("It", user1))
    print(biblioteca1.prestar_libro("It", user2))
    biblioteca1.prestar_libro("El Extranjero", user1)
    print(user1.get_libros())
    biblioteca1.devolver_libro("It", user1)
    print(user1.get_libros())

main()