class Libro:
    def __init__(self,titulo,autor,genero,puntuacion):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.puntuacion=puntuacion

def agregar_libro_usuario():
    # Solicita al usuario que ingrese el título, autor, género y
    # puntuación del libro. Crea un objeto Libro con estos atributos y agrega el
    # objeto a la lista lista_libros
    print("Ingresar título, autor, genero y puntuacion")
    t=str(input())
    a=str(input())
    g=str(input())
    p=float(input())
    print("Se agregó el libro",t," del autor ",a," del género ",g," y puntuacion ",p)
    nuevo_libro=Libro(t,a,g,p)
    return nuevo_libro

def buscar_libro_x_genero(lista_libros):
    #Buscar Libros por Género: Pregunta al usuario por un género y muestra
    #una lista de títulos de libros en ese género.
    print("Ingrese género del libro a buscar: ")
    g=str(input())
    i=0
    print ("Lista de libros del género",g,":\n")
    for i in lista_libros:
        if(i.genero==g):
            print(i.titulo, "\n")

def recomendar_libro(lista_libros):
    #Pregunta al usuario por su género de interés y muestra
    #el título del libro con la puntuación más alta en ese género
    print("Ingrese género del libro a buscar y devuelve el titulo con puntuación mas alta: ")
    g=str(input())
    max=0
    
    for i in lista_libros:
        if(i.genero==g):
            if i.puntuacion > max:
                max = i.puntuacion
                titulo_max= i.titulo
    print ("Libro con mejor puntuación del genero ",g,": ",titulo_max,"con puntación ", max,"\n")
   
lista_libros=[] 
#Se ingresan los 10 libros inciales, no se si hay otra forma mas rapida de hacerlo
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)
lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)
lista_libros.append(libro4)
lista_libros.append(libro5)
lista_libros.append(libro6)
lista_libros.append(libro7)
lista_libros.append(libro8)
lista_libros.append(libro9)
lista_libros.append(libro10)

i=1
while i!=0:
    print("------------------------------")
    print("Seleccione la opción deseada: \n 1: Agregar libro\n 2: Buscar libro por género\n 3: Recomendar libro por puntuación\n 0: Salir del menú")
    i=int(input())
    if i==1:
        lista_libros.append(agregar_libro_usuario())
    if i==2:
        buscar_libro_x_genero(lista_libros)
    if i==3:
        recomendar_libro(lista_libros)
    if i==0:
        print("Saliendo del menú\n")

