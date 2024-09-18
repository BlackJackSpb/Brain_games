from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def generate_question_and_answer():
    number = randint(START, END)
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
