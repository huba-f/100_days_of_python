print('welcome to treasure island\n your mission is to find the trasure')

direction = input('left or right? ')
if direction == 'right':
    print('game over')
else:
    swim_or_not = input('swim or wait? ')
    if swim_or_not == 'swim':
        print('game over')
    else:
        door = input('which door you want to go in? (red - blue - yellow)')
        if door == 'red' or door == 'blue':
            print('game over')
        else:
            print('you find the trasure, YOU WON!')
