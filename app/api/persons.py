# -*- coding: utf-8 -*-
"""
Person tag API endpoint.

This endpoint generate human basic values. It's a selected assortment of
perons providers from mimesis found here
https://mimesis.name/api.html#person

"""
from fastapi import APIRouter

route = APIRouter()


@route.get("/")
def ping():
    """
    Test endpoint.
    """
    return {"ping": "pong!"}
