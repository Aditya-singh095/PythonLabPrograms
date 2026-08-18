import sys

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

def main():
    # Take input from command line
    if len(sys.argv) >= 3:
        text = sys.argv[1]
        shift = sys.argv[2]

    # Otherwise take input from user
    else:
        text = input("Enter text: ")
        shift = input("Enter shift key: ")

    # Validate shift
    if not shift.lstrip("-").isdigit():
        print("Error: Shift key must be an integer.")
        return

    shift = int(shift)

    choice = input("Enter E to encrypt or D to decrypt: ").upper()

    if choice == "D":
        shift = -shift
    elif choice != "E":
        print("Error: Enter E or D.")
        return

    result = caesar_cipher(text, shift)

    print("Result:", result)


if __name__ == "__main__":
    main()
