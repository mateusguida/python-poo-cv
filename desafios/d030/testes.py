import hashlib

# SHA = Secure Hash Algorithm
texto = "Gafanhoto"
cod = texto.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()

print(hash)