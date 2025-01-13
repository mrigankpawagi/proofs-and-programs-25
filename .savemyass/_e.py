import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import base64

def generate_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

def encrypt_file(filepath, passphrase):
    with open(filepath, 'rb') as file:
        data = file.read()
    salt = os.urandom(16)
    key = generate_key(passphrase, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(salt), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    with open(filepath, 'wb') as file:
        file.write(base64.b64encode(salt + encrypted_data))

def decrypt_file(filepath, passphrase):
    with open(filepath, 'rb') as file:
        data = base64.b64decode(file.read())
    salt, encrypted_data = data[:16], data[16:]
    key = generate_key(passphrase, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(salt), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    with open(filepath, 'wb') as file:
        file.write(data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python _e.py [encrypt|decrypt] <filepath> <passphrase>")
        sys.exit(1)
    
    command, filepath, passphrase = sys.argv[1:]
    if command == "encrypt":
        encrypt_file(filepath, passphrase)
    elif command == "decrypt":
        decrypt_file(filepath, passphrase)
    else:
        print("Invalid command. Use 'encrypt' or 'decrypt'")
        sys.exit(1)
