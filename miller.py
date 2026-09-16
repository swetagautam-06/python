import random

# Function to perform Miller-Rabin Primality Test
def is_prime(n, k=5):

    # Handle small numbers
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds of testing
    for _ in range(k):

        # Choose a random base
        a = random.randint(2, n - 2)

        # Compute a^d mod n
        x = pow(a, d, n)

        # Check first condition
        if x == 1 or x == n - 1:
            continue

        # Repeat squaring
        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


# Main Program
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is Probably Prime.")
else:
    print(num, "is Composite.")