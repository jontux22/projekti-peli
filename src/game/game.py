import random
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, selectinload

from src.database.db import engine
from src.database.models import Question, Score


class Game:
    def __init__(self, name: str, category: str):
        self.name: str = name
        self.category: str = category
        self.used_lifelines: List[str] = []
        self.questions = []
        self.question_count: int = 8
        self.current_question = None
        self.score = 0

        # Get SQLAlchemy session
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session

    def get_questions_and_answers(self, limit: int = 8):
        # Query to get questions with answers limited to "limit"
        query = (
            select(Question)
            .where(Question.category == self.category)
            .options(selectinload(Question.answers))
            .order_by(Question.id)
            .limit(limit)
        )

        questions = self.session.scalars(query).all()

        # Save questions into more easily usable list form
        for question in questions:
            self.questions.append({
                "id": question.id,
                "question": question.question,
                "difficulty": question.difficulty,
                "answers": [{"id": answer.id, "answer": answer.answer, "correct": answer.correct} for answer in question.answers]
            })

        self.current_question = {"index": 0, "data": self.questions[0]}

    def run_question(self):
        print(f"Kysymys {self.current_question["index"] + 1}/{len(self.questions)}: {self.current_question["data"]['question']}")
        print("_"*30)

        for key, answer in enumerate(self.current_question["data"]["answers"], 1):
            print(f"{key}: {answer["answer"]}")

        # Ask for answer, check correct or incorrect or lifelines
        while True:
            try:
                user_answer_index = int(input("Anna vastausnumero: ")) - 1
                if 0 <= user_answer_index < len(self.current_question["data"]["answers"]):
                    break
                else:
                    print("Anna kelvollinen vastausnumero")
            except ValueError:
                print('Anna kelvollinen vastaus')

        if self.current_question["data"]["answers"][user_answer_index]["correct"]:
            print("Oikein!")
            self.score += self.current_question["data"]["difficulty"]
            print(f"Pisteesi ovat: {self.score}")
        else:
            print("Väärin!")
            print(f"Pisteesi ovat: {self.score}")

        if self.current_question["index"] + 1 < len(self.questions):
            self.current_question = {"index": self.current_question["index"] + 1,
                                     "data": self.questions[self.current_question["index"] + 1]}
        else:
            # TODO: Kierros suoritettu mitä tapahtuu?
            pass

    # TODO: Oispa aikaa tehä :)
    # def lifeline_fiftyfifty(self):
    #     if not self.used_lifelines["fifty_fifty"]:
    #         print("Olet jo kayttanyt 50/50 lifelinen")
    #         return
    #     pass
    #
    # def lifeline_extra_guess(self):
    #     if not self.used_lifelines["extra_guess"]:
    #         self.used_lifelines["extra_guess"] = True
    #         return True
    #     return False
    #
    # def lifeline_skip_question(self):
    #     """Used to skip the current question."""
    #     if not self.used_lifelines["skip"]:
    #         self.used_lifelines["skip"] = True
    #         self.questions += 1
    #         return True
    #     return False


def run_new_game(session):
    name: str = input("Kirjoita nimesi: ")
    category: str = select_category(session)

    game = Game(name, category)
    game.get_questions_and_answers()

    while game.question_count > 0:
        game.run_question()
        game.question_count = game.question_count - 1

    print("_"*30)
    print(f"Peli päättyi! Lopulliset pisteesi ovat {game.score}!\n")

    # End game and save score to leaderboard
    stmt_scheck = select(Score).where(Score.name == game.name)
    existing_entry = session.execute(stmt_scheck).scalar_one_or_none()

    if existing_entry:
        if game.score > existing_entry.score:
            existing_entry.score = game.score

    else:
        add_to_leaderboard = Score(
            name=game.name,
            score=game.score
        )
        session.add(add_to_leaderboard)

    session.commit()


def select_category(session) -> str:
    query = select(Question.category).distinct()
    categories = session.execute(query).scalars().all()

    options = list(categories)

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
