#!/usr/bin/python3
"""
Add the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Set up connection to the database
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db_name), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name='Louisiana')

    # Add State object to the session
    session.add(new_state)

    # Commit changes to the database and print new state id
    session.commit()
    print(new_state.id)
