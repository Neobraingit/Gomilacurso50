
cadena = 'Me encanta el chocolate...'
print (cadena.lower()) # Lo trasforma en minusculas
print (cadena.upper()) # Lo transforma en mayúsculas
print (cadena.count('o')) # Cuenta las veces que aparece una letra
print (cadena.capitalize()) # Convierte en mayúsculas en primer caracter
print (cadena.title()) # Convierte cada primera letra de cada palabra en mayúculas
print (cadena.swapcase()) # Intercambia mayúsculas en minúsculas y al revés
print (cadena.replace('Me', 'Le')) # Reemplaza el caracter que queramos por otro que indicquemos
print (cadena.split('e')) # Rompe por el caracter o palabra que indiquemos
print (cadena. rstrip()) # Elimina los espacios sobrantes a la derecha del string
print (cadena.strip()) # Elimina los espacios al principio y al final
print (cadena.find('chocolate')) # Nos muestra el índice en el que está. Con start y end indicamos donde empieza y finaliza la búsqueda
print (cadena.index('e')) # Nos muestra la primera aparición donde se encuentra y también cuenta con start y end
print (len(cadena)) # Nos dice el tamaño del string
print (cadena.rindex('e')) # Nos busca el caracter indicado en la última posición y también tiene start y end
print (type(cadena)) # Nos muestra el tipo de dato que es

# Input es una función para que el usuario introduzca datos
cadena = input('Introduce tu nombre: ')
print (cadena)
nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))
altura = float(input('Introduce tu altura: '))
print (f'Te llamas {nombre} y tu edad es {edad} y tu altura es {altura}')

'''Ejercicio: conseguir un texto sin la palabra introducida por el usuario'''
string = 'El camino está cerrado pero seguro que podemos encontrar una alternativa'
print ('Este el string original:', end= ' ')
print (string)
print ('Introduce la palabra que quieras eliminar: ')
word = input('Palabra: ')
indice = string.find(word)
substring = string[:indice] + string[indice +len(word) + 1:]
print (substring)


