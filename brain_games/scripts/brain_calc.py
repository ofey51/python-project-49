from brain_games.games.calc import brain_calc, main_question
from brain_games.engine import run_game


def main():
    run_game(main_question, brain_calc)


if __name__ == "__main__":
    main()
