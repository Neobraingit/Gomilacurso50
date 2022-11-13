edad = 20
nombre = 'Marcos'
if edad >= 18:
    if nombre.startswith('M') or nombre.startswith('m'):
        print ('Eres demasiado joven para leer esto')
    else:
        print (f'Eres mayor de edad por que tienes {edad} años')

else:
        print ('Eres muy joven')