# src/util/db/mongo_util.py
"""Mongo DB Utility."""
from pymongo import MongoClient
from src.common.settings import config
from loguru import logger

class MongoConnect:
    """Mongo Connection Class."""

    def __init__(self, uri):
        try:
            self.uri = uri
            self.client = MongoClient(self.uri, connect=False)
        except Exception as e:
            logger.exception(str(e))
            raise
    
    def __call__(self, *args, **kwargs):
        return self.client
    
    def __repr__(self):
        """Object Representation."""
        return f"Mongo Client(uri:{self.uri}, server_info={self.client.server_info()})"

class MongoCollectionBaseClass:
    """Mongo Collection Base Class."""
    def __init__(self, mongo_client, database, collection):
        self.client = mongo_client
        self.collection = mongo_client[database][collection]  # store collection object

    def insert(self, data: dict):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def find(self, query: dict = None):
        return list(self.collection.find(query or {}))

    def update_one(self, query: dict, update_data: dict, upsert: bool = False) -> bool:
        """Update a single document based on query."""
        result = self.collection.update_one(query, {"$set": update_data}, upsert=upsert)
        return result.modified_count > 0
