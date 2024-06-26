class ConditionClimateService:
    def __init__(self, accu_weather: Any):
        self._accu_weather_client = AccuWeather()

