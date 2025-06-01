from datetime import datetime, timedelta, timezone

from src.shared.api.mongo_db import AsyncMongoDBClient, MongoManager

from src.shared.api.logger import Logger


logger = Logger


from .dto import GetLastDetectionDTO


class GetLastDetectionService:

    def __init__(self, mongo_manager: MongoManager):
        self._mongo_manager = mongo_manager

    async def get_last_detection(self) -> GetLastDetectionDTO | None:

        async with self._mongo_manager.get_collection("DetectionResult") as collection:

            result = await collection.find_one(sort=[("timestamp", -1)])

            if result is None:
                return None

            return GetLastDetectionDTO(
                id=str(result["_id"]),
                timestamp=result["timestamp"],
                model_type=result["modelType"],
                model_conf=result["modelConf"],
                bbox=result["bbox"],
            )
