# calculator app


# add
def add(n1, n2):
    return n1 + n2
# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

# operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = float(input('enter your number: '))
operation_symbol = input('enter your operation: ')
num2 = float(input('enter another number: '))
# choosing the operation
calculation_func = operations[operation_symbol]
# assigning the result of the operation to the 'answer'
answer = calculation_func(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')

continue_or_not = input('do you want to continue (y/n):')
while continue_or_not == 'y':
    operation_symbol = input('enter your operation: ')
    another_number = float(input('enter another number: '))
    calculation_func = operations[operation_symbol]
    prew_answer = answer
    answer = calculation_func(answer, another_number)
    print(f'{prew_answer} {operation_symbol} {another_number} = {answer}')
    continue_or_not = input('do you want to continue (y/n):')

if continue_or_not == 'n':
    print('\nthank you for choosing us')
