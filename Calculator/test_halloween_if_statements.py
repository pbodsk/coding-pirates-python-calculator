error = False

try:
    dato = int(input("Skriv en dato: "))
except ValueError:
    error = True
    print("Du skrev noget forkert...")

if error == False and dato == 31:
    print("Det er Halloween!")
elif error == False and dato > 31:
    print("Du er for sent på den!! Halloween er færdig!")
elif error == False and dato < 31:
    print("Du er for tidligt på den!! Halloween er først om " + str(31 - dato) + " dage! :(")
