from main import get_temperature
import pytest
from unittest.mock import patch


temperature_tests = [
    [62, -14.235004, -51.92528, 16],
    [77.67, -20.235004, -30.92528, 25],
    [-72.33, -76.2350, 120.92528, -57],
]

type_error_tests = [
    ['strrr', -51.92528],
    [-14.235004, 'sdfsdf'],
    [b'efsdfsd', False],
]

value_error_tests = [
    [90.1, 12],
    [1, 181],
    [100, 210],
]


''' Esse método abaixo é menos verboso mas não consegui fazer rodar com o
    @pytest.mark.parametrize para testar vários dados ao mesmo tempo '''

# @patch('main.requests.get')
# def test_get_temperature_by_lat_lng(mock_get):
#     mock_get.return_value.json.return_value = {'currently': {'temperature': temperature}}
#     result = get_temperature(lat, lng)
#     assert result == expected


@pytest.mark.parametrize('temperature, lat, lng, expected', temperature_tests)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):
    mock_get_patcher = patch('main.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.json.return_value = {'currently': {'temperature': temperature}}
    result = get_temperature(lat, lng)
    mock_get_patcher.stop()

    assert result == expected


@pytest.mark.parametrize('lat, lng', type_error_tests)
def test_type_error_lat_lng(lat, lng):
    with pytest.raises(TypeError):
        get_temperature(lat, lng)


@pytest.mark.parametrize('lat, lng', value_error_tests)
def test_value_error_lat_lng(lat, lng):
    with pytest.raises(ValueError):
        get_temperature(lat, lng)
