from datetime import datetime
from logging import info, error
from typing import List, Any

from fastapi.exceptions import HTTPException

from app.db.connection import Conn
from app.models.employee import Employee


def validate_filter(field: str, value: Any = None) -> Any:
    if value is None:
        return None
    if field == "age" or field == "salary":
        return int(value)
    elif field == "join_date":
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    else:
        return value


def find_by_field(
        filter_field: str = None,
        filter_value: Any = None
) -> List[Employee]:
    info("Method findByField called field: {}, value: {}".format(filter_field, filter_value))
    value = validate_filter(filter_field, filter_value)

    if value is None:
        error("Failed to validate filter value")
        raise HTTPException(status_code=400, detail="failed to validate value")

    result = []
    for e in Conn.find({filter_field: value}, {'_id': 0}):
        result.append(Employee(**e))

    return result


def validate_range(field: str, range_from: Any = None, range_to: Any = None):
    if range_from is None or range_to is None:
        return None
    elif field == "age" or field == "salary":
        try:
            r = {"from": int(range_from), "to": int(range_to)}
            return r
        except ValueError as e:
            return None
    else:
        return {"from": range_from, "to": range_to}


def find_by_range(
        filter_field: str = None,
        range_from: Any = None,
        range_to: Any = None
) -> List[Employee]:
    info("Method findByRange called field: {}, from: {}, to: {}".format(filter_field, range_from, range_to))

    ranges = validate_range(filter_field, range_from, range_to)
    if ranges is None:
        error("Failed to validate range parameters")
        raise HTTPException(status_code=400, detail="failed to validate range parameters")

    result = []

    cursor = Conn.find(
        filter={filter_field: {"$gte": ranges["from"], "$lte": ranges["to"]}},
        projection={"_id": 0})

    for e in cursor:
        result.append(Employee(**e))

    return result
