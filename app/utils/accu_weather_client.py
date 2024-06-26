import os
import requests


class AccuWeather:

    def get_climate_from_5_days(self, city_code: int) -> dict:
        url = (f""
               f"{os.getenv('ACCU_BASE_URL')}/forecasts/v1/daily/5day/{city_code}?"
               f"apikey={os.getenv('API_KEY')}&details=true"
               )
        response = requests.request(method="GET", url=url)
        return response.json()
