texto = input('Introduce un texto: ')
contador = 0
for i in texto:
    if ' ' in i:
        contador += 1
print (contador)
