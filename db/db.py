from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sqlalchemy.orm import sessionmaker, declarative_base, Session

load_dotenv()
db_url = os.getenv("DB_URL")

engine = create_engine(db_url)
SessionLocal = sessionmaker(engine)
Base = declarative_base()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
