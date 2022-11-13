'''Vamos a pedirle al usuario palabras y se los devolveremos modificados con alguno de los métodos aprendidos
      1) Devolver la palabra en mayúscula
      2) Devolver la palabra con la primera letra en mayúsculas
      3) Devolver la palabra con todas las letras menos la tercera en mayúsculas
      4) Devolver la palabra con todas las letras en mayúsculas menos la primera y la última
      '''

palabra = input('Introduce una palabra: ')
print (palabra.upper())
print (palabra.title())
palabra = palabra[:2].lower() + palabra[:2].upper() + palabra[3:].lower()
print (palabra)
palabra = palabra[0].lower() + palabra[1:(len(palabra) -1)].upper() + palabra[-1].lower()
print (palabra)

