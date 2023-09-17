#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

from relationship_state import Base, State
from state import Base, Address
from user import User
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)
"""
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')]
Session = sessionmaker(bind=engine)
session = Session()
session.add_all([jack, fake_user])
for u, a in session.query(User, Address).filter(User.id == Address.user_id).all():
    print(u.__dict__, a.__dict__)

#for user in session.query(User).filter(User.addresses).all():
    #print(User.__dict__)

"""
