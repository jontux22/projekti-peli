from src.game.add_question import run_add_question
from src.game.game import run_new_game
from src.game.leaderboard import run_leaderboard


def run_main_menu(session):  # Lisätään parametri
    print("Haluatko insinööriksi? 🧑‍💻\n")
    print("""Valitse numerolla ja paina enter
1. Uusi peli
2. Leaderboard
3. Lisää kysymys
4. Lopeta peli""")

    selection = int(input("Valitse: "))

    if selection == 1:
        run_new_game()  # Saattaa tarvita session ehkä
        return True
    elif selection == 2:
        run_leaderboard(session)
        return True
    elif selection == 3:
        run_add_question(session)  # Välitetään sessio tänne
        return True
    elif selection == 4:
        return False
    else:
        print("Virheellinen valinta\n")
        return True
