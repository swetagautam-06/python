# Program to verify Fermat's Little Theorem

# Input values
a = int(input("Enter value of a: "))
p = int(input("Enter prime number p: "))

# Compute a^(p-1) mod p
result = pow(a, p - 1, p)

# Check Fermat's theorem
if result == 1:
    print("Fermat's Theorem is Verified.")
else:
    print("Fermat's Theorem is Not Verified.")

# Display the remainder
print("Result =", result)