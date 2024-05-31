#!/usr/bin/env python3
from brain_games.cli import welcome_user


def hello():
    print("Welcome to the Brain Games!")
    return welcome_user()


def check_answer(player_answer, correct_answer, player_name):
    if player_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(
            f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {player_name}!")
        return False


def run_game(game_question, game):
    player = hello()
    print(game_question())
    game_rounds = range(3)
    all_rounds_win = True
    for _ in game_rounds:
        question, correct_answer = game()
        print(f"Question: {question}")
        player_answer = input("Your answer: ")
        if check_answer(player_answer, correct_answer, player) is True:
            continue
        else:
            all_rounds_win = False
            break

    if all_rounds_win:
        print(f"Congratulations, {player}!")


def main():
    run_game()


if __name__ == "__main__":
    main()
