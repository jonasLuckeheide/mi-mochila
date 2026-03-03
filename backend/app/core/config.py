import os
from pydantic import AnyHttpUrl
from typing import List

class Settings:
    PROJECT_NAME: str = "Mi Mochila API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mimochila")
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

settings = Settings()
