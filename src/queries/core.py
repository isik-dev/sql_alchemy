from sqlalchemy import text

from src.database import sync_engine, async_engine
from src.models import metadata_obj


# diff between engine.connect and engine.begin
# -> begin autocommits everything on session exist
# -> connect rolls back, hence you have to explicitely write conn.commit
def get_version_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))

        print(f"{res.first()=}")
        conn.commit()


async def get_version_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))

        print(f"{res.first()=}")
        await conn.commit()


def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


def insert_data():
    with sync_engine.connect() as conn:
        conn.execute(
            text(
                """
                insert into
                    workers (username)
                values
                    ('Mike Tyson'),
                    ('Muhammad Ali'),
                    ('Floyd Mayweather');
                """
            )
        )
