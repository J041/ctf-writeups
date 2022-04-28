
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b"lagandcrashtwntytwenty2chalflagz"


def encrypt(plaintext_utf8):
    plaintext_utf8 = plaintext_utf8.encode("utf8")
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')


def decrypt(ciphertext_string):
    ciphertext = base64.b64decode(ciphertext_string)
    cipher = AES.new(key, AES.MODE_ECB)
    decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decryptedtext_utf.decode("utf8")
