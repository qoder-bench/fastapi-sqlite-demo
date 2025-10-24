import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

ASYNC_DATABASE_URL = os.environ.get(
    "ASYNC_SQLITE3_URL", "sqlite+aiosqlite:///db/demo.sqlite3"
)


# for SQLite only
connect_args = {"check_same_thread": False}

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,
    future=True,
    connect_args=connect_args,
)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
