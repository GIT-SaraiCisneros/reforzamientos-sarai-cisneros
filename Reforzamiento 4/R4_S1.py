'''
1. Dada una frase u oración encontrar que palabra es la que tiene más caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa” Output: “programación” – 12 caracteres
'''

frase = input("Ingrese frase: ")

palabras = frase.split()
print (palabras)
mas_caracteres = max(palabras)
print('La palabra que tien más caracteres es "{}" - {} caracteres.'.format(mas_caracteres,len(mas_caracteres)))


