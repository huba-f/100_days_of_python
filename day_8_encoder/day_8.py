import day_8
# check if the number prime or not
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
direction = input('type \'ENCODE\' to encrypt or \'DECODE\' to decrypt or \'EXIT\' to exit: ').lower()
text = ''
shift = ''
encrypted_word = ''
def start():
    def information():
        global text
        global shift
        text = input('type your message: ').lower().replace('', ' ').split()
        shift = int(input('type your shift number: '))

    def encrypt(text_func, shift_func, encrypted_word_func):
        for l in range(len(text_func)):
            position = letters.index(text[l])
            encrypted_word_func += letters[position + shift_func]
        print(encrypted_word_func)

    def decrypt(text_func, shift_func, encrypted_word_func):
        for l in range(len(text_func)):
            position = letters.index(text[l])
            if text[l] in numbers:
                encrypted_word_func += numbers[position - shift_func]
            else:
                encrypted_word_func += letters[position - shift_func]
        print(encrypted_word_func)

    information()
    encrypt(text_func=text, shift_func=shift, encrypted_word_func=encrypted_word)
if direction == 'encode':
    start()
elif direction == 'decode':
    start()
elif direction == 'exit':
    print('bye')
    exit()
