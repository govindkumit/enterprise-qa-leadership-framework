import os
import requests

BASE_URL = os.getenv("BASE_URL", "https://httpbin.org")


def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/status/200", timeout=10)
    assert response.status_code == 200
