import pytest
import requests
import threading
from werkzeug.serving import make_server
from fake_server import app

@pytest.fixture(scope='session')
def setup_server():
    server = make_server('localhost', 5000, app)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    yield

    # Stop the Flask server
    server.shutdown()
    server_thread.join()

def test_people_endpoint(setup_server):
    endpoint = '/people/1/'
    expected_status = 200
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'id' in data
    assert 'name' in data
    assert 'age' in data

def test_people_endpoint_not_found(setup_server):
    endpoint = '/people/999/'
    expected_status = 404
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'error' in data

def test_planets_endpoint(setup_server):
    endpoint = '/planets/42/'
    expected_status = 200
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'id' in data
    assert 'name' in data
    assert 'population' in data

def test_planets_endpoint_not_found(setup_server):
    endpoint = '/planets/999/'
    expected_status = 404
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'error' in data

def test_starships_endpoint(setup_server):
    endpoint = '/starships/1000/'
    expected_status = 404
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'error' in data

def test_starships_endpoint_not_found(setup_server):
    endpoint = '/starships/999/'
    expected_status = 404
    url = f'http://localhost:5000{endpoint}'
    response = requests.get(url)
    assert response.status_code == expected_status
    data = response.json()
    assert 'error' in data
