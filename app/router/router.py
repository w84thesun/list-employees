from typing import List

from fastapi import APIRouter

from app.models.employee import Employee
from app.router.endpoints import employee

api = APIRouter()

api.add_api_route("/findByField", endpoint=employee.find_by_field, methods=["GET"], response_model=List[Employee])
api.add_api_route("/findByRange", endpoint=employee.find_by_range, methods=["GET"], response_model=List[Employee])
