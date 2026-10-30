"""Pruebas del endpoint que indica si la API responde."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_ok() -> None:
    """El endpoint debe responder con éxito y con el contrato JSON acordado."""
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {"status": "ok"}
