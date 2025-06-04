from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///movie_db.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)

    def __repr__(self):
        return f"<Movie(movie_title={self.movie_title}, genre={self.genre})>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)

"""
    first_movie = Movie(movie_title="Terminator", genre="Action")
    print(first_movie.movie_title)
    print(first_movie.id)
    session.add(first_movie)
    print(session.new)
"""
