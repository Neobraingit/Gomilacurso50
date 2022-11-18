# Programación orientada a objetos
'''Una clase es una plantilla para crear objetos. Las clases contienen la definición de los objetos con los que
trabajamos y definen sus propiedades'''

# Mi primera clase en Python
class Book():
    '''Creamos la clase Book para crear libros como objetos'''
    is_electronic = False

libro1 = Book()
print (type(libro1))
print (Book.is_electronic) # Accedemos a través de la clase por qué es una variable estática
print (Book.__doc__) # Accedemos al docstring de la clase

# El método constructor
class Book():
    '''Repetimos la clase implementando el método init(constructor)'''
    def __init__(self, título, autor, electronic = False):
        self.título =  título
        self.autor = autor
        self.electronic = electronic
    def __del__(self):
        ''' El método destructor (se usa para eliminar instancias de un objeto)'''

libro2 = Book('El señor de los anillos', 'J.R.R Tolkien', False)
print (libro2.autor)
print (libro2.electronic)
print (libro2.título)
print (libro2.__dict__) # Con esto accedemos a todos los atributos del objeto en formato diccionario
#
# del libro2 # Esto, en compañía del método destructor borra una instancia
print (libro2.autor)

# Métodos de una clase
'''Existen tres tipos de mètodos:
   1) Métodos de instancia
   2) Métodos estáticos
   3) Métodos de clase'''

'''Métodos de instancia'''
class Rectángulo ():
    def __init__(self, base = 1, height = 1, color ='blue' ):
        self.base = base
        self.height = height
        self.color = color

    def perimetro(self):
        '''Esto es un método de instancia'''
        return 2 * self.base + 2 * self.height

    def area(self):
        ''' Esto es un método de instancia'''
        return self.base * self.height

    def __str__(self):
        '''Este método se utiliza cuando se va a imprimir un objeto'''


rec1 = Rectángulo(5, 2, 'Rojo')
print (rec1.perimetro())
print (rec1.area())
rec2 = Rectángulo(1,2,'verde')
print (rec2.perimetro())

# Métodos estáticos
'''A diferencia de los métodos de instancia, no pasan como argumento self y se definen 
con el decorador @staticmethod'''


class Rectángulo():
    def __init__(self, base=1, height=1, color='blue'):
        self.base = base
        self.height = height
        self.color = color

    def perimetro(self):
        '''Esto es un método de instancia'''
        return 2 * self.base + 2 * self.height

    def area(self):
        ''' Esto es un método de instancia'''
        return self.base * self.height

    def __str__(self):
        '''Este método se utiliza cuando se va a imprimir un objeto'''

    @staticmethod
    '''Aquí iria el método que creemos '''

# Métodos de clase
'''Necesitamos pasar toda la clase entera como argumento con cls y lleva el decorador @classmethod'''

# Propiedades
'''Permite a un método ser acessible sin parámetros y se llama con @property'''









