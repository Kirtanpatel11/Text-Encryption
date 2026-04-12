from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import base64
import hashlib
import time


# class Block:
#     def __init__(self, index, data, previous_hash):
#         self.index = index
#         self.timestamp = time.time()
#         self.data = data
#         self.previous_hash = previous_hash
#         self.hash = self.calculate_hash()

#     def calculate_hash(self):
#         blockString = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
#         return hashlib.sha256(blockString.encode()).hexdigest()
    
# class Blockchain:
#     def __init__(self):   
#         self.chain = [self.create_genesis_block()]

#     def create_genesis_block(self):
#         return Block(0, "Genesis Block", "0")
    
#     def get_latest_block(self):
#         return self.chain[-1]
    
#     def add_block(self, data):  
#         latest_block = self.get_latest_block()
#         new_block = Block(len(self.chain), data, latest_block.hash)
#         self.chain.append(new_block)

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

# Selection

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

    # bc = Blockchain()
    # bc.add_block(details)
    # print("\n --Blockchain Mode--")

    # for block in bc.chain:
    #     print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, previous Hash: {block.previous_hash}")

elif choice == '2':
    key = b'8bytekey'
    encrypted = des_encrypt(details, key)
    print("\n--- DES Encryption ---")
    print("Encrypted:", encrypted)
    print("Key:", key)
    print("")

    # bc = Blockchain()
    # bc.add_block(details)
    # print("\n --Blockchain Mode--")

    # for block in bc.chain:
    #     print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, previous Hash: {block.previous_hash}")

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

    # bc = Blockchain()
    # bc.add_block(details)
    # print("\n --Blockchain Mode--")

    # for block in bc.chain:
    #     print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, previous Hash: {block.previous_hash}")
    

else: 
    print("Invalid choice.")
    print("")