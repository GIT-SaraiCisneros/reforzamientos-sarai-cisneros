'''
1.Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal.
'''

alumnos = {'nombre': "Gustavo", "edad": 27, "salario": 18}
print("Diccionario de alumnos es: {}".format(alumnos))

#me muestra como lista
alumnos_lis= list(alumnos)
print("Diccionario de alumnos transformado a lista: {}".format(alumnos_lis))

#mostrando los valores de diccionario
alumnos_keys=list(alumnos.keys())
print("Values:{}".format(alumnos_keys))

#mostrando los valores de diccionario
alumnos_values=list(alumnos.values())
print("Values:{}".format(alumnos_values))