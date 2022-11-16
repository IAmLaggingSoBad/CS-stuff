def encryption():
    text = str(input("Text: "))
    s = int(input("Shift: "))
    encrypt = ""
    for x in text:
        if (text.isupper()):
            encrypt += chr((ord(x) + s-65) % 26 + 65)
        else:
            encrypt += chr((ord(x) + s - 97) % 26 + 97)
    print("Encrypted text: " + encrypt)
    restart()


def decryption():
    text = str(input("Text: "))
    s = int(input("Shift: "))
    decrypt = ""
    for char in text:
        if (text.isupper()):
            decrypt += chr((ord(char) - s-65) % 26 + 65)
        else:
            decrypt += chr((ord(char) - s - 97) % 26 + 97)
    print("Encrypted text: " + decrypt)
    restart()

def choice():
    temp = input("Would you like to: \n1. Encrypt \n2. Decrypt \n[1/2]: ")
    if temp == "1":
        encryption()
    if temp == "2":
        decryption()
    else:
        print("Input either 1 or 2")
        choice()

def restart():
    temp1 = input("Would you like to continue: \n[Y/N]: ")
    if temp1 == "Y":
        choice()
    elif temp1 == "N":
        print("Ok Bye")
    else:
        print("Input either Y or N")
        restart()


choice()
