import pytest
import requests
from fastapi.testclient import TestClient
from .BackEnd import app

# Test Client
client = TestClient(app)

# test for get_all_world_covid_data endpoint
def test_World_Data():
    response = client.get("/get_all_world_covid_data")
    assert response.status_code == 200
    data = response.json()
    world_data = [d for d in data if d['Country'] == 'World']
    assert len(world_data) == 1


# test for get_all_countries_covid_data endpoint
def test_All_Countries():
    response = client.get("/get_all_countries_covid_data")
    assert response.status_code == 200
    data = response.json()
    usa_data = [d for d in data if d['Country'] == 'USA']
    assert len(usa_data) == 1

# test for get_specific_country_covid_data endpoint with a country name that exists in the API
def test_specific_country_success():
    response = client.get("/get_specific_country_covid_data/USA")
    assert response.status_code == 200
    assert response.json()['Country'] == 'USA'

# test for get_specific_country_covid_data endpoint with a country name that does not exist in the API
def test_specific_country_failure():
    response = client.get("/get_specific_country_covid_data/Moon")
    assert response.status_code == 200
    assert response.json()['Message'] == 'Country not found'
