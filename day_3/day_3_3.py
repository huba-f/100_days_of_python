print('order a pizza')
price = 0
size = input('what size pizza do you want? (s - m - l)')
extra_meet = input('do you want extra meet? (y -n)')
extra_chees = input('do you want extra chees? (y - n)')

small_size = 15
medium_size = 20
large_size = 25


if size == 's':
    price = small_size
elif size == 'm':
    price = medium_size
else:
    price == large_size
if extra_meet == 'y':
    price += 5
if extra_chees == 'y':
    price += 3
print(f'your pizza will be ${price}')
