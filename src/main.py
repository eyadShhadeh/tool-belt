from typing import Union
from fastapi import FastAPI, Request
from src.util.log import log_config, CustomizeLogger


def create_app() -> FastAPI:
    app = FastAPI(title='tool_belt')
    logger = CustomizeLogger.make_logger()
    app.logger = logger

    return app


app = create_app()


@app.get('/custom-logger')
def customize_logger(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successf"}


@app.get("/")
async def read_root():
    return {"likes": 1}
