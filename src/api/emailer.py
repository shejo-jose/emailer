# emailer.py
from fastapi import APIRouter, BackgroundTasks, HTTPException
from src.core.emailer import send_email
from src.util.job_utils import get_status, set_status
import uuid
from loguru import logger

router = APIRouter(tags=["Emailer API"], prefix="/v1/emailer")

@router.post("/email")
async def send_email_message(background_tasks: BackgroundTasks, email: str, subject: str, body: str):
    job_id = str(uuid.uuid4())
    set_status(job_id, "QUEUED")
    logger.info(f"[API] Job {job_id} queued for email: {email}")

    background_tasks.add_task(send_email, job_id, email, subject, body)
    logger.info(f"[API] Background task added for job {job_id}")

    return {
        "message": "Job started",
        "job_id": job_id
    }

@router.get("/status/{job_id}")
async def job_status(job_id: str):
    status = get_status(job_id)
    logger.info(f"[API] Job {job_id} status requested: {status}")
    return {"job_id": job_id, "status": status}
