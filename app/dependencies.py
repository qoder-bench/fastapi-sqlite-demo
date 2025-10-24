from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.infra.db import get_async_session
from app.domain.repository.hero_repo import HeroRepository


async def get_hero_repo(
    async_session: AsyncSession = Depends(get_async_session),
) -> HeroRepository:
    return HeroRepository(async_session=async_session)
