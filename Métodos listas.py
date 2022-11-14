lista = ['Marcos', 'David', 'Eva', 'Marta']
print (lista.count('Marcos')) # Recibe un argumento y cuenta las veces que aparece en la lista
lista6 = [6]
print (lista.extend([lista6])) # Extiende la lista con otra lista
print (lista.index('Marcos')) # Nos muestra el índice en el que aparece el objeto
print (lista.pop()) # Borra y devuelve un objeto al final de la lista
print (lista.remove('Marcos')) # Nos borra el objeto que le pasemos
print (lista.reverse()) # Devuelve la lista en orden inverso
print (lista.sort()) # Devuelve la lista en orden

'''Eliminando un elemento indicado por el usuario'''
usuario = ['Marcos', 'David', 'Eva', 'Marta']
print ('Dime que elemento quieres eliminar: ')
elemento= input()
print (usuario.remove(elemento))

numeros = [2,3,4,5,6,6]
print (numeros.sort())
print (numeros)



