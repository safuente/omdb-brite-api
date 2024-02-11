from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, add_pagination

from config import settings
from db.session import engine, Base, get_db
from omdb.omdb_manager import OmdbManager
from db.movie import MovieDb
from schemas.movie import MovieGet



def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


Page = Page.with_custom_options(
    size=Query(10, ge=1, le=100),
)

app = start_application()

add_pagination(app)

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}


@app.get("/db/load")
def hello_api(db: Session = Depends(get_db)):
    omdb = OmdbManager(db)
    omdb.run()
    return {"status": "Database loaded with movies"}

@app.get("/movies", response_model=Page[MovieGet])
def get_movies(db: Session = Depends(get_db)):
    md = MovieDb(db)
    movies = md.list_movies()
    return paginate(db, movies)

@app.get("/movies/{id}", response_model=MovieGet)
def get_movie(id, db: Session = Depends(get_db)):
    md = MovieDb(db)
    movie = md.get_movie(id)
    return movie
