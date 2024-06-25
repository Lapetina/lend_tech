import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routers.climate_condition_router import climate_router

API_VERSION = "v1"


def create_app() -> FastAPI:
    app = FastAPI()
    # Configure Routers
    app.include_router(climate_router, prefix=f"/{API_VERSION}/climate", dependencies=[])

    @app.exception_handler(ValueError)
    async def value_error_exception_handler(request, exc: ValueError):
        try:
            _args = exc.args
            if _args and len(_args):
                _args = _args[0]
                if not isinstance(_args, dict):
                    _args = {"message": "Campos informados inválidos!"}
            else:
                _args = {"message": "Campos informados inválidos!"}
            message = _args.get("message")
            return JSONResponse(
                status_code=400,
                content={"title": "Campos inválidos", "message": message},
            )
        except Exception:
            return JSONResponse(
                status_code=400,
                content={"title": "Campos inválidos", "message": "Campos informados inválidos!"},
            )

    return app


if __name__ == "__main__":
    the_app = create_app()

    uvicorn.run(the_app, host="0.0.0.0", port=8000)
