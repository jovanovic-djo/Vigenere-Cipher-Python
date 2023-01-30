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
            if mode == 'e':
                result += ALPHABET[(alphabet_index + ALPHABET.find(key_char)) % 26]
            elif mode == 'd':
                result += ALPHABET[(alphabet_index - ALPHABET.find(key_char) + 26) % 26]
            else:
                print("Invalid Input!")
    return result

while True:
    mode = input("Enter Mode: Encryption(E)/Decryption(D): ").lower()
    if mode == 'd' or mode == 'e':
        message = input("Enter Message: ")
        key = input("Enter Key: ")
        print("Result: ", vigenere_cipher(message, key, mode))
    else:
        print("Invalid Input!")
