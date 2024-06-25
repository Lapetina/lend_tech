import logging

from fastapi import APIRouter
from fastapi import status as response_status
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from fastapi.encoders import jsonable_encoder
from fastapi_utils.inferring_router import InferringRouter
from app.service.climate_condition import ClimateService

logger = logging.Logger(__name__)
router = APIRouter()
climate_router = InferringRouter()


@cbv(climate_router)
class ClimateConditionRouter:
    def __init__(self):
        self._climate_service = ClimateService()

    @climate_router.get("/check-conditions", status_code=response_status.HTTP_200_OK)
    async def check_climate_conditions(self, city_code: int):
        try:
            result = self._climate_service.check_climate_conditions(city_code=city_code)
            return JSONResponse(content=jsonable_encoder(result))
        except Exception as err:
            logger.error(f"Request Failed, error: {err}")
            return JSONResponse(
                content={"title": "Request failed", "message": f"{err}"},
                status_code=500
            )
