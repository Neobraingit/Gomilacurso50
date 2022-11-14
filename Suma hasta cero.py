'''Vamos a hacer que el ususario meta números e ir sumándolos. Cuando introduzca cero saldremos del bucle y mostraremos la suma
'''
numero = int(input('Introduce un número: '))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input('Introduce un número: '))

else:
    print (suma)