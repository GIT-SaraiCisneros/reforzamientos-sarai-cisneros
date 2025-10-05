'''
1. Pedir dos números positivos mediante terminal al usuario. Mostrar como salida el número
cuya sumatoria de dígitos es el mayor y los números cuya sumatoria de dígitos es menor que 10.
Utilizar una o más funciones, según sea conveniente.
'''

# función
def suma_dig(numero):
    sum=0
    for digit in str(numero):
        sum=sum+int(digit)
    print(sum)
    return sum

num1 = int(input("Ingrese 1er número positivo: "))
num2 = int(input("Ingrese 2do número positivo: "))

sum1 = suma_dig(num1)
sum2 = suma_dig(num2)

if sum1 > sum2:
    print("El N° {} tiene mayor suma de dígitos ({}).".format(num1, sum1))
elif sum2 > sum1:
    print("El N° {} tiene mayor suma de dígitos ({}).".format(num2, sum2))
else:
    print("Ambos números tienen la misma suma de dígitos ({}).".format(sum1))

# Mostrar los números cuya suma de dígitos es menor que 10

if sum1 < 10:
    print("El N° {} tiene suma de dígitos {} < 10".format(num1, sum1))
if sum2 < 10:
    print("El N° {} tiene suma de dígitos {} < 10".format(num2, sum2))
if sum1 >= 10 and sum2 >= 10:
    print("Ningún número tiene suma menor que 10.")
