from fastapi import FastAPI
from app.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.handlers import router


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(router, prefix=API_PREFIX)
    return application


app = get_application()
