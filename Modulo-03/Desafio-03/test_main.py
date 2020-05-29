from main import get_temperature
import pytest
from unittest.mock import patch

# Parâmetros passados pelos decorator parametrize para serem testatos
test_parameters = [
    (53.3, -22.469910, -43.177092, 11),  # Petrópolis - RJ
    (65.69, -27.600526, -48.510145, 18),  # Florianópolis - SC
    (68.55, -15.794906, -47.882278, 20),  # Brasília - DF
    (83.1, -3.731859, -38.529593, 28),  # Fortaleza - CE
    (46.62, 61.800948, 7.690592, 8),  # Breheimen - Noruega
    (-73.91, -75.079231, 123.245337, -58)  # Base Concordia - Antartica
]


@pytest.mark.parametrize("temperature, lat, lng, expected", test_parameters)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):

    # Utilizando o patch() como Context Manager. Simula a requisição "requests.get" realizada
    # na variável "response" do arquivo "main.py"
    with patch('main.requests.get') as mock_requests:
        # Simula a estrutu de dados json da api darksky
        data_test = {
            "currently": {
                "temperature": temperature
            }
        }

        # Faz a busca com a versão patched da "main.request.get" nos dados de teste
        mock_requests.return_value.json.return_value = data_test
        test = get_temperature(lat, lng)
        assert test == expected
