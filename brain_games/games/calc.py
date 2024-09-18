from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
START = 0
END = 10


def generate_question_and_answer():

    sign = choice(['+', '-', '*'])
    number1 = randint(START, END)
    number2 = randint(START, END)
    question = f'{number1} {sign} {number2}'

    if sign == '+':
        correct_answer = number1 + number2
    elif sign == '-':
        correct_answer = number1 - number2
    elif sign == '*':
        correct_answer = number1 * number2

    return question, str(correct_answer)
