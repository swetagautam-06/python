# Function to encrypt text
def encrypt(text, rails):

    # Create empty rails
    fence = ['' for _ in range(rails)]

    rail = 0
    direction = 1

    # Arrange text in zigzag
    for char in text:
        fence[rail] += char

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return ''.join(fence)


# Function to decrypt text
def decrypt(cipher, rails):

    # Create zigzag pattern
    pattern = [['' for _ in cipher] for _ in range(rails)]

    rail = 0
    direction = 1

    for i in range(len(cipher)):
        pattern[rail][i] = '*'

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    # Fill pattern with ciphertext
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if pattern[i][j] == '*':
                pattern[i][j] = cipher[index]
                index += 1

    # Read plaintext
    result = ""
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        result += pattern[rail][i]

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return result


# Main Program
text = input("Enter Plain Text: ")
rails = int(input("Enter Number of Rails: "))

cipher = encrypt(text, rails)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decrypt(cipher, rails))