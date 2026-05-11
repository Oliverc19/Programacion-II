#pagina composicion con libro
class Pagina:

    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Pagina {self.numero}: {self.contenido}")
#horario composicion con biblioteca
class Horario:

    def __init__(self, dias, apertura, cierre):
        self.dias = dias
        self.apertura = apertura
        self.cierre = cierre

    def mostrarHorario(self):

        print("\nHORARIO")
        print("Dias:", self.dias)
        print("Hora apertura:", self.apertura)
        print("Hora cierre:", self.cierre)

class Libro:

    def __init__(self, titulo, isbn, contenidos):

        self.titulo = titulo
        self.isbn = isbn

        # COMPOSICION
        self.paginas = []

        numero = 1

        for contenido in contenidos:

            pagina = Pagina(numero, contenido)

            self.paginas.append(pagina)

            numero += 1

    def leer(self):

        print(f"\nLEYENDO LIBRO: {self.titulo}")

        for pagina in self.paginas:
            pagina.mostrarPagina()

class Autor:

    def __init__(self, nombre, nacionalidad):

        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):

        print("\nAUTOR")
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)

class Estudiante:

    def __init__(self, codigo, nombre):

        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):

        print("\nESTUDIANTE")
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
#prestamo asociacion entre estudiante y libro
class Prestamo:

    def __init__(self, estudiante, libro):

        self.fechaPrestamo = "10/05/2026"
        self.fechaDevolucion = "17/05/2026"

        # ASOCIACION
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):

        print("\nPRESTAMO")
        print("Estudiante:", self.estudiante.nombre)
        print("Libro:", self.libro.titulo)
        print("Fecha prestamo:", self.fechaPrestamo)
        print("Fecha devolucion:", self.fechaDevolucion)

class Biblioteca:

    def __init__(self, nombre):

        self.nombre = nombre

        # AGREGACION
        self.libros = []
        self.autores = []

        # ASOCIACION
        self.prestamos = []

        # COMPOSICION
        self.horario = Horario(
            "Lunes a Viernes",
            "08:00",
            "20:00"
        )

    def agregarLibro(self, libro):

        self.libros.append(libro)

        print(f"\nLibro agregado: {libro.titulo}")

    def agregarAutor(self, autor):

        self.autores.append(autor)

        print(f"\nAutor agregado: {autor.nombre}")

    def prestarLibro(self, estudiante, libro):

        prestamo = Prestamo(estudiante, libro)

        self.prestamos.append(prestamo)

        print("\nPrestamo realizado correctamente")

    def mostrarEstado(self):

        print("\n==========================")
        print("BIBLIOTECA:", self.nombre)
        print("==========================")

        print("\nLIBROS")

        for libro in self.libros:
            print("-", libro.titulo)

        print("\nAUTORES")

        for autor in self.autores:
            print("-", autor.nombre)

        print("\nPRESTAMOS")

        for prestamo in self.prestamos:
            prestamo.mostrarInfo()

        self.horario.mostrarHorario()

    def cerrarBiblioteca(self):

        print("\nLa biblioteca esta cerrando...")

        self.prestamos.clear()

        print("Los prestamos fueron eliminados")
#MAIN ----------------------------------  
# AUTORES
autor1 = Autor(
    "Gabriel Garcia Marquez",
    "Colombiano"
)

autor2 = Autor(
    "Mario Vargas Llosa",
    "Peruano"
)

# LIBROS
libro1 = Libro(
    "Cien años de soledad",
    "ISBN-111",
    [
        "Muchos años despues...",
        "La familia Buendia...",
        "Fin del libro..."
    ]
)

libro2 = Libro(
    "La ciudad y los perros",
    "ISBN-222",
    [
        "Inicio de historia...",
        "Desarrollo...",
        "Final..."
    ]
)

# ESTUDIANTE
estudiante1 = Estudiante(
    "2024001",
    "Juan Perez"
)

# BIBLIOTECA
biblioteca = Biblioteca(
    "Biblioteca Central UMSA"
)
#demo agregacion
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)

biblioteca.agregarAutor(autor1)
biblioteca.agregarAutor(autor2)
#demo asociacion
biblioteca.prestarLibro(
    estudiante1,
    libro1
)
#estado
biblioteca.mostrarEstado()
#demo cpmposicion
libro1.leer()
#cerrar
biblioteca.cerrarBiblioteca()

biblioteca.mostrarEstado()