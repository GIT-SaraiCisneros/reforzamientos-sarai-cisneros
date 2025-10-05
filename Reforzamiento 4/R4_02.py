'''
2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu diccionario,
incluyendo su valor. Mostrar finalmente el diccionario actualizado.
'''

alumnos = {'nombre': "Gustavo", "edad": 27, "salario": 18}
print("Diccionario de alumnos es: {}".format(alumnos))

alumnos['dni'] = "44673980"
print("Diccionario de alumnos agregando dni: {}".format(alumnos))


print("Salario: {}, DNI: {}".format(alumnos['salario'], alumnos['dni']))


