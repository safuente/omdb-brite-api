from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSONB
from db.session import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(String(50), primary_key=True, nullable=False)
    title = Column(String(150), nullable=False)
    year = Column(String(150), nullable=False)
    rated = Column(String(150), nullable=False)
    runtime = Column(String(150), nullable=False)
    genre = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    writer = Column(String(250), nullable=False)
    actors = Column(String(250), nullable=False)
    plot = Column(String(150), nullable=False)
    language = Column(String(150), nullable=False)
    country = Column(String(150), nullable=False)
    awards = Column(String(150), nullable=False)
    poster = Column(String(450), nullable=False)
    ratings = Column(JSONB)
    metascore = Column(String(150), nullable=False)
    imdb_rating = Column(String(150), nullable=False)
    imdb_votes = Column(String(150), nullable=False)
    imdb_id = Column(String(150), nullable=False)
    type = Column(String(150), nullable=False)
    total_seasons = Column(String(150), nullable=False)
    response = Column(String(150), nullable=False)



