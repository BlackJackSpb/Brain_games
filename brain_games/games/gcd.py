from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def generate_question_and_answer():

    number1 = randint(START, END)
    number2 = randint(START, END)
    question = f'{number1} {number2}'
    correct_answer = deduction(number1, number2)

    return question, str(correct_answer)


def deduction(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2
