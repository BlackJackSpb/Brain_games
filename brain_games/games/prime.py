from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():

    def prime(numbers):

        for i in range(2, numbers // 2 + 1):
            if numbers % i == 0:
                return False
        return True

    number = randint(1, 100)
    question = f'Question: {number}'

    correct_answer = 'yes' if prime(number) else 'no'

    return question, correct_answer
