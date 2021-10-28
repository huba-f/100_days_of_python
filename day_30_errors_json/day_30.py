# # FileNotFound

try:
    file = open('file.txt')
    a_dictionary = {'kak': 'a'}
    print(a_dictionary['kak'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('somehtnsdsd')
except KeyError as error_message:
    print(f'{error_message}as')
else:
    content = file.read()
    print(content)
finally:
    raise KeyError('this is a made up error')

# height = float(input('enter your height: '))
# weight = float(input('enter your height: '))
#
# if height > 100:
#     raise ValueError('the height should not be over 100.')
