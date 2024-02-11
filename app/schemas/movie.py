from pydantic import BaseModel
from typing import Optional


class Rating(BaseModel):
    source: str
    value: str


class MovieGet(BaseModel):
    id: int
    title: str
    year: str
    rated: str
    runtime: str
    released: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str
    language: str
    country: str
    awards: str
    poster: str
    ratings: Optional[list[Rating]]
    metascore: str
    imdb_rating: str
    imdb_votes: str
    imdb_id: str
    type: str
    dvd: str
    box_office: str
    production: str
    website: str
    response: str
