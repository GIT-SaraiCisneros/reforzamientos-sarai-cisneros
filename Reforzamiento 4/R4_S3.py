'''
3. Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está
dentro de la oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0” Métodos útiles: lower() y find()
'''

frase = input("Ingrese frase: ")
palabra = input("Ingrese palabra: ")

frase_minusc = frase.lower()    #lower: minuscula
palabra_minusc = palabra.lower()

posicion_palabra = frase_minusc.find(palabra_minusc)    #find: busca posicion, -1 en find significa que no encontró la palabra

if posicion_palabra != -1:
    print('En la frase, la palabra "{}" aparece en la posición {}'.format(palabra,posicion_palabra))
else:
    print('La palabra "{}" no aparece en la frase'.format(palabra))