import aiohttp
import asyncio

URL = 'https://swapi.dev/api/people/'


async def main(url):
    async with aiohttp.ClientSession() as session:
        people = []
        num = 1
        while True:
            async with session.get(url+f'?page={num}', ssl=False) as resp:
                text = await resp.json()
                results = text['results']
                people += results
                if text['next'] is None:
                    break
                num += 1
        return people


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
characters = asyncio.run(main(URL))


async def get_films(films):
    movies = []
    for film in films:
        async with aiohttp.ClientSession() as session:
            async with session.get(film, ssl=False) as resp:
                text = await resp.json()
                movie = text['title']
                movies.append(movie)
    return movies


async def get_info(links):
    names = []
    for link in links:
        async with aiohttp.ClientSession() as session:
            async with session.get(link, ssl=False) as resp:
                text = await resp.json()
                name = text['name']
                names.append(name)
    return names


async def get_home_info(planet):
    async with aiohttp.ClientSession() as session:
        async with session.get(planet, ssl=False) as resp:
            text = await resp.json()
            name = text['name']
    return name


if __name__ == '__main__':
    print(characters[0]['films'])
