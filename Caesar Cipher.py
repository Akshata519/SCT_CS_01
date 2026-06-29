def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


while True:
    print("\n===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted Text:", encrypt(message, shift))

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted Text:", decrypt(message, shift))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
