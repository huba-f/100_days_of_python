import turtle
import pandas
from text_mover import TextMover


screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
text = TextMover()
data = pandas.read_csv('50_states.csv')

round_count = 0
correct_answers = 0
all_states = data.state.to_list()

while round_count <= 50:
    guess_state = screen.textinput(title=f'{correct_answers}/50 Guess a State', prompt='Enter a state name you know').title()
    state = data[data['state'] == guess_state]
    if guess_state in all_states:
        text.write_state(guess_state, int(state.x), int(state.y))
        all_states.remove(guess_state)
        correct_answers += 1

    if guess_state == 'Exit':
        break

    if correct_answers == 50:
        text.won()
        break

    round_count += 1
    if round_count == 50:
        text.end_of_game()

df = pandas.DataFrame(all_states)
df.to_csv('states_to_learn.csv')

turtle.mainloop()
