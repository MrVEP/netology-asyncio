import sqlalchemy
import asyncio
from databases import Database
from sqlalchemy import Table, Column, Integer, String, MetaData
from main import characters, get_films, get_info, get_home_info

database = Database('postgresql://async_user:netology@127.0.0.1:5432/netology_async')
metadata = MetaData()

heroes = Table(
        'heroes',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('birth_year', String),
        Column('eye_color', String),
        Column('films', String),
        Column('gender', String),
        Column('hair_color', String),
        Column('height', String),
        Column('homeworld', String),
        Column('mass', String),
        Column('name', String),
        Column('skin_color', String),
        Column('species', String),
        Column('starships', String),
        Column('vehicles', String)
)

engine = sqlalchemy.create_engine('postgresql://async_user:netology@127.0.0.1:5432/netology_async')
metadata.create_all(engine)


async def main():
    await database.connect()

    for person in characters:
        query = heroes.insert()
        kino = await get_films(person['films'])
        if person['species']:
            race = await get_info(person['species'])
        else:
            race = ''
        if person['starships']:
            space_transport = await get_info(person['starships'])
        else:
            space_transport = ''
        if person['vehicles']:
            not_space_transport = await get_info(person['vehicles'])
        else:
            not_space_transport = ''
        if person['homeworld']:
            home = await get_home_info(person['homeworld'])
        else:
            home = ''
        values = {
            'id': int(person['url'].split('/')[-2]),
            'birth_year': person['birth_year'],
            'eye_color': person['eye_color'],
            'films': ', '.join(kino),
            'gender': person['gender'],
            'hair_color': person['hair_color'],
            'height': person['height'],
            'homeworld': home,
            'mass': person['mass'],
            'name': person['name'],
            'skin_color': person['skin_color'],
            'species': ', '.join(race),
            'starships': ', '.join(space_transport),
            'vehicles': ', '.join(not_space_transport),
        }
        await database.execute(query=query, values=values)

    await database.disconnect()

asyncio.run(main())





