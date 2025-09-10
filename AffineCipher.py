# Affine Cipher Implementation 

def mod_inverse(a, m):
    """Find modular inverse of a under modulo m"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"No modular inverse for a = {a} under modulo {m}")

def encrypt_affine_cipher(plaintext, a, b):
    """
    Encryption formula: E(x) = (a*x + b) mod 26
    plaintext: string to encrypt
    a, b: keys (a must be coprime with 26)
    """
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            cipher_char = (a * x + b) % 26
            ciphertext += chr(cipher_char + base)
    return ciphertext

def decrypt_affine_cipher(ciphertext, a, b):
    """
    Decryption formula: D(y) = a_inv * (y - b) mod 26
    a_inv: modular inverse of a modulo 26
    """
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            plain_char = (a_inv * (y - b)) % 26
            plaintext += chr(plain_char + base)
    return plaintext

# Example usage
text = "Its raining"
a = 5   # Key a (must be coprime with 26)
b = 7   # Key b

print("AFFINE CIPHER")
print("-------------\n")
print("Original text :", text)

encrypted_text = encrypt_affine_cipher(text, a, b)
print("Cipher Text (Encrypted) :", encrypted_text)

decrypted_text = decrypt_affine_cipher(encrypted_text, a, b)
print("Plain Text (Decrypted)  :", decrypted_text)
