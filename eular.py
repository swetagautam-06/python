# Function to calculate GCD
def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


# Function to calculate Euler Totient Function
def phi(n):

    count = 0

    # Check every number from 1 to n
    for i in range(1, n + 1):

        # Count numbers that are coprime with n
        if gcd(i, n) == 1:
            count += 1

    return count


# Main Program
n = int(input("Enter a Positive Integer: "))

print("Euler Totient Function φ(", n, ") =", phi(n))