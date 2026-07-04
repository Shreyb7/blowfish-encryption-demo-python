"""
Blowfish Encryption Demo

A simple Python implementation demonstrating Blowfish
encryption and decryption using the PyCryptodome library.

"""

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad


def blowfish_encrypt_decrypt():
    key = b'secretkey'
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    text = input("Enter plaintext: ").encode()

    ciphertext = cipher.encrypt(pad(text, Blowfish.block_size))
    print("\nEncrypted (Blowfish):", ciphertext)

    decrypted = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    print("Decrypted (Blowfish):", decrypted.decode())


if __name__ == "__main__":
    blowfish_encrypt_decrypt()
