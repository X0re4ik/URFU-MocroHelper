from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

from src.shared.configs import PROJECT_SETTINGS


class MongoManager:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    @asynccontextmanager
    async def get_collection(self, collection_name: str):
        """Контекстный менеджер для работы с коллекцией MongoDB."""
        try:
            self.client = AsyncIOMotorClient(self.uri)
            self.db = self.client[self.db_name]
            collection = self.db[collection_name]
            yield collection  # Передаем коллекцию в контекст
        finally:
            # Закрываем соединение с MongoDB, когда контекст завершен
            if self.client:
                self.client.close()


AsyncMongoDBClient = MongoManager(
    PROJECT_SETTINGS.mongo_db.URI,
    PROJECT_SETTINGS.mongo_db.name,
)
