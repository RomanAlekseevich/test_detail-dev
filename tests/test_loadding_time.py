import time
import requests


def test_loading_time(url):
    start = time.time()
    response = requests.get(url)
    assert response.status_code == 200, "Код 200 не получен"
    finish = time.time()
    assert round(finish - start, 2) < 3,  "Время ожедания ответа привышено"