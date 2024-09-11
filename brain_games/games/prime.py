from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def generate_question_and_answer():

    def prime(numbers):

        chek = 0
        half_the_numbers = int((numbers + 1) / 2)

        for i in range(1, half_the_numbers + 1):
            if numbers % i == 0:
                chek += 1

        if chek == 1:
            return True
        else:
            return False

    number = randint(START, END)
    question = f'Question: {number}'

    if prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
