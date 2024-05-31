#!/usr/bin/env python3
from random import randint


def brain_progression():
    first_elem = randint(1, 100)
    step = randint(1, 20)
    progression = []
    for i in range(10):
        progression.append(first_elem + step * (i + 1))
    index_sec_elem = randint(0, len(progression) - 1)
    secret_elem = progression[index_sec_elem]
    progression[index_sec_elem] = ".."
    return ' '.join(map(str, progression)), str(secret_elem)


def main_question():
    return "What number is missing in the progression?"


def main():
    brain_progression()


if __name__ == "__main__":
    main()
