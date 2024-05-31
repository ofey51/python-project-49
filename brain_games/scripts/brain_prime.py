from brain_games.games.prime import brain_prime, main_question
from brain_games.engine import run_game


def main():
    run_game(main_question, brain_prime)


if __name__ == "__main__":
    main()