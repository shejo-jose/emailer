"""Project settings.
Make sure you have a .env file in the root of the project.
"""

import urllib.parse
from pydantic_settings import BaseSettings, SettingsConfigDict

class Configurations(BaseSettings):
    """Project Settings"""

    api_prefix: str
    sender_email: str
    sender_password: str

    model_config = SettingsConfigDict(
        env_prefix="", env_file=".env", env_file_encoding="utf-8", extra="allow"
    )

config = Configurations()