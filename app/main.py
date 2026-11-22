from fastapi import FastAPI
from app.database.database import Base, engine

def create_app():
    app = FastAPI(
        title="Blackened Camisetas API",
        version="0.1.0",
    )
    Base.metadata.create_all(bind=engine)

    @app.get("/",)
    async def root() -> dict:
        return { "message": "Bienvenidos a la API de Blackened" }

    # Endpoints

    return app




