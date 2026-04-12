import unittest
from AES_DES_DSA import aes_encrypt, des_encrypt, PKCS1_OAEP
from Crypto.Random import get_random_bytes

class TestEncryption(unittest.TestCase):
    def test_aes(self):
        key = get_random_bytes(16)
        result = aes_encrypt("hello", key)
        self.assertTrue(len(result) > 0)

    def test_des(self):
        key = b'8bytekey'
        result = des_encrypt("hello", key)
        self.assertTrue(len(result) > 0)

    def test_rsa(self):
        result, pub, priv = PKCS1_OAEP("hello")
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
