import logging

from app.utils.accu_weather import AccuWeather


logger = logging.Logger(__name__)


class ClimateService:
    def __init__(self):
        self._accu_weather = AccuWeather()

    def check_climate_conditions(self, city_code: int) -> dict:
        try:
            logger.info(f"Initial check climate conditions from city code {city_code}")
            result_payload = self._accu_weather.request_climate_condition(city_code=city_code)
            days_details_list = self._accu_weather.get_days_infos(daily_forecasts_list=result_payload['DailyForecasts'])
            forecast = {"forecasts": []}
            for day_details in days_details_list:
                clothes = self._match_clothes_for_climate(day_details=day_details)
                formatted_forecast = {
                    "date": day_details['date'],
                    'clothes': clothes
                }
                forecast['forecasts'].append(formatted_forecast)

            return forecast
        except Exception as err:
            logger.debug(f"Failed check climate conditions. Error: {err}")
            raise err

    def _match_clothes_for_climate(self, day_details: dict) -> list:
        temperature = day_details['maximum_value']
        day_rain_prob = day_details['day_rain_probability']
        night_rain_prob = day_details['night_rain_probability']
        day_snow_prob = day_details['day_snow_probability']
        night_snow_prob = day_details['night_snow_probability']
        day_ice_prob = day_details['day_ice_probability']
        night_ice_prob = day_details['night_ice_probability']

        clothes = []
        if temperature < 45:
            clothes.append("Coat")
            clothes.append("Winter jacket")
        elif 45 <= temperature <= 79:
            clothes.append("Fleece")
            clothes.append("Short Sleeves")
        elif temperature >= 80:
            clothes.append("Shorts")

        if day_rain_prob > 50 or night_rain_prob > 50:
            clothes.append("Rain Coat")

        if day_snow_prob > 50 or night_snow_prob > 50:
            clothes.append("Snow Outfit")

        if day_ice_prob > 50 or night_ice_prob > 50:
            clothes.append("Shell Jacket")

        return clothes
