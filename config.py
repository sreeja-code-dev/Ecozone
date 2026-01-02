from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "recycling_mvp"

    class Config:
        env_file = ".env"

settings = Settings()