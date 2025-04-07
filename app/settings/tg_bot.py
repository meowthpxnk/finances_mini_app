from pydantic import Field
from pydantic_settings import BaseSettings


class TGBotSettings(BaseSettings):
    token: str = Field(None, alias="TG_BOT_TOKEN")
    admin_id: int = Field(None, alias="TG_ADMIN_ID")
