frase = input('Introduce una frase: ')
frase = frase.lower()
letra = 'aeiou'
contador = 0
for i in frase:
    if i in 'aeiou':
        contador += 1
print (contador)
