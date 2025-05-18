from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from wishwise_pr.configs.database.engine import engine 

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
