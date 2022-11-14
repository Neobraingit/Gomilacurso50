lista = ['Marcos', 'David', 'Eva', 'Marta']
lista.append('mamá')
print (lista)

'''Vamos a pedir al usuario la longitud de una lista y haremos que introduzca tantos números enteros como haya indicado
que se guarda´´an en u na lista. Al acabar imprimiremos la lista'''

longitud = int(input('Introduce la longitud de una lista: '))
lista = []
for i in range (longitud):
    lista.append(int(input()))

print (lista)