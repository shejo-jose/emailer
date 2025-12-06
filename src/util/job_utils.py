# job_utils.py

job_status = {}

def set_status(job_id: str, status: str):
    job_status[job_id] = status

def get_status(job_id: str):
    return job_status.get(job_id, "NOT FOUND")
