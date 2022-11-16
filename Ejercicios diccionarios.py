string = input('Introduce una frase: ')
string = string.lower()
counter = []
letters = {}
for i in string:
    if i not in counter and i != ' ':
        letters[i] = string.count(i)

print (letters)
