from aiopg.sa import create_engine

from config import DB_URL


async def get_engine():
    engine = await create_engine(DB_URL)

    return engine

