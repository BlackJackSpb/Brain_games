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
    step = randint(START_STEP, END_STEP)
    start = randint(START, END)
    end = start + (step * progression_size)
    progression = []
    correct = randint(0, progression_size - 1)

    for number in range(start, end, step):
        progression.append(number)

    correct_answer = progression[correct]
    progression[correct] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'

    return question, str(correct_answer)
