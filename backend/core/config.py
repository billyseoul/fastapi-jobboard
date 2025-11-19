import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

class Settings:
    PROJECT_TITLE: str ="Job Board"
    PROJECT_VERSION: str ="0.1.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db_course")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()