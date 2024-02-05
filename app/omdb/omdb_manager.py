import os
import aiohttp
import asyncio


class OmdbManager:

    _session = None

    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    @property
    def session(self):
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self) -> None:
        await self._session.close()

    async def get_movie(self, url):
        async with self.session.get(url) as resp:
            movie = await resp.json()
            return movie

    async def get_movies(self):
        tasks = []
        for number in range(128000, 128100):
            url = f'http://www.omdbapi.com/?i=tt00{number}&apikey={self.api_key}'
            tasks.append(asyncio.ensure_future(self.get_movie(url)))

        movies = await asyncio.gather(*tasks)
        for movie in movies:
            print(movie)
        await self.close()

    def run(self):
        asyncio.run(self.get_movies())

om = OmdbManager()
om.run()


