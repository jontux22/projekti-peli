from typing import List

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from src.database.db import engine
from src.database.models import Question


class Game:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

        # Get SQLAlchemy session
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session

    def get_questions_and_answers(self, limit: int = 10) -> List[Question]:
        # TODO: SQLAlchemy query for questions of given category
        # Jos joku viisas keksii miten queryyn ne järkevästi ni saa tehä :D
        query = (
            select(Question)
            .where(Question.category == self.category)
            .join(Question.answers)
            .order_by(Question.id)
        )

        results = self.session.execute(query).all()
        print(results)
        return results


def run_new_game():
    # TODO: Koodaa funktioon mitä tapahtuu kun valikosta valitaan uusi peli
    # Kalle voi vastata tästä
    name: str = input("Kirjoita nimesi: ")
    category: str = select_category()

    game = Game(name, category)
    game.get_questions_and_answers()


def select_category() -> str:

    session = sessionmaker(bind=engine)
    with session() as session:
        query = select(Question.category).distinct()
        categories = session.execute(query).scalars().all()

    options = list(categories)
    options.append("Kaikki kategoriat")

    print("\n--- Valitse kategoria ---")
    for i, cat in enumerate(options, 1):
        print(f"{i}. {cat}")

    while True:
        try:
            choice = int(input("Valitse numero: "))
            if 1 <= choice <= len(options):
                selected = options[choice - 1]
                print(f"Valitsit: {selected}\n")
                return selected
            else:
                print("Virheellinen numero, yritä uudelleen. ")
        except ValueError:
            print("Syötä vain numeroita. ")

    # TODO: Hae kategoriat ja valitse
    # Vaatimukset:
    # Käytä SQLAlchemy kirjastoa hakeaksesi kategoriat, käytä luokkaa "Question" src.database.models.question
    # listaa numeroituna, pyydä käyttäjää valitsemaan kategoria, palauta kategoria str returnilla
    # muista myös vaihtoehto "kaikki kategoriat", tällöin funktio voisi palauttaa esim "kaikki"
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#simple-select
    pass