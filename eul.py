# Function to calculate GCD using Euclidean Algorithm
def gcd(a, b):

    # Continue until remainder becomes zero
    while b != 0:
        a, b = b, a % b

    # Return the Greatest Common Divisor
    return a


# Main Program
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result = gcd(num1, num2)

print("Greatest Common Divisor =", result)