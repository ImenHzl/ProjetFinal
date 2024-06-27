import pytest
import requests
import requests_mock
from app.api.v1.foreCast import get_weather_forecast
from fastapi import HTTPException

@pytest.fixture
def mock_weather_api():
    with requests_mock.Mocker() as m:
        mock_response = {
            "forecast": {
                "forecastday": [
                    {
                        "date": "2023-01-01",
                        "day": {
                            "avgtemp_c": 10,
                            "condition": {
                                "text": "Sunny"
                            }
                        }
                    },
                    {
                        "date": "2023-01-02",
                        "day": {
                            "avgtemp_c": 12,
                            "condition": {
                                "text": "Cloudy"
                            }
                        }
                    },
                    {
                        "date": "2023-01-03",
                        "day": {
                            "avgtemp_c": 14,
                            "condition": {
                                "text": "Rain"
                            }
                        }
                    }
                ]
            }
        }
        m.get('http://api.weatherapi.com/v1/forecast.json', json=mock_response)
        yield m

def test_get_weather_forecast(mock_weather_api):
    city = "Paris"
    days = 3

    try:
        forecast_data = get_weather_forecast(city, days)
        assert isinstance(forecast_data, list), "Les données de prévision doivent être une liste."
        assert len(forecast_data) == days, f"Le nombre de jours retournés est {len(forecast_data)}, mais {days} étaient attendus."
        for forecast in forecast_data:
            assert "date" in forecast, "Chaque prévision doit contenir une date."
            assert "day" in forecast, "Chaque prévision doit contenir des données de jour."
            assert "avgtemp_c" in forecast["day"], "Les données de jour doivent contenir la température moyenne."
            assert "condition" in forecast["day"], "Les données de jour doivent contenir les conditions météorologiques."
            assert "text" in forecast["day"]["condition"], "Les conditions météorologiques doivent contenir un texte descriptif."
    except HTTPException as e:
        pytest.fail(f"Les données météorologiques pour {city} n'ont pas pu être récupérées ({e.status_code})")
