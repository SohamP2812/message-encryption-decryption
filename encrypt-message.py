import string    
import random
import base64
from secret import get_secret_key

def menu():
    print(('-'*13) + ' Options ' + ('-' *13))
    print('1. Encrypt a message')
    print('2. Decrypt a message')
    print('3. Regenerate key')
    print('Q. Exit')
    print('-'*35)
    return input('-> ')

def encrypt_message():
    key = get_secret_key()
    print('Please enter a message to encrypt: ')
    message = input()
    encryption = []
    for i in range(len(message)):
        key_char = key[i % len(key)]
        encryption.append(chr((ord(message[i]) + ord(key_char)) % 256))
    encoded_encryption = base64.urlsafe_b64encode("".join(encryption).encode()).decode()
    print("Your encrypted message is: ")
    print(encoded_encryption)
    print("It was generated using the key in secret.py")

def decrypt_message():
    print('Please enter a key')
    key = input()
    print('Please enter a message to decrypt: ')
    message = input()
    message = base64.urlsafe_b64decode(message).decode()
    decryption = []
    for i in range(len(message)):
        key_char = key[i % len(key)]
        decryption.append(chr((256 + ord(message[i]) - ord(key_char)) % 256))
    print("Your decrypted message is: ")
    print("".join(decryption))

def regenerate_key():
    curr = get_secret_key()
    key_len = 10 
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = key_len))    
    with open('secret.py', 'r') as file:
            filedata = file.read()

    filedata = filedata.replace(curr, ran)

    with open('secret.py', 'w') as file:
        file.write(filedata)
    print('A new key has been generated. Please copy this and keep it safe: ')
    print(ran)

key = get_secret_key()

if key == 'default':
    key = regenerate_key()

choice = menu()
while choice != 'Q':
    if choice == '1':
        encrypt_message()
        choice = menu()
    if choice == '2':
        decrypt_message()
        choice = menu()
    if choice == '3':
        regenerate_key()
        exit()
    else:
        choice = menu()
exit()