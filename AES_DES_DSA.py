#TEXT ENCRYPTION USING AES, DES, AND RSA

from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import base64

def AESpad(details):
    return details + (16 - len(details) % 16) * ' '

def aes_encrypt(details, key):
    cipher = AES.new(key, AES.MODE_GCM)
    encrypted = cipher.encrypt(AESpad(details).encode())
    return base64.b64encode(encrypted).decode()

def DESpad(details):
    return details + (8 - len(details) % 8) * ' '

def des_encrypt(details, key):
    cipher = DES.new(key, DES.MODE_CBC)
    encrypted = cipher.encrypt(DESpad(details).encode())
    return base64.b64encode(encrypted).decode()


#------------------------------------------------------------------------------------------------------------------------------

# Select the option for encryption

print("Select the encryption method:")
print("1. AES - Advanced Encryption Standard")
print("2. DES - Data Encryption Standard")
print("3. RSA - Rivest-Shamir-Adleman")

choice = input("Enter your choice in number (1, 2, 3): ")
details = input("Enter the details you want to encrypt: ")

if choice == '1': 
    key = get_random_bytes(16)
    encrypted = aes_encrypt(details, key)
    print("\n--- AES Encryption ---")
    print("Encrypted:", encrypted)
    print("Key:", key)
    print("")


elif choice == '2':
    key = b'8bytekey'
    encrypted = des_encrypt(details, key)
    print("\n--- DES Encryption ---")
    print("Encrypted:", encrypted)
    print("Key:", key)
    print("")

elif choice == "3":
    key_pair = RSA.generate(2048)
    public_key = key_pair.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(details.encode())

    print("\n--- RSA Encryption ---")
    print("\nEncrypted:", base64.b64encode(encrypted).decode())
    print("\nPublic Key:", public_key.export_key().decode())
    print("\nPrivate Key:", key_pair.export_key().decode())
    print("")

else: 
    print("Invalid choice.")
    print("")