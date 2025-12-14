from sqlalchemy import text, insert

from src.database import sync_engine, async_engine
from src.models import metadata_obj, workers_table


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
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        
        stmt = insert(table=workers_table).values([
            {"username": "Bobr"},
            {"username": "Volk"}
        ])
        
        conn.execute(statement=stmt)
        conn.commit()
