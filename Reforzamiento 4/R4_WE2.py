'''
2. Crear una función y dentro la respectiva excepción o excepciones para el
siguiente bloque de código para que tu programa no se bloquee, ya que solo aceptará
datos tipos entero y además imprimir un mensaje al usuario la causa y/o solución.
También debe indicar el índice donde ingresarás este nuevo dato, si el índice está fuera
de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error
'''

lista = [2, 6, 10, 4, 5, 23, 1]

def funccc(lista, indice, valor_nuevo):
    print ("la lista original es: ", lista)
    try:
        #indice = int(input("Ingresa la posicion a ingresar el valor: "))
        indice=int(indice)
        valor_nuevo=int(valor_nuevo)
        if indice < 0 or indice > len(lista) -1:
            raise IndexError
        else:
            #valor_nuevo = int(input("Ingresa nuevo valor: "))
            lista.insert(indice, valor_nuevo)
        print("La lista actualizada es: ", lista)
    except IndexError:
        print("No es posible ingresar dato en la posición {} de la lista porque está fuera del rango entre 0 y {}".format(indice, len (lista)-1))
    except ValueError:
        print("Error: los datos deben ser tipo entero")
    else:
        print("El valor se agregó")
    finally:
        print("Operación finalizada\n")


funccc(lista,2, 20)
funccc(lista,10, 30)
funccc(lista,5, "cuarenta")
