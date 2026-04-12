from flask import Flask, render_template, request
from AES_DES_DSA import aes_encrypt, des_encrypt, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        method = request.form["method"]

        if method == "AES":
            key = get_random_bytes(16)
            result = aes_encrypt(text, key)

        elif method == "DES":
            key = b'8bytekey'
            result = des_encrypt(text, key)

        elif method == "RSA":
            key_pair = RSA.generate(2048)
            public_key = key_pair.publickey()
            cipher = PKCS1_OAEP.new(public_key)
            encrypted = cipher.encrypt(text.encode())
            result = base64.b64encode(encrypted).decode()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
