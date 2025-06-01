from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict, Field
from dotenv import load_dotenv

load_dotenv()


class BaseConfig(BaseSettings):
    """ """

    model_config = SettingsConfigDict(
        extra="allow", env_file=".env", env_file_encoding="utf-8"
    )


class APPConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="APP_")

    develop: bool = Field(default=False)
    logger_level: str = Field(default="INFO")


class MongoDBConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="MONGO_DB_")

    user: str
    password: str
    host: str
    port: int
    name: str

    @property
    def URI(self) -> str:
        return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/"


class Settings(BaseConfig):
    app: APPConfig = Field(default_factory=APPConfig)
    mongo_db: MongoDBConfig = Field(default_factory=MongoDBConfig)
