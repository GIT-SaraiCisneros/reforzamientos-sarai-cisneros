'''
4. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te pedirá ingresar
el nombre de un estudiante, la cuál será eliminada de lista inicial en caso que no exista en
la lista mostrar un mensaje donde indique que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
'''

estudiantes = ["Pedro", "Juan", "Fernando", "Pablo", "Alcides"]
var_1 = "Juan"

print('\n*** RESULTADO LISTA 4 ***\n')

print("La lista inicial de estudiantes es: {}". format(estudiantes))


if estudiantes[0]== var_1:
    estudiantes.remove(var_1)
    print("La lista de estudiantes sin el alumno {} es: {}".format(var_1, estudiantes))
elif estudiantes[1] == var_1:
    estudiantes.remove(var_1)
    print("La lista de estudiantes sin el alumno {} es: {}".format(var_1, estudiantes))
elif estudiantes[2] == var_1:
    estudiantes.remove(var_1)
    print("La lista de estudiantes sin el alumno {} es: {}".format(var_1, estudiantes))
elif estudiantes[3] == var_1:
    estudiantes.remove(var_1)
    print("La lista de estudiantes sin el alumno {} es: {}".format(var_1, estudiantes))
elif estudiantes[4] == var_1:
    estudiantes.remove(var_1)
    print("La lista de estudiantes sin el alumno {} es: {}".format(var_1, estudiantes))
else:
    estudiantes.append(var_1)
    print("No se encuentre en la lista y a sido agregada a la lista, siendo: {}".format(estudiantes))

