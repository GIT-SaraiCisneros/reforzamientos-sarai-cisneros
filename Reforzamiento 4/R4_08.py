'''
8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”

'''


agendita = {}

def registro(nombre):
    if nombre in agendita:
        return True
    else:
        return False

while True:
    print("\n--- Menú de la Agenda ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar agenda")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == '1':

        nombre = input("Ingresa el nombre: ")
        existe = registro(nombre)

        if existe == False:
            telefono = input("Ingresa el número de teléfono: ")
            agendita[nombre] = telefono
            print(f"Contacto '{nombre}' agregado correctamente.")
        else:
            print(f"'{nombre}' ya se encuestra registrado")

    elif opcion == '2':

        nombre = input("Ingresa el nombre a buscar: ")
        existe = registro(nombre)

        if existe == True:
            print(f"Teléfono de {nombre}: {agendita[nombre]}")
        else:
            print("No se encuentra registrado en la agenda.")
    elif opcion == '3':
        print(agendita)
    elif opcion == '4':
        print("Cerrando sistema...")
        break
    else:
        print("Ingrese una opción válida")