import prompt

ROUND = 3


def play(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    for _ in range(ROUND):
        question, correct_answer = game.generate_question_and_answer()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
