''''
Cryptography of Julius Caesar
'''

def encrypt(text, shift):
    return ''.join([char if char in ' ,.' else chr((ord(char) + shift - 97) % 26 + 97) for char in text.lower()])

def decrypt(text, shift):
    return ''.join([char if char in ' ,.' else chr((ord(char) - shift - 97) % 26 + 97) for char in text.lower()])
