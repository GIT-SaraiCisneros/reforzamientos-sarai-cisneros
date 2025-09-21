'''
3. Escribe un programa que reciba dos flotantes, luego estos pasarán a ser convertidos en enteros.
Indique si el primero es múltiplo del segundo. Usar mod para la verificación si el residuo es 0
'''
from selectors import SelectSelector

var_1 = 12.6
var_2 = 6.3

var_1_entero = int(var_1)
var_2_entero = int(var_2)

print('\n*** RESULTADO EJERCICIO 3 ***\n')

if var_1_entero % var_2_entero == 0:
    print("El primer valor ({}) es múltiplo del segundo valor ({})".format(var_1_entero, var_2_entero))
else:
    print("El primer valor ({}) NO es múltiplo del segundo valor ({})".format(var_1_entero, var_2_entero))