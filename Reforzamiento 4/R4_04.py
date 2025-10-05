'''
4. Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del diccionario.
'''

departamentos = {'dep_1': "Lima", 'dep_2': "Ica", 'dep_3': "Cusco", 'dep_4': "Arequipa", 'dep_5': "Ayacucho", 'dep_6': "Pasco"}
print("Diccionario de Departamentos es: {}".format(departamentos))

del departamentos['dep_5']
print("Diccionario de Departamentos, borrando el dep_5: {}".format(departamentos))

departamentos ['dep_4']="Loreto"
print("Diccionario de Departamentos con el penúltimo modificado: {}".format(departamentos))


if "Ayacucho" in departamentos.values():
    print ("Existe el departamento eliminado")
else:
    print ("No Existe el departamento eliminado")
