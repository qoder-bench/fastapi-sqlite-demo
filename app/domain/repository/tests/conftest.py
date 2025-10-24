import pytest_asyncio

from app.domain.infra.db import async_engine
from app.domain.repository.hero_repo import HeroRepository
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession


@pytest_asyncio.fixture(scope="function")
async def hero_repo() -> HeroRepository:
    session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with session() as async_session:
        yield HeroRepository(async_session)
