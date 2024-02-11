from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from models.movie import Movie


class MovieDb:

    def __init__(self, db:Session):
        self.db = db

    def create_movie(self, movie: Movie):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def list_movies(self):
        movies = self.db.query(Movie).order_by('title').filter()
        return movies

    def get_movie(self, id):
        movie = self.db.query(Movie).filter(Movie.id==id).first()
        return movie