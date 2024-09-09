#!/usr/bin/env python3
from .brain_games import brain
from random import randint
import prompt


def main():
    name = brain()
    print("Answer 'yes' if number even otherwise answer 'no'.")

    for i in range(3):
        random_numbers = randint(0, 1000000)
        print(f'Question: {int(random_numbers)}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == 'yes' and random_numbers % 2 == 0:
            print('Correct!')
        elif players_answer == 'no' and random_numbers % 2 == 1:
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
