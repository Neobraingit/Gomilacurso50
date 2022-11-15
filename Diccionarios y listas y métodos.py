dic = {
    'Lista' : [1,2,3,4,5],
    'Diccionario' : {'Nombre' : 'Marcos'}
}

'''Más métodos de diccionarios'''

diccionario = {'a': 4, 'b': 1, 'c': 2}
print (diccionario.clear()) # Nos deja el diccionario vacío
diccionario = {'a': 4, 'b': 1, 'c': 2}
print (diccionario.copy()) # Nos hace una copia de un diccionario
print (diccionario.fromkeys('d')) # Nos genera un diccionario donde las claves son elementos iterables
print (diccionario.get('a')) # Recibe como valor una clave y nos devuelve el valor de dicha gracia
print (diccionario.pop('a'))# Recibe como parámetro una clave, la devuelve y la elimina
print (diccionario.setdefault('h')) # Agrega un nuevo elemento al diccionario

'''Construyendo diccionarios con dict()'''



