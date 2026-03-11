import ast
import csv
import logging

from sqlalchemy import insert, delete, select
from unicodedata import category

from sqlalchemy.orm import sessionmaker

from src.database.db import engine
from src.database.models import Question, Answer, Score
from src.database.models.base import Base

from src.game.main_menu import run_main_menu


# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Disable logging
logging.getLogger('sqlalchemy.engine.Engine').disabled = True


# Testidatan lisäys
# questions = [
#     Question(question="Onko tämä testikysymys?", difficulty=2, category="Yleinen", answers=[
#         Answer(answer="Testivastaus 1", correct=False),
#         Answer(answer="Testivastaus 2", correct=False),
#         Answer(answer="Testivastaus 3", correct=True),
#         Answer(answer="Testivastaus 4", correct=False),
#     ]),
#     Question(question="Onko tämä toinen testikysymys?", difficulty=3, category="Yleinen", answers=[
#         Answer(answer="Toinen vastaus 1", correct=True),
#         Answer(answer="Toinen vastaus 2", correct=False),
#         Answer(answer="Toinen vastaus 3", correct=False),
#         Answer(answer="Toinen vastaus 4", correct=False),
#     ])
# ]
#
# session.add_all(questions)
# session.commit()

# Vibekoodattu importteri :)
# def import_questions_from_csv(
#     session: Session,
#     questions_csv_path: str,
#     answers_csv_path: str,
# ):
#     session.execute(delete(Answer))
#     session.execute(delete(Question))
#     session.commit()
#
#     questions = []
#     with open(questions_csv_path, newline="", encoding="cp1252") as file:
#         reader = csv.reader(file, delimiter=";")
#
#         for row in reader:
#             question = Question(
#                 id=int(row[0]),
#                 question=row[1],
#                 difficulty=int(row[2]),
#                 category=row[3],
#             )
#             questions.append(question)
#
#     session.add_all(questions)
#     session.commit()
#
#     answers = []
#     with open(answers_csv_path, newline="", encoding="utf-8-sig") as file:
#         reader = csv.reader(file, delimiter=";")
#
#         for row in reader:
#             answer = Answer(
#                 id=int(row[0]),
#                 answer=row[1],
#                 correct=row[2].strip().lower() in ("true", "1", "yes"),
#                 question_id=int(row[3]),
#             )
#             answers.append(answer)
#
#     session.add_all(answers)
#     session.commit()
#
#
# import_questions_from_csv(session,
#                           "C:/Users/kalle/PycharmProjects/projekti-peli/data/tietovisapeli_kysymykset.csv",
#                           "C:/Users/kalle/PycharmProjects/projekti-peli/data/tietovisapeli_vastaus.csv")

# TODO: Pelikoodi tähän
running = True

while running:
    if not run_main_menu(session):  # Annetaan session mukaan
        running = False

# Close session
session.close()
