def encrypt(plaintext, key):
    """Encrypt the plaintext using Caesar cipher with the given key (shift)."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            start = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - start + shift) % 26 + start)
        else:
            ciphertext += char  # Non-alphabetic characters remain unchanged
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using Caesar cipher with the given key (shift)."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            start = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - start - shift) % 26 + start)
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    return plaintext

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    # Input the message and the key
    message = input("Enter your message: ")
    key = int(input("Enter the shift key (an integer): "))
    
    # Encrypt the message
    encrypted_message = encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message back
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
