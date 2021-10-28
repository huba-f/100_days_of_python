import random

rock_symb = '''
                _
               | |
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   <
|_|  \___/ \___|_|\_\
'''

paper_symb = '''
.--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""
'''

scissors_symb = '''
  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''


player = input('1 for rock - 2 for paper - 3 for scissors: ')
player = int(player) - 1
computer = random.randint(0, 2)
computer = int(computer) -1

rock = 0
paper = 1
scissors = 2
#rock
if player == rock and computer == paper:
    print(f'{rock_symb}\n\nloses\n{paper_symb}')
elif player == rock and computer == scissors:
    print(f'{rock_symb}\n\nbeats\n{scissors_symb}')
elif player == rock and computer == rock:
    print(f'{rock_symb}\n\nequals\n{rock_symb}')
# paper
elif player == paper and computer == rock:
    print(f'{paper_symb}\n\nbeats\n{rock_symb}')
elif player == paper and computer == scissors:
    print(f'{paper_symb}\n\nloses to\n{scissors_symb}')
elif player == paper and computer == paper:
    print(f'{paper_symb}\n\nequals\n{paper_symb}')
#scissors
elif player == scissors and computer == rock:
    print(f'{scissors_symb}\n\nloses to\n{rock_symb}')
elif player == scissors and computer == paper:
    print(f'{scissors_symb}\n\nbeats\n{paper_symb}')
elif player == scissors and computer == scissors:
    print(f'{scissors_symb}\n\nequals\n{scissors_symb}')
else:
    print('enter a valid option')
