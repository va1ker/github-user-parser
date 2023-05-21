from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "users.sqlite"

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
