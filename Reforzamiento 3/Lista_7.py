guests = ["Ana", "Pedro", "Raúl", "Fiorella", "Katherine", "Miguel", "Luis"]
par = []
impar = []

if len(guests[0]) % 2 == 0:
    par.append(guests[0])
else:
    impar.append(guests[0])

if len(guests[1]) % 2 == 0:
    par.append(guests[1])
else:
    impar.append(guests[1])

if len(guests[2]) % 2 == 0:
    par.append(guests[2])
else:
    impar.append(guests[2])

if len(guests[3]) % 2 == 0:
    par.append(guests[3])
else:
    impar.append(guests[3])

if len(guests[4]) % 2 == 0:
    par.append(guests[4])
else:
    impar.append(guests[4])

if len(guests[5]) % 2 == 0:
    par.append(guests[5])
else:
    impar.append(guests[5])

if len(guests[6]) % 2 == 0:
    par.append(guests[6])
else:
    impar.append(guests[6])

print(guests)
print(par)
print(impar)