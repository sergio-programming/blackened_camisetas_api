from fastapi import FastAPI


app = FastAPI(
    title="Blackened Camisetas API",
    version="0.1.0",
)


@app.get("/",)
async def root() -> dict:
    return { "message": "Bienvenidos a la API de Blackened" }
