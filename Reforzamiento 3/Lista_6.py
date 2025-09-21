'''
6. Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
'''

guests = ["Ana", "Pedro", "Raúl", "Fiorella", "Katherine", "Miguel", "Luis"]
lista_par=[]
lista_impar=[]

if len(guests[0])%2!=0:
    lista_impar.append(guests[0])
else:
    lista_par.append(guests[0])

if len(guests[1])%2!=0:
    lista_impar.append(guests[1])
else:
    lista_par.append(guests[1])

if len(guests[2])%2!=0:
    lista_impar.append(guests[2])
else:
    lista_par.append(guests[2])

if len(guests[3])%2!=0:
    lista_impar.append(guests[3])
else:
    lista_par.append(guests[3])

if len(guests[4])%2!=0:
    lista_impar.append(guests[4])
else:
    lista_par.append(guests[4])

if len(guests[5])%2!=0:
    lista_impar.append(guests[5])
else:
    lista_par.append(guests[5])

if len(guests[6])%2!=0:
    lista_impar.append(guests[6])
else:
    lista_par.append(guests[6])

print('\n*** RESULTADO LISTA 6 ***\n')

print ("La lista inicial es:",guests)
print ("la lista impar es: ",lista_impar)
print ("la lista par es: ",lista_par)
print ("la lista reorganizada es: ",lista_impar + lista_par)
