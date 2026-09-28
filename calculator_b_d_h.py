"""Binary, Deniary, Hexadecimal"""

import sys


def format_binary(value):
    if value < 0:
        return "-" + bin(abs(value))[2:]
    return bin(value)[2:]


def format_hex(value):
    if value < 0:
        return "-" + hex(abs(value))[2:].upper()
    return hex(value)[2:].upper()


def main():
    """Main function."""
    calculating = True

    while calculating is True:
        print("1. Binary")
        print("2. Deniary")
        print("3. Hexadecimal")
        type_value = input(
            "Enter the number of the type of value you want to calculate with: "
        ).strip()
        num_1_text = input("Enter the first number: ").strip()
        calculate = input(
            "Enter the type of calculation you want to do (+, -, *, /, ^, %, DIV, MOD): "
        ).strip().upper()
        num_2_text = input("Enter the second number: ").strip()

        if type_value == "1":
            base = 2
            invalid_message = "Invalid binary number"
        elif type_value == "2":
            base = 10
            invalid_message = "Invalid deniary number"
        elif type_value == "3":
            base = 16
            invalid_message = "Invalid hexadecimal number"
        else:
            print("Invalid type of value")
            print("\n")
            continue

        try:
            num_1 = int(num_1_text, base)
            num_2 = int(num_2_text, base)
        except ValueError:
            print(invalid_message)
            print("\n")
            continue

        if calculate == "+":
            result = num_1 + num_2
        elif calculate == "-":
            result = num_1 - num_2
        elif calculate == "*":
            result = num_1 * num_2
        elif calculate == "/":
            if num_2 == 0:
                print("Cannot divide by zero")
                print("\n")
                continue
            result = num_1 / num_2
        elif calculate == "^":
            result = num_1 ** num_2
        elif calculate == "%":
            if num_2 == 0:
                print("Cannot divide by zero")
                print("\n")
                continue
            result = num_1 % num_2
        elif calculate == "DIV":
            if num_2 == 0:
                print("Cannot divide by zero")
                print("\n")
                continue
            result = num_1 // num_2
        elif calculate == "MOD":
            if num_2 == 0:
                print("Cannot divide by zero")
                print("\n")
                continue
            result = num_1 % num_2
        else:
            print("Invalid type of calculation")
            print("\n")
            continue

        if isinstance(result, float) and not result.is_integer():
            print("Result:", result)
            print("Binary: N/A for non-integer result")
            print("Hexadecimal: N/A for non-integer result")
        else:
            int_result = int(result)
            print("Result:", int_result)
            print("Binary:", format_binary(int_result))
            print("Hexadecimal:", format_hex(int_result))

        calculating_user = input("Do you want to calculate again? (yes/no): ")
        if calculating_user.lower() == "yes":
            calculating = True
        elif calculating_user.lower() == "no":
            calculating = False
            sys.exit()
        else:
            print("Invalid input")
            print("\n")

if __name__ == "__main__":
    main()
