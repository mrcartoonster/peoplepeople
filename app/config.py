# -*- coding: utf-8 -*-
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Base setting depency for entire app.
    """

    environment: str = os.getenv("Envrionment", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Base setting function injection.
    """
    log.info("Loding config settings form the environment.")
    return Settings()
