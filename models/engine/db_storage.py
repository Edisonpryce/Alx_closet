from sqlalchemy import create_engine

class DBStorage:
    __engine = None

    # Interacting with the actual database
    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = 'root'
        MYSQL_PWD = 'Password@5756'
        MYSQL_HOST = 'localhost'
        MYSQL_DB= 'AlxCloset'
        self.__engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}')