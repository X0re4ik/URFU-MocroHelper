from datetime import datetime, timedelta, timezone

from src.shared.api.mongo_db import AsyncMongoDBClient, MongoManager

from src.shared.api.logger import Logger


logger = Logger


from .dto import GetServerInfoDTO


class GetServerInfoService:

    async def get_server_info(self) -> GetServerInfoDTO:
        return GetServerInfoDTO(
            server_name="4t2t482t3874t32",
            detection_model="Yolo",
            classification_model="Mobi",
            gpu="GPU",
            latency=120,
            fps=25,
        )
