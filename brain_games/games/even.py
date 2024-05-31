#!/usr/bin/env python3
from random import randint


def brain_even():
    random_number = randint(1, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return random_number, correct_answer


def main_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    brain_even()


if __name__ == "__main__":
    main()
