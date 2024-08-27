from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.tables import Base
from models.tables import User, Product, Cart, Order

classes = {"User": User, "Product": Product, "Cart": Cart, "Order": Order}

class DBStorage:
    __engine = None
    __session = None

    # Interacting with the actual database
    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = 'edison'
        MYSQL_PWD = 'password'
        MYSQL_HOST = 'localhost'
        MYSQL_DB= 'alxcloset'
        self.__engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}')

    def all(self, cls, id=None):
        if cls and id:
            obj = self.__session.query(classes[cls]).get(id)
            obj = dict(obj)
            return obj
        else:
            users_dict = [dict(user) for user in self.__session.query(User).all()]
        return users_dict
    
    
    def save(self):
        """ This commits changes to the database"""
        self.__session.commit()


    def reload(self):
        """Creation and reloads of data into the database"""

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session