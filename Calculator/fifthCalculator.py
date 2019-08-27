print("femte version")

def toInt(s):
    try:
        intTal = int(s)
        return intTal
    except ValueError:
        print("kunne ikke lave ", s, " om til et tal")


tal1 = input("skriv det første tal: ")
tal2 = input("skriv det andet tal: ")

intTal1 = toInt(tal1)
intTal2 = toInt(tal2)

if intTal1 is None or intTal2 is None:
    print("kunne ikke lægge ", tal1, " sammen med ", tal2)
else:
    resultat = intTal1 + intTal2
    print("det giver ", resultat)

