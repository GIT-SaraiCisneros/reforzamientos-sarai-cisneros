'''
2. Crear un programa que cuente cuántas veces aparece cada vocal en la oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
'''

oracion = input("Ingrese oración: ")
oracion = oracion.lower().replace("ó","o")   # minuscula
vocales = "aeiou"

for cada_vocal in vocales:
    print("la vocal {} aparece {} veces".format(cada_vocal,oracion.count(cada_vocal)))
