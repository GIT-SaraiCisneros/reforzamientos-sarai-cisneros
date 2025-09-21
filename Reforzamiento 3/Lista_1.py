'''
1. Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la lista que fueron ingresados.
'''


alumnos = [] #inicio una lista vacía
print("La lista de alumnos es: {}".format(alumnos))
print("Cantidad de alumnos es: {}".format(len(alumnos)))

"""Agregar los nombres de alumnos en lista"""
alumnos.append("Juan")
alumnos.append("Saul")
alumnos.append("Pedro")

print('\n*** RESULTADO LISTA 1 ***\n')

print("La lista de alumnos es: {}".format(alumnos))
print("Cantidad de alumnos es: {}".format(len(alumnos)))


