import pytest

from app.domain.repository.hero_repo import HeroRepository


@pytest.mark.asyncio
async def test_find_csv_agents(hero_repo: HeroRepository):
    heros = await hero_repo.get_all_hero()
    print(heros)
