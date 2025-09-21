
'''
12. Escribe un programa que almacene información de un producto:
Tu nombre, nombre del producto, precio unitario (float),
cantidad (int) e imprimirá finalmente algo como lo siguiente:

Buen día Nombre, el detalle de su compra es el siguiente:
- Producto: Pollo a la brasa
- Precio unitario: 50.50
- Cantidad: 2
- Total a pagar: 101
'''

var_nombre = "Sarai Cisneros"
var_producto = "Vestido"
var_precio = 350.50
var_cantidad = 2
var_total = var_precio * var_cantidad

print('\n*** RESULTADO EJERCICIO 12 ***\n')

print ( "Buen día {}, el detalle de su compra es el siguiente:".format(var_nombre))
print ( "- Producto:", var_producto )
print ( "- Precio unitario:", var_precio)
print ( "- Cantidad:", var_cantidad)
print ( "- Total a pagar:", var_total)

