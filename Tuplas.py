''' Son escritas entre paréntesis y puede contener distintos tipos separados por comas'''
tupla = ('Marcos', ' Carmona', 'García')
print (tupla)

# Acceder a los elementos de una tupla
'''Volvemos a utilizar el slicing'''
print (tupla[0])

'''Método de unpacking'''
''' Consiste en extraer los valores de una tupla asignándolos a variables'''
frutas = ('Naranja', 'Limón', 'Manzana', 'Mandarina')
(fruits1, fruits2, fruits3, fruits4) = frutas # Así asignamos cada elemento de una tupla a una variable
print (fruits1)

'''Concatenación de tuplas'''
tupla1 = (1,2,3)
tupla2 = (4,5,6)
print (tupla1 + tupla2)

'''Tamaño de una tupla'''
print (len(tupla))

'''Bucles y tuplas: podemos usar las tuplas con el bucle for'''
for i in tupla:
    print (i)