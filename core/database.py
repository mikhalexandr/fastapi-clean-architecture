import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import text


engine = create_async_engine("sqlite+aiosqlite:///sqlite.db")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)





async def get_async_session():
    async with async_session_maker() as session:
        yield session
