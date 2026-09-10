# DecodeLabs Project 2
# Basic Encryption and Decryption - Caesar Cipher

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text


# Test message
plaintext = "HELLO WORLD"
shift = 3

ciphertext = encrypt(plaintext, shift)
decrypted_text = decrypt(ciphertext, shift)

print("Plaintext:", plaintext)
print("Shift Key:", shift)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text)
