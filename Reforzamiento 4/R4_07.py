'''
7. Realizar un programa donde se ingresarán por consola los nombres de los alumnos
(indicar previamente la cantidad de alumnos a ingresar) de un curso y las notas de c/u.
Guardarás la información en un diccionario donde las claves serán los nombres de c/u de
estos alumnos y sus valores serán las notas de esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
'''


n = int(input("Cantidad de alumnos: "))

alumnos = {}
for i in range(n):
    nombre = input("Nombre del alumno {}: ".format(i+1))
    nota = float(input("Nota del alumno {}: ".format(i+1)))
    alumnos[nombre] = nota

# Alumnos con sus notas
for nombre, nota in alumnos.items():
    print("{} tiene la nota de {}".format(nombre, nota))

# Promedio de notas
media = sum(alumnos.values()) / len(alumnos)
print("El promedio de todas las notas es: {:.2f}".format(media))