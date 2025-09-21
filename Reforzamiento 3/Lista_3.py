'''
3. Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en la terminal
'''


var_1 = []
var_1.extend([1, 2, 5, 3, 4, 8, 7, 1, 10, 20])

print('\n*** RESULTADO LISTA 3 ***\n')

suma= var_1[0] + var_1[1] + var_1[2] + var_1[3] + var_1[4] + var_1[5] + var_1[6] + var_1[7] + var_1[8] + var_1[9]
print ("La suma de la lista {}, es: {}".format(var_1, suma))


media= (var_1[0] + var_1[1] + var_1[2] + var_1[3] + var_1[4] + var_1[5] + var_1[6] + var_1[7] + var_1[8] + var_1[9])/10
print ("La media de la lista {}, es: {}".format(var_1, media))

