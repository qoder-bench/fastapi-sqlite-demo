from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.models import Hero


class HeroRepository:
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    async def get_all_hero(self) -> list[Hero]:
        statement = select(Hero)
        results = await self.async_session.exec(statement)
        return results.all()
