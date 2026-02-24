from main import quit_game
from src.game.add_question import run_add_question
from src.game.game import run_new_game
from src.game.leaderboard import run_leaderboard


def run_main_menu():
    print("Haluatko insinööriksi?\n\n")
    print("""Valitse numerolla ja paina enter
    1. Uusi peli
    2. Leaderboard
    3. Lisää kysymys
    4. Lopeta peli""")

    selection = int(input("Valitse: "))

    if selection == 1:
        run_new_game()
    elif selection == 2:
        run_leaderboard()
    elif selection == 3:
        run_add_question()
    elif selection == 4:
        quit_game()
    else:
        print("Invalid selection\n")
