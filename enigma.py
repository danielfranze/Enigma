# name: Enigma
# autor: Daniel Franze

from sys import exit

rotor_50 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rotor_51 = list("ADCBEHFGILJKMPNOQTRSUXVWZY")
rotor_60 = list("ACEDFHGIKJLNMOQPRTSUWVXZYB")
rotor_61 = list("AZXVTRPNDJHFLBYWUSQOMKIGEC")
rotor_70 = list("AZYXWVUTSRQPONMLKJIHGFEDCB")
rotor_71 = list("AEBCDFJGHIKOLMNPTQRSUYVWXZ")

rotor_01 = None
rotor_02 = None
rotor_03 = None
rotor_01_index = None
rotor_02_index = None
rotor_03_index = None

text = None
print_rot = 1
print_rot_de = 1


def encrypt(single_char):
    """
    Starts the encryption of the program
    :param single_char: str
    :return:
    """
    global rotor_01, rotor_02, rotor_03, rotor_01_index, rotor_02_index, rotor_03_index, print_rot
    index_char = rotor_01.index(single_char)
    index2_char = rotor_02.index(single_char)

    if print_rot is 1:
        while index_char is not rotor_01_index:
            rotor_01_index += 1
            if rotor_01_index is 26:
                rotor_01_index = 0
            rotor_02_index -= 1
            if rotor_02_index is -1:
                rotor_02_index = 25
            rotor_03_index += 1
            if rotor_03_index is 26:
                rotor_03_index = 0
    if print_rot is 2:
        while index2_char is not rotor_02_index:
            rotor_01_index -= 1
            if rotor_01_index is -1:
                rotor_01_index = 25
            rotor_02_index += 1
            if rotor_02_index is 26:
                rotor_02_index = 0
            rotor_03_index -= 1
            if rotor_03_index is -1:
                rotor_03_index = 25

    if print_rot == 1:
        print(rotor_03[rotor_03_index], end="")
        print_rot = 2
    else:
        print(rotor_03[rotor_03_index], end="")
        print_rot = 1


def decrypt(single_char):
    """
    Starts the decryption of the program
    :param single_char: str
    :return:
    """
    global rotor_01, rotor_02, rotor_03, rotor_01_index, rotor_02_index, rotor_03_index, print_rot, print_rot_de
    index_char = rotor_03.index(single_char)

    while index_char is not rotor_03_index:
        rotor_01_index += 1
        if rotor_01_index is 26:
            rotor_01_index = 0
        rotor_02_index -= 1
        if rotor_02_index is -1:
            rotor_02_index = 25
        rotor_03_index += 1
        if rotor_03_index is 26:
            rotor_03_index = 0

    if print_rot_de == 1:
        print(rotor_01[rotor_01_index], end="")
        print_rot_de = 2
    else:
        print(rotor_02[rotor_02_index], end="")
        print_rot_de = 1


def set_index(code):
    """
    Sets the rotors to the correct position
    :param code: str
    :return:
    """
    global rotor_01_index, rotor_02_index, rotor_03_index
    rotor_01_index = rotor_01.index(code[0])
    rotor_02_index = rotor_02.index(code[1])
    rotor_03_index = rotor_03.index(code[2])


def set_rotor(rotor):
    """
    Sets 3 rotors of 6 in the right sequence
    :param rotor:
    :return:
    """
    global rotor_50, rotor_51, rotor_60, rotor_61, rotor_70, rotor_71
    if rotor == "50":
        return rotor_50
    elif rotor == "51":
        return rotor_51
    elif rotor == "60":
        return rotor_60
    elif rotor == "61":
        return rotor_61
    elif rotor == "70":
        return rotor_70
    elif rotor == "71":
        return rotor_71


def menu_enter_code():
    """
    Shows a sub menu for the code
    :return:
    """
    while True:
        code = input("Enter the code (three uppercase letters): ")
        error = False
        for element in list(code):
            if element in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                pass
            else:
                error = True
        if error is True:
            print("Error: wrong values!")
            continue
        if len(code) is not 3:
            print("Error: code has not the right length!")
            continue
        set_index(code)
        break


def menu_rotors():
    """
    Shows the menu of the rotors selection
    :return:
    """
    global rotor_01, rotor_02, rotor_03, text
    print("*---------------------------Selection----------------------------*")
    print("* Choose three of the following rotors:                          *")
    print("* Rotor 50: ABCDEFGHIJKLMNOPQRSTUVWXYZ    value: 50              *")
    print("* Rotor 51: ADCBEHFGILJKMPNOQTRSUXVWZY    value: 51              *")
    print("* Rotor 60: ACEDFHGIKJLNMOQPRTSUWVXZYB    value: 60              *")
    print("* Rotor 61: AZXVTRPNDJHFLBYWUSQOMKIGEC    value: 61              *")
    print("* Rotor 70: AZYXWVUTSRQPONMLKJIHGFEDCB    value: 70              *")
    print("* Rotor 71: AEBCDFJGHIKOLMNPTQRSUYVWXZ    value: 71              *")
    print("*                                                                *")
    print("*----------------------------------------------------------------*")
    while True:
        rotor = input("Enter a value for position 1: ")
        if rotor in ["50", "51", "60", "61", "70", "71"]:
            rotor_01 = set_rotor(rotor)
            break
        else:
            print("Error: wrong value!")

    while True:
        rotor = input("Enter a value for position 2: ")
        if rotor in ["50", "51", "60", "61", "70", "71"]:
            rotor_02 = set_rotor(rotor)
            break
        else:
            print("Error: wrong value!")

    while True:
        rotor = input("Enter a value for position 3: ")
        if rotor in ["50", "51", "60", "61", "70", "71"]:
            rotor_03 = set_rotor(rotor)
            break
        else:
            print("Error: wrong value!")


def menu():
    """
    Shows the menu (TUI) of the program
    :return:
    """
    global rotor_01, rotor_02, rotor_03, text
    menu_rotors()
    menu_enter_code()

    while True:
        print("*---------------------------Selection----------------------------*")
        print("*     encrypt: 1  |  decrypt: 2                                  *")
        print("*     new Code: 0 |  new sequence of rotors: 4                   *")
        print("*     exit: 3                                                    *")
        print("*                                                                *")
        print("*----------------------------------------------------------------*")
        choose = input("Enter: ")
        try:
            if int(choose) is 1:
                while True:
                    text_for_conv = input("Enter a text: ")
                    error = False
                    for element in list(text_for_conv):
                        if element in list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
                            pass
                        else:
                            error = True
                            continue
                    if error is not True:
                        text = text_for_conv.upper()
                        break
                    print("Error: only ascii characters are allowed!")

                print("Result (encrypt): ", end="")
                for element in list(text):
                    encrypt(element)
                print("")
            elif int(choose) is 2:
                result_encrypt = input("Enter a text (decryption): ")
                print("Result (decrypt): ", end="")
                for element in list(result_encrypt):
                    decrypt(element)
                print("")
            elif int(choose) is 3:
                exit(0)
            elif int(choose) is 0:
                menu_enter_code()
            elif int(choose) is 4:
                menu_rotors()
            else:
                print("Error: selection not possible!")
        except ValueError:
            print("Error: selection not possible!")
            continue


def main():
    menu()


if __name__ == '__main__':
    main()
