'''
3.
Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de todos estos dígitos.
'''

def sumatoria_dig (num):
    sumando = 0
    for digit in str(num):
       sumando = sumando + int(digit)
    print(sumando)
    return sumando

# Mostrando
resultado = input("Ingresa un número: ")
#sumatoria_dig (resultado)

try:
    int(resultado)
    print ("La sumatoria de los digitos de {} es: {}".format(resultado, sumatoria_dig (resultado)))
except:
    print ("Se debe ingresar un número entero")