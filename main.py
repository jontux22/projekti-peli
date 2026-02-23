from sqlalchemy.orm import sessionmaker

from src.database.db import engine
from src.database.models.base import Base


# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Everything else here
print("Hello world")

# TODO: Pelikoodi tähän

# Close session
session.close()
