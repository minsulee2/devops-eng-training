# TODO(everyone): 웹서버의 healthz가 response code 200 확인
import pytest
import requests


def test_health_check():
    response = requests.get(url="http://localhost:3000/healthz")
    assert response.status_code == 200
