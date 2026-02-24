from sqlalchemy.orm import sessionmaker

from src.database.db import engine
from src.database.models.base import Base

from src.game.main_menu import run_main_menu


# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# TODO: Pelikoodi tähän
running = True

while running:
    if not run_main_menu():
        running = False

# Close session
session.close()
