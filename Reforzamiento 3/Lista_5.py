'''
5. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los datos
mediante consola también (5 compañías relacionadas con al mundo de TI) y harás una copia
donde adrede agregarás nombres que estarán repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial
'''

compañia=["Google", "Oracle", "SAP", "IBM", "Microsoft"]
compañia_n = compañia.copy()
compañia_n.extend(["Oracle", "IBM"])
compañia_nn = list(set(compañia_n))

print('\n*** RESULTADO LISTA 5 ***\n')

print ("La lista inicial es: {}".format(compañia))
print ("La lista copia es: {}".format(compañia_n))
print ("La lista sin repetidos es: {}".format(compañia_nn))
