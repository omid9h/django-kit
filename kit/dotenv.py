from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class DotEnv(BaseSettings):
    debug_mode: bool
    secret_key: str

    db_host: str
    db_name: str
    db_user: str
    db_pass: str
    disable_server_side_cursors: bool

    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_file_encoding="utf-8",
    )


@lru_cache()
def new_dotenv() -> DotEnv:
    return DotEnv()  # type: ignore
