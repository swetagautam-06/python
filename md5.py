# Import the hashlib module
import hashlib

# Read input message from the user
message = input("Enter a message: ")

# Convert the message into bytes
message_bytes = message.encode()

# Generate the MD5 hash
md5_hash = hashlib.md5(message_bytes)

# Convert the hash into hexadecimal format
hash_value = md5_hash.hexdigest()

# Display the original message
print("Original Message:", message)

# Display the MD5 hash value
print("MD5 Hash Value:", hash_value)
