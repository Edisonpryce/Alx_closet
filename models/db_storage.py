from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from tables import Base
from tables import User, Product, Cart, Order

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

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ This commits changes to the database"""
        self.__session.commit()


    def reload(self):
        """Creation and reloads of data into the database"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session

db = DBStorage()
db.reload()
customer4 = User(id='44', username="Mr asare", email="Yoooooo@ndnnd ", password="ddjdjjdjd", telephone=10088282)
db.new(customer4)
db.save()