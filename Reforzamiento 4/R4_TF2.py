'''
2. Crea una función que al ingresar dos números por parámetro mostrará todos los cuadrados
de los números que hay entre ellos (Usar la función una vez y mostrar el resultado por consola).
Los números serán ingresados y solicitados al usuario.
'''

def cuadrado(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    for num in range(num_1 + 1, num_2):
        print("{}^2 = {}".format(num, num**2))
# Pedir los dos números al usuario
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
cuadrado(numero_1, numero_2)