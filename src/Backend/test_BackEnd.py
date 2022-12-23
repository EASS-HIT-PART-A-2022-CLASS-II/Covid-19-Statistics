
from .BackEnd import *


def test_specificCountry():
    response = specicif_country("Canada")
    assert response.Message == "OK"
    assert response.Country == "USA" # example for false test
