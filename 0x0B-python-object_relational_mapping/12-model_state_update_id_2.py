#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine. The "echo" flag is set to True to display
    # the executed SQL queries.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_name), echo=False)

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # Create a Session instance.
    session = Session()

    # Query the State object to be updated.
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State object.
    state_to_update.name = "New Mexico"

    # Commit the change to the database.
    session.commit()

    # Close the session.
    session.close()
