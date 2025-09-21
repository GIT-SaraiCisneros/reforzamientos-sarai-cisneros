'''2. Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo departamento
que ingreses sustituirá al primero de la lista.
'''

#2da forma para agregar valores a una lista (más reducido)
departamentos = ["Cusco", "Ica", "La Libertad", "Piura", "Lambayeque", "Tumbes"]

print('\n*** RESULTADO LISTA 2 ***\n')

print("Mi lista de departamentos es: {}".format(departamentos))

#Agregando 1 departamento al final
departamentos.append("Amazonas")
print("Mi lista insertando al final un departamento:{}".format(departamentos))

#eliminando en una posición
departamentos.pop(0) #0 es el primer valor de la lista
print("Mi lista con el 2do departamento eliminado es: {}".format(departamentos))

#insertando en una posición
departamentos.insert(0,'San Martín')
print("Mi lista insertando en la 2da posición otro departamento:{}".format(departamentos))





