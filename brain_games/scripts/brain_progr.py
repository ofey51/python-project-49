from brain_games.games.progr import brain_progression, main_question
from brain_games.engine import run_game


def main():
    run_game(main_question, brain_progression)


if __name__ == "__main__":
    main()
