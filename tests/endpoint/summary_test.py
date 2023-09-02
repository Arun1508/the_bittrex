from fastapi.testclient import TestClient

from main import app


def test_summary():
    with TestClient(app) as client:
        response = client.get(
            "/summary", headers={"Authorization": "Basic YWRtaW46QWRtaW5AMTIzIQ=="}
        )
        assert response.status_code == 200
