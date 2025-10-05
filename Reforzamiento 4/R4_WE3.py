'''
3.Crear una función funciona_indice(persona, indice) y dentro la respectiva excepción para
el siguiente bloque de código para que tu programa no se bloquee y además imprime un mensaje
al usuario: “El índice “nombre_indice” ingresado no existe en el diccionario”, tipo de datos,
etc que más pueden incurrir para este caso (los datos se pedirán por consola):
persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'} persona['profesion']
#El índice en este caso no existe
Usar la función al menos 2 veces incluyendo un caso de error
'''


persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}

def funciona_indice(persona, keyy):
    try:
        print("El dato de {} es {}".format(keyy, persona[keyy]))
    except KeyError:
        print ("El índice {} ingresado no existe en el diccionario".format(keyy))

funciona_indice(persona, 'dni')
funciona_indice(persona, 'profesion')



