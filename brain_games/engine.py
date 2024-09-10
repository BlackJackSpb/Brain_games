import prompt
from brain_games.scripts.brain_games import brain


def play(module):
    name = brain()
    print(module.DESCRIPTION)
    
    for _ in range(3):
        question, correct_answer = module.generate_question_and_answer()
        
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
