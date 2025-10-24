from fastapi import APIRouter, Depends

from app.dependencies import get_hero_repo
from app.domain.repository.hero_repo import HeroRepository

router = APIRouter()


@router.get("/heros", tags=["hero"])
async def read_users(
    agent_repo: HeroRepository = Depends(get_hero_repo),
):
    return await agent_repo.get_all_hero()
