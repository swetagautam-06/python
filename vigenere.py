# Function to encrypt text
def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        # Encrypt only alphabetic characters
        if char.isalpha():
            char = char.upper()

            # Calculate shift from the key letter
            shift = ord(key[key_index % len(key)]) - ord('A')

            # Encrypt the character
            encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            result += encrypted
            key_index += 1
        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


# Function to decrypt text
def decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            # Reverse the encryption
            decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            result += decrypted
            key_index += 1
        else:
            result += char

    return result


# Main Program
text = input("Enter Plain Text: ")
key = input("Enter Keyword: ")

cipher = encrypt(text, key)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decrypt(cipher, key))