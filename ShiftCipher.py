# Shift Cipher 

def encrypt_shift_cipher(plaintext, shift):
    
    plaintext = plaintext.replace(" ", "")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        # Ignore non-alphabetic characters
    return ciphertext

def decrypt_shift_cipher(ciphertext, shift):
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
    return plaintext

# Example usage
text = "Its raining"
shift_key = 3

print("SHIFT CIPHER")
print("------------\n")
print("Original text : ",text)

encrypted_text = encrypt_shift_cipher(text, shift_key)
print("Cipher Text (Encrypted) :", encrypted_text)  # Output: KhoorZruog

decrypted_text = decrypt_shift_cipher(encrypted_text, shift_key)
print("Plain text (Decrypted):", decrypted_text)  # Output: HelloWorld
