from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Fire Engineering Platform"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER: str

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()