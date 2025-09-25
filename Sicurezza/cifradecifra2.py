from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

def encrypt(plein_text, key):
    cypher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_test = cypher.encrypt(pad(plein_text).encode("utf-8"))
    return base64.b64encode(encrypted_test).decode("utf-8")

def decrypt(encrypted_test, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = (cipher.decrypt(base64.b64decode(encrypted_test)).decode("utf-8").strip())
    return decrypted_text

key = "TuPadre"
plein_text = "6"
encrypted_text = encrypt(plein_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Originale: ", plein_text)
print("Cifrato  : ", encrypted_text)
print("Decifrato: ", decrypted_text)