#!/usr/bin/env python3
from random import randint


def is_prime(number):
    exceptions = [1, 4, 6, 8, 9]
    if number in exceptions:
        return False

    for i in range(2, round(number ** 0.5)):
        if number % i == 0:
            return False

    return True


def brain_prime():
    number = randint(1, 150)
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"
    return number, answer


def main_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    brain_prime()


if __name__ == "__main__":
    main()
