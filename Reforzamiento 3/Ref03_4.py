'''
4. Crea un programa que tome un número decimal (con 6 número en la parte decimal) e imprima ese número con:
1 decimal, 2 decimales y 4 decimales
'''

var_decimal = 2.486514

print('\n*** RESULTADO EJERCICIO 4 ***\n')

print("El valor de {} a 1 decimal es: {}".format( var_decimal, f'{var_decimal:.1f}'))
print("El valor de {} a 2 decimal es: {}".format( var_decimal, f'{var_decimal:.2f}'))
print("El valor de {} a 4 decimal es: {}".format( var_decimal, f'{var_decimal:.4f}'))