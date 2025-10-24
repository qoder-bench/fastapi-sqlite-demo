import dotenv
from fastapi import FastAPI

from .routers import heros

dotenv.load_dotenv()

app = FastAPI(
    title="FastAPI SQLite demo",
    description="FastAPI SQLite demo",
    version="0.0.1",
    contact={
        "name": "linux_china",
    },
)

app.include_router(heros.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
