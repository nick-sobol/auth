from sqlalchemy import Table, Column, Integer, String, MetaData
from database import get_engine, get_engine


metadata = MetaData()

User = Table('users', metadata,
             Column('id', Integer, primary_key=True),
             Column('username', String(32), unique=True, nullable=False),
             Column('password', String(32), nullable=False))


async def get_user(username):
    engine = await get_engine()

    async with engine.acquire() as conn:
        result = await conn.execute(
            User.select().where(User.c.username == username)
        )

        user = await result.first()

        return dict(user) if user else None


User.get_user = get_user