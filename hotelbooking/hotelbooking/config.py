import yaml
from pydantic_settings import BaseSettings
from pydantic import Field
import os


class Settings(BaseSettings):
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    secret_key: str = Field(..., env="SECRET_KEY")
    debug: bool = Field(False, env="DEBUG")


def load_yaml_settings(path="hotelbooking/config.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file {path} not found!")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # Передаём ключи как есть (нижний регистр)
    return Settings(**data)


settings = load_yaml_settings()
