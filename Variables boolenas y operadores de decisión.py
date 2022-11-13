'''¿Qué es un operador de decisión?'''
'''Si algo cumple una condición, se sigue ejecutando el software (True); si no, no (False'''
es_adulto = True
print (type(es_adulto))

# Operadores de decisión
''' Los operadores de decisión son:
    > mayor que
    < menor que
    != distinto que
    == igual que
    '''

if 17 > 2:
    print (True)
else:
    False

# Múltiples comparaciones simultáneas
edad = 17
if (edad < 18) and (edad > 18):
    print (True)
else:
    print (False)