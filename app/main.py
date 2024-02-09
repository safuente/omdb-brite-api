from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config import settings
from db.session import engine, Base, get_db
from omdb.omdb_manager import OmdbManager
from db.movie import MovieDb



def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}


@app.get("/db/load")
def hello_api(db: Session = Depends(get_db)):
    omdb = OmdbManager(db)
    omdb.run()
    return {"status": "Database loaded with movies"}

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    md = MovieDb(db)
    movies = md.list_movies()
    return movies