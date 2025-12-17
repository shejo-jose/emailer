# src/api/clients.py
from fastapi import APIRouter
from src.util.db.mongo_coll.client_db import ClientDB, ClientModel
from src.util.db.mongo_util import MongoConnect
from src.common.settings import config
from pydantic import BaseModel
import datetime

router = APIRouter(tags=["Clients API"], prefix="/clients")

# Initialize Mongo client and DB wrapper
mongo_client = MongoConnect(config.pymongo_uri)()
client_db = ClientDB(mongo_client)

@router.post("/create")
async def create_client(
    client_name: str,
    client_email: str,
    client_phone: str,
    client_address: str,
    po_box: str,
    trn_number: str,
    contact_person: str,
    contact_number: str
):
    """
    Create a new client in the database.
    """
    timestamp = int(datetime.datetime.now().timestamp())
    client = ClientModel(
        client_name=client_name,
        client_email=client_email,
        client_phone=client_phone,
        client_address=client_address,
        po_box=po_box,
        trn_number=trn_number,
        contact_person=contact_person,
        contact_number=contact_number,
        created_at=timestamp,
        updated_at=timestamp
    )
    client_id = client_db.create_client(client)
    return {"message": "Client created successfully", "client_id": client_id}
