# src/db/__init__.py
from src.common.settings import config
from src.util.db.mongo_util import MongoConnect
from src.util.db.mongo_coll.client_db import ClientDB

mongo_client = MongoConnect(uri=config.pymongo_uri)()

client_db = ClientDB(mongo_client)
