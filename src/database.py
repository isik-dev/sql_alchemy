import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text

from config import settings


# creating synchronous engine
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,  # all queries will be logged into the console
    pool_size=5,
    max_overflow=10,  # additional conns to the default 5 conns
)

# creating asynchronous engine
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,  # all queries will be logged into the console
    pool_size=5,
    max_overflow=10,  # additional conns to the default 5 conns
)
