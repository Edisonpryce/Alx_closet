from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from db_storage import Base
class DBStorage:
    __engine = None
    __session = None

    # Interacting with the actual database
    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = 'root'
        MYSQL_PWD = 'Password@5756'
        MYSQL_HOST = 'localhost'
        MYSQL_DB= 'AlxCloset'
        self.__engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}')


    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session