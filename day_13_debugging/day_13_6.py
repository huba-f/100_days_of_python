# debugger

def mutate(a_list):
    full_list = []
    for piece in a_list:
        multiplied_list = piece * 2
        full_list.append(multiplied_list)
    print(full_list)

mutate([1, 2, 3, 4, 5, 6])
