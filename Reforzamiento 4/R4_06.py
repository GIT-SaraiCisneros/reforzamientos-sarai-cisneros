'''
6. Ingresar por consola 4 números mediante consola, crear un diccionario donde los ‘key’
serán los números indicados y los valores serán los cubos de las estos keys. Mostrar finalmente este diccionario.
'''

num_1 = int(input("Ingresar 1er numero: "))
num_2 = int(input("Ingresar 2do numero: "))
num_3 = int(input("Ingresar 3er numero: "))
num_4 = int(input("Ingresar 4to numero: "))

numeros={}
numeros[num_1]=num_1**3
numeros[num_2]=num_2**3
numeros[num_3]=num_3**3
numeros[num_4]=num_4**3
print (numeros)



