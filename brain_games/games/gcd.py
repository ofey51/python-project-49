#!/usr/bin/env python3
from random import randint


def brain_gcd():
    a = randint(1, 100)
    b = randint(1, 100)
    question_of_round = f"{a} {b}"
    while a != b:
        if a > b:
            a = a - b
        else: 
            b = b - a
    gcd = a
    return question_of_round, str(gcd)


def main_question():
    return "Find the greatest common divisor of given numbers."


def main():
    brain_gcd()


if __name__ == "__main__":
    main()