# Diffie-Hellman Key Exchange Algorithm

# Publicly known prime number
P = int(input("Enter Prime Number (P): "))

# Publicly known primitive root
G = int(input("Enter Primitive Root (G): "))

# Alice's private key
a = int(input("Enter Alice's Private Key: "))

# Bob's private key
b = int(input("Enter Bob's Private Key: "))

# Calculate Alice's public key
A = pow(G, a, P)

# Calculate Bob's public key
B = pow(G, b, P)

print("\nAlice's Public Key =", A)
print("Bob's Public Key =", B)

# Alice computes the shared secret key
alice_secret = pow(B, a, P)

# Bob computes the shared secret key
bob_secret = pow(A, b, P)

print("\nShared Secret Key (Alice) =", alice_secret)
print("Shared Secret Key (Bob) =", bob_secret)

# Verify whether both keys match
if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
else:
    print("\nKey Exchange Failed!")