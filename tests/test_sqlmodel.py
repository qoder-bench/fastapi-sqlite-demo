import pytest
from sqlalchemy.orm import sessionmaker
from sqlmodel import select

from app.domain.models import Hero
from app.domain.infra.db import async_engine
from sqlmodel.ext.asyncio.session import AsyncSession


# noinspection PyTypeChecker
@pytest.fixture(scope="function")
async def async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


@pytest.mark.asyncio
async def test_hello(async_session: AsyncSession):
    statement = select(Hero)
    result = await async_session.exec(statement)
    print(result.all())
