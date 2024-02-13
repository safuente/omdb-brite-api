from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from models.movie import Movie
from exceptions import HTTPCustomException, my_http_exception_handler



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
        movie_in_db = self.db.query(Movie).filter(Movie.id==id)
        if not movie_in_db.first():
            raise HTTPCustomException(
                status_code=404,
                detail=f"Could not find a movie with id {id}"
            )
        movie = movie_in_db.first()
        return movie

    def delete_movie(self, id):
        movie_in_db = self.db.query(Movie).filter(Movie.id == id)
        if not movie_in_db.first():
            raise HTTPCustomException(
                status_code=404,
                detail=f"Could not find a movie with id {id}"
            )
        movie_in_db.delete()
        self.db.commit()
        raise HTTPCustomException(
            status_code=204
        )





