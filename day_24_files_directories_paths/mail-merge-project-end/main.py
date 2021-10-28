
with open("../mail-merge-project-end/Input/Names/invited_names.txt", mode='r') as names:
    list_of_names = names.readlines()
    print(list_of_names)

with open('../mail-merge-project-end/Input/Letters/starting_letter.txt', mode='r') as starting_letter:
    letter = starting_letter.read()

for name in list_of_names:
    with open(f"../mail-merge-project-end/Output/ReadyToSend/letter_for_{name}.txt", mode='w') as mail:
        mail.write(letter.replace('[name]', f'{name.strip()}'))
    print(name.strip())
