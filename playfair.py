# Function to prepare the plaintext
def prepare_text(text):

    # Convert text to uppercase
    text = text.upper()

    # Replace J with I (Playfair rule)
    text = text.replace("J", "I")

    # Remove spaces
    text = text.replace(" ", "")

    return text


# Function to create the Playfair matrix
def generate_matrix(keyword):

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"   # J is omitted

    matrix = []
    used = ""

    # Add keyword letters first
    for letter in keyword.upper():
        if letter == "J":
            letter = "I"

        if letter not in used and letter in alphabet:
            used += letter

    # Add remaining alphabet letters
    for letter in alphabet:
        if letter not in used:
            used += letter

    # Create a 5 × 5 matrix
    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))

    return matrix


# Main Program
keyword = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

prepared = prepare_text(plaintext)

print("\nPrepared Text:", prepared)

matrix = generate_matrix(keyword)

print("\nPlayfair Matrix:")

# Display the matrix row by row
for row in matrix:
    print(row)

print("\n(Note: Encryption follows Playfair Cipher rules using this matrix.)")