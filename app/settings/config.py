from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "DDD Secunda TZ"
    environment: str = "local"
    debug: bool = True

    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_pass: str

    rabbitmq_url: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
