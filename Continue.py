# Es muy similar al break pero lo que hace es interrumpir la iteración actual y sigue con la siguiente

for i in range(1,10,2):
    print (i)
    continue
for h in range(1, 100, 2):
    print (h)

''' Con un bucle for vamos a recorrer un string e imprimiremos todas las letras menos la insdicada por el usuario'''
s = 'Mi mamá me mima mucho'
letra = input('Introduce la letra que quieras eliminar: ')
letra = letra.lower()
s = s.lower()
for c in s:
    if c == letra:
        continue
    else:
        print (c)