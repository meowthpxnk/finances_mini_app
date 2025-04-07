from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .api import ApiSettings
from .database import DatabaseSettings
from .logger import LoggerSettings
from .redis import RedisSettings
from .tg_bot import TGBotSettings


load_dotenv()


class Settings(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()
    logger: LoggerSettings = LoggerSettings()
    api: ApiSettings = ApiSettings()
    redis: RedisSettings = RedisSettings()
    tg_bot: TGBotSettings = TGBotSettings()
