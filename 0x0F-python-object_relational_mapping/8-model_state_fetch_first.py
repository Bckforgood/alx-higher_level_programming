#!/usr/bin/python3
""" This script prints the first state from the
database using ORM syntax"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    s = session.query(State).first()
    if s:
        print("{}: {}".format(s.id, s.name))
    else:
        print("Nothing")
