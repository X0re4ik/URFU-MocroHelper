from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class GetServerInfoDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    server_name: str
    detection_model: str
    classification_model: str
    gpu: str
    latency: float
    fps: float
