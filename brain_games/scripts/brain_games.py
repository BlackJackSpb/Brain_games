#!/usr/bin/env python3

from brain_games.cli import welcome_user


def main():

    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()
