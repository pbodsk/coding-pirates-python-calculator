print("fjerde version")
tal1 = input("skriv det første tal: ")
tal2 = input("skriv det andet tal: ")

try:
    intTal1 = int(tal1)
except ValueError:
    print("kunne ikke lave ", tal1, " om til et tal")

try:
    intTal2 = int(tal2)
except ValueError:
    print("kunne ikke lave ", tal2, " om til et tal")

if intTal1 is None and intTal2 is None:
    resultat = intTal1 + intTal2
    print("det giver ", resultat)
else:
    print("kunne ikke lægge ", tal1, " sammen med ", tal2)
