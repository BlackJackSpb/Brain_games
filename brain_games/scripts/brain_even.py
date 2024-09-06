#!/usr/bin/env python3
from ..cli import welcome_user
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print("Answer 'yes' if number even otherwise answer 'no'.")
    chek = 0

    for ckek in range(3):
        random_numbers = randint(0, 1000000)
        print(f'Question: {int(random_numbers)}')
        players_answer = prompt.string('Your answer: ')
        if players_answer == 'yes' and random_numbers % 2 == 0:
            chek += 1
            print('Correct!')
        elif players_answer == 'no' and random_numbers % 2 == 1:
            chek += 1
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            break

    if chek == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
