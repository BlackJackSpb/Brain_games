#!/usr/bin/env python3
from ..cli import welcome_user


def brain():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


if __name__ == '__main__':
    brain()
