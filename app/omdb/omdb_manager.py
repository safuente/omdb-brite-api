import os
import re
from aiohttp.client import ClientSession
import asyncio
from db.movie import MovieDb
from sqlalchemy.orm import Session
from models.movie import Movie


class OmdbManager:

    _session = None

    def __init__(self, db=None):
        self.api_key = os.getenv("API_KEY", )
        self.db = db
        self.type = "movie"

    @property
    def session(self):
        if self._session is None:
            self._session = ClientSession()
        return self._session

    async def close(self) -> None:
        await self._session.close()

    async def get_movie(self, url):
        async with self.session.get(url) as resp:
            movie = await resp.json()
            return movie

    def camel_to_snake(self, name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    async def get_movies(self):
        tasks = []
        for number in range(128000, 129000):
            url = f'http://www.omdbapi.com/?i=tt00{number}&?type={self.type}&apikey={self.api_key}'

            tasks.append(asyncio.ensure_future(self.get_movie(url)))

        movies = await asyncio.gather(*tasks)
        await self.close()

        movies_inserted = 0

        for movie in movies:
            if movies_inserted >= 100:
                break
            if movie.get('Type') == 'movie':
                movies_inserted += 1
                mdb = MovieDb(self.db)
                movie = {self.camel_to_snake(k): v for k, v in movie.items()}
                movie_db = Movie(**movie)
                mdb.create_movie(movie_db)
                #print(movie)


    def run(self):
        asyncio.run(self.get_movies())





