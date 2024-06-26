from __future__ import annotations

from pydantic import BaseModel, model_validator


class Conditions(BaseModel):
    date: str
    clothes: list[str]


class ResponseClimateFrom5Days(BaseModel):
    result: list[Conditions]

    @model_validator(mode='before')
    def build(cls, data: dict) -> ResponseClimateFrom5Days:
        data_forecasts_list = data['forecasts']
        conditions_list = [Conditions(**item) for item in data_forecasts_list]
        return cls(result=conditions_list)


class DateInfos(BaseModel):
    date: str
    condition: int


class ResponseDailyForecasts(BaseModel):
    result: list[DateInfos]

    @model_validator(mode='before')
    def build(cls, data: dict) -> ResponseClimateFrom5Days:
        data_forecasts_list = data['EffectiveDate']['DailyForecasts']

        conditions_list = [Conditions(**item) for item in data_forecasts_list]
        return cls(result=conditions_list)
