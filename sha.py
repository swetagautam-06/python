# Import hashlib module
import hashlib

# Read message from user
message = input("Enter a message: ")

# Convert message into bytes
message_bytes = message.encode()

# Generate SHA-1 hash
sha1_hash = hashlib.sha1(message_bytes).hexdigest()

# Generate SHA-256 hash (SHA-2)
sha256_hash = hashlib.sha256(message_bytes).hexdigest()

# Display results
print("\nOriginal Message:", message)
print("SHA-1 Hash   :", sha1_hash)
print("SHA-256 Hash :", sha256_hash)