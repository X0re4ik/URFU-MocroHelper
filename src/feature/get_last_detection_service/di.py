from .service import GetLastDetectionService


from src.shared.api.mongo_db import AsyncMongoDBClient


class GetLastDetectionServiceFactory:

    @staticmethod
    def create():

        return GetLastDetectionService(
            AsyncMongoDBClient,
        )
