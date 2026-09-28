"""Ceaser cipher"""

import sys
import random

daily_keys = {"bananna": 15, "Toby": 3, "BRAZIL": 23}
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


def main():
    """Main function to run the Caesar cipher program."""
    daily_key = random.choice(list(daily_keys.keys()))
    incoding = True

    while incoding is True:
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print("\n")
        choice = input("Enter a number:")
        print("\n")
        if choice == "1":
            incoding = incode_info(daily_key)
        elif choice == "2":
            incoding = decode_info()
        elif choice == "3":
            incoding = False
            sys.exit()
        else:
            print("Invalid choice")
            print("\n" * 3)


def incode_info(daily_key):
    """Get encoding information from the user."""
    print("1. Return Letters")
    print("2. Return Morse Code")
    print("3. Return Binary")
    print("\n")
    encyption_type = input("Enter a number: ")
    print("\n")

    if encyption_type == "1":
        incode_letter(daily_key)
        return True

    if encyption_type == "2":
        incode_morse_code(daily_key)
        return True

    if encyption_type == "3":
        incode_binary(daily_key)
        return True

    print("Not a valid input.")
    return True


def incode_letter(daily_key):
    """Encodes text using a Caesar cipher and returns letters."""
    cipher = input("Enter cipher number  or daily key (1-25 or DK): ")

    if cipher == "DK":
        cipher = daily_keys[daily_key]
        print("\n")
        print(daily_key)
        print("\n")

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True

    input_text = input("Enter text:")
    input_list = list(input_text)

    encoded_list = []
    for i, letter in enumerate(input_list):
        encoded_list.append(ord(letter))

    for i, letter in enumerate(encoded_list):

        if encoded_list[i] == 32:
            encoded_list[i] = chr(encoded_list[i])

        elif 65 <= encoded_list[i] <= 90:
            encoded_list[i] += cipher

            if encoded_list[i] > 90:
                encoded_list[i] = chr((encoded_list[i] - 65) % 26 + 65)
            else:
                encoded_list[i] = chr(encoded_list[i])

        elif 97 <= encoded_list[i] <= 122:
            encoded_list[i] += cipher

            if encoded_list[i] > 122:
                encoded_list[i] = chr((encoded_list[i] - 97) % 26 + 97)
            else:
                encoded_list[i] = chr(encoded_list[i])

    output_text = "".join(encoded_list)

    print(output_text)
    print("\n")
    return True


def incode_morse_code(daily_key):
    """Encodes text using Morse code."""
    cipher = input("Enter cipher number  or daily key (1-25 or DK): ")

    if cipher == "DK":
        cipher = daily_keys[daily_key]
        print("\n")
        print(daily_key)
        print("\n")

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True

    input_text = input("Enter text:")
    input_list = list(input_text)

    encoded_list = []
    for i, letter in enumerate(input_list):
        encoded_list.append(ord(letter))

    for i, letter in enumerate(encoded_list):

        if encoded_list[i] == 32:
            encoded_list[i] = chr(encoded_list[i])

        elif 65 <= encoded_list[i] <= 90:
            encoded_list[i] += cipher

            if encoded_list[i] > 90:
                encoded_list[i] = chr((encoded_list[i] - 65) % 26 + 65)
            else:
                encoded_list[i] = chr(encoded_list[i])

        elif 97 <= encoded_list[i] <= 122:
            encoded_list[i] += cipher

            if encoded_list[i] > 122:
                encoded_list[i] = chr((encoded_list[i] - 97) % 26 + 97)
            else:
                encoded_list[i] = chr(encoded_list[i])

        else:
            print("Not a valid input.")
            return True

    for i, letter in enumerate(encoded_list):
        if letter.upper() in morse_code:
            encoded_list[i] = morse_code[letter.upper()]
        else:
            encoded_list[i] = letter

    output_text = " ".join(encoded_list)

    print(output_text)
    print("\n")
    return True


def incode_binary(daily_key):
    """Encodes text using a Caesar cipher and returns binary."""
    cipher = input("Enter cipher number  or daily key (1-25 or DK): ")

    if cipher == "DK":
        cipher = daily_keys[daily_key]
        print("\n")
        print(daily_key)
        print("\n")

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True

    input_text = input("Enter text:")
    input_list = list(input_text)

    encoded_list = []
    for i, letter in enumerate(input_list):
        encoded_list.append(ord(letter))

    for i, letter in enumerate(encoded_list):

        if encoded_list[i] == 32:
            encoded_list[i] = format(ord(encoded_list[i]), "08b")

        elif 65 <= encoded_list[i] <= 90:
            encoded_list[i] += cipher

            if encoded_list[i] > 90:
                encoded_list[i] = format((encoded_list[i] - 65) % 26 + 65, "08b")
            else:
                encoded_list[i] = format(encoded_list[i], "08b")

        elif 97 <= encoded_list[i] <= 122:
            encoded_list[i] += cipher

            if encoded_list[i] > 122:
                encoded_list[i] = format((encoded_list[i] - 97) % 26 + 97, "08b")
            else:
                encoded_list[i] = format(encoded_list[i], "08b")

        else:
            print("Not a valid input.")
            return True

    output_text = " ".join(encoded_list)

    print(output_text)
    print("\n")
    return True


def decode_info():
    """Get decoding information from the user."""

    print("1. Return Letters")
    print("2. Return Morse Code")
    print("3. Return Binary")
    print("\n")
    encyption_type = input("Enter a number: ")
    print("\n")

    if encyption_type == "1":
        decode_letters()
        return True

    if encyption_type == "2":
        decode_morse_code()
        return True

    if encyption_type == "3":
        decode_binary()
        return True
    
    print("Not a valid input.")
    return True


def decode_letters():
    """Decodes text using a Caesar cipher."""
    cipher = input("Enter cipher number or daily key (1-25): ")

    if cipher in daily_keys.get(cipher, None):
        cipher = daily_keys[cipher]

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True

    input_text = input("Enter text:")
    input_list = list(input_text)

    decoded_list = []
    for i, letter in enumerate(input_list):
        decoded_list.append(ord(letter))

    for i, letter in enumerate(decoded_list):
        if decoded_list[i] == 32:
            decoded_list[i] = chr(decoded_list[i])

        elif 65 <= decoded_list[i] <= 90:
            decoded_list[i] -= cipher

            if decoded_list[i] < 65:
                decoded_list[i] = chr((decoded_list[i] - 65) % 26 + 65)
            else:
                decoded_list[i] = chr(decoded_list[i])

        elif 97 <= decoded_list[i] <= 122:
            decoded_list[i] -= cipher

            if decoded_list[i] < 97:
                decoded_list[i] = chr((decoded_list[i] - 97) % 26 + 97)
            else:
                decoded_list[i] = chr(decoded_list[i])

    output_text = "".join(decoded_list)

    print(output_text)
    print("\n")
    return True


def decode_morse_code():
    """Decodes text using Morse code."""
    cipher = input("Enter cipher number  or a daily key (1-25): ")

    if cipher in daily_keys.get(cipher, None):
        cipher = daily_keys[cipher]

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True
    input_text = input("Enter Morse code (separate letters with spaces): ")
    input_list = input_text.split(" ")

    decoded_list = []
    for i, code in enumerate(input_list):
        for letter, morse in morse_code.items():
            if code == morse:
                decoded_list.append(ord(letter))
                break
        else:
            decoded_list.append(ord(code[0]) if code else 32)

    for i, letter in enumerate(decoded_list):
        if decoded_list[i] == 32:
            decoded_list[i] = chr(decoded_list[i])

        elif 65 <= decoded_list[i] <= 90:
            decoded_list[i] -= cipher

            if decoded_list[i] < 65:
                decoded_list[i] = chr((decoded_list[i] - 65) % 26 + 65)
            else:
                decoded_list[i] = chr(decoded_list[i])

        elif 97 <= decoded_list[i] <= 122:
            decoded_list[i] -= cipher

            if decoded_list[i] < 97:
                decoded_list[i] = chr((decoded_list[i] - 97) % 26 + 97)
            else:
                decoded_list[i] = chr(decoded_list[i])

    output_text = "".join(decoded_list)

    print(output_text)
    print("\n")
    return True


def decode_binary():
    """Decodes text using binary."""
    cipher = input("Enter cipher number  or a daily key (1-25): ")

    if cipher in daily_keys.get(cipher, None):
        cipher = daily_keys[cipher]

    try:
        cipher = int(cipher)
        if not 1 <= cipher <= 25:
            print("Invalid cipher number")
            return True
    except ValueError:
        print("Invalid cipher number")
        print("\n")
        return True

    input_text = input("Enter binary code (separate letters with spaces): ")
    input_list = input_text.split(" ")

    decoded_list = []
    for i, code in enumerate(input_list):
        try:
            decoded_list.append(int(code, 2))
        except ValueError:
            decoded_list.append(32)

    for i in enumerate(decoded_list):
        if decoded_list[i] == 32:
            decoded_list[i] = chr(decoded_list[i])

        elif 65 <= decoded_list[i] <= 90:
            decoded_list[i] -= cipher

            if decoded_list[i] < 65:
                decoded_list[i] = chr((decoded_list[i] - 65) % 26 + 65)
            else:
                decoded_list[i] = chr(decoded_list[i])

        elif 97 <= decoded_list[i] <= 122:
            decoded_list[i] -= cipher

            if decoded_list[i] < 97:
                decoded_list[i] = chr((decoded_list[i] - 97) % 26 + 97)
            else:
                decoded_list[i] = chr(decoded_list[i])

    output_text = "".join(decoded_list)

    print(output_text)
    print("\n")
    return True


if __name__ == "__main__":
    main()
