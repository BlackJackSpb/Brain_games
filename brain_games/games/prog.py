from random import randint

DESCRIPTION = 'What number is missing in the progression?'
START_STEP = 1
END_STEP = 10
START = 1
END = 100
START_SIZE = 4
END_SIZE = 9


def generate_question_and_answer():

    progression_size = randint(START_SIZE, END_SIZE)
    start = randint(START, END)
    step = randint(START_STEP, END_STEP)
    progression = [start]
    correct = randint(0, step - 1)

    for _ in range(progression_size):
        start += step
        progression.append(start)

    correct_answer = progression[correct]
    progression[correct] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'

    return question, str(correct_answer)
