import random
import string

# Create a list of characters (including space)
chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy()
random.shuffle(key)

# Encryption
plain_text = input("Enter your plain text: ")
cipher_text = ""

# Encrypt each character by replacing it with its corresponding character in the shuffled key
for char in plain_text:
    index = chars.index(char)  # Find the index in the original character set
    cipher_text += key[index]  # Use the index to get the character from the shuffled key

print(f"Encrypted Message: {cipher_text}")

# Decryption
cipher_text = input("Enter your encrypted text: ")
decrypted_text = ""

# Decrypt each character by reversing the process
for char in cipher_text:
    index = key.index(char)  # Find the index in the shuffled key
    decrypted_text += chars[index]  # Use the index to get the original character from chars

print(f"Decrypted Message: {decrypted_text}")
