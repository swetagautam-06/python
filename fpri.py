# Program to perform Fermat Primality Test

# Input number
n = int(input("Enter a number: "))

# Choose a test value
a = 2

# Handle small numbers
if n <= 1:
    print("Composite")
elif n == 2:
    print("Prime")
else:

    # Apply Fermat's Primality Test
    if pow(a, n - 1, n) == 1:
        print("Probably Prime")
    else:
        print("Composite")