from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class GetLastDetectionDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True  # позволяет использовать snake_case при инициализации
    )

    id: str
    timestamp: datetime

    model_type: str
    model_conf: float
    bbox: list[float]
