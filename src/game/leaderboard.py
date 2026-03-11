from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from src.database.models import Score


def run_leaderboard(session: Session, limit=10):
    stmt = (
            select(Score)
            .order_by(desc(Score.score))
            .limit(limit)
        )

    results = session.execute(stmt).scalars().all()

    print("\n" + "="*30)
    print(f"{"SIJA":<5} {'PELAAJA':<15} {'PISTEET':<10}")
    print("-"*30)

    if not results:
        print('Ei tuloksia tietokannassa.')
    else:
        for i, entry in enumerate(results, start=1):
            print(f"{i:<5} {entry.name:<15} {entry.score:<10}")

    print("="*30 + "\n")
