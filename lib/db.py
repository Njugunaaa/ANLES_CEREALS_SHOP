# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use SQLite for simplicity
DATABASE_URL = "sqlite:///cereal.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
