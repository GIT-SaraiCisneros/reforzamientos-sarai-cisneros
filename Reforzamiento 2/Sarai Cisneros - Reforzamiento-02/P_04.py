
'''
4.Hallar el volumen de una esfera, cada dato requerido para
hallar el volumen debe estar en una variable.
Mostrar el volumen por pantalla indicándoselo al usuario.
Considera a π = 3.14159

La fórmula para calcular el volumen de una esfera es:
V = (4/3) . π . r ^3 Y finalmente deberá verse lo siguiente:

Radio de la esfera: 5.5
Volumen de la esfera: 696.91
'''

var_π = 3.14159
var_radio = 5.5
volumen= (4/3) * var_π * pow(var_radio,3)
volumen_2decimal= round (volumen, 2)

print('\n*** RESULTADO EJERCICIO 04 ***\n')
print("El volumen de la esfera es: ", volumen_2decimal)


#print("El volumen de la esfera es: ", f'{volumen:.2f}')




