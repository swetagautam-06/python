# Import gcd function to check if two numbers are coprime
from math import gcd

# Function to find modular inverse of e
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Input two prime numbers
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

# Calculate n
n = p * q

# Calculate Euler's Totient Function
phi = (p - 1) * (q - 1)

# Input public exponent
e = int(input("Enter public exponent (e): "))

# Check whether e and phi are coprime
if gcd(e, phi) != 1:
    print("Invalid value of e. It must be coprime with phi(n).")
else:

    # Find private key
    d = mod_inverse(e, phi)

    print("\nPublic Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    # Input message (must be less than n)
    message = int(input("\nEnter message (integer less than n): "))

    # Encrypt the message
    cipher = pow(message, e, n)

    # Decrypt the ciphertext
    decrypted = pow(cipher, d, n)

    print("\nEncrypted Message:", cipher)
    print("Decrypted Message:", decrypted)