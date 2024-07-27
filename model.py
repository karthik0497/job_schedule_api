from pydantic import BaseModel
from typing import Optional, Dict, Any


def sequential_id_generator(start: int = 10000):
    current = start
    while True:
        yield current
        current += 1


id_generator = sequential_id_generator()


# Function to get the next ID
def generate_sequential_id():
    return next(id_generator)


class Job(BaseModel):
    job_id: int
    job_name: str
    job_schedule: str
    job_description: str
    job_type: Optional[str]
    job_params: Optional[Dict[str, Any]]


class JobCreate(BaseModel):
    job_name: str
    job_schedule: str
    job_description: str
    job_type: Optional[str]
    job_params: Optional[Dict[str, Any]]
