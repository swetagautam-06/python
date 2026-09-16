# Function to encrypt or decrypt the text
def encrypt(text, shift):
    result = ""

    # Loop through every character in the input text
    for char in text:

        # Check if the character is an alphabet
        if char.isalpha():

            # Determine whether the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')

            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) - start + shift) % 26 + start)

        else:
            # Keep spaces, numbers, and symbols unchanged
            result += char

    return result


# Take input from the user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
cipher = encrypt(text, shift)
print("Encrypted Text:", cipher)

# Decrypt the text by shifting in the opposite direction
plain = encrypt(cipher, -shift)
print("Decrypted Text:", plain)