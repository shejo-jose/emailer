# main.py
from fastapi import FastAPI
from src.api.emailer import router as email_router
from src.api.clients import router as clients_router
from src.common.settings import config

app = FastAPI(title="Invoice Generator Service", description="API to send emails in the background with job tracking")

app.include_router(
    email_router,
    prefix=config.api_prefix
)

app.include_router(
    clients_router,
    prefix=config.api_prefix
)