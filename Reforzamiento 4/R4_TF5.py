'''
aaa ddd vv
5.Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado.
'''


def func (lista, eliminar):
    print("\nLista original es: {}".format(lista))
    if eliminar in lista:
        lista.remove(eliminar)
        print("Lista actualizada es: {}".format(lista))
        print("El valor eliminado es: {}".format(eliminar))
    else:
        print ("No se encontró el valor {} en la lista".format(eliminar))

lista =[]
cantidad = int(input ("¿Cuántos valores desea ingresar?: "))
for n in range (1,cantidad+1):
    valor = input("Ingresa el valor: ")
    lista.append(valor)
print (lista)
valor_eliminar = input("Ingresa el valor a eliminar: ")

func(lista, valor_eliminar)

