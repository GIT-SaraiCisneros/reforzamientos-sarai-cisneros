'''
5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a una variable c/u
'''

datos={"nombre": "Sara", "apellido": "Cisneros", "Edad":31}

datos["carrera"]="Estadística"
print ("El diccionario agregando carrera es:{}".format(datos))

#datos_valores=datos.values()
#print ("Los valores son:{}".format(datos_valores))

carreras=datos["carrera"]
nombres=datos["nombre"]
print ("Los valores de tu carrera y nombre son: {}, {}".format(carreras, nombres))






