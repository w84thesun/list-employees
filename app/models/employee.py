from datetime import datetime

from pydantic import BaseModel
from pydantic.typing import Optional


class Employee(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: Optional[datetime] = datetime.now()
    job_title: str
    gender: str
    salary: int
