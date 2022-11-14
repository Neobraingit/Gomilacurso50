'''Tablas de multiplicar'''
for i in range(1, 11):
    print ('\nTabla de multiplicar del {}'.format(i))
    for j in range(1, 21):
        print ('{} x {} = {}'.format(i, j, i * j))