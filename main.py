from fastapi import FastAPI

from routers import categoria_router

app = FastAPI(
    title="Controle de Gastos API",
    version="1.0.0"
)

app.include_router(categoria_router)