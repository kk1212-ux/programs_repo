import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


# Encryption

print()
print("#####################################################################################")
print()
plain_text = input("Enter the message: ")
print()
print("#####################################################################################")
print()

cipher_text = ""

for letter in plain_text:
    ind = chars.index(letter)
    cipher_text += key[ind]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")
print()
print("#####################################################################################")
print()

# Decryption

cipher_text = input("Enter the encrypted message: ")
plain_text = ""

for letter in cipher_text:
    ind = key.index(letter)
    plain_text += chars[ind]
print()
print("#####################################################################################")
print()
print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")