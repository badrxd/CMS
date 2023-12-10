""" database connection """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel

classes = {
    "BaseModel": BaseModel
}


class DBStorage:
    """interaacts with the PostgreSQL database"""
    __engine = None
    __session = None

    def __init__(self):
        db_url = "postgresql://admin:admin@127.0.0.1:5432/cms"
        self.__engine = create_engine(db_url)

    def all(self):
        """query on the current database session"""
        new_dict = {}
        objs = self.__session.query(BaseModel).all()
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
