def valid_calculation_method(entered_value):
    return  entered_value == "+" \
            or entered_value == "-" \
            or entered_value == "/" \
            or entered_value == "*" \
            or entered_value.lower()  == "stop"


def stop_calulating(method):
    return method.lower() == "stop"


def ask_for_input_and_calculate():
    input_string_1 = input("skriv det første tal: ")
    input_int_1 = to_int(input_string_1)

    input_string_2 = input("skriv det andet tal: ")
    input_int_2 = to_int(input_string_2)

    if input_int_1 is not None and input_int_2 is not None:
        value = perform_calculation(calculation_method, input_int_1, input_int_2)
        if value is not None:
            print(input_string_1 + " " + calculation_method + " " + input_string_2 + " = " + str(value))
    else:
        print("det kunne jeg ikke regne ud, prøv igen")


def to_int(s):
    try:
        int_tal = int(s)
        return int_tal
    except ValueError:
        print("kunne ikke lave ", s, " om til et tal")


def perform_calculation(method, value1, value2):
    if method == "+":
        return value1 + value2
    elif method == "-":
        return value1 - value2
    elif method == "/":
        return value1 / value2
    elif method == "*":
        return value1 * value2


should_continue = True

while should_continue:
    instruction_string = "vælg regnemetode (muligheder: +, -, * og /) eller skriv stop for at stoppe: "
    calculation_method = input(instruction_string)
    if valid_calculation_method(calculation_method):
        if stop_calulating(calculation_method):
            should_continue = False

        if should_continue:
            ask_for_input_and_calculate()
    else:
        print(calculation_method + " er ikke et muligt valg, " + instruction_string)