""" database connection """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.user import User
from models.reservation import Reservation
from models.car import Car
from models.customer import Customer
from models.revenue import Revenue
from models.settings import Settings


classes = {
    "User": User,
    "Car": Car,
    "Reservation": Reservation,
    "Reservation": Customer,
    "Revenue": Revenue,
    "Settings": Settings
}


class DBStorage:
    """interaacts with the PostgreSQL database"""
    __engine = None
    __session = None

    def __init__(self):
        db_url = "postgresql://postgres:root@127.0.0.1:5432/cms"
        self.__engine = create_engine(db_url)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls is None:
            for val in classes.values():
                objs = self.__session.query(val).order_by(
                    val.created_at.desc()).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
            return (new_dict)
        objs = self.__session.query(cls).order_by(cls.created_at.desc()).all()
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def getById(self, cls, id):
        """return a model by id"""
        data = self.__session.query(cls).filter(cls.id == id).first()
        return data

    # TODO(def getFirst(self, cls))
    # def getFirst(self, cls):
    #     """return a first by id"""
    #     data = self.__session.query(cls).order_by(
    #         cls.created_at.desc()).first()
    #     return data

    @property
    def session(self):
        return self.__session
