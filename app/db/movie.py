from sqlalchemy.orm import Session
from models.movie import Movie


class MovieDb:

    def __init__(self, db:Session):
        self.db = db

    def create_movie(self, movie: Movie):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie