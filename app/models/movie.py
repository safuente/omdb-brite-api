from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from db.session import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    year = Column(String(150), nullable=False)
    rated = Column(String(150), nullable=False)
    runtime = Column(String(150), nullable=False)
    released = Column(String(150), nullable=False)
    genre = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    writer = Column(String(250), nullable=False)
    actors = Column(String(250), nullable=False)
    plot = Column(String(2000), nullable=False)
    language = Column(String(150), nullable=False)
    country = Column(String(150), nullable=False)
    awards = Column(String(150), nullable=False)
    poster = Column(String(1000), nullable=False)
    ratings = Column(JSONB)
    metascore = Column(String(150), nullable=False)
    imdb_rating = Column(String(150), nullable=False)
    imdb_votes = Column(String(150), nullable=False)
    imdb_id = Column(String(150), nullable=False)
    type = Column(String(150), nullable=False)
    dvd = Column(String(150), nullable=False)
    box_office = Column(String(150), nullable=False)
    production = Column(String(150), nullable=False)
    website = Column(String(1000), nullable=False)
    response = Column(String(150), nullable=False)



