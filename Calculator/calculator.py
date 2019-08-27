def toInt(stringValue):
    try:
        numberValue = int(stringValue)
        return numberValue
    except ValueError:
        print("could not convert '", stringValue, "' to an integer")
        return

firstValue = ""
secondValue = ""

shouldContinue = True

while shouldContinue:
    firstValue = input("Enter first value: ")
    secondValue = input("Enter second value: ")
    if firstValue != "stop" and secondValue != "stop":
        firstInt = toInt(firstValue)
        secondInt = toInt(secondValue)
        if firstInt != None and secondInt != None:
            total = firstInt + secondInt
            print(total)
        else:
            print("could not add ", firstValue, " to ", secondValue)
    else:
        shouldContinue = False
        print("OK, bye")

