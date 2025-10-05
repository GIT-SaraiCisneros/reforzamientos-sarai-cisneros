'''
1. Crear una función llamada division_segura(a, b) que recibirá dos números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally
- Valida que los datos ingresados sean numéricos de lo contrario mostrar “Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error
'''

def division_segura(a, b):
    try:
        resultado = a / b
        print("Resultado de dividir {}/{} es: {}". format(a,b,resultado))
    except ZeroDivisionError:
        print("Error: {}/{} no puedes dividir entre cero".format(a,b))
    except TypeError:
        print("Error: Entrada no numérica al querer dividir {}/{}".format(a,b))
    finally:
        print("Operación finalizada\n")

division_segura(20, 2)
division_segura(30, 0)
division_segura(2, 10)
division_segura(2, "ocho")


