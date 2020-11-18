# -*- coding: utf-8 -*-
"""
App factory and routing hub for endpoints.
"""
import logging

from fastapi import FastAPI

from app.api import internet, persons

log = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """
    FastAPI instance and routing function.
    """
    application = FastAPI()
    application.include_router(
        persons.router,
        prefix="/persons",
        tags="person",
    )
    application.include_router(
        internet.router,
        prefix="/internet",
        tags="internet",
    )

    return application


app = create_app()
