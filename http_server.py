

API_VERSION = "v1"


def create_app() -> FastAPI:
    app = FastAPI()
    app.router.redirect_slashes = True
    # Configure Routers
    app.include_router(example.router, prefix=f"/{API_VERSION}/account", dependencies=[])

    @app.exception_handler(ExceptionMessageBuilder)
    async def http_exception_handler(request, exc: ExceptionMessageBuilder):
        return JSONResponse(
            content={"title": exc.title, "message": exc.message},
            status_code=exc.status_code,
        )

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
        except Exception as err:
            return JSONResponse(
                status_code=400,
                content={"title": "Campos inválidos", "message": "Campos informados inválidos!"},
            )

    return app


if __name__ == "__main__":
    the_app = create_app()

    uvicorn.run(the_app, host="0.0.0.0", port=settings.http_api_port)
