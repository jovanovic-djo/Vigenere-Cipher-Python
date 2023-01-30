def vigenere_cipher(message, key, mode):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    message = message.lower()
    key = key.lower()

    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        alphabet_index = ALPHABET.find(char)

        if alphabet_index == -1:
            result += char
        else:
            if mode == 'encrypt':
                result += ALPHABET[(alphabet_index + ALPHABET.find(key_char)) % 26]
            elif mode == 'decrypt':
                result += ALPHABET[(alphabet_index - ALPHABET.find(key_char) + 26) % 26]
    return result

mode = input("Enter mode (encrypt/decrypt): ")
message = input("Enter message: ")
key = input("Enter key: ")

print("Result: ", vigenere_cipher(message, key, mode))
