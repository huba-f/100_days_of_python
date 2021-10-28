import pandas

nato_alphabet_data_frame = pandas.read_csv('nato_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}


def message_coder():
    try:
        message = input('Enter your message: ').upper()
        list_message = list(message)
        final_message = [nato_alphabet_dict[letter] for letter in list_message]
    except KeyError:
        print('letters only')
        message_coder()
    else:
        print(final_message)


message_coder()
