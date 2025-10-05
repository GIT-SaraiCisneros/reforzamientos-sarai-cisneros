'''
4.Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una excepción para el siguiente
bloque de código y tu programa no se bloquee. Además, imprime un mensaje al usuario la causa y/o solución
(Pedir nombre, día, mes, año por consola):

Nombre: No debe recibir un dato numérico, sino decírselo al usuario
Día, mes y año:No debe recibir un dato string, sino decírselo al usuario

cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025

Independientemente del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error
'''
from weakref import finalize


def saluda_fecha():
    try:
        nombre = str(input("Ingrese nombre: "))
        try:
            if int(nombre):
                raise TypeError
        except ValueError:
            print(nombre)
        dia = int(input("Ingrese dia: "))
        mes = int(input("Ingrese mes: "))
        anio = int(input("Ingrese anio: "))
    except TypeError:
        print ("El 'Nombre' no debe ser numéricoxxx")
    except ValueError:
        print("No debe recibir un dato string")
    else:
        print ("Hello {}, hoy estamos {} de {} del {}".format(nombre, dia, mes, anio))
    finally:
        print("Operación finalizada\n")

saluda_fecha ()