# emailer.py
import time
from src.util.job_utils import set_status
from src.common.settings import config
from loguru import logger
from email.message import EmailMessage
import smtplib

def send_email(job_id: str, email: str, subject: str, body: str):

    set_status(job_id, "STARTED")
    logger.info(f"[EMAIL] Job {job_id} STARTED")
    try: 
        msg = EmailMessage()
        msg["From"] = config.sender_email
        msg["To"] = email
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(config.sender_email, config.sender_password)
            smtp.send_message(msg)

        set_status(job_id, "COMPLETED")
        logger.info(f"[EMAIL] Job {job_id} COMPLETED")

    except Exception as e:
        set_status(job_id, "FAILED")
        logger.info(f"[EMAIL] Job {job_id} FAILED")