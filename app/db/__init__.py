from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable

# engine variable manages overall connection to database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#session variable generates temporary connections for performing create, read, update, and delete operations
Session = sessionmaker(bind=engine)
# base variable helps us map the models to real MySQL tables
Base = declarative_base()
