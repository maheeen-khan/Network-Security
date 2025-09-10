# Vigenère Cipher 

def generate_key(plaintext, key):
    """Extend or truncate key to match the length of plaintext"""
    key = key.replace(" ", "")
    key_length = len(key)
    key_extended = ""
    for i in range(len(plaintext)):
        key_extended += key[i % key_length]
    return key_extended

def encrypt_vigenere_cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    key_extended = generate_key(plaintext, key)
    ciphertext = ""
    
    for p_char, k_char in zip(plaintext, key_extended):
        if p_char.isalpha():
            base = ord('A') if p_char.isupper() else ord('a')
            shift = ord(k_char.upper()) - ord('A')  # Convert key char to 0-25
            ciphertext += chr((ord(p_char) - base + shift) % 26 + base)
    return ciphertext

def decrypt_vigenere_cipher(ciphertext, key):
    key_extended = generate_key(ciphertext, key)
    plaintext = ""
    
    for c_char, k_char in zip(ciphertext, key_extended):
        if c_char.isalpha():
            base = ord('A') if c_char.isupper() else ord('a')
            shift = ord(k_char.upper()) - ord('A')
            plaintext += chr((ord(c_char) - base - shift) % 26 + base)
    return plaintext

# Example usage
text = "Its raining"
key = "KEY"

print("VIGENÈRE CIPHER")
print("----------------\n")
print("Original text :", text)

encrypted_text = encrypt_vigenere_cipher(text, key)
print("Cipher Text (Encrypted) :", encrypted_text)

decrypted_text = decrypt_vigenere_cipher(encrypted_text, key)
print("Plain Text (Decrypted)  :", decrypted_text)
