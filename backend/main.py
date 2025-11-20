from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base import Base

def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print(f"Tables created: {list(Base.metadata.tables.keys())}")

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()

@app.get("/")
def hello_api():
    return {"message": "Hello"}

