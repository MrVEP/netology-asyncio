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

if __name__ == '__main__':

    print(characters[0]['name'])
