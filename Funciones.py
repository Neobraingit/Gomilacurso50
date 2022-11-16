'''Una función es una pieza de código reutilizable que solo se ejecuta cuando es llamada'''
def mi_función():
    num = 2
    num2 = 2
    print (num + num2)


mi_función()

def conparametros(nombre):
    print (f'Buenos días {nombre}')

conparametros('MARCOS')

def contadordeletras():
    string = input('Introduce un string: ')
    contador = 0
    vocales = 'aeiou'
    for i in string:
        if i in vocalesa:
            contador += 1
    print (contador)

contadordeletras()