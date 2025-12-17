# src/util/db/mongo_coll/clients_db.py
from typing import Optional, List
from pydantic import BaseModel, Field
from src.util.db.mongo_util import MongoCollectionBaseClass
from src.common.settings import config

class ClientModel(BaseModel):
    client_name: str
    client_email: str
    client_phone: Optional[str] = None
    client_address: Optional[str] = None
    po_box: Optional[str] = None
    trn_number: Optional[str] = None
    contact_person: Optional[str] = None
    contact_number: Optional[str] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

class ClientDB(MongoCollectionBaseClass):
    def __init__(self, mongo_client, database: str = config.database_name, collection: str = "clients"):
        super().__init__(mongo_client, database, collection)

    def create_client(self, client: ClientModel) -> str:
        inserted_id = self.insert(client.model_dump())
        return str(inserted_id)

    def get_all_clients(self) -> List[ClientModel]:
        return [ClientModel(**doc) for doc in self.find({})]

    def get_client_by_email(self, email: str):
        data = self.find({"email": email})
        if data:
            return data[0]
        return None


    def update_client(self, email: str, update_data: dict) -> bool:
        import time
        update_data["updated_at"] = int(time.time())
        return self.update_one({"email": email}, update_data)
