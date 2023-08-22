from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class DotEnv(BaseSettings):
    secret_key: str
    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_file_encoding="utf-8",
    )


@lru_cache()
def new_dotenv() -> DotEnv:
    return DotEnv()  # type: ignore
