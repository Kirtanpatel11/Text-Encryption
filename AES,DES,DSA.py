from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    return text + (16 - len(text) % 16) * ' '

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(text).encode())
    return base64.b64encode(encrypted).decode()

key = get_random_bytes(16)
details = input("Enter what you want to encrypt: ")
encrypted = aes_encrypt(details, key)

print("AES Key:", key)
print("Encrypted: ", encrypted)

#--------------------------------------------------------------------------------------------------------

# DES Encryption 