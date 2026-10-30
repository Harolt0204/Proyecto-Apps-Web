"""Punto de entrada de la API."""

import os  # Fallo intencional del Workshop 6: importación sin usar.

from fastapi import FastAPI

app = FastAPI(
    title="Thesis Management API",
    description="API para gestionar el proceso de tesis y titulación de pregrado.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health() -> dict[str, str]:
    """Confirma que la API responde; todavía no comprueba la base de datos."""
    return {"status": "ok"}
