import os
from datetime import datetime

import requests


class AccuWeather:
    def __init__(self):
        self.__accu_base_url = os.getenv('ACCU_BASE_URL')
        self.__accu_api_key = os.getenv('ACCU_API_KEY')

    def request_climate_condition(self, city_code: int, from_days: int = 5) -> dict:
        url = (
            f'{self.__accu_base_url}/forecasts/v1/daily/{from_days}day/{city_code}?'
            f'apikey={self.__accu_api_key}'
            f'&details=true'
        )
        response = requests.request(method='GET', url=url)
        return response.json()

    @staticmethod
    def get_days_infos(daily_forecasts_list: list[dict]) -> list[dict]:
        days_infos_list = []
        for day in daily_forecasts_list:
            day_infos = {
                "date": datetime.fromisoformat(day['Date']).date(),
                "maximum_value": day['Temperature']['Maximum']['Value'],
                "day_rain_probability": day['Day']['RainProbability'],
                "day_snow_probability": day['Day']['SnowProbability'],
                "day_ice_probability": day['Day']['IceProbability'],
                "night_rain_probability": day['Night']['RainProbability'],
                "night_snow_probability": day['Night']['SnowProbability'],
                "night_ice_probability": day['Night']['IceProbability'],
            }
            days_infos_list.append(day_infos)

        return days_infos_list
