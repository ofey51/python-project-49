from brain_games.games.even import brain_even, main_question
from brain_games.engine import run_game


def main():
    run_game(main_question, brain_even)


if __name__ == "__main__":
    main()