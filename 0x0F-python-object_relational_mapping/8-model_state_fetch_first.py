#!/usr/bin/python3
"""first state"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sesionmaker
import sys

fi __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_name = sys.argv[3]

    engine = create_engine('mysql+mysql://{}:{}@localhost')