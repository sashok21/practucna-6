from fastapi import FastAPI

from contextlib import asynccontextmanager
from core.models.base import BaseModel
from core.settings.db import Database

from routers import products
from routers import users
from routers import brands
from routers import categories
from routers import orders
from routers import order_items

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
db = Database(url=DATABASE_URL)

@asynccontextmanager
async def lifespan(_fastapi_app: FastAPI):
    print("Database connecting...")
    await db.connect()
    async with db.engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)
    print("Database connected and tables created.")
    yield
    print("Database disconnecting...")
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

# Включення всіх маршрутизаторів один раз
app.include_router(products.router)
app.include_router(users.router)
app.include_router(brands.router)
app.include_router(categories.router)
app.include_router(orders.router)
app.include_router(order_items.router)