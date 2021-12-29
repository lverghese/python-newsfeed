from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to database using env variable

# engine variable manages overall connection to database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#session variable generates temporary connections for performing create, read, update, and delete operations
Session = sessionmaker(bind=engine)
# base variable helps us map the models to real MySQL tables
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    # with this, Flask will run close_db and this so connections do not remain open 
    app.teardown_appcontext(close_db)

# whenever this is called it returns a new session-connection object
def get_db():
    if 'db' not in g:
        #store db connection in app context
        g.db = Session()
    return g.db

def close_db(e=None):
    #pop method attempts to find and remove db from g object. 
    # if db exists (if db does not equal None), then db_close will end the connection
    db = g.pop('db', None)

    if db is not None:
        db.close()