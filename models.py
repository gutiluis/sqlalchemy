from sqlalchemy import create_engine, Column, Integer, String

# create a model with table name and column names
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///users.db", echo=True)
# regarding the model. next step after creating a model
# how to make a variable? is Base. as a python class
Base = declarative_base() # map the class to the database
# pass the base class Base to the model class declared



class User(Base):
    __tablename__ = "users"

# first column. primary_key each entry has unique ID number
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"


if __name__ == "__main__":
    Base.metadata.create_all(engine) # connect engine with model class to create db table