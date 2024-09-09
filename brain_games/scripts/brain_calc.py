#!/usr/bin/env python3
from .brain_games import brain
from random import randint, choice
import prompt


def main():
    name = brain()
    print('What is the result of the expression?')
    sing = ['-', '+', '*']

    for i in range(3):
        random_numbers_1 = randint(0, 100)
        random_numbers_2 = randint(0, 100)
        random_sign = choice(sing)
        summa = random_numbers_1 + random_numbers_2
        difference = random_numbers_1 - random_numbers_2
        multiplication = random_numbers_1 * random_numbers_2
        print(f'Question: {random_numbers_1, random_sign, random_numbers_2}')
        players_answer = prompt.integer('Your answer: ')

        if random_sign == '+' and players_answer == summa or\
            random_sign == '*' and players_answer == multiplication or\
                random_sign == '-' and players_answer == difference:
            print('Correct!')

        else:
            if random_sign == '+':
                print(f"'{players_answer}' is wrong answer ;(. Correct answe"
                      f"r was '{summa}'.\n", end='')
                print(f"Let's try again, {name}")
                return
            elif random_sign == '-':
                print(f"'{players_answer}' is wrong answer ;(. Correct answe"
                      f"r was '{difference}'.\n", end='')
                print(f"Let's try again, {name}")
                return
            else:
                print(f"'{players_answer}' is wrong answer ;(. Correct answe"
                      f"r was '{multiplication}'.\n", end='')
                print(f"Let's try again, {name}")
                return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
