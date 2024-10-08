from random import shuffle
import string

def encrypt(chars, keys, message):
    plain_text = message
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += keys[index]
    return cipher_text

def decrypt(chars, keys, message):
    cipher_text = message
    plain_text = ""
    for letter in cipher_text:
        index = keys.index(letter)
        plain_text += chars[index]
    return plain_text

def printmainMenu():
    print('*'*20)
    print('      Welcome    ')
    print('*' * 20)
    print('1. Encrypt Message')
    print('2. Dencrypt Message')
    print('3. Leave')
    while True:
        try:
            op = int(input('Option: '))
        except:
            print('\033[31mInvalid Option\033[m')
        else:
            if 1 <= op <= 3:
                break
            else:
                print('\033[31mInvalid Option\033[m')
    return op

def mainMenu():
    is_running = True
    chars = (' ' +
             string.punctuation +
             string.digits +
             string.ascii_letters)

    chars = list(chars)
    keys = chars.copy()
    shuffle(keys)
    while is_running:
        op = printmainMenu()
        match op:
            case 1:
                message = input('Enter the message to Encrypt: ').strip()
                encrypt_message = encrypt(message=message, chars=chars, keys=keys)
                print(f'Encrypt Message: {encrypt_message}')
            case 2:
                encrypt_message = input('Enter the message to Decrypt: ').strip()
                message = decrypt(message=encrypt_message, chars=chars, keys=keys)
                print(f'Decrypt Message: {message}')
            case 3:
                is_running = False
                continue


if __name__ == '__main__':
    mainMenu()