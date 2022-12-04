import sqlalchemy
import asyncio
from databases import Database
from sqlalchemy import Table, Column, Integer, String, MetaData
from main import characters


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
        values = {
            'id': int(person['url'].split('/')[-2]),
            'birth_year': person['birth_year'],
            'eye_color': person['eye_color'],
            'films': ', '.join(person['films']),
            'gender': person['gender'],
            'hair_color': person['hair_color'],
            'height': person['height'],
            'homeworld': person['homeworld'],
            'mass': person['mass'],
            'name': person['name'],
            'skin_color': person['skin_color'],
            'species': ', '.join(person['species']),
            'starships': ', '.join(person['starships']),
            'vehicles': ', '.join(person['vehicles']),
        }
        await database.execute(query=query, values=values)

    await database.disconnect()

asyncio.run(main())





