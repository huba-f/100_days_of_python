
row_1 = ['🗅', '🗅', '🗅']
row_2 = ['🗅', '🗅', '🗅']
row_3 = ['🗅', '🗅', '🗅']
map = [row_1, row_2, row_3]
print(f'{row_1}\n{row_2}\n{row_3}')

vertical = input('enter vertical column: ')
horizontal = input('enter horizontal column: ')

position = map[int(vertical) - 1]
position[int(horizontal) - 1] = 'X'

print(row_1)
print(row_2)
print(row_3)
