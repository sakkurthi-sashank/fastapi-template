from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = ""
    database_port: str = ""
    database_password: str = ""
    database_name: str = ""
    database_username: str = ""

    port: int = 8000
    host: str = "0.0.0.0"

    class Config:
        env_file = ".env"


settings = Settings()
