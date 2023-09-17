#!/usr/bin/python3
""" This script adds a city in from the state class
using the relation"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).all()
    for s in state:
        print("{}: {}".format(s.id, s.name))
        [print("\t{}: {}".format(city.id, city.name)) for city in s.cities]

    session.commit()
