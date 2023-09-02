from fastapi.testclient import TestClient

from main import app


def test_market():
    with TestClient(app) as client:
        response = client.get(
            "/markets/1INCH-BTC", headers={"Authorization": "Basic YWRtaW46QWRtaW5AMTIzIQ=="}
        )
        assert response.status_code == 200


def test_invalid_market_symbol():
    with TestClient(app) as client:
        response = client.get(
            "/markets/INCH-BTC", headers={"Authorization": "Basic YWRtaW46QWRtaW5AMTIzIQ=="}
        )
        assert response.status_code == 400
