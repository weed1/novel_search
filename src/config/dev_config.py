# -*- coding:utf-8 -*-

import os
from .config import Config


class DevConfig(Config):
    # Database config
    REDIS_DICT = dict(
        IS_CACHE=True,
        REDIS_ENDPOINT=os.getenv('REDIS_ENDPOINT', "localhost"),
        REDIS_PORT=int(os.getenv('REDIS_PORT', 6379)),
        REDIS_PASSWORD=os.getenv('REDIS_PASSWORD', None),
        CACHE_DB=0,
        SESSION_DB=1,
        POOLSIZE=10,
    )
    MONGODB = dict(
        MONGO_HOST=os.getenv('MONGO_HOST', ""),
        MONGO_PORT=int(os.getenv('MONGO_PORT', 27017)),
        MONGO_USERNAME=os.getenv('MONGO_USERNAME', ""),
        MONGO_PASSWORD=os.getenv('MONGO_PASSWORD', ""),
        DATABASE='novel',
    )

    # website
    WEBSITE = dict(
        IS_RUNNING=os.getenv('NOVEL_IS_RUNNING', True),
        TOKEN=os.getenv('NOVEL_TOKEN', '')
    )

    AUTH = {
        "Novel-Api-Key": os.getenv('NOVEL_API_KEY', "your key")
    }
