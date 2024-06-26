import asyncio
from datetime import datetime
from typing import AsyncGenerator, Optional

from fastapi import Depends
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from sqlalchemy import DateTime, NullPool, String, ForeignKey, func, inspect
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from src.core.config import settings


DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class BaseModel(DeclarativeBase):
    pass


class UserModel(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    tasks: Mapped[list['TaskModel']] = relationship(lazy="selectin")

    def __repr__(self):
        return f'UserModel(id={self.id} username={self.username} email={self.email})'


class TaskModel(BaseModel):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    completed: Mapped[bool]
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=func.now())
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    def __repr__(self):
        return (
            f'TaskModel(id={self.id} '
            f'title={self.title} '
            f'description={self.description} '
            f'completed={self.completed} '
            f'created_at={self.created_at})'
        )


# def check_database_status() -> None:
#     if not inspect(engine).has_table(TaskModel):
#         asyncio.run(init_models())


# async def database_status():
#     async with engine.begin() as conn:
#         await conn.run_sync(check_database_status())


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, UserModel)
