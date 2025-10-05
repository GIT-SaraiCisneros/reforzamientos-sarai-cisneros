'''
3.
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes.
'''


alumnos = {'nombre': "Gustavo", "edad": 27, "salario": 18.0}
print("Diccionario de alumnos es: {}".format(alumnos))

#me muestra como lista
alumnos_lis= list(alumnos.values())
print("Diccionario de alumnos transformado a lista: {}".format(alumnos_lis))

for dato in alumnos_lis:
    print("{} = {}".format(dato , type(dato)))

