from sqlalchemy import create_engine
from models import Dog
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

engine = create_engine('sqlite:///:memory:')

def create_table(base, engine):
    sql = """
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
        );
    """
    with engine.connect() as connection:
        connection.execute(sql)

def save(session, dog):
    session.add(dog)
    session.commit()

    return session

def new_from_db(session, row):
    return session.query(Dog).filter_by(id = row.id).first()

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter_by(name = name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id = id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name = name, breed = breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return session