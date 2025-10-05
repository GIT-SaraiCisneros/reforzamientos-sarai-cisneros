'''
9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura “00054”
y su value será el coste de la factura. El programa tendrá la opción de pedir nueva
factura (por consola) que se agregará al diccionario. Cada vez que el área de
contabilidad pague una factura se pedirá el número de factura que fue cancelada,
si existe mostrar un mensaje donde indicará “La factura ya está cancelada” caso
contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva factura
se mostrará inmediatamente al diccionario actualizado.
'''



facturas = {}

while True:
    print("\n--- MENÚ ---")
    print("1. Registrar")
    print("2. Pagar")
    print("3. Pendientes")
    print("4. Salir")

    opcion = input("Elija opción (1-4): ")

    if opcion == "1":
        numero = input("Ingrese número de factura: ")
        if numero in facturas:
            print("La factura ya existe.")
        else:
            costo = float(input("Ingrese monto de factura: "))
            facturas[numero] = costo
            print("Factura registrada correctamente.")
        print("Facturas actuales:", facturas)

    elif opcion == "2":
        numero = input("Ingrese número de factura a pagar: ")
        if numero in facturas:
            del facturas[numero]
            print("Factura cancelada.")
        else:
            print("La factura no existe.")
        print("Facturas actualizadas:", facturas)

    elif opcion == "3":
        if facturas:
            print("Facturas pendientes:")
            for num, costo in facturas.items():
                print("Factura {} con valor S/{}".format(num, costo))
        else:
            print("No hay facturas pendientes")

    elif opcion == "4":
        print("Saliendo de sistema ...")
        break

    else:
        print("Opción invalida. Intentar otra vez.")