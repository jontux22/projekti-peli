from sqlalchemy import insert
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

# TODO: Pelikoodi tähän
running = True

while running:
    if not run_main_menu(session):  # Annetaan session mukaan
        running = False

# Close session
session.close()
