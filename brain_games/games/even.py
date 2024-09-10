from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
END = 100


def generate_question_and_answer():

    number = randint(START, END)
    question = f'{number}'

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
