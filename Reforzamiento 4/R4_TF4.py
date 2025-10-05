'''
4.Pedir al usuario que ingrese un nombre y apellidos el cual será usada por
un parámetro para una función que se creará e indicará cuantas letras tiene
el nombre solamente. Usar la función un mínimo de dos veces para dos personas e
indicar quien tiene el nombre con mayor número de caracteres (condicional)
'''


def contar_letras_nom (nombre_apellido):
    nombre = nombre_apellido.split()[0]
    contando = len(nombre)
    print ("El nombre {} tiene {} letras". format(nombre, contando))
    return nombre, contando

nombre_apellido = input("Ingresar nombre y apellido: ")
nom_1, cont_1 = contar_letras_nom (nombre_apellido)

nombre_apellido = input("Ingresar nombre y apellido: ")
nom_2, cont_2 = contar_letras_nom (nombre_apellido)

if cont_1>cont_2:
    print ( "{} tiene mas letras que {}".format(nom_1, nom_2))
elif cont_2>cont_1:
    print("{} tiene mas letras que {}".format(nom_2, nom_1))
else:
    print("{} tiene la misma cantidad de letras que {}".format(nom_1, nom_2))


