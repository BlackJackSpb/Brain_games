from random import randint

DESCRIPTION = 'What number is missing in the progression?'
START_STEP = 1
END_STEP = 10
START = 1
END = 100
START_SIZE = 5
END_SIZE = 10


def generate_question_and_answer():

    progression_size = randint(START_SIZE, END_SIZE)
    start = randint(START, END)
    step = randint(START_STEP, END_STEP)
    progression = []
    correct = randint(0, progression_size - 1)

    for _ in range(progression_size):
        progression.append(start)
        start += step

    correct_answer = progression[correct]
    progression[correct] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'

    return question, str(correct_answer)
