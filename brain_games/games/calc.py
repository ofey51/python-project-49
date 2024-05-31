#!/usr/bin/env python3

from random import randint, choice

def evaluation(num_1, num_2, operation):
    match operation:
        case '+':
            return int(num_1) + int(num_2)
        case '-':
            return int(num_1) - int(num_2)
        case '*':
            return int(num_1) * int(num_2)
        case _:
            return None
           

def main_question():
    return 'What is the result of the expression?'


def brain_calc():
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operation = choice(['+', '-', '*'])
    question_of_round = f"{num_1} {operation} {num_2}"
    correct_answer = str(evaluation(num_1, num_2, operation))
    return question_of_round, correct_answer
    

def main():
    brain_calc()


if __name__ == "__main__":
    main()